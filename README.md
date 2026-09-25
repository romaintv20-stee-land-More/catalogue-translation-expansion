# Catalogue Translation Expansion

Client-side localization expansion for [Catalogue](https://github.com/MrCrayfish/Catalogue), covering its Forge, Fabric and NeoForge generations. The project adds translations only; it does not add gameplay content.

## Maintainers and future ChatGPT sessions

**Read [`PROJECT_STATUS.md`](PROJECT_STATUS.md) first.** It is the canonical handoff containing the audited version history, six localization generations, language policy, release grouping, licensing decisions, QA state and update procedure.

Then read [`docs/UPDATING.md`](docs/UPDATING.md) before adding support for a new Catalogue/Minecraft release.

## Current scope

- audited Minecraft span: **1.16.5 → 26.3** (as of 2026-09-17)
- **6** localization generations: 3 / 11 / 14 / 30 / 32 / 34 keys
- **15** release JARs (13 previous groups plus dedicated 26.3 Fabric and NeoForge builds)
- **109** locale codes across the supported union (108 previous primary locales plus custom Marathi)
- **101** previous primary locales plus Marathi (`mr_in`) as an additional custom Minecraft language
- **52** complete modern-union translations (including Marathi)
- documented English fallback for low-confidence rare locales

## Marathi all-in-one — Minecraft 26.3

The two dedicated **Fabric and NeoForge 26.3** add-on JARs embed Marathi (`mr_in`) translations for both Catalogue (all 34 active G6 keys) and Minecraft 26.3 (all 8,559 official vanilla keys). They also register `मराठी` in `pack.mcmeta`. One JAR per loader goes in `mods/`, alongside the original Catalogue mod; **no separate resource-pack ZIP is needed**. There is no upstream Forge build for Minecraft 26.3.

The Minecraft Marathi source is reused from the user's Beyond & More-derived [Controlling Language Expansion](https://github.com/romaintv20-stee-land-More/controlling-language-expansion) translation, with 722 machine-assisted new/changed strings. The Marathi translation requires native-language review, and the two 26.3 loader variants require in-game testing before public release. See [the Marathi 26.3 release notes](docs/MARATHI_ALL_IN_ONE.md).

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
