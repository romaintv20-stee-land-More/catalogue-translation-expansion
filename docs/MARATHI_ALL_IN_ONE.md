# Catalogue Translation Expansion 1.0.1 — Minecraft 26.3 Marathi in one JAR

**Status:** static-validated candidate, not yet released. The original Catalogue mod is still required.

## Two single-JAR editions

The upstream [Catalogue 1.12.3 release for Minecraft 26.3](https://github.com/MrCrayfish/Catalogue/releases/tag/v1.12.3%2B26.3) was published on September 17, 2026 for **Fabric** and **NeoForge**. No Forge 26.3 build is provided upstream. This repository generates two dedicated 26.3 artifacts:

- `CatalogueTranslationExpansion-1.0.1-fabric-mc26.3.jar`
- `CatalogueTranslationExpansion-1.0.1-neoforge-mc26.3.jar`

Install the **one JAR matching your loader** into `mods/` together with the original Catalogue mod. Both JARs contain all active Catalogue Marathi translations and the matching Minecraft 26.3 Marathi resource in the same archive. No separate `resourcepacks/` ZIP or second add-on JAR is necessary.

Each 26.3 JAR contains:

- `assets/catalogue/lang/mr_in.json` — all **34 active** Catalogue G6 keys (from the 36-key complete modern union).
- `assets/minecraft/lang/mr_in.json` — all **8,559** official Minecraft 26.3 vanilla translation keys, adapted directly from Beyond & More and reused from the owner's Controlling Language Expansion translation source.
- `pack.mcmeta` — registers Marathi (`mr_in`, `मराठी`, `भारत`) as a custom language and targets Minecraft resource format 97.1.

Catalogue's English localization keys and values are **unchanged** between 26.2 and 26.3: the existing G6 (34 keys) remains valid. Earlier grouped 1.20.4–26.2 releases are deliberately not shipped with Minecraft 26.3 vanilla strings; they retain their original ranges and receive the new Catalogue Marathi locale where applicable.

## Provenance and review

The vanilla translation is a byte-identical copy of `translations/minecraft/26.3/mr_in.json` from the owner's Controlling Language Expansion repository, which sourced the original Marathi strings from Beyond & More 26.1.2. It contains **7,790 unchanged-key/same-English** inherited values, **45 uniquely identical-English cross-key** reuses, **2 curated changes** and **722 machine-assisted** new/modified translations. All 8,559 key names and 1,082 technical-token signatures are checked against official Minecraft 26.3 source signatures.

The new 36-key Catalogue Marathi modern-union file is a proposed translation and requires native Marathi proofreading. The 722 machine-assisted vanilla strings also require review. Correct selection of `मराठी`, Devanagari glyph rendering, and Catalogue UI display must be verified in actual Minecraft 26.3 on both Fabric and NeoForge before public release.

## Changelog (English)

Catalogue Translation Expansion 1.0.1 — Marathi and Minecraft 26.3 Update

- Added Marathi (`mr_in`) with full coverage of the 36-key Catalogue translation union, including all 34 active keys in Catalogue 1.12.3 for Minecraft 26.3.
- Added separate Fabric and NeoForge 26.3 editions, following the official upstream release. No Forge edition is claimed for 26.3.
- Embedded the complete Minecraft 26.3 Marathi localization (8,559 keys) **inside each Catalogue Translation Expansion 26.3 JAR**. No companion resource-pack ZIP is required.
- Reused Beyond & More-derived translations for 7,835 English-compatible keys and added 722 machine-assisted values for new or changed Minecraft strings.
- Preserved the original 13 earlier release groups; the 26.3 editions bring the planned total to **15 JARs**.
- Retained official upstream localization priority, with version-specific resource packs so newer vanilla translations do not overwrite older Minecraft versions.
- Added full JSON/key/placeholder validation and reproducible packaging checks.

**Publication gate:** native-language proofreading and real-world Fabric/NeoForge game testing are still outstanding.

## Rebuild

Run `python scripts/build_release.py` with JDK 25 and Python 3.12+. The build emits 15 JARs to `dist/`; the new 26.3 JARs include both required `mr_in.json` files. CI builds twice and checks identical output checksums. The original complete Minecraft translation, frozen key signatures and B&M provenance are checked into the repository for offline reproducibility.
