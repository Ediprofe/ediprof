/**
 * PDFLoader - Maneja la carga y renderizado de PDFs con PDF.js
 */

import * as pdfjsLib from 'pdfjs-dist';
import type { PDFDocumentProxy, PDFPageProxy } from 'pdfjs-dist';
import { PDFPresentationController } from './PDFPresentationController';

// Configurar el worker de PDF.js
// Usamos archivo local para mayor confiabilidad
const workerSrc = '/pdf-worker/pdf.worker.mjs';
pdfjsLib.GlobalWorkerOptions.workerSrc = workerSrc;

export class PDFLoader {
  private static instance: PDFLoader;
  private pdfDocument: PDFDocumentProxy | null = null;
  private currentPage: number = 1;
  private totalPages: number = 0;
  private scale: number = 1.5;
  private rotation: number = 0;
  private presentationController: PDFPresentationController | null = null;
  private pdfContainer: HTMLElement | null = null;
  private pdfPagesContainer: HTMLElement | null = null;

  private constructor() {}

  public static getInstance(): PDFLoader {
    if (!PDFLoader.instance) {
      PDFLoader.instance = new PDFLoader();
    }
    return PDFLoader.instance;
  }

  /**
   * Carga un PDF desde un archivo File
   */
  public async loadPDF(file: File): Promise<void> {
    try {
      const arrayBuffer = await file.arrayBuffer();
      const pdf = await pdfjsLib.getDocument({ data: arrayBuffer }).promise;
      
      this.pdfDocument = pdf;
      this.totalPages = pdf.numPages;
      this.currentPage = 1;
      this.rotation = 0;
      
      // Obtener referencias a los contenedores
      this.pdfContainer = document.getElementById('pdf-container');
      this.pdfPagesContainer = document.getElementById('pdf-pages');
      
      if (!this.pdfContainer || !this.pdfPagesContainer) {
        throw new Error('Contenedores del PDF no encontrados');
      }

      // Renderizar todas las páginas
      await this.renderAllPages();
      
      // Emitir evento de PDF cargado
      document.dispatchEvent(new CustomEvent('pdf-loaded', {
        detail: { totalPages: this.totalPages }
      }));
      
      // Actualizar indicador de página
      this.updatePageIndicator();
      
    } catch (error) {
      console.error('Error loading PDF:', error);
      document.dispatchEvent(new CustomEvent('pdf-error', {
        detail: { message: error instanceof Error ? error.message : 'Error desconocido' }
      }));
      throw error;
    }
  }

  /**
   * Renderiza todas las páginas del PDF
   */
  private async renderAllPages(): Promise<void> {
    if (!this.pdfDocument || !this.pdfPagesContainer) return;

    // Limpiar páginas anteriores
    this.pdfPagesContainer.innerHTML = '';

    // Renderizar cada página
    for (let pageNum = 1; pageNum <= this.totalPages; pageNum++) {
      await this.renderPage(pageNum);
    }
  }

  /**
   * Renderiza una página específica con resolución Retina
   */
  private async renderPage(pageNum: number): Promise<void> {
    if (!this.pdfDocument || !this.pdfPagesContainer) return;

    const page = await this.pdfDocument.getPage(pageNum);
    
    // devicePixelRatio para renderizado nítido en pantallas Retina
    const dpr = window.devicePixelRatio || 1;
    
    // Viewport CSS (tamaño visual)
    const cssViewport = page.getViewport({ scale: this.scale, rotation: this.rotation });
    
    // Viewport de renderizado (resolución real del canvas = scale * dpr)
    const renderViewport = page.getViewport({ scale: this.scale * dpr, rotation: this.rotation });

    // Crear contenedor de la página
    const pageContainer = document.createElement('div');
    pageContainer.className = 'pdf-page';
    pageContainer.style.position = 'relative';
    pageContainer.style.width = `${cssViewport.width}px`;
    pageContainer.style.height = `${cssViewport.height}px`;
    pageContainer.dataset.pageNumber = String(pageNum);

    // Crear canvas para la página
    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');
    
    if (!context) {
      throw new Error('No se pudo obtener el contexto 2D del canvas');
    }

    // Canvas interno a resolución alta (scale * dpr)
    canvas.width = renderViewport.width;
    canvas.height = renderViewport.height;
    
    // CSS muestra a tamaño visual (scale * 1)
    canvas.style.width = `${cssViewport.width}px`;
    canvas.style.height = `${cssViewport.height}px`;

    // Renderizar la página con la resolución alta
    await page.render({
      canvasContext: context,
      viewport: renderViewport
    }).promise;

    pageContainer.appendChild(canvas);
    this.pdfPagesContainer!.appendChild(pageContainer);

    // Liberar recursos de la página
    page.cleanup();
  }

