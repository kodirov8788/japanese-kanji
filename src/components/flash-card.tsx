"use client";

import { KanjiData } from "@/types/kanji";
import { Card, CardContent, CardHeader } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { ChevronLeft, ChevronRight, Eye, EyeOff } from "lucide-react";
import { useState } from "react";

interface FlashCardProps {
  kanji: KanjiData;
  currentExampleIndex: number;
  onPrevious: () => void;
  onNext: () => void;
  onSpecificExample?: (index: number) => void;
  onComplete: () => void;
}

export function FlashCard({
  kanji,
  currentExampleIndex,
  onPrevious,
  onNext,
  onSpecificExample,
  onComplete,
}: FlashCardProps) {
  const [showRomaji, setShowRomaji] = useState(false);
  const [showEnglish, setShowEnglish] = useState(false);
  const [showUzbek, setShowUzbek] = useState(false);

  const example = kanji.examples[currentExampleIndex];
  const totalExamples = kanji.examples.length;

  const resetShowStates = () => {
    setShowRomaji(false);
    setShowEnglish(false);
    setShowUzbek(false);
  };

  const handlePrevious = () => {
    resetShowStates();
    onPrevious();
  };

  const handleNext = () => {
    resetShowStates();
    onNext();
  };

  return (
    <div className="w-full max-w-2xl mx-auto">
      {/* Kanji Header - Mobile shows simplified version */}
      <Card className=" mb-2 py-1 sm:mb-4 bg-gradient-to-br from-blue-50 to-indigo-50 dark:from-blue-900/20 dark:to-indigo-900/20">
        <CardHeader className="text-center  sm:py-2 px-3 sm:px-6">
          {/* Mobile: Only kanji + meanings */}
          <div className="block sm:hidden">
            <div className="text-2xl font-bold text-primary mb-0.5">
              {kanji.kanji}
            </div>
            <div className="text-xs font-medium text-gray-700 dark:text-gray-300">
              {kanji.meanings.join(", ")}
            </div>
          </div>

          {/* Desktop: Full header with N5 badge */}
          <div className="hidden sm:block">
            <div className="flex justify-center items-center gap-1 mb-1">
              <Badge variant="secondary" className="text-sm">
                {kanji.jlptLevel}
              </Badge>
              <div className="text-4xl md:text-6xl font-bold text-primary">
                {kanji.kanji}
              </div>
              <Badge variant="outline" className="text-xs">
                {kanji.strokes}
              </Badge>
            </div>
            <div className="text-lg font-medium text-gray-700 dark:text-gray-300">
              {kanji.meanings.join(", ")}
            </div>
            <div className="text-xs text-gray-500 dark:text-gray-400 mt-0.5">
              Example {currentExampleIndex + 1} of {totalExamples}
            </div>
            {/* Progress indicator for desktop */}
            <div className="mt-1">
              <div className="flex justify-center space-x-1">
                {Array.from({ length: totalExamples }, (_, i) => (
                  <div
                    key={i}
                    className={`w-3 h-3 rounded-full ${
                      i === currentExampleIndex
                        ? "bg-blue-500"
                        : i < currentExampleIndex
                        ? "bg-green-500"
                        : "bg-gray-300 dark:bg-gray-600"
                    }`}
                  />
                ))}
              </div>
            </div>
          </div>
        </CardHeader>
      </Card>

      {/* Example Word Card */}
      <Card className="min-h-[280px] sm:min-h-[450px] flex flex-col">
        <CardHeader className="text-center pb-1 sm:pb-2 px-3 sm:px-6 pt-2 sm:pt-3 ">
          <div className="space-y-1">
            <div className="text-xl sm:text-2xl md:text-3xl font-bold text-primary mb-1">
              {example.word}
            </div>
            <div className="flex justify-center gap-2 flex-wrap">
              <Badge variant="default" className="text-xs sm:text-sm px-2 py-1">
                {example.reading}
              </Badge>
              <Badge variant="outline" className="text-xs sm:text-sm px-2 py-1">
                {example.meaning}
              </Badge>
            </div>
            {/* Context indicator */}
            <div className="text-xs text-gray-500 dark:text-gray-400 mt-0.5">
              {currentExampleIndex === 0 && "Basic usage"}
              {currentExampleIndex === 1 && "Daily life"}
              {currentExampleIndex === 2 && "Academic context"}
              {currentExampleIndex === 3 && "Professional usage"}
              {currentExampleIndex === 4 && "Casual conversation"}
              {currentExampleIndex === 5 && "Formal context"}
              {currentExampleIndex > 5 && "Additional usage"}
            </div>
          </div>
        </CardHeader>

        <CardContent className="flex-1 flex flex-col justify-between px-3 sm:px-6 py-2 sm:py-3">
          {/* Japanese Sentence */}
          <div className="text-center mb-3 sm:mb-6">
            <div className="text-lg sm:text-xl md:text-2xl font-medium mb-2 sm:mb-4 p-3 bg-slate-100 dark:bg-slate-800 rounded-lg">
              {example.sentence.japanese}
            </div>

            {/* Revealable Translation */}
            <div className="space-y-2">
              {/* Romaji */}
              <Button
                variant={showRomaji ? "default" : "outline"}
                onClick={() => setShowRomaji(!showRomaji)}
                className="w-full flex items-center gap-2 h-9 sm:h-10 text-sm sm:text-base"
              >
                {showRomaji ? (
                  <EyeOff className="h-4 w-4" />
                ) : (
                  <Eye className="h-4 w-4" />
                )}
                {showRomaji ? "Hide" : "Show"} Romaji
              </Button>

              {showRomaji && (
                <span className="block text-sm sm:text-lg font-mono text-gray-600 dark:text-gray-400 p-3 bg-slate-50 dark:bg-slate-700 rounded-lg">
                  {example.sentence.romaji}
                </span>
              )}

              {/* English */}
              <Button
                variant={showEnglish ? "default" : "outline"}
                onClick={() => setShowEnglish(!showEnglish)}
                className="w-full flex items-center gap-2 h-9 sm:h-10 text-sm sm:text-base"
              >
                {showEnglish ? (
                  <EyeOff className="h-4 w-4" />
                ) : (
                  <Eye className="h-4 w-4" />
                )}
                {showEnglish ? "Hide" : "Show"} English
              </Button>

              {showEnglish && (
                <div className="text-left p-3 bg-blue-50 dark:bg-blue-900/20 rounded-lg">
                  <span className="text-sm text-blue-800 dark:text-blue-200">
                    English: {example.sentence.english}
                  </span>
                </div>
              )}

              {/* Uzbek */}
              <Button
                variant={showUzbek ? "default" : "outline"}
                onClick={() => setShowUzbek(!showUzbek)}
                className="w-full flex items-center gap-2 h-9 sm:h-10 text-sm sm:text-base"
              >
                {showUzbek ? (
                  <EyeOff className="h-4 w-4" />
                ) : (
                  <Eye className="h-4 w-4" />
                )}
                {showUzbek ? "Hide" : "Show"} Uzbek
              </Button>

              {showUzbek && (
                <div className="text-left p-3 bg-orange-50 dark:bg-orange-900/20 rounded-lg">
                  <span className="text-sm text-orange-800 dark:text-orange-200">
                    Uzbek: {example.sentence.uzbek}
                  </span>
                </div>
              )}
            </div>
          </div>

          {/* Navigation */}
          <div className="flex gap-2 sm:gap-3 pt-2 sm:pt-3 border-t">
            <Button
              variant="outline"
              onClick={handlePrevious}
              disabled={currentExampleIndex === 0}
              className="flex items-center gap-1 sm:gap-2 flex-1 h-9 sm:h-10 text-sm"
            >
              <ChevronLeft className="h-4 w-4" />
              <span className="hidden sm:inline">Previous</span>
              <span className="sm:hidden">Prev</span>
            </Button>

            {/* Example selector for desktop */}
            <div className="hidden sm:flex items-center gap-1">
              {Array.from({ length: Math.min(totalExamples, 6) }, (_, i) => (
                <Button
                  key={i}
                  variant={i === currentExampleIndex ? "default" : "outline"}
                  size="sm"
                  className="w-8 h-8 p-0 text-xs"
                  onClick={() => {
                    resetShowStates();
                    onSpecificExample?.(i);
                  }}
                >
                  {i + 1}
                </Button>
              ))}
              {totalExamples > 6 && (
                <span className="text-xs text-gray-500 ml-1">
                  +{totalExamples - 6}
                </span>
              )}
            </div>

            <Button
              variant="outline"
              onClick={handleNext}
              disabled={currentExampleIndex >= totalExamples - 1}
              className="flex items-center gap-1 sm:gap-2 flex-1 h-9 sm:h-10 text-sm"
            >
              <span className="hidden sm:inline">Next</span>
              <span className="sm:hidden">Next</span>
              <ChevronRight className="h-4 w-4" />
            </Button>
          </div>

          {/* Complete Kanji Button */}
          <div className="pt-2 sm:pt-3">
            <Button
              size="lg"
              className="w-full h-10 sm:h-11 text-sm sm:text-base"
              onClick={onComplete}
              disabled={!showRomaji || !showEnglish || !showUzbek}
            >
              ✓ Complete Example {currentExampleIndex + 1}/{totalExamples}
            </Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
