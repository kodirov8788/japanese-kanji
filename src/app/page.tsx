"use client";

import { useState, useEffect } from "react";
import { JLPTLevel, UserProgress, LearningStats } from "@/types/kanji";
import {
  loadProgressFromStorage,
  saveProgressToStorage,
  calculateProgress,
  getKanjiByLevel,
  getDefaultProgress,
  formatProgressMessage,
} from "@/lib/kanji-utils";
import { FlashCard } from "@/components/flash-card";
import { ProgressBar } from "@/components/progress-bar";
import { LevelSelector } from "@/components/level-selector";
import { Header } from "@/components/header";
import { MobileSummary } from "@/components/mobile-summary";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { ArrowLeft, ArrowRight, RotateCcw, CheckCircle } from "lucide-react";

type ViewMode = "level-select" | "learning";

export default function HomePage() {
  const [viewMode, setViewMode] = useState<ViewMode>("level-select");
  const [selectedLevel, setSelectedLevel] = useState<JLPTLevel>("N5");
  const [progress, setProgress] = useState<UserProgress>(getDefaultProgress());
  const [stats, setStats] = useState<LearningStats | null>(null);
  const [showProgressMessage, setShowProgressMessage] = useState(false);
  const [currentExampleIndex, setCurrentExampleIndex] = useState(0);

  // Load progress from localStorage on mount
  useEffect(() => {
    const savedProgress = loadProgressFromStorage();
    setProgress(savedProgress);

    if (savedProgress.currentLevel) {
      setSelectedLevel(savedProgress.currentLevel);
      setViewMode("learning");
    }
  }, []);

  // Calculate stats when progress or level changes
  useEffect(() => {
    try {
      const newStats = calculateProgress(
        progress.currentLevel,
        progress.currentKanjiIndex,
        progress.completedKanji
      );
      setStats(newStats);
    } catch (error) {
      console.error("Error calculating stats:", error);
      // Reset to safe state if calculation fails
      setStats(null);
    }
  }, [progress]);

  const handleLevelSelect = (level: JLPTLevel) => {
    setSelectedLevel(level);
    goToLevel(level);
  };

  const goToLevel = (level: JLPTLevel) => {
    if (level === progress.currentLevel) {
      setViewMode("learning");
      return;
    }

    const newProgress: UserProgress = {
      ...progress,
      currentLevel: level,
      currentKanjiIndex: 0,
    };

    setProgress(newProgress);
    saveProgressToStorage(newProgress);
    setViewMode("learning");
  };

  const handleKanjiComplete = () => {
    const currentKanji = stats?.currentKanji;

    if (currentKanji) {
      const newProgress: UserProgress = {
        ...progress,
        currentKanjiIndex: progress.currentKanjiIndex + 1,
        completedKanji: [...progress.completedKanji, currentKanji.id],
        studyStreak: progress.studyStreak + 1,
        lastStudied: new Date(),
        totalTimeSpent: progress.totalTimeSpent + 5, // Estimate 5 minutes per kanji
      };

      setProgress(newProgress);
      saveProgressToStorage(newProgress);

      // Show progress message
      setShowProgressMessage(true);
      setTimeout(() => setShowProgressMessage(false), 3000);

      // Reset example index for next kanji
      setCurrentExampleIndex(0);

      // Check if level is complete
      const kanjiList = getKanjiByLevel(currentKanji.jlptLevel);
      if (progress.currentKanjiIndex + 1 >= kanjiList.length) {
        setTimeout(() => {
          alert(
            `🎉 Congratulations!\nYou've completed ${currentKanji.jlptLevel}!\nMaster the examples to proceed.\n\nTotal kata mastered: ${newProgress.completedKanji.length}`
          );
        }, 1000);
      }
    }
  };

  const resetProgress = () => {
    const newProgress = getDefaultProgress();
    newProgress.currentLevel = selectedLevel;
    setProgress(newProgress);
    saveProgressToStorage(newProgress);
  };

  const goToPreviousExample = () => {
    if (currentExampleIndex > 0) {
      setCurrentExampleIndex(currentExampleIndex - 1);
    }
  };

  const goToNextExample = () => {
    const currentKanji = stats?.currentKanji;
    if (
      currentKanji &&
      currentExampleIndex < currentKanji.examples.length - 1
    ) {
      setCurrentExampleIndex(currentExampleIndex + 1);
    }
  };

  const goToSpecificExample = (index: number) => {
    if (
      stats?.currentKanji &&
      index >= 0 &&
      index < stats.currentKanji.examples.length
    ) {
      setCurrentExampleIndex(index);
    }
  };

  const goToPreviousKanji = () => {
    if (progress.currentKanjiIndex > 0) {
      const newProgress = {
        ...progress,
        currentKanjiIndex: progress.currentKanjiIndex - 1,
      };
      setProgress(newProgress);
      saveProgressToStorage(newProgress);
      setCurrentExampleIndex(0);
    }
  };

  const goToNextKanji = () => {
    const kanjiList = getKanjiByLevel(progress.currentLevel);
    if (progress.currentKanjiIndex < kanjiList.length - 1) {
      const newProgress = {
        ...progress,
        currentKanjiIndex: progress.currentKanjiIndex + 1,
      };
      setProgress(newProgress);
      saveProgressToStorage(newProgress);
      setCurrentExampleIndex(0);
    }
  };

  if (viewMode === "level-select") {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 dark:from-slate-900 dark:to-slate-800">
        <Header
          currentLevel={selectedLevel}
          onLevelChange={handleLevelSelect}
        />
        <div className="container mx-auto px-4 py-8">
          <LevelSelector
            selectedLevel={selectedLevel}
            onLevelSelect={handleLevelSelect}
          />
        </div>
      </div>
    );
  }

  if (!stats?.currentKanji) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 dark:from-slate-900 dark:to-slate-800">
        <Header
          currentLevel={selectedLevel}
          onLevelChange={handleLevelSelect}
        />
        <div className="container mx-auto px-4 py-8">
          <Card className="max-w-md mx-auto">
            <CardContent className="pt-6 text-center">
              <p className="text-muted-foreground mb-4">
                No kanji available for {selectedLevel} level.
              </p>
              <Button
                onClick={() => setViewMode("level-select")}
                variant="outline"
              >
                Choose Different Level
              </Button>
            </CardContent>
          </Card>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 dark:from-slate-900 dark:to-slate-800">
      <Header currentLevel={selectedLevel} onLevelChange={handleLevelSelect} />

      <div className="container mx-auto px-3 sm:px-4 py-3 sm:py-5 md:py-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-3 sm:gap-5 md:gap-8">
          {/* Main Learning Area */}
          <div className="lg:col-span-2 order-2 lg:order-1">
            <div className="space-y-3 sm:space-y-5">
              {/* Progress Message */}
              {showProgressMessage && (
                <Card className="bg-green-50 dark:bg-green-900/20 border-green-200 dark:border-green-800 p-4">
                  <div className="text-center">
                    <CheckCircle className="h-6 w-6 sm:h-8 sm:w-8 text-green-600 mx-auto mb-2" />
                    <p className="text-green-800 dark:text-green-200 text-sm sm:text-base">
                      Excellent! All examples mastered ✅
                    </p>
                  </div>
                </Card>
              )}

              {/* FlashCard */}
              <FlashCard
                kanji={stats.currentKanji}
                currentExampleIndex={currentExampleIndex}
                onPrevious={goToPreviousExample}
                onNext={goToNextExample}
                onSpecificExample={goToSpecificExample}
                onComplete={handleKanjiComplete}
              />

              {/* Navigation */}
              <div className="flex justify-between items-center">
                <div className="space-y-3 w-full">
                  <div className="flex justify-between items-center">
                    <span className="text-xs sm:text-sm text-muted-foreground font-medium">
                      <span className="hidden sm:inline">
                        Kanji {progress.currentKanjiIndex + 1} of{" "}
                        {getKanjiByLevel(progress.currentLevel).length}
                      </span>
                      <span className="sm:hidden">
                        K {progress.currentKanjiIndex + 1}/
                        {getKanjiByLevel(progress.currentLevel).length}
                      </span>
                      {stats?.currentKanji && (
                        <span className="ml-1 sm:ml-2 text-xs">
                          • {currentExampleIndex + 1}/
                          {stats.currentKanji.examples.length}
                        </span>
                      )}
                    </span>
                  </div>
                  <div className="flex gap-2 sm:gap-3">
                    <div className="flex items-center gap-1">
                      <Button
                        variant="outline"
                        size="icon"
                        onClick={resetProgress}
                        className="h-9 sm:h-10 w-9 sm:w-10"
                        title="Reset Progress"
                      >
                        <RotateCcw className="h-4 w-4" />
                      </Button>
                      <Button
                        variant="outline"
                        onClick={goToPreviousKanji}
                        disabled={progress.currentKanjiIndex === 0}
                        className="flex items-center gap-1 sm:gap-2 flex-1 h-9 sm:h-10 text-xs sm:text-sm"
                      >
                        <ArrowLeft className="h-3 w-3 sm:h-4 w-4" />
                        <span className="hidden sm:inline">Previous Kanji</span>
                        <span className="sm:hidden">Prev K</span>
                      </Button>
                    </div>

                    <Button
                      variant="outline"
                      onClick={goToNextKanji}
                      disabled={
                        progress.currentKanjiIndex >=
                        getKanjiByLevel(progress.currentLevel).length - 1
                      }
                      className="flex items-center gap-1 sm:gap-2 flex-1 h-9 sm:h-10 text-xs sm:text-sm"
                    >
                      <span className="hidden sm:inline">Next Kanji</span>
                      <span className="sm:hidden">Next K</span>
                      <ArrowRight className="h-3 w-3 sm:h-4 w-4" />
                    </Button>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Sidebar */}
          <div className="space-y-4 sm:space-y-6 order-1 lg:order-2">
            {/* Mobile Summary */}
            <MobileSummary
              stats={stats}
              currentExampleIndex={currentExampleIndex}
            />

            {/* Desktop Progress */}
            <div className="hidden sm:block">
              <ProgressBar stats={stats} />

              {/* Current Progress Message */}
              <Card>
                <CardContent className="pt-4 sm:pt-6">
                  <div className="space-y-2 text-sm">
                    <div className="whitespace-pre-line font-mono text-xs bg-slate-100 dark:bg-slate-800 p-3 rounded">
                      {formatProgressMessage(stats)}
                    </div>
                  </div>
                </CardContent>
              </Card>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
