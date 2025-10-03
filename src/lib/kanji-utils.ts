import {
  KanjiData,
  JLPTLevel,
  UserProgress,
  LearningStats,
} from "@/types/kanji";

// Import kanji data
import n5KanjiData from "@/data/kanji/n5-complete.json";
import n4KanjiData from "@/data/kanji/n4.json";

const kanjiData: Record<JLPTLevel, KanjiData[]> = {
  N5: n5KanjiData as KanjiData[],
  N4: n4KanjiData as KanjiData[],
  N3: [], // Placeholder for now
  N2: [], // Placeholder for now
  N1: [], // Placeholder for now
};

export function getAllKanji(): Record<JLPTLevel, KanjiData[]> {
  return kanjiData as Record<JLPTLevel, KanjiData[]>;
}

export function getKanjiByLevel(level: JLPTLevel): KanjiData[] {
  return kanjiData[level] || [];
}

export function getKanjiById(id: string): KanjiData | undefined {
  for (const level in kanjiData) {
    const kanji = kanjiData[level as JLPTLevel].find((k) => k.id === id);
    if (kanji) return kanji;
  }
  return undefined;
}

export function getNextKanji(
  currentLevel: JLPTLevel,
  currentIndex: number
): KanjiData | null {
  const kanjiList = getKanjiByLevel(currentLevel);
  return kanjiList[currentIndex] || null;
}

export function calculateProgress(
  level: JLPTLevel,
  currentIndex: number,
  completedKanji: string[]
): LearningStats {
  const kanjiList = getKanjiByLevel(level);
  const currentKanji = getNextKanji(level, currentIndex);

  if (!currentKanji) {
    throw new Error(
      `No kanji found for level ${level} at index ${currentIndex}`
    );
  }

  const levelProgress = {
    current: level,
    completed: completedKanji.filter((id) => kanjiList.some((k) => k.id === id))
      .length,
    total: kanjiList.length,
    percentage: Math.round((completedKanji.length / kanjiList.length) * 100),
  };

  return {
    currentKanji,
    progress: {
      current: currentIndex + 1,
      total: kanjiList.length,
      percentage: Math.round(((currentIndex + 1) / kanjiList.length) * 100),
      remaining: kanjiList.length - currentIndex - 1,
    },
    levelProgress,
  };
}

export function getDefaultProgress(): UserProgress {
  return {
    currentLevel: "N5",
    currentKanjiIndex: 0,
    completedKanji: [],
    studyStreak: 0,
    lastStudied: new Date(),
    totalTimeSpent: 0,
  };
}

export function formatProgressMessage(stats: LearningStats): string {
  const { currentKanji, progress } = stats;

  const onReading = currentKanji.readings.on[0] || "";
  const kunReading = currentKanji.readings.kun[0] || "";
  const readingText =
    onReading && kunReading
      ? `${onReading}・${kunReading}`
      : onReading || kunReading;

  const meanings = currentKanji.meanings.join(", ");

  return `Perfect 👍 The next JLPT ${currentKanji.jlptLevel} kanji is ${currentKanji.kanji}（${readingText}）, meaning ${meanings}.
We're at Kanji #${progress.current} of ${progress.total} → ${progress.remaining} left.
(Progress: about ${progress.percentage}% complete ✅)`;
}

// Browser storage utilities
export function loadProgressFromStorage(): UserProgress {
  if (typeof window === "undefined") return getDefaultProgress();

  try {
    const stored = localStorage.getItem("kanji-progress");
    if (!stored) return getDefaultProgress();

    const parsed = JSON.parse(stored);
    return {
      ...parsed,
      lastStudied: new Date(parsed.lastStudied) || new Date(),
    };
  } catch {
    return getDefaultProgress();
  }
}

export function saveProgressToStorage(progress: UserProgress): void {
  if (typeof window === "undefined") return;

  try {
    localStorage.setItem("kanji-progress", JSON.stringify(progress));
  } catch (error) {
    console.error("Failed to save progress:", error);
  }
}
