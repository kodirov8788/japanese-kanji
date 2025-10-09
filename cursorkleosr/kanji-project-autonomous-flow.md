# Japanese Kanji Project - Autonomous Agent Flow

## 🎯 Project-Specific Autonomous Agent Configuration

### Project Context

- **Project:** Japanese Kanji Learning Application
- **Framework:** Next.js 15 with App Router + TypeScript
- **UI:** Tailwind CSS + Shadcn UI + Radix UI
- **Data:** JSON-based kanji database (N5-N1 JLPT levels)
- **Current Status:** N3 complete (370), N2 partial (50), N1 pending (1100)

## 🧠 Phase 0: Reconnaissance & Mental Modeling

### Repository Inventory

- **Frontend:** Next.js 15 with App Router, React 19, TypeScript 5
- **Styling:** Tailwind CSS 4, Shadcn UI components, Radix UI primitives
- **Data Structure:** JSON files in `src/data/kanji/` (n5-complete.json, n4-complete.json, n3-complete.json)
- **Components:** Modular React components with TypeScript interfaces
- **Build Tools:** Turbopack for development, ESLint for linting

### Current Data State

- **N5:** 103 kanji (complete with 5+ examples each)
- **N4:** 167 kanji (complete)
- **N3:** 370 kanji (complete)
- **N2:** 50 kanji (batch 8 complete, 324 remaining)
- **N1:** 0 kanji (1100 target)

### Quality Gates

- TypeScript compilation: `tsc --noEmit`
- Linting: `npm run lint`
- Build: `npm run build`
- Development: `npm run dev --turbopack`

## 🔄 Autonomous Agent Workflow

### Agent Roles for Kanji Project

#### 1. Kanji Data Generation Agent

**Primary Function:** Generate kanji data for JLPT levels

**Responsibilities:**

- Create Python scripts for batch kanji generation
- Generate complete kanji data structure (id, kanji, readings, meanings, examples)
- Execute scripts to add kanji to JSON datasets
- Update JLPT levels configuration
- Maintain data consistency across levels

**Quality Standards:**

- 5-layer example format (Japanese/Romaji/English/Uzbek)
- Consistent ID format (n2-001, n1-001, etc.)
- Proper on/kun readings
- Multiple meanings per kanji
- Authentic Japanese vocabulary

#### 2. UI Enhancement Agent

**Primary Function:** Enhance user interface and experience

**Responsibilities:**

- Improve mobile responsiveness
- Enhance example navigation
- Add progress indicators
- Implement accessibility features
- Optimize performance

**Quality Standards:**

- Mobile-first design
- WCAG accessibility compliance
- Smooth animations and transitions
- Consistent component patterns
- TypeScript type safety

#### 3. Data Validation Agent

**Primary Function:** Ensure data integrity and quality

**Responsibilities:**

- Validate kanji data structure
- Check example format consistency
- Verify JLPT level accuracy
- Test data loading functionality
- Monitor data quality metrics

**Quality Standards:**

- Zero data inconsistencies
- Complete example coverage
- Accurate JLPT classifications
- Proper Japanese language usage
- Valid JSON structure

#### 4. Performance Optimization Agent

**Primary Function:** Optimize application performance

**Responsibilities:**

- Implement code splitting
- Optimize bundle size
- Add lazy loading
- Improve loading times
- Monitor performance metrics

**Quality Standards:**

- Load time < 3 seconds
- Optimized bundle size
- Efficient memory usage
- Smooth user interactions
- Fast data loading

## 🎯 Autonomous Execution Protocol

### Standard Request Protocol

#### Phase 0: Reconnaissance & Mental Modeling (Read-Only)

1. **Data State Analysis:** Check current kanji counts and completion status
2. **Component Analysis:** Review UI components and their functionality
3. **Configuration Review:** Verify TypeScript, Next.js, and build configurations
4. **Quality Assessment:** Run quality gates and identify issues
5. **Reconnaissance Digest:** Produce concise synthesis of current state

#### Phase 1: Planning & Strategy

1. **Objective Definition:** Define specific kanji expansion or enhancement goals
2. **Impact Analysis:** Identify all files, components, and workflows affected
3. **Execution Plan:** Create detailed step-by-step implementation plan
4. **Quality Strategy:** Define quality gates and validation steps

#### Phase 2: Execution & Implementation

