"use client";

import { LearningStats } from "@/types/kanji";
import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

interface MobileSummaryProps {
  stats: LearningStats;
  currentExampleIndex: number;
}

export function MobileSummary({
  stats,
  currentExampleIndex,
}: MobileSummaryProps) {
  const { currentKanji, progress } = stats;
  const totalExamples = currentKanji.examples.length;

  return (
    <Card className="sm:hidden bg-gradient-to-r from-blue-50 to-purple-50 dark:from-blue-900/20 dark:to-purple-900/20 border-blue-200 dark:border-blue-800">
      <CardContent className="pt-2 pb-2 px-3">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Badge variant="secondary" className="text-xs px-2 py-0.5">
              {currentKanji.jlptLevel}
            </Badge>
            <div className="text-xs font-medium text-gray-700 dark:text-gray-300">
              {progress.current}/{progress.total}
            </div>
          </div>
          <div className="text-xs text-gray-500 dark:text-gray-400">
            Ex {currentExampleIndex + 1}/{totalExamples}
          </div>
        </div>
        {/* Mini progress bar for examples */}
        <div className="mt-1">
          <div className="flex space-x-0.5">
            {Array.from({ length: Math.min(totalExamples, 8) }, (_, i) => (
              <div
                key={i}
                className={`h-1 flex-1 rounded ${
                  i === currentExampleIndex
                    ? "bg-blue-500"
                    : i < currentExampleIndex
                    ? "bg-green-500"
                    : "bg-gray-300 dark:bg-gray-600"
                }`}
              />
            ))}
            {totalExamples > 8 && (
              <div className="text-xs text-gray-400 ml-1">
                +{totalExamples - 8}
              </div>
            )}
          </div>
        </div>
      </CardContent>
    </Card>
  );
}
