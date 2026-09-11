# Project Status — Catalogue Translation Expansion

> **Start here in a new chat.** This is the canonical handoff for maintaining the project without relying on previous ChatGPT conversation history.

Last synchronized: **2026-09-11**  
Development branch: **`dev/catalogue-audit`**  
Upstream: **MrCrayfish/Catalogue**  
Latest audited upstream branch: **`multiloader/26.2`** — Catalogue **1.12.3**, Minecraft **26.2**.

## Purpose

Catalogue Translation Expansion is a client-side localization add-on for Catalogue. It adds no gameplay blocks, items, mobs or mechanics. The goal is broad real-language coverage across Catalogue's Minecraft history while avoiding unnecessary replacement of official Catalogue translations.

## Localization generations

| Generation | Era | English keys | Important note |
|---|---|---:|---|
| G1 | Forge 1.16.5 → 1.19.3 | 3 | `catalogue.gui.info` says the menu was **redesigned** |
| G2 | Fabric 1.19.3 | 11 | modern info meaning begins: **provided by Catalogue** |
| G3 | Multiloader 1.19.4 → 1.21 | 14 | Forge/Fabric, later NeoForge |
| G4 | 1.21.1 → 1.21.8 | 30 | favorites, filters, sorting, dependencies |
| G5 | 1.21.9 → 1.21.11 | 32 | adds Website + Submit Bug |
| G6 | 26.1 → 26.2 | 34 | adds Missing Branding + guide description |

The cross-generation union contains **36 distinct keys**. Reuse a translation only when the key **and the English meaning** are unchanged. G1/G2+ `catalogue.gui.info` is the canonical semantic-change example.

## Language policy

- Target real languages present in Minecraft.
- First pass uses one primary locale per language.
- Regional/orthographic duplicates are deferred for later (`en_gb`, `fr_ca`, `pt_pt`, `zh_tw`, etc.).
- Novelty/fantasy entries are deferred/excluded (Pirate Speak, Upside Down English, LOLCAT, Quenya, Klingon, etc.).
- Historical primary-locale union used by the build: **108 locale codes**.
- Current Minecraft 26.2 primary selection: **101 locale codes**.
- **38 locales** currently have complete translations for the full 36-key modern union.
- Low-confidence/rare locales deliberately fall back to English rather than receiving speculative translations.

Full modern translations are stored as JSON in `translations/modern-union/`. G1 historical translations are stored in `translations/g1-legacy-forge-3/`.

Complete modern locales:

`fr_fr de_de es_es it_it pt_br nl_nl pl_pl ru_ru uk_ua cs_cz sk_sk ro_ro hu_hu tr_tr da_dk sv_se no_no fi_fi ja_jp ko_kr zh_cn id_id ca_es gl_es ar_sa he_il hi_in vi_vn th_th bg_bg hr_hr sl_si sr_sp et_ee lt_lt lv_lv ms_my fil_ph`

## Official upstream translation protection

Do not overwrite an official Catalogue key simply for stylistic consistency. The build strips protected upstream-owned keys where practical. Incomplete or stale upstream translations should be documented before any intentional override.

Historical upstream pattern: early branches include `de_de` and `it_it`; later G1 branches also include `pl_pl` and `zh_cn`; modern branches commonly include `de_de`, `pl_pl`, `zh_cn`, with `en_au` and later `ru_ru` appearing in newer versions.

## Release strategy — 13 JARs

The project deliberately groups compatible versions instead of publishing about 57 per-version/per-loader files.

| Loader | Minecraft coverage | Packaging |
|---|---|---|
| Forge | 1.16.5 | dedicated |
| Forge | 1.17.1 | dedicated |
| Forge | 1.18.2 | dedicated |
| Forge | 1.19.2 | dedicated |
| Forge | 1.19.3 | dedicated |
| Forge | 1.19.4 | dedicated |
| Forge | 1.20.1 | dedicated |
| Forge | 1.20.4 → 1.21.11 | grouped |
| Fabric | 1.19.3 | dedicated |
| Fabric | 1.19.4 | dedicated |
| Fabric | 1.20.1 | dedicated |
| Fabric | 1.20.4 → 26.2 | grouped |
| NeoForge | 1.20.4 → 26.2 | grouped |

Important upstream facts:
- Catalogue branch `multiloader/1.21.5` actually targets **Minecraft 1.21.6**; do not create a fake 1.21.5 release from the branch name.
- 26.1+ actual Catalogue loaders are Fabric + NeoForge.
- Several upstream `pack.mcmeta` files are historically stale; do not copy their pack format blindly.

## Audited Minecraft resource formats

`1.16.5=6`, `1.17.1=7`, `1.18.2=8`, `1.19–1.19.2=9`, `1.19.3=12`, `1.19.4=13`, `1.20–1.20.1=15`, `1.20.4=22`, `1.20.5–1.20.6=32`, `1.21–1.21.1=34`, `1.21.3=42`, `1.21.4=46`, `1.21.6=63`, `1.21.7–1.21.8=64`, `1.21.9–1.21.10=69`, `1.21.11=75`, `26.1=84`, `26.2=88`.

Grouped modern packs include compatibility metadata for both the older `supported_formats` era and the newer `min_format` / `max_format` era.

## Licensing

Project policy: **GPL-3.0-only**, chosen conservatively because historical Catalogue branches include GPLv3 while later branches declare MIT. Do not copy Catalogue Java implementation code.

## Reproducible build

Requirements: Python 3.11+ and JDK 21+ (`javac` must support `--release 8` and `--release 17`).

```bash
python scripts/build_release.py
```

The script reads the translation JSON files, generates the six localization generations, compiles tiny loader entrypoints against local annotation stubs, builds all 13 JARs, validates JSON/placeholders/metadata, creates checksums and writes a combined ZIP. No precompiled local `.class` files are required.

## Current QA status

Version **1.0.0** has been structurally built as 13 artifacts. Scripted QA passes.

**Runtime caveat:** the grouped JARs have not yet been launched in every Minecraft/loader combination. Before a stable public release, runtime-test representative endpoints, especially Forge 1.16.5, Forge 1.20.4/1.21.11, Fabric 1.19.3/1.20.4/26.2, and NeoForge 1.20.4/26.2. If a grouped metadata range is rejected, split only that affected group.

## New-chat resume procedure

1. Read this file.
2. Read `docs/UPDATING.md` and `docs/RELEASE_MATRIX.md`.
3. Check the current upstream Catalogue branches before assuming 26.2 is still latest.
4. Diff the upstream English localization against the six-generation model.
5. Reuse translations only for unchanged English meaning; translate new/changed strings.
6. Audit Minecraft's language list for new/removed locales and apply the real-language/primary-locale policy.
7. Run `python scripts/build_release.py`.
8. Review `dist/build-report.json` and `dist/SHA256SUMS.txt`.
9. Runtime-test representative endpoints before publishing stable artifacts.
10. Update this file after every support/matrix decision so GitHub remains the source of truth.
