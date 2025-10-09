# Japanese Kanji Project Configuration

## 🎯 Project Goal

Build a comprehensive Japanese kanji learning application with complete JLPT N5-N1 coverage, modern UI, and educational best practices.

## 🛠️ Tech Stack

- **Framework:** Next.js 15 with App Router
- **Language:** TypeScript 5 (strict mode)
- **Styling:** Tailwind CSS 4 + Shadcn UI + Radix UI
- **Data:** JSON-based kanji database
- **Icons:** Lucide React
- **Theme:** Next-themes (dark/light mode)

## 📁 Project Structure

```
src/
├── app/                    # Next.js app router pages
├── components/             # React components
│   ├── ui/                # Shadcn UI components
│   ├── kanji-card.tsx     # Main kanji display
│   ├── progress-bar.tsx   # Progress tracking
│   ├── level-selector.tsx # JLPT level selection
│   └── header.tsx         # Navigation
├── data/                   # Data files
│   ├── kanji/            # Kanji JSON files by level
│   └── jlpt-levels.ts    # JLPT level definitions
├── lib/                   # Utility functions
│   └── kanji-utils.ts   # Kanji data management
└── types/                 # TypeScript definitions
    └── kanji.ts          # Kanji-related types
```

## 🎨 Critical Patterns & Conventions

- Use functional components with TypeScript interfaces
- Define explicit interfaces for all props
- Implement proper error handling and validation
- Follow Next.js 15 App Router best practices
- Maintain 5-layer example format (Japanese/Romaji/English/Uzbek)
- Use consistent ID format (n5-001, n4-001, etc.)

## 🚫 Critical Limitations

- No hardcoded values (use environment variables)
- No security vulnerabilities
- No performance bottlenecks
- No accessibility issues
- No data format inconsistencies
- No TypeScript errors or warnings

## 📊 Current Data Status

- **N5:** 103 kanji (complete with 5+ examples each)
- **N4:** 167 kanji (complete, 5 enhanced with 5+ examples each)
- **N3:** 370 kanji (complete with 2 examples each)
- **N2:** 50 kanji (324 remaining - batches 10-15)
- **N1:** 0 kanji (1100 target - batches 16-37)

## 🔧 Quality Gates

- TypeScript compilation: `tsc --noEmit`
- Linting: `npm run lint`
- Build: `npm run build`
- Development: `npm run dev --turbopack`

## 🎯 Success Metrics

- Zero TypeScript errors
- Zero linting warnings
- Complete JLPT coverage (N5-N1)
- 5+ examples per kanji
- Mobile-first responsive design
- WCAG accessibility compliance
- < 3 second load times