1. **Data Generation:** Create Python scripts for kanji batch generation
2. **Data Integration:** Execute scripts and update JSON files
3. **UI Updates:** Enhance components as needed
4. **Configuration Updates:** Update JLPT levels and related configs
5. **Quality Validation:** Run all quality gates

#### Phase 3: Verification & Autonomous Correction

1. **Type Safety:** Run `tsc --noEmit`
2. **Linting:** Run `npm run lint`
3. **Build Test:** Run `npm run build`
4. **Data Validation:** Verify kanji data integrity
5. **UI Testing:** Test application functionality

#### Phase 4: Mandatory Zero-Trust Self-Audit

1. **Fresh Verification:** Re-run all quality gates
2. **Regression Testing:** Test critical workflows
3. **Data Consistency:** Verify all kanji data is consistent
4. **Performance Check:** Ensure no performance regressions

#### Phase 5: Final Report & Verdict

- **Changes Applied:** List all modified files and data
- **Verification Evidence:** Commands and outputs from testing
- **System-Wide Impact:** Confirmation of all dependencies checked
- **Final Verdict:** Complete success or critical issue identification

## 🚫 Project-Specific Limitations

### Data Integrity Constraints

- **No Data Loss:** Never remove existing kanji data
- **Consistent Format:** Maintain 5-layer example format
- **ID Consistency:** Preserve existing ID patterns
- **JLPT Accuracy:** Ensure official JLPT kanji lists

### Technical Constraints

- **TypeScript Only:** No JavaScript files
- **Component Patterns:** Follow existing component architecture
- **Performance:** Maintain fast loading times
- **Mobile-First:** Ensure mobile compatibility

### Quality Constraints

- **Zero Errors:** No TypeScript or linting errors
- **Data Validation:** All kanji data must be valid
- **UI Consistency:** Maintain design system consistency
- **Accessibility:** WCAG compliance required

## 🔧 Kanji-Specific Quality Gates

### Data Quality Gates

```bash
# Validate kanji data structure
node -e "console.log('Validating kanji data...'); const fs = require('fs'); const levels = ['n5-complete', 'n4-complete', 'n3-complete']; levels.forEach(level => { const data = JSON.parse(fs.readFileSync(\`src/data/kanji/\${level}.json\`, 'utf8')); console.log(\`\${level}: \${data.length} kanji\`); });"

# TypeScript compilation
tsc --noEmit

# Linting
npm run lint

# Build test
npm run build
```

### UI Quality Gates

```bash
# Component type checking
tsc --noEmit --project tsconfig.json

# Build optimization
npm run build -- --analyze

# Development server test
npm run dev --turbopack
```

## 📊 Success Metrics for Kanji Project

### Data Expansion Metrics

- **Kanji Count:** Accurate JLPT level completion
- **Example Quality:** 5+ examples per kanji
- **Data Consistency:** Zero format inconsistencies
- **Loading Performance:** Fast data loading

### UI/UX Metrics

- **Mobile Responsiveness:** Perfect mobile experience
- **Accessibility:** WCAG AA compliance
- **Performance:** < 3 second load times
- **User Experience:** Smooth interactions

### Development Metrics

- **Code Quality:** Zero TypeScript errors
- **Build Success:** Successful production builds
- **Test Coverage:** Comprehensive functionality testing
- **Documentation:** Complete and accurate

## 🚀 Autonomous Kanji Expansion Workflow

### N2 Completion (324 kanji remaining)

1. **Batch 9:** Generate N2 kanji 51-100 (50 kanji)
2. **Batch 10:** Generate N2 kanji 101-150 (50 kanji)
3. **Continue:** Until N2 complete (374 total)

### N1 Expansion (1100 kanji)

1. **Batch 16:** Generate N1 kanji 1-50 (50 kanji)
2. **Continue:** Systematic expansion in 50-kanji batches
3. **Complete:** Until N1 complete (1100 total)

### Enhancement Tasks

1. **Example Enhancement:** Expand N5 examples to 5+ per kanji
2. **UI Improvements:** Mobile optimization and accessibility
3. **Performance:** Bundle optimization and lazy loading
4. **Features:** Add practice mode and stroke order

## 🎯 Final Directive

This autonomous agent flow enables systematic, high-quality expansion of the Japanese Kanji learning application while maintaining data integrity, UI consistency, and performance standards. All operations follow the core operational doctrine with project-specific adaptations for kanji data management and educational application requirements.
