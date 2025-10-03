"use client";

import { KanjiData } from "@/types/kanji";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Eye, EyeOff } from "lucide-react";
import { useState } from "react";

interface KanjiCardProps {
  kanji: KanjiData;
  onComplete: () => void;
}

export function KanjiCard({ kanji, onComplete }: KanjiCardProps) {
  const [showReadings, setShowReadings] = useState(false);
  const [currentExample, setCurrentExample] = useState(0);

  const onReadings = kanji.readings.on || [];
  const kunReadings = kanji.readings.kun || [];

  const nextExample = () => {
    setCurrentExample((prev) => (prev + 1) % kanji.examples.length);
  };

  const prevExample = () => {
    setCurrentExample(
      (prev) => (prev - 1 + kanji.examples.length) % kanji.examples.length
    );
  };

  return (
    <Card className="w-full max-w-2xl mx-auto">
      <CardHeader className="text-center p-4 sm:p-6">
        <div className="flex justify-center items-center gap-2 sm:gap-4 mb-4">
          <Badge variant="secondary" className="text-sm sm:text-lg">
            {kanji.jlptLevel}
          </Badge>
          <div className="text-6xl sm:text-8xl font-bold text-primary">
            {kanji.kanji}
          </div>
          <Badge variant="outline" className="text-xs sm:text-sm">
            {kanji.strokes} strokes
          </Badge>
        </div>
        <CardTitle className="text-xl font-semibold text-center">
          {kanji.meanings.join(", ")}
        </CardTitle>
      </CardHeader>

      <CardContent className="space-y-4 sm:space-y-6 p-4 sm:p-6">
        {/* Readings Section */}
        <div className="space-y-3">
          <div className="flex items-center gap-2">
            <Button
              variant="outline"
              size="sm"
              onClick={() => setShowReadings(!showReadings)}
              className="flex items-center gap-2 w-full sm:w-auto"
            >
              {showReadings ? (
                <EyeOff className="h-4 w-4" />
              ) : (
                <Eye className="h-4 w-4" />
              )}
              <span className="hidden sm:inline">
                {showReadings ? "Hide Readings" : "Show Readings"}
              </span>
              <span className="sm:hidden">
                {showReadings ? "Hide" : "Show"}
              </span>
            </Button>
          </div>

          {showReadings && (
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4">
              <div className="bg-slate-50 dark:bg-slate-800 p-3 rounded-lg">
                <Badge variant="default" className="mb-2">
                  On-yomi
                </Badge>
                <div className="flex gap-2 flex-wrap">
                  {onReadings.map((reading, index) => (
                    <span key={index} className="font-mono text-lg">
                      {reading}
                    </span>
                  ))}
                </div>
              </div>

              <div className="bg-slate-50 dark:bg-slate-800 p-3 rounded-lg">
                <Badge variant="default" className="mb-2">
                  Kun-yomi
                </Badge>
                <div className="flex gap-2 flex-wrap">
                  {kunReadings.map((reading, index) => (
                    <span key={index} className="font-mono text-lg">
                      {reading}
                    </span>
                  ))}
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Examples Section */}
        {kanji.examples.length > 0 && (
          <div className="space-y-3">
            <h4 className="font-semibold text-lg">
              Common Compounds with Example Sentences:
            </h4>

            {kanji.examples.map((example, index) => (
              <div
                key={index}
                className={`p-4 rounded-lg border transition-all duration-200 ${
                  index === currentExample
                    ? "border-primary bg-primary/10 dark:bg-primary/20"
                    : "border-border hover:border-primary/50"
                }`}
              >
                <div className="space-y-3">
                  {/* Example header */}
                  <div className="flex items-center justify-between">
                    <div>
                      <span className="font-bold text-lg text-primary">
                        {example.word}
                      </span>
                      <div className="text-sm text-muted-foreground mt-1">
                        <Badge variant="outline" className="mr-2">
                          {example.reading}
                        </Badge>
                        <span className="font-medium">{example.meaning}</span>
                      </div>
                    </div>
                    {kanji.examples.length > 1 && (
                      <div className="flex gap-1">
                        <Button
                          variant="outline"
                          size="sm"
                          onClick={nextExample}
                          className="text-xs"
                        >
                          Next
                        </Button>
                        <Button
                          variant="outline"
                          size="sm"
                          onClick={prevExample}
                          className="text-xs"
                        >
                          Prev
                        </Button>
                      </div>
                    )}
                  </div>

                  {/* Example sentence in 5-layer format */}
                  <div className="space-y-2">
                    <div className="text-xl font-medium">
                      {example.sentence.japanese}
                    </div>
                    <div className="text-lg font-mono text-primary">
                      {example.sentence.romaji}
                    </div>
                    <div className="text-sm text-muted-foreground italic">
                      English: {example.sentence.english}
                    </div>
                    <div className="text-sm text-orange-600 dark:text-orange-400">
                      Uzbek: {example.sentence.uzbek}
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}

        {/* Action Buttons */}
        <div className="flex flex-col sm:flex-row gap-3 pt-4 border-t">
          <Button size="lg" className="w-full sm:flex-1" onClick={onComplete}>
            ✓ I&apos;ve studied this kanji
          </Button>
          <Button variant="outline" size="lg" className="w-full sm:w-auto">
            Practice Writing
          </Button>
        </div>
      </CardContent>
    </Card>
  );
}
