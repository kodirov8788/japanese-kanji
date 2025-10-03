# Japanese Kanji Learner

A comprehensive Next.js application for learning Japanese kanji from JLPT N5 to N1 levels with modern UI design and progress tracking.

## Features

- 🎯 **JLPT Level Structure**: Organized learning path from N5 to N1
- 📚 **Comprehensive Kanji Data**: Complete kanji database with readings, meanings, and examples
- 🎨 **Modern UI**: Built with Next.js, TypeScript, Tailwind CSS, and Shadcn UI
- 📱 **Mobile-First Design**: Optimized for smartphones with touch-friendly interactions
- 💡 **Adaptive Interface**: Compact mobile summary cards and expandable desktop views
- 🌙 **Dark Mode**: Toggle between light and dark themes
- 📊 **Progress Tracking**: Track your learning journey with statistics
- 🎵 **Audio Support**: Proper pronunciation guides with romaji
- 📝 **Example Sentences**: Real-world usage with 5-layer format (Japanese, Spoken Japanese, Romaji, English, Uzbek)
- 💾 **Local Storage**: Progress automatically saved in your browser

## Sample Output Format

The application provides detailed kanji information in this format:

```
Perfect 👍 The next JLPT N4 kanji is 教（きょう・おしえる・おそわる）, meaning teach, instruct.
We're at Kanji #63 of 167 → 104 left.
(Progress: about 38% complete ✅)

Here are 5 common compounds with example sentences in the 5-layer format:

1. 教える（おしえる） to teach, to tell
   先生が日本語を教える。
   せんせいがにほんごをおしえる
   Romaji: Sensei ga Nihongo o oshieru.
   English: The teacher teaches Japanese.
   Uzbek: O'qituvchi yapon tilini o'qitadi.

2. 教わる（おそわる） to be taught, to learn
   彼にピアノを教わった。
   かれにピアノをおそわった
   Romaji: Kare ni piano o osowatta.
   English: I learned piano from him.
   Uzbek: Men undan pianino chalishni o'rgandim.
```

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd japanese-kanji
```

2. Install dependencies:

```bash
npm install
```

3. Run the development server:

```bash
npm run dev
```

## Technology Stack

- **Frontend**: Next.js 15 with App Router
- **Language**: TypeScript for type safety
- **Styling**: Tailwind CSS for utility-first styling
- **UI Components**: Shadcn UI for modern, accessible components
- **Icons**: Lucide React for beautiful icons
- **Theme**: Next-themes for dark/light mode support
- **Data**: JSON-based kanji database

## Project Structure

```
src/
├── app/                    # Next.js app router pages
├── components/             # React components
│   ├── ui/                # Shadcn UI components
│   ├── kanji-card.tsx     # Main kanji display component
│   ├── progress-bar.tsx   # Progress tracking component
│   ├── level-selector.tsx # JLPT level selection
│   ├── header.tsx         # Navigation header
│   └── theme-provider.tsx # Theme management
├── data/                   # Data files
│   ├── kanji/            # Kanji JSON files by JLPT level
│   └── jlpt-levels.ts    # JLPT level definitions
├── lib/                   # Utility functions
│   └── kanji-utils.ts   # Kanji data management
└── types/                 # TypeScript type definitions
    └── kanji.ts          # Kanji-related types
```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint
- `npx shadcn add <component>` - Add new Shadcn UI components

## Usage

1. **Select JLPT Level**: Choose from N5 to N1 difficulty levels
2. **Study Kanji**: View kanji with detailed information including readings, meanings, and examples
3. **Track Progress**: Monitor your advancement through each level
4. **View Examples**: Learn kanji through common compounds with example sentences
5. **Practice Writing**: Use practice mode for stroke order (future feature)

## Contributing

This project follows modern development practices:

- TypeScript strict mode enabled
- ESLint configuration for code quality
- Tailwind CSS for consistent styling
- Component-based architecture
- Mobile-first responsive design

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Roadmap

Future features planned:

- Audio pronunciation support
- Stroke order animations
- Spaced repetition algorithm
- Progress analytics
- Export study sessions
- Offline support with PWA
- Kanji recognition quizzes
