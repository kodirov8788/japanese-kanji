"use client";

import { JLPTLevel, JLPTLevelInfo } from "@/types/kanji";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { JLPT_LEVELS } from "@/data/jlpt-levels";
import { BookOpen, Star, Users, Briefcase, Award } from "lucide-react";
import Image from "next/image";

interface LevelSelectorProps {
  selectedLevel: JLPTLevel;
  onLevelSelect: (level: JLPTLevel) => void;
  disabled?: JLPTLevel[];
}

const levelIcons = {
  N5: BookOpen,
  N4: Star,
  N3: Users,
  N2: Briefcase,
  N1: Award,
};

export function LevelSelector({
  selectedLevel,
  onLevelSelect,
  disabled = [],
}: LevelSelectorProps) {
  const levels = Object.values(JLPT_LEVELS) as JLPTLevelInfo[];

  return (
    <div className="space-y-3">
      {/* Logo Section */}
      <div className="text-center mb-6 sm:mb-8">
        <div className="flex justify-center mb-4">
          <div className="relative h-16 w-16 sm:h-20 sm:w-20">
            <Image
              src="/kanji-app.png"
              alt="KANJI APP Logo"
              fill
              className="object-contain"
              priority
            />
          </div>
        </div>
        <p className="text-sm sm:text-base text-muted-foreground">
          Master Japanese kanji from JLPT N5 to N1 levels
        </p>
      </div>

      <h2 className="text-lg sm:text-xl font-semibold text-center mb-4 sm:mb-6">
        Choose Your JLPT Level
      </h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-3 sm:gap-4">
        {levels.map((level) => {
          const Icon = levelIcons[level.level];
          const isSelected = selectedLevel === level.level;
          const isDisabled = disabled.includes(level.level);

          return (
            <Card
              key={level.level}
              className={`cursor-pointer transition-all duration-200 hover:scale-105 ${
                isSelected
                  ? "ring-2 ring-primary bg-primary/10 dark:bg-primary/20"
                  : isDisabled
                  ? "opacity-50 cursor-not-allowed"
                  : "hover:shadow-md"
              }`}
              onClick={() => !isDisabled && onLevelSelect(level.level)}
            >
              <CardHeader className="text-center pb-3">
                <div className="flex justify-center mb-3">
                  <div className={`p-3 rounded-full ${level.color} text-white`}>
                    <Icon className="h-6 w-6" />
                  </div>
                </div>
                <CardTitle className="text-lg">{level.name}</CardTitle>
                <Badge variant="outline" className="w-fit mx-auto">
                  {level.totalKanji} kanji
                </Badge>
              </CardHeader>
              <CardContent className="pt-0">
                <p className="text-sm text-muted-foreground text-center">
                  {level.description}
                </p>
                {isDisabled && (
                  <Button
                    variant="secondary"
                    size="sm"
                    className="w-full mt-3"
                    disabled
                  >
                    Locked
                  </Button>
                )}
              </CardContent>
            </Card>
          );
        })}
      </div>
    </div>
  );
}
