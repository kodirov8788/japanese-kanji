"use client";

import { Button } from "@/components/ui/button";
import { Moon, Sun, BookOpen } from "lucide-react";
import { useTheme } from "next-themes";
import { JLPTLevel } from "@/types/kanji";

interface HeaderProps {
  currentLevel: JLPTLevel;
  onLevelChange: (level: JLPTLevel) => void;
}

export function Header({ currentLevel, onLevelChange }: HeaderProps) {
  const { theme, setTheme } = useTheme();

  const toggleTheme = () => {
    setTheme(theme === "dark" ? "light" : "dark");
  };

  return (
    <header className="border-b border-gray-200 dark:border-gray-800">
      <div className="container mx-auto px-3 sm:px-4 py-3 sm:py-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2 sm:gap-3">
            <BookOpen className="h-6 w-6 sm:h-8 sm:w-8 text-primary" />
            <div>
              <h1 className="text-lg sm:text-2xl font-bold">
                Japanese Kanji Learner
              </h1>
              <p className="text-xs sm:text-sm text-muted-foreground hidden sm:block">
                Master JLPT kanji from N5 to N1
              </p>
            </div>
          </div>

          <div className="flex items-center gap-1 sm:gap-4">
            <div className="flex gap-1">
              <Button
                variant="outline"
                size="sm"
                onClick={() => onLevelChange("N5")}
                className={`text-xs px-2 ${
                  currentLevel === "N5" ? "bg-primary text-white" : ""
                }`}
              >
                N5
              </Button>
              <Button
                variant="outline"
                size="sm"
                onClick={() => onLevelChange("N4")}
                className={`text-xs px-2 ${
                  currentLevel === "N4" ? "bg-primary text-white" : ""
                }`}
              >
                N4
              </Button>
            </div>
            <div className="hidden sm:flex gap-1">
              <Button
                variant="outline"
                size="sm"
                onClick={() => onLevelChange("N3")}
                className={currentLevel === "N3" ? "bg-primary text-white" : ""}
              >
                N3
              </Button>
              <Button
                variant="outline"
                size="sm"
                onClick={() => onLevelChange("N2")}
                className={currentLevel === "N2" ? "bg-primary text-white" : ""}
              >
                N2
              </Button>
              <Button
                variant="outline"
                size="sm"
                onClick={() => onLevelChange("N1")}
                className={currentLevel === "N1" ? "bg-primary text-white" : ""}
              >
                N1
              </Button>
            </div>

            <div className="w-px h-6 bg-gray-300 dark:bg-gray-600" />

            <Button
              variant="ghost"
              size="sm"
              onClick={toggleTheme}
              className="p-2"
            >
              {theme === "dark" ? (
                <Sun className="h-4 w-4" />
              ) : (
                <Moon className="h-4 w-4" />
              )}
            </Button>
          </div>
        </div>
      </div>
    </header>
  );
}
