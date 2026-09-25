# Updating the project

## 1. Audit Catalogue upstream
Do not trust branch names alone. For each new branch inspect `gradle.properties`, enabled loader modules/settings, Java version, Catalogue version, license, and `assets/catalogue/lang/en_us.json`.

## 2. Compare English localization semantically
- same key + same meaning → reuse translation;
- same key + changed meaning → translate again;
- new key → translate;
- removed key → remove from that generation.

Never use key identity alone as proof of semantic identity. G1 `catalogue.gui.info` (redesigned) versus G2+ (provided) is the known example.

## 3. Audit Minecraft language availability
Use the actual language list for the new Minecraft version. Keep real languages and one primary locale first. Defer novelty/fantasy entries and regional/orthographic duplicates until the primary-language pass is mature.

## 4. Protect official Catalogue strings
Inspect upstream locale files for the target branch. Generated payloads should normally contain only missing keys. A stale/incomplete official string is a documented issue, not automatic permission to override it.

## 5. Add translations
- G1 historical translations: `translations/g1-legacy-forge-3/`
- full modern translations: `translations/modern-union/`

Every modern-union file must contain the complete 36-key union. Preserve `%s` placeholders exactly. For low-confidence languages, English fallback is preferred to invented wording.

## 6. Preserve grouping where safe
The target is 15 release JARs: 13 original groups plus dedicated 26.3 Fabric and NeoForge builds. The 26.3 extension reuses G6 with no new languages. Only split a grouped JAR when loader metadata, Catalogue dependency ranges, Minecraft dependency ranges or resource-pack compatibility actually break.

## 7. Build and QA
```bash
python scripts/build_release.py
```
Review `dist/build-report.json`, `dist/SHA256SUMS.txt`, generated sources and any errors.

## 8. Runtime test
Launch representative first/last versions of grouped ranges and verify Catalogue opens and translated strings render.

## 9. Update the handoff
Always update `PROJECT_STATUS.md` with the latest upstream version, generation/key changes, language counts, grouping changes and runtime-test state.
