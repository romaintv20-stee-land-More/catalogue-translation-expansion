# Catalogue Translation Expansion

Client-side localization expansion for [Catalogue](https://github.com/MrCrayfish/Catalogue), covering its Forge, Fabric and NeoForge generations. The project adds translations only; it does not add gameplay content.

## Maintainers and future ChatGPT sessions

**Read [`PROJECT_STATUS.md`](PROJECT_STATUS.md) first.** It is the canonical handoff containing the audited version history, six localization generations, language policy, release grouping, licensing decisions, QA state and update procedure.

Then read [`docs/UPDATING.md`](docs/UPDATING.md) before adding support for a new Catalogue/Minecraft release.

## Current scope

- audited Minecraft span: **1.16.5 → 26.3** (as of 2026-09-17)
- **6** localization generations: 3 / 11 / 14 / 30 / 32 / 34 keys
- **15** release JARs (13 original groups plus separate 26.3 Fabric and NeoForge)
- **108** primary real-language locale codes across the historical union
- **101** primary locales in the current 26.2 policy
- **51** complete modern-union translations
- documented English fallback for low-confidence rare locales

## Minecraft 26.3 compatibility

Catalogue 1.12.3 supports Minecraft 26.3 on Fabric and NeoForge. The 34 official English translation keys are unchanged from 26.2, so the two dedicated 26.3 JARs reuse the existing G6 translations. **No new languages or vanilla Minecraft translations** are included in this update: the project retains 108 historical locales, 101 current primary languages, and 51 complete modern translations.

## Build

Requirements: Python 3.11+ and JDK 21+.

```bash
python scripts/build_release.py
```

Build outputs are generated into `dist/`; generated localization snapshots go into `generated_sources/`.

## Translation sources

- `translations/g1-legacy-forge-3/` — historical G1 translations
- `translations/modern-union/` — complete 36-key translations for fully translated modern locales

## License

MIT. Catalogue remains the work of MrCrayfish; this is an independent localization add-on and does not redistribute Catalogue's Java implementation.
