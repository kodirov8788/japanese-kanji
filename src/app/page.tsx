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
  getKanjiOfTheDay,
} from "@/lib/kanji-utils";
import { FlashCard } from "@/components/flash-card";
import { ProgressBar } from "@/components/progress-bar";
import { LevelSelector } from "@/components/level-selector";
import { Header } from "@/components/header";
import { MobileSummary } from "@/components/mobile-summary";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { ArrowLeft, ArrowRight, RotateCcw, CheckCircle, Calendar, Sparkles } from "lucide-react";
import { KanjiData } from "@/types/kanji";

type ViewMode = "level-select" | "learning";

export default function HomePage() {
  const [viewMode, setViewMode] = useState<ViewMode>("level-select");
  const [selectedLevel, setSelectedLevel] = useState<JLPTLevel>("N5");
  const [progress, setProgress] = useState<UserProgress>(getDefaultProgress());
  const [stats, setStats] = useState<LearningStats | null>(null);
  const [showProgressMessage, setShowProgressMessage] = useState(false);
  const [currentExampleIndex, setCurrentExampleIndex] = useState(0);
  const [kanjiOfTheDay, setKanjiOfTheDay] = useState<KanjiData | null>(null);

  // Load progress from localStorage on mount
  useEffect(() => {
    const savedProgress = loadProgressFromStorage();
    setProgress(savedProgress);

    if (savedProgress.currentLevel) {
      setSelectedLevel(savedProgress.currentLevel);
      setViewMode("learning");
    }

    setKanjiOfTheDay(getKanjiOfTheDay());
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

          {kanjiOfTheDay && (
            <div className="mt-12 max-w-4xl mx-auto">
              <div className="flex items-center gap-2 mb-6">
                <Calendar className="h-5 w-5 text-primary" />
                <h2 className="text-xl font-bold">Kanji of the Day</h2>
                <Badge variant="secondary" className="ml-2">Daily Challenge</Badge>
              </div>

              <Card className="overflow-hidden border-primary/20 bg-white/50 dark:bg-slate-900/50 backdrop-blur-sm hover:shadow-lg transition-all duration-300 group">
                <div className="grid grid-cols-1 md:grid-cols-2">
                  <div className="p-8 flex flex-col items-center justify-center bg-primary/5 border-b md:border-b-0 md:border-r border-primary/10">
                    <span className="text-sm font-medium text-primary mb-2 uppercase tracking-wider">{kanjiOfTheDay.jlptLevel} Level</span>
                    <div className="text-9xl font-bold text-slate-900 dark:text-white group-hover:scale-110 transition-transform duration-500">
                      {kanjiOfTheDay.kanji}
                    </div>
                    <div className="mt-4 flex gap-2">
                      {kanjiOfTheDay.readings.on.slice(0, 2).map((r, i) => (
                        <Badge key={i} variant="outline" className="bg-white/80 dark:bg-slate-800/80">{r}</Badge>
                      ))}
                    </div>
                  </div>
                  <div className="p-8 flex flex-col justify-center">
                    <div className="flex items-start gap-3 mb-4">
                      <Sparkles className="h-6 w-6 text-amber-500 shrink-0 mt-1" />
                      <div>
                        <h3 className="text-2xl font-bold text-slate-800 dark:text-slate-100 mb-1">
                          {kanjiOfTheDay.meanings.join(", ")}
                        </h3>
                        <p className="text-slate-500 dark:text-slate-400">
                          Master this kanji today to boost your Japanese proficiency.
                        </p>
                      </div>
                    </div>
                    
                    <div className="mt-6 space-y-4">
                      <div className="bg-slate-100 dark:bg-slate-800/80 p-4 rounded-xl">
                        <p className="text-xs font-bold text-slate-400 mb-2 uppercase tracking-tighter">Example Sentence</p>
                        <p className="text-lg font-medium mb-1">{kanjiOfTheDay.examples[0].sentence.japanese}</p>
                        <p className="text-sm text-primary font-mono">{kanjiOfTheDay.examples[0].sentence.romaji}</p>
                      </div>
                      
                      <Button 
                        className="w-full group/btn py-6 text-lg shadow-md"
                        onClick={() => {
                          setSelectedLevel(kanjiOfTheDay.jlptLevel);
                          // Find index of this kanji in its level
                          const levelKanji = getKanjiByLevel(kanjiOfTheDay.jlptLevel);
                          const index = levelKanji.findIndex(k => k.id === kanjiOfTheDay.id);
                          
                          const newProgress: UserProgress = {
                            ...progress,
                            currentLevel: kanjiOfTheDay.jlptLevel,
                            currentKanjiIndex: index !== -1 ? index : 0,
                          };
                          setProgress(newProgress);
                          saveProgressToStorage(newProgress);
                          setViewMode("learning");
                        }}
                      >
                        Study This Kanji Now
                        <ArrowRight className="ml-2 h-5 w-5 group-hover/btn:translate-x-1 transition-transform" />
                      </Button>
                    </div>
                  </div>
                </div>
              </Card>
            </div>
          )}
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
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-3 sm:gap-5 md:gap-8 min-h-[calc(100vh-120px)]">
          {/* Main Learning Area */}
          <div className="lg:col-span-2 order-2 lg:order-1 flex flex-col gap-3 sm:gap-5 min-h-[calc(100vh-180px)] sm:min-h-0">
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
            <div className="flex-1 flex">
              <FlashCard
                kanji={stats.currentKanji}
                currentExampleIndex={currentExampleIndex}
                onPrevious={goToPreviousExample}
                onNext={goToNextExample}
                onSpecificExample={goToSpecificExample}
                onComplete={handleKanjiComplete}
              />
            </div>

            {/* Navigation */}
            <div className="border-t pt-2 sm:pt-3">
              <div className="flex justify-between items-center">
                <div className="space-y-3 w-full">
                  <div className="flex justify-between items-center">
                    <span className="text-xs sm:text-sm text-muted-foreground font-medium">
                      <span className="hidden sm:inline">
                        Kanji {progress.currentKanjiIndex + 1} of {" "}
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
