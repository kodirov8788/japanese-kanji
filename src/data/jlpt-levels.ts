import { JLPTLevelInfo, JLPTLevel } from "@/types/kanji";

export const JLPT_LEVELS: Record<JLPTLevel, JLPTLevelInfo> = {
  N5: {
    level: "N5",
    name: "N5 (Basic)",
    description: "Basic kanji for beginners",
    totalKanji: 103,
    color: "bg-green-500",
  },
  N4: {
    level: "N4",
    name: "N4 (Elementary)",
    description: "Elementary kanji for daily use",
    totalKanji: 167,
    color: "bg-blue-500",
  },
  N3: {
    level: "N3",
    name: "N3 (Intermediate)",
    description: "Intermediate kanji for communication",
    totalKanji: 370,
    color: "bg-yellow-500",
  },
  N2: {
    level: "N2",
    name: "N2 (Advanced)",
    description: "Advanced kanji for business",
    totalKanji: 374,
    color: "bg-orange-500",
  },
  N1: {
    level: "N1",
    name: "N1 (Expert)",
    description: "Expert kanji for fluency",
    totalKanji: 1100,
    color: "bg-red-500",
  },
};
