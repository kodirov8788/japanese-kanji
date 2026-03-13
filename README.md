# 🎌 Japanese Kanji — Autonomous Learning Enhancement

An AI-driven language education platform designed to accelerate Kanji mastery from JLPT N3 to N1 levels. This repository showcases an innovative **Agentic AI Workflow**, featuring automated expansion strategies and autonomous state management.

![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat&logo=nextdotjs&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white)
![Agentic AI](https://img.shields.io/badge/Workflow-Agentic%20AI-orange?style=flat&logo=openai)
![Level](https://img.shields.io/badge/JLPT-N3%20%E2%86%92%20N1-red)

---

## 🧠 What Makes This Unique?

Unlike standard flashcard apps, this project implements a **Self-Optimizing Learning System**:

- **Autonomous Learning Protocol**: Uses a sophisticated "Long-Term Memory" (LTM) and "Short-Term Memory" (STM) architecture to track learning phases and quality gates.
- **N1 Expansion Strategy**: A data-driven approach to programmatically enhance N3 vocabulary into N1 proficiency levels using AI agents.
- **Agentic State Tracking**: Continuous synchronization between local JSON registries (`enhancement_progress.json`) and AI-managed memory files.
- **Automated Validation**: Integrated scripts (`autonomous.sh`) for verifying Kanji analysis results and maintaining data integrity.

---

## 🏗️ Project Components

- **`src/`**: Modern Next.js frontend for Kanji visualization and practice.
- **`cursorkleosr/`**: Central "Source of Truth" for the AI Agent, containing project configuration and workflow state.
- **`scripts/`**: Automation tools for Kanji expansion and analysis.
- **`kanji_analysis_results.json`**: Real-time registry of Kanji mastered and pending enhancement.

---

## 🔄 Autonomous Workflow

The project operates on a rigorous cycle of:
1. **Context Reading**: Source of truth analysis.
2. **Rule Coordination**: Aligning with phase goals (N3 to N1).
3. **Agentic Execution**: Automated coding and data enhancement.
4. **State Persistence**: Updating progress registries.

---

## 📄 Documentation

For deep dives into the architecture:
- [Autonomous Workflow Protocol](./AUTONOMOUS_WORKFLOW.md)
- [N1 Expansion Strategy](./N1_EXPANSION_STRATEGY.md)

---

## 📄 License
Apache 2.0 — Developed by [Kodirov Dev](https://github.com/kodirov8788)
