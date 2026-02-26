import { memo } from 'react';
import { Pressable, StyleSheet, Text, View } from 'react-native';
import { Image } from 'expo-image';
import type { WorkshopSummary } from '../types/api';

type Props = {
  item: WorkshopSummary;
  isSelected: boolean;
  onPress: (id: string) => void;
  progress?: {
    completionPercent: number;
    resumeQuestionIndex: number;
    evaluatedCount: number;
  } | null;
};

function WorkshopCardImpl({ item, isSelected, onPress, progress = null }: Props) {
  const preview = item.asset_preview[0];
  const isCompleted = progress ? progress.completionPercent >= 100 : false;
  const progressLabel = isCompleted ? 'completado' : 'en curso';
  const progressStyle = isCompleted ? styles.progressCompleted : styles.progressInProgress;

  return (
    <Pressable
      style={[styles.card, isSelected ? styles.cardSelected : null]}
      onPress={() => onPress(item.id)}
    >
      {preview ? <Image source={preview} style={styles.preview} contentFit="cover" /> : null}
      <View style={styles.content}>
        <Text style={styles.title}>{item.title}</Text>
        <Text style={styles.meta}>
          {item.area_slug ?? 'general'} · {item.stats.total_questions} preguntas
        </Text>
        <View style={styles.row}>
          <Text style={[styles.badge, item.access_tier === 'premium' ? styles.premium : styles.free]}>
            {item.access_tier}
          </Text>
          <Text style={[styles.badge, item.can_access ? styles.ok : styles.locked]}>
            {item.can_access ? 'acceso' : 'bloqueado'}
          </Text>
          {progress ? (
            <Text style={[styles.badge, progressStyle]}>
              {progressLabel} · {progress.completionPercent}% · P{progress.resumeQuestionIndex + 1}
            </Text>
          ) : null}
        </View>
        {progress ? (
          <Text style={styles.progressMeta}>
            {progress.evaluatedCount} de {item.stats.total_questions} evaluadas
          </Text>
        ) : null}
      </View>
    </Pressable>
  );
}

export const WorkshopCard = memo(WorkshopCardImpl);

const styles = StyleSheet.create({
  card: {
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#26355e',
    backgroundColor: '#0f1a33',
    overflow: 'hidden',
    marginBottom: 10,
  },
  cardSelected: {
    borderColor: '#4f7cff',
  },
  preview: {
    width: '100%',
    height: 110,
    backgroundColor: '#0a1328',
  },
  content: {
    padding: 12,
    gap: 6,
  },
  title: {
    color: '#f2f5ff',
    fontSize: 15,
    fontWeight: '700',
  },
  meta: {
    color: '#97a6cd',
    fontSize: 12,
  },
  row: {
    flexDirection: 'row',
    gap: 8,
  },
  badge: {
    borderRadius: 999,
    paddingHorizontal: 8,
    paddingVertical: 3,
    fontSize: 11,
    overflow: 'hidden',
  },
  premium: {
    color: '#ffd27a',
    backgroundColor: 'rgba(255, 189, 79, 0.15)',
  },
  free: {
    color: '#90efc0',
    backgroundColor: 'rgba(64, 199, 129, 0.15)',
  },
  ok: {
    color: '#90efc0',
    backgroundColor: 'rgba(64, 199, 129, 0.15)',
  },
  locked: {
    color: '#ff9da6',
    backgroundColor: 'rgba(255, 99, 114, 0.15)',
  },
  progressInProgress: {
    color: '#87d6ff',
    backgroundColor: 'rgba(80, 186, 255, 0.18)',
  },
  progressCompleted: {
    color: '#9df0ca',
    backgroundColor: 'rgba(59, 201, 132, 0.18)',
  },
  progressMeta: {
    color: '#7fa8d6',
    fontSize: 11,
  },
});
