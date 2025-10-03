export interface KanjiReading {
  on: string[];
  kun: string[];
}

export interface ExampleSentence {
  japanese: string;
  romaji: string;
  english: string;
  uzbek: string;
}

export interface KanjiExample {
  word: string;
  reading: string;
  meaning: string;
  sentence: ExampleSentence;
}

export interface KanjiData {
  id: string;
  kanji: string;
  readings: KanjiReading;
  meanings: string[];
  jlptLevel: JLPTLevel;
  examples: KanjiExample[];
  frequency: number;
  strokes: number;
}

export type JLPTLevel = "N5" | "N4" | "N3" | "N2" | "N1";

export interface JLPTLevelInfo {
  level: JLPTLevel;
  name: string;
  description: string;
  totalKanji: number;
  color: string;
}

export interface UserProgress {
  currentLevel: JLPTLevel;
  currentKanjiIndex: number;
  completedKanji: string[];
  studyStreak: number;
  lastStudied: Date;
  totalTimeSpent: number; // in minutes
}

export interface LearningStats {
  currentKanji: KanjiData;
  progress: {
    current: number;
    total: number;
    percentage: number;
    remaining: number;
  };
  levelProgress: {
    current: JLPTLevel;
    completed: number;
    total: number;
    percentage: number;
  };
}
