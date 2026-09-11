# Catalogue Translation Expansion

**Catalogue Translation Expansion** is a client-side localization add-on for [Catalogue](https://github.com/MrCrayfish/Catalogue) by MrCrayfish.

The project extends Catalogue's localization without copying or blindly replacing upstream translations. It tracks real localization generations, the Minecraft languages available to each target version, and produces loader-specific resource-only JARs.

## Current phase

Initial upstream audit + build scaffold.

- 6 localization generations: **3 / 11 / 14 / 30 / 32 / 34 keys**
- audited Minecraft span: **1.16.5 → 26.2**
- current 26.2 target set: **137 translation targets**
- loaders: Forge, Fabric, NeoForge where Catalogue actually supports them
- G1 / Minecraft 1.16.5 scope: **91 primary real-language locales** (89 supplied by this add-on + 2 already supplied by Catalogue)
- G1 translated now: **69 locales**; **20 low-confidence locales** intentionally retain documented English fallback pending review
- build policy: **separate JAR per loader and Minecraft target**
- official Catalogue keys are protected by default; deliberate overrides require an explicit allowlist

## Initial test targets

- Minecraft 1.16.5: Forge
- Minecraft 1.21.11: Forge / Fabric / NeoForge
- Minecraft 26.2: Fabric / NeoForge

The localization payload can be shared internally, but loader metadata, version constraints and Catalogue loader availability differ. A single cross-loader JAR is therefore not assumed safe.

## Development

```bash
python scripts/qa.py
python scripts/build.py --all
python scripts/inspect_jars.py
```

Generated artifacts are written to `dist/`.

## Repository layout

- `audit/` — upstream/version/language audit
- `sources/` — authoritative `en_us` by localization generation
- `translations/` — translations by generation
- `config/targets.json` — loader/Minecraft build targets
- `config/overrides-allowlist.json` — intentional upstream collisions (empty by default)
- `scripts/` — QA, build and JAR inspection
- `docs/TRANSLATION_METHOD.md` — translation/reuse/AI policy

## AI-assisted translations

Some translations may be generated or assisted by AI. They are subject to the same structural QA as human translations and may be left as documented English fallbacks when reliable translation quality cannot be reached.

## License and attribution

This project is licensed under **GPL-3.0-only**. See `LICENSE` and `THIRD_PARTY_NOTICES.md`.

Catalogue remains the work of MrCrayfish. This is an independent add-on and is not an official Catalogue project.
