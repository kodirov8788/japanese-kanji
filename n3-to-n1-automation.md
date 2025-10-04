# N3 to N1 Kanji Expansion Automation Plan

## 🎯 Objective

Systematically expand N3 kanji dataset to complete N1 level (370 total kanji) using 50-kanji batches, then continue with N2 and N1 levels.

## 📊 Current Status

- **N3 Current:** 370 kanji (100% of 370 target) ✅ COMPLETE!
- **N3 Remaining:** 0 kanji - N3 LEVEL COMPLETE! 🎉
- **N2 Target:** 374 kanji
- **N1 Target:** 1100 kanji

## 🔄 Batch Process Workflow

### Phase 1: Complete N3 ✅ COMPLETED!

- [x] **Batch 5:** Add N3 kanji 243-292 (50 kanji)
- [x] **Batch 6:** Add N3 kanji 293-342 (50 kanji)
- [x] **Batch 7:** Add N3 kanji 343-370 (28 kanji) - Final N3 batch ✅

### Phase 2: Complete N2 (374 kanji)

- [ ] **Batch 8:** Add N2 kanji 1-50 (50 kanji)
- [ ] **Batch 9:** Add N2 kanji 51-100 (50 kanji)
- [ ] **Batch 10:** Add N2 kanji 101-150 (50 kanji)
- [ ] **Batch 11:** Add N2 kanji 151-200 (50 kanji)
- [ ] **Batch 12:** Add N2 kanji 201-250 (50 kanji)
- [ ] **Batch 13:** Add N2 kanji 251-300 (50 kanji)
- [ ] **Batch 14:** Add N2 kanji 301-350 (50 kanji)
- [ ] **Batch 15:** Add N2 kanji 351-374 (24 kanji) - Final N2 batch

### Phase 3: Complete N1 (1100 kanji)

- [ ] **Batch 16:** Add N1 kanji 1-50 (50 kanji)
- [ ] **Batch 17:** Add N1 kanji 51-100 (50 kanji)
- [ ] **Batch 18:** Add N1 kanji 101-150 (50 kanji)
- [ ] **Batch 19:** Add N1 kanji 151-200 (50 kanji)
- [ ] **Batch 20:** Add N1 kanji 201-250 (50 kanji)
- [ ] **Batch 21:** Add N1 kanji 251-300 (50 kanji)
- [ ] **Batch 22:** Add N1 kanji 301-350 (50 kanji)
- [ ] **Batch 23:** Add N1 kanji 351-400 (50 kanji)
- [ ] **Batch 24:** Add N1 kanji 401-450 (50 kanji)
- [ ] **Batch 25:** Add N1 kanji 451-500 (50 kanji)
- [ ] **Batch 26:** Add N1 kanji 501-550 (50 kanji)
- [ ] **Batch 27:** Add N1 kanji 551-600 (50 kanji)
- [ ] **Batch 28:** Add N1 kanji 601-650 (50 kanji)
- [ ] **Batch 29:** Add N1 kanji 651-700 (50 kanji)
- [ ] **Batch 30:** Add N1 kanji 701-750 (50 kanji)
- [ ] **Batch 31:** Add N1 kanji 751-800 (50 kanji)
- [ ] **Batch 32:** Add N1 kanji 801-850 (50 kanji)
- [ ] **Batch 33:** Add N1 kanji 851-900 (50 kanji)
- [ ] **Batch 34:** Add N1 kanji 901-950 (50 kanji)
- [ ] **Batch 35:** Add N1 kanji 951-1000 (50 kanji)
- [ ] **Batch 36:** Add N1 kanji 1001-1050 (50 kanji)
- [ ] **Batch 37:** Add N1 kanji 1051-1100 (50 kanji) - Final N1 batch

## 🛠️ Automated Batch Process

### For Each Batch:

1. **Create Python Script:** `expand_[level]_batch[X].py`
2. **Generate Kanji Data:** 50 kanji with complete structure
3. **Execute Script:** Add to existing dataset
4. **Update JLPT Levels:** Update count in `src/data/jlpt-levels.ts`
5. **Test Application:** Verify count displays correctly
6. **Clean Up:** Remove temporary script
7. **Type Check:** Run `tsc --noEmit` (no build)

### Kanji Data Structure (Per Kanji):

```json
{
  "id": "[level]-[number]",
  "kanji": "漢字",
  "readings": {"on": ["音読み"], "kun": ["訓読み"]},
  "meanings": ["meaning1", "meaning2"],
  "jlptLevel": "[N3/N2/N1]",
  "frequency": [number],
  "strokes": [number],
  "examples": [
    {
      "word": "単語",
      "reading": "たんご",
      "meaning": "word",
      "sentence": {
        "japanese": "日本語の文",
        "romaji": "Nihongo no bun",
        "english": "Japanese sentence",
        "uzbek": "Yapon tilidagi jumla"
      }
    }
  ]
}
```

## 📋 Execution Commands

### For Each Batch:

```bash
# 1. Create script
python3 expand_[level]_batch[X].py

# 2. Execute expansion
python3 expand_[level]_batch[X].py

# 3. Update levels file
# (Manual edit of src/data/jlpt-levels.ts)

# 4. Test application
curl -s http://localhost:3000 | grep -A 3 -B 3 "[count].*kanji"

# 5. Type check
tsc --noEmit

# 6. Clean up
rm expand_[level]_batch[X].py
```

## 🎯 Success Criteria

### Per Batch:

- [ ] Script executes without errors
- [ ] Kanji count increases by 50 (or remaining amount)
- [ ] JLPT levels file updated correctly
- [ ] Application displays new count
- [ ] TypeScript compilation passes
- [ ] Temporary files cleaned up

### Final Completion:

- [ ] N3: 370 kanji total
- [ ] N2: 374 kanji total
- [ ] N1: 1100 kanji total
- [ ] All levels functional in application
- [ ] No TypeScript errors
- [ ] All temporary files removed

## 🔄 Continuous Process

After each batch completion:

1. **Read this MD file again**
2. **Check next unchecked batch**
3. **Execute next batch automatically**
4. **Continue until all batches complete**

## 📝 Notes

- **No project builds** - only `tsc --noEmit` for type checking
- **Maintain data quality** - each kanji must have complete structure
- **Consistent naming** - follow established patterns
- **Error handling** - skip problematic batches, continue with next
- **Progress tracking** - update checkboxes as batches complete

## 🚀 Ready to Execute

This automation plan will systematically complete all JLPT levels from N3 to N1 using consistent 50-kanji batches, ensuring comprehensive kanji coverage for the application.

**Total Batches:** 37 batches
**Total Kanji:** 1,844 kanji (N3: 128 + N2: 374 + N1: 1100)
**Estimated Completion:** 37 automated cycles

---

_Created: 2025-01-10_
_Status: Ready for automated execution_
