import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const projectRoot = path.resolve(__dirname, "..");
const dataDir = path.join(projectRoot, "src", "data", "kanji");

const activeFiles = [
  { level: "N5", file: "n5-complete.json", expectedCount: 103 },
  { level: "N4", file: "n4.json", expectedCount: 167 },
  { level: "N3", file: "n3-complete.json", expectedCount: 370 },
  { level: "N2", file: "n2-complete.json", expectedCount: 374 },
  { level: "N1", file: "n1-complete.json", expectedCount: 118 },
];

function isNonEmptyString(value) {
  return typeof value === "string" && value.trim().length > 0;
}

function validateExample(example, index, kanjiId, errors) {
  if (!isNonEmptyString(example?.word)) {
    errors.push(`${kanjiId} example ${index + 1}: missing word`);
  }
  if (!isNonEmptyString(example?.reading)) {
    errors.push(`${kanjiId} example ${index + 1}: missing reading`);
  }
  if (!isNonEmptyString(example?.meaning)) {
    errors.push(`${kanjiId} example ${index + 1}: missing meaning`);
  }

  const sentence = example?.sentence ?? {};
  for (const field of ["japanese", "romaji", "english", "uzbek"]) {
    if (!isNonEmptyString(sentence[field])) {
      errors.push(`${kanjiId} example ${index + 1}: missing sentence.${field}`);
    }
  }
}

function validateKanjiItem(item, level, seenIds, errors) {
  if (!isNonEmptyString(item?.id)) {
    errors.push(`${level}: item missing id`);
    return;
  }

  if (seenIds.has(item.id)) {
    errors.push(`${item.id}: duplicate id`);
  }
  seenIds.add(item.id);

  if (!isNonEmptyString(item.kanji)) {
    errors.push(`${item.id}: missing kanji`);
  }
  if (item.jlptLevel !== level) {
    errors.push(`${item.id}: expected jlptLevel ${level}, got ${item.jlptLevel}`);
  }
  if (!Number.isInteger(item.strokes) || item.strokes <= 0) {
    errors.push(`${item.id}: invalid strokes`);
  }
  if (!Number.isInteger(item.frequency) || item.frequency <= 0) {
    errors.push(`${item.id}: invalid frequency`);
  }
  if (!Array.isArray(item.meanings) || item.meanings.length === 0) {
    errors.push(`${item.id}: missing meanings`);
  }
  if (!Array.isArray(item.readings?.on) || !Array.isArray(item.readings?.kun)) {
    errors.push(`${item.id}: invalid readings`);
  }
  if (!Array.isArray(item.examples) || item.examples.length === 0) {
    errors.push(`${item.id}: missing examples`);
    return;
  }

  item.examples.forEach((example, index) =>
    validateExample(example, index, item.id, errors)
  );
}

function loadJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

const errors = [];

for (const entry of activeFiles) {
  const filePath = path.join(dataDir, entry.file);
  const payload = loadJson(filePath);

  if (!Array.isArray(payload)) {
    errors.push(`${entry.file}: root payload must be an array`);
    continue;
  }

  if (payload.length !== entry.expectedCount) {
    errors.push(
      `${entry.file}: expected ${entry.expectedCount} items, found ${payload.length}`
    );
  }

  const seenIds = new Set();
  payload.forEach((item) => validateKanjiItem(item, entry.level, seenIds, errors));
}

if (errors.length > 0) {
  console.error("Kanji data validation failed:");
  for (const error of errors) {
    console.error(`- ${error}`);
  }
  process.exit(1);
}

console.log("Kanji data validation passed.");
