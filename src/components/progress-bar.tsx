"use client";

import { Progress } from "@/components/ui/progress";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { LearningStats } from "@/types/kanji";

interface ProgressBarProps {
  stats: LearningStats;
}

export function ProgressBar({ stats }: ProgressBarProps) {
  const { progress, levelProgress } = stats;

  return (
    <Card className="w-full">
      <CardHeader className="pb-3">
        <CardTitle className="text-lg flex items-center gap-2">
          Learning Progress
          <Badge variant="secondary">{levelProgress.current}</Badge>
        </CardTitle>
      </CardHeader>
      <CardContent className="space-y-4">
        {/* Current Level Progress */}
        <div className="space-y-2">
          <div className="flex justify-between items-center text-sm">
            <span>Current Level ({levelProgress.current})</span>
            <span className="font-medium">
              {levelProgress.completed}/{levelProgress.total}
            </span>
          </div>
          <Progress value={levelProgress.percentage} className="h-3" />
          <div className="text-center text-sm text-muted-foreground">
            {levelProgress.percentage}% Complete
          </div>
        </div>

        {/* Kanji Count Progress */}
        <div className="space-y-2">
          <div className="flex justify-between items-center text-sm">
            <span>Kanji Progress</span>
            <span className="font-medium">
              {progress.current}/{progress.total}
            </span>
          </div>
          <Progress
            value={(progress.current / progress.total) * 100}
            className="h-2"
          />
          <div className="text-center text-xs text-muted-foreground">
            {progress.remaining} kanji remaining
          </div>
        </div>

        {/* Status Badges */}
        <div className="flex gap-2 justify-center pt-2">
          <Badge className="bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200">
            ✓ {levelProgress.completed} Completed
          </Badge>
          <Badge variant="outline">📚 Current: #{progress.current}</Badge>
        </div>
      </CardContent>
    </Card>
  );
}
