import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { ThemeProvider } from "@/components/theme-provider";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "KANJI APP | Japanese Kanji Learner | JLPT N5-N1",
  description:
    "Master Japanese kanji from JLPT N5 to N1 levels with comprehensive examples and progress tracking.",
  icons: {
    icon: "/kanji-app.png",
    shortcut: "/kanji-app.png",
    apple: "/kanji-app.png",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={inter.className}>
        <ThemeProvider
          attribute="class"
          defaultTheme="system"
          enableSystem
          disableTransitionOnChange
        >
          {children}
        </ThemeProvider>
      </body>
    </html>
  );
}
