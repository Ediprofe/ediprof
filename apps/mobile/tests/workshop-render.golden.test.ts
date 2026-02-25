const test = require('node:test');
const assert = require('node:assert/strict');

const {
  cleanInlineMarkdown,
  normalizeMathForDisplay,
  toBlocks,
} = require('../src/lib/workshopRender.ts');

test('Q1 golden: equation arrow and subscripts are normalized', () => {
  assert.equal(
    normalizeMathForDisplay('4Fe + 3O_2 \\rightarrow 2Fe_2O_3'),
    '4Fe + 3O₂ → 2Fe₂O₃',
  );

  assert.equal(
    normalizeMathForDisplay('4Fe + 3O_2 rightarrow 2Fe_2O_3'),
    '4Fe + 3O₂ → 2Fe₂O₃',
  );

  assert.equal(
    normalizeMathForDisplay('4Fe + 3O_2 arrow 2Fe_2O_3'),
    '4Fe + 3O₂ → 2Fe₂O₃',
  );
});

test('Q4 golden: \\text blocks are rendered as readable units', () => {
  assert.equal(
    cleanInlineMarkdown(
      'Recipiente II (Agua): 2 \\\\text{ ml} × 0,99 \\\\text{ g/ml} = 1,98 \\\\text{ g}',
    ),
    'Recipiente II (Agua): 2 ml × 0,99 g/ml = 1,98 g',
  );
});

test('Q12 golden: image order from markdown is preserved', () => {
  const stem = `
  El siguiente diagrama muestra cómo el agua cambia de estado al variar la presión y la temperatura:

  ![Diagrama de fases del agua](https://cdn.ediprofe.com/img/saber/quimica/diagrama-de-fases.webp)

  Si partimos del punto X, donde el agua existe al mismo tiempo como líquido y gas dentro de un tanque cilíndrico, y aumentamos la temperatura del tanque a presión constante, ¿qué imagen representa el estado resultante del agua?

  ![Agua líquida y gaseosa](https://cdn.ediprofe.com/img/saber/quimica/agua-liquida-y-gaseosa.webp)
  `;

  const blocks = toBlocks(stem);
  const imageBlocks = blocks.filter((block: any) => block.type === 'image');

  assert.equal(imageBlocks.length, 2);
  assert.equal(
    imageBlocks[0].url,
    'https://cdn.ediprofe.com/img/saber/quimica/diagrama-de-fases.webp',
  );
  assert.equal(
    imageBlocks[1].url,
    'https://cdn.ediprofe.com/img/saber/quimica/agua-liquida-y-gaseosa.webp',
  );
});
