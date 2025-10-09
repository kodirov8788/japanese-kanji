# Autonomous AI Workflow Guide

# Based on Cursor Forum: https://forum.cursor.com/t/guide-a-simpler-more-autonomous-ai-workflow-for-cursor-new-update/70688/22?page=2

## 🎯 Two-File System

### Long-Term Memory (LTM): `cursorkleosr/project-config.md`

- Project goals, tech stack, structure
- Critical patterns and conventions
- Quality gates and success metrics
- Current data status

### Short-Term Memory (STM): `cursorkleosr/workflow_state.md`

- Current phase and progress
- Rules and execution standards
- Plan and next actions
- Autonomous execution protocol

## 🔄 Autonomous Workflow Protocol

### 1. Read Sources of Truth

```bash
# Always read these files before any action
- cursorkleosr/project-config.md (LTM)
- cursorkleosr/workflow_state.md (STM)
```

### 2. Consult Rules

- Check `## Rules` section based on current `## State`
- Follow quality gates and execution standards
- Maintain code quality requirements

### 3. Act via Cursor

- Execute planned actions through Cursor tools
- Follow TypeScript and linting standards
- Implement proper error handling

### 4. Update State

- Immediately update `workflow_state.md` after each action
- Track progress and phase changes
- Log completion status

### 5. Check TODO

- Look at `todo.md` for next unchecked task
- Work on tasks in priority order
- Mark completed tasks with [x]

## 📋 Task Management

### todo.md Format

```markdown
# TODO

- [x] Completed task
  - Detail 1
  - Detail 2
- [ ] Next task to work on
  - Specific instruction 1
  - Specific instruction 2
  - etc
```

## 🚀 Usage

### Start Autonomous Workflow

```bash
./autonomous.sh
```

### Cursor AI Prompt

```
You are an autonomous AI developer using a two-file system. Your sole sources of truth are @project_config.md (LTM) and @workflow_state.md (STM/Rules/Log). Before every action, read workflow_state.md, consult ## Rules based on ## State, act via Cursor, then immediately update workflow_state.md. Look at @todo.md and work on the next unchecked task.
```

## 🔧 Quality Gates

### Mandatory Checks

- TypeScript compilation: `tsc --noEmit`
- Linting: `npm run lint`
- Build: `npm run build`
- Data validation: All kanji data must be valid JSON

### Execution Standards

- Batch Strategy: 50 kanji per batch, 5 per iteration
- Progress Tracking: Real-time updates in AI Work Log
- Error Handling: Automatic rollback on failures
- Code Quality: Zero TypeScript errors, zero linting warnings

## 📊 Current Status

- **N5:** 103 kanji (complete with 5+ examples each)
- **N4:** 167 kanji (complete, 5 enhanced with 5+ examples each)
- **N3:** 370 kanji (complete with 5+ examples each)
- **N2:** 374 kanji (complete with 5+ examples each)
- **N1:** 0 kanji (1100 target - Strategy Complete, Ready for Implementation)

## 🎯 Next Actions - N1 Implementation Phases

### Phase 1: Data Structure Setup (1-2 days)

1. Create N1 data structure and TypeScript interfaces
2. Set up batch processing scripts and validation
3. Create n1-complete.json with empty structure
4. Update jlpt-levels.ts configuration

### Phase 2: Batch Processing (22 batches, 8-11 days)

1. **Batch 1:** n1-001 to n1-050 (2-3 hours)
2. **Batch 2:** n1-051 to n1-100 (2-3 hours)
3. **Batch 3:** n1-101 to n1-150 (2-3 hours)
4. **Batch 4:** n1-151 to n1-200 (2-3 hours)
5. **Batch 5:** n1-201 to n1-250 (2-3 hours)
6. **Batch 6:** n1-251 to n1-300 (2-3 hours)
7. **Batch 7:** n1-301 to n1-350 (2-3 hours)
8. **Batch 8:** n1-351 to n1-400 (2-3 hours)
9. **Batch 9:** n1-401 to n1-450 (2-3 hours)
10. **Batch 10:** n1-451 to n1-500 (2-3 hours)
11. **Batch 11:** n1-501 to n1-550 (2-3 hours)
12. **Batch 12:** n1-551 to n1-600 (2-3 hours)
13. **Batch 13:** n1-601 to n1-650 (2-3 hours)
14. **Batch 14:** n1-651 to n1-700 (2-3 hours)
15. **Batch 15:** n1-701 to n1-750 (2-3 hours)
16. **Batch 16:** n1-751 to n1-800 (2-3 hours)
17. **Batch 17:** n1-801 to n1-850 (2-3 hours)
18. **Batch 18:** n1-851 to n1-900 (2-3 hours)
19. **Batch 19:** n1-901 to n1-950 (2-3 hours)
20. **Batch 20:** n1-951 to n1-1000 (2-3 hours)
21. **Batch 21:** n1-1001 to n1-1050 (2-3 hours)
22. **Batch 22:** n1-1051 to n1-1100 (2-3 hours)

### Phase 3: Quality Assurance (2-3 days)

1. Data validation and integrity checks
2. Example enhancement and verification
3. Performance testing and optimization
4. UI integration testing

### Phase 4: Final Integration (1 day)

1. Complete N1 data integration
2. Final quality gates validation
3. Performance optimization
4. Documentation updates

## 📈 N1 Implementation Timeline

### Total Estimated Time: 11-16 days

- **Phase 1:** 1-2 days (Data Structure Setup)
- **Phase 2:** 8-11 days (Batch Processing - 22 batches)
- **Phase 3:** 2-3 days (Quality Assurance)
- **Phase 4:** 1 day (Final Integration)

### Progress Tracking

- **Current:** N1 Strategy Complete (0/1100)
- **Target:** N1 Complete (1100/1100)
- **Batches:** 22 batches of 50 kanji each
- **Quality Gates:** TypeScript compilation after each iteration

### Success Metrics

- **Data Integrity:** 100% valid JSON
- **TypeScript Errors:** 0 errors
- **Build Success:** 100% success rate
- **Performance:** < 3 second load times
- **Example Quality:** 5+ examples per kanji
