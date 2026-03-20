# Japanese Kanji

AI-assisted Kanji learning platform built with Next.js and TypeScript. The app lets learners move through JLPT levels, review example-rich flash cards, and keep progress locally in the browser.

**Live demo:** [japanese-kanji.vercel.app](https://japanese-kanji.vercel.app)

## What This Project Shows

- Product-focused frontend delivery for a real learning workflow
- Structured educational datasets with local validation gates
- Practical AI-assisted content expansion without making the app depend on a backend

## Why This Stack / Tooling

- **Next.js 15 + React 19** keep the product fast to iterate and easy to deploy as a static-first app.
- **TypeScript** protects the Kanji dataset and UI state from silent shape drift.
- **JSON datasets** keep the content portable and easy to validate without introducing database complexity.
- **Project workflow files** support long-running content operations, but the user-facing app remains simple to run.

## Stack

- Next.js 15
- React 19
- TypeScript
- Tailwind CSS 4
- Static JSON content

## Core Features

- JLPT level navigation from N5 through N1
- Flash-card based learning flow with examples, readings, and meanings
- Local progress persistence with study streak and completion tracking
- Dark mode and mobile-friendly layout
- Dataset validation script for content quality checks

## Getting Started

```bash
yarn install
yarn dev
```

Open [http://localhost:3000](http://localhost:3000).

## Quality Checks

```bash
yarn validate:data
yarn typecheck
yarn lint
yarn build
```

Run the full verification pass:

```bash
yarn qa
```

## Project Structure

- `src/app/`: application shell and main learning experience
- `src/components/`: reusable UI and learning components
- `src/data/kanji/`: JLPT dataset files
- `src/lib/kanji-utils.ts`: progress logic, dataset access, storage helpers
- `scripts/validate-kanji-data.mjs`: dataset validation for local and CI use
- `cursorkleosr/`: workflow memory and autonomous content operations

## Current Status

- N5, N4, N3, N2, and the current N1 dataset are wired into the product
- The app builds cleanly and can be run locally without external services
- Content growth is still ongoing, especially for deeper N1 coverage

## Why It Matters For Hiring

This repo shows product execution, data modeling, and maintainable frontend architecture in one place. It is stronger than a tutorial app because the core problem is real: delivering structured learning content with a workflow that can keep evolving.