  /**
   * Inicializa el controlador de presentación
   */
  private initPresentationController(): void {
    if (!this.pdfContainer) return;

    // Destruir controlador anterior si existe
    if (this.presentationController) {
      this.presentationController.stop();
    }

    // Crear nuevo controlador
    this.presentationController = new PDFPresentationController(
      this.pdfContainer,
      () => {
        // Callback al cerrar
        console.log('Modo presentación cerrado');
      }
    );
  }

  /**
   * Navega a la página anterior
   */
  public prevPage(): void {
    if (this.currentPage > 1) {
      this.currentPage--;
      this.scrollToPage(this.currentPage);
      this.updatePageIndicator();
    }
  }

  /**
   * Navega a la página siguiente
   */
  public nextPage(): void {
    if (this.currentPage < this.totalPages) {
      this.currentPage++;
      this.scrollToPage(this.currentPage);
      this.updatePageIndicator();
    }
  }

  /**
   * Hace scroll a una página específica
   */
  private scrollToPage(pageNum: number): void {
    if (!this.pdfPagesContainer) return;

    const pageElement = this.pdfPagesContainer.querySelector(`[data-page-number="${pageNum}"]`) as HTMLElement;
    if (pageElement && this.pdfContainer) {
      this.pdfContainer.scrollTo({
        top: pageElement.offsetTop - 20,
        behavior: 'smooth'
      });
    }
  }

  /**
   * Actualiza el indicador de página
   */
  private updatePageIndicator(): void {
    document.dispatchEvent(new CustomEvent('pdf-page-changed', {
      detail: { current: this.currentPage, total: this.totalPages }
    }));
  }

  /**
   * Aumenta el zoom
   */
  public zoomIn(): void {
    this.scale = Math.min(this.scale * 1.2, 3.0);
    this.rebuildPages();
    document.dispatchEvent(new CustomEvent('pdf-zoom-changed', {
      detail: { scale: this.scale }
    }));
  }

  /**
   * Disminuye el zoom
   */
  public zoomOut(): void {
    this.scale = Math.max(this.scale / 1.2, 0.5);
    this.rebuildPages();
    document.dispatchEvent(new CustomEvent('pdf-zoom-changed', {
      detail: { scale: this.scale }
    }));
  }

  /**
   * Rota el PDF a la izquierda
   */
  public rotateLeft(): void {
    this.rotation = (this.rotation - 90) % 360;
    if (this.rotation < 0) this.rotation += 360;
    this.rebuildPages();
  }

  /**
   * Rota el PDF a la derecha
   */
  public rotateRight(): void {
    this.rotation = (this.rotation + 90) % 360;
    this.rebuildPages();
  }

  /**
   * Reconstruye las páginas con el zoom/rotación actual
   */
  private async rebuildPages(): Promise<void> {
    if (!this.presentationController) return;

    // Guardar trazos actuales si los hay
    // TODO: Implementar persistencia de anotaciones entre cambios de zoom

    // Re-renderizar páginas
    await this.renderAllPages();

    // Reinicializar controlador
    this.initPresentationController();
  }

  /**
   * Exporta el PDF con anotaciones como imagen
   */
  public exportToImage(): string | null {
    if (!this.presentationController) return null;
    return this.presentationController.exportToImage();
  }

  /**
   * Obtiene el documento PDF actual
   */
  public getPDFDocument(): PDFDocumentProxy | null {
    return this.pdfDocument;
  }

  /**
   * Obtiene la página actual
   */
  public getCurrentPage(): number {
    return this.currentPage;
  }

  /**
   * Obtiene el total de páginas
   */
  public getTotalPages(): number {
    return this.totalPages;
  }

  /**
   * Activa el modo de presentación (Modo Clase)
   * @param onClose - Callback opcional cuando se cierra el modo presentación
   * @returns El controlador de presentación
   */
  public activatePresentationMode(onClose?: () => void): PDFPresentationController | null {
    // Si no tenemos el contenedor guardado, intentar obtenerlo ahora
    if (!this.pdfContainer) {
      this.pdfContainer = document.getElementById('pdf-container');
    }
    
    if (!this.pdfContainer) {
      console.error('PDFLoader: No hay pdfContainer configurado');
      return null;
    }

    // Si ya hay un controlador activo, destruirlo primero
    if (this.presentationController) {
      this.presentationController.stop();
      this.presentationController = null;
    }

    // Crear nuevo controlador
    this.presentationController = new PDFPresentationController(
      this.pdfContainer,
      () => {
        this.presentationController = null;
        onClose?.();
      }
    );

    return this.presentationController;
  }

  /**
   * Desactiva el modo de presentación
   */
  public deactivatePresentationMode(): void {
    if (this.presentationController) {
      this.presentationController.stop();
      this.presentationController = null;
    }
  }

  /**
   * Verifica si el modo de presentación está activo
   */
  public isPresentationModeActive(): boolean {
    return this.presentationController !== null;
  }
}
