"use client";

import { useState } from "react";
import { KanjiData } from "@/types/kanji";
import { Card, CardContent, CardHeader } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { ChevronLeft, ChevronRight } from "lucide-react";

interface FlashCardProps {
  kanji: KanjiData;
  currentExampleIndex: number;
  onPrevious: () => void;
  onNext: () => void;
  onSpecificExample?: (index: number) => void;
  onComplete: () => void;
}

type TranslationLayer = "romaji" | "english" | "uzbek";

const TRANSLATION_LAYERS: Array<{ key: TranslationLayer; label: string }> = [
  { key: "romaji", label: "Romaji" },
  { key: "english", label: "English" },
  { key: "uzbek", label: "Uzbek" },
];

export function FlashCard({
  kanji,
  currentExampleIndex,
  onPrevious,
  onNext,
  onSpecificExample,
  onComplete,
}: FlashCardProps) {
  const [activeLayer, setActiveLayer] = useState<
    "none" | TranslationLayer
  >("none");
  const [visitedLayers, setVisitedLayers] = useState<Set<TranslationLayer>>(
    () => new Set()
  );

  const example = kanji.examples[currentExampleIndex];
  const totalExamples = kanji.examples.length;

  if (!example) {
    console.error(
      `No example found at index ${currentExampleIndex} for kanji ${kanji.kanji}`
    );
    return null;
  }

  const resetLayers = () => {
    setActiveLayer("none");
    setVisitedLayers(new Set());
  };

  const handlePrevious = () => {
    resetLayers();
    onPrevious();
  };

  const handleNext = () => {
    resetLayers();
    onNext();
  };

  const handleSpecificExample = (index: number) => {
    resetLayers();
    onSpecificExample?.(index);
  };

  const handleLayerToggle = (layer: TranslationLayer) => {
    setActiveLayer((current) => (current === layer ? "none" : layer));
    setVisitedLayers((current) => {
      const next = new Set(current);
      next.add(layer);
      return next;
    });
  };

  const allLayersViewed = TRANSLATION_LAYERS.every(({ key }) =>
    visitedLayers.has(key)
  );

  return (
    <div className="w-full max-w-2xl mx-auto flex flex-col h-full">
      {/* Kanji Header */}
      <Card className="mb-2 py-1 sm:mb-4 bg-gradient-to-br from-blue-50 to-indigo-50 dark:from-blue-900/20 dark:to-indigo-900/20">
        <CardHeader className="text-center sm:py-2 px-3 sm:px-6">
          <div className="block sm:hidden">
            <div className="text-2xl font-bold text-primary mb-0.5">
              {kanji.kanji}
            </div>
            <div className="text-xs font-medium text-gray-700 dark:text-gray-300">
              {kanji.meanings.join(", ")}
            </div>
          </div>

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

      {/* Example card */}
      <Card className="flex-1 flex flex-col overflow-hidden">
        <CardHeader className="text-center pb-1 sm:pb-2 px-3 sm:px-6 pt-2 sm:pt-3">
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

        <CardContent className="flex-1 flex flex-col px-3 sm:px-6 py-2 sm:py-3 overflow-hidden">
          <div className="text-center mb-2 sm:mb-4">
            <div className="text-lg sm:text-xl md:text-2xl font-medium p-3 bg-slate-100 dark:bg-slate-800 rounded-lg min-h-[86px] flex items-center justify-center">
              {example.sentence.japanese}
            </div>
          </div>

          <div className="flex-1 flex flex-col space-y-2 sm:space-y-3">
            <div className="grid grid-cols-3 gap-1">
              {TRANSLATION_LAYERS.map((layer) => (
                <Button
                  key={layer.key}
                  variant={activeLayer === layer.key ? "default" : "outline"}
                  size="sm"
                  className="h-9 text-xs sm:text-sm"
                  onClick={() => handleLayerToggle(layer.key)}
                >
                  {layer.label}
                </Button>
              ))}
            </div>

            <div className="flex-1 border border-dashed border-slate-300 dark:border-slate-600 rounded-lg p-3 bg-slate-50 dark:bg-slate-800/40 text-left overflow-auto">
              {activeLayer === "none" && (
                <p className="text-xs sm:text-sm text-muted-foreground text-center">
                  Choose a layer to reveal the translation.
                </p>
              )}
              {activeLayer === "romaji" && (
                <p className="text-sm sm:text-lg font-mono text-gray-700 dark:text-gray-300">
                  {example.sentence.romaji}
                </p>
              )}
              {activeLayer === "english" && (
                <p className="text-sm sm:text-base text-blue-900 dark:text-blue-200">
                  {example.sentence.english}
                </p>
              )}
              {activeLayer === "uzbek" && (
                <p className="text-sm sm:text-base text-orange-800 dark:text-orange-200">
                  {example.sentence.uzbek}
                </p>
              )}
            </div>
          </div>

          <div className="flex gap-2 sm:gap-3 pt-2 sm:pt-3 border-t mt-2">
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

            <div className="hidden sm:flex items-center gap-1">
              {Array.from({ length: Math.min(totalExamples, 6) }, (_, i) => (
                <Button
                  key={i}
                  variant={i === currentExampleIndex ? "default" : "outline"}
                  size="sm"
                  className="w-8 h-8 p-0 text-xs"
                  onClick={() => handleSpecificExample(i)}
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

          <div className="pt-2 sm:pt-3">
            <Button
              size="lg"
              className="w-full h-10 sm:h-11 text-sm sm:text-base"
              onClick={onComplete}
              disabled={!allLayersViewed}
            >
              ✓ Complete Example {currentExampleIndex + 1}/{totalExamples}
            </Button>
            {!allLayersViewed && (
              <p className="text-[11px] sm:text-xs text-muted-foreground text-center mt-1">
                View Romaji, English, and Uzbek to unlock completion.
              </p>
            )}
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
