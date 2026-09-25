# Project Status — Catalogue Translation Expansion

> **Start here in a new chat.** This is the canonical handoff for maintaining the project without relying on previous ChatGPT conversation history.

Last synchronized: **2026-09-25**
Release line: **1.0.1**  
Upstream: **MrCrayfish/Catalogue**  
Latest audited upstream branch: **`multiloader/26.3`** — Catalogue **1.12.3**, Minecraft **26.3** (September 17; Fabric and NeoForge).

## Minecraft 26.3 support in 1.0.1

Catalogue 1.12.3 for Minecraft 26.3 is available on Fabric and NeoForge only. Its **34 English keys and values are unchanged** from 26.2, so G6 is reused. Add exactly two 26.3 JARs to the existing 13 release groups, resulting in **15 JARs**. The 26.3 pack format is **97.1** and the GitHub build runs on JDK 25.

**No new languages:** preserve 108 historical locales, 101 current primary locales and 51 complete modern translations. The earlier draft's Marathi language and Minecraft vanilla translation pack have been removed from Catalogue Translation Expansion; no custom language registration is included. Native runtime testing remains open.

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
- **51 locales** currently have complete translations for the full 36-key modern union.
- Low-confidence/rare locales deliberately fall back to English rather than receiving speculative translations.

Full modern translations are stored as JSON in `translations/modern-union/`. G1 historical translations are stored in `translations/g1-legacy-forge-3/`.

Complete modern locales:

`af_za ar_sa az_az be_by bg_bg bs_ba ca_es cs_cz da_dk de_de el_gr es_es et_ee eu_es fa_ir fi_fi fil_ph fr_fr gl_es he_il hi_in hr_hr hu_hu hy_am id_id is_is it_it ja_jp ka_ge kk_kz ko_kr lt_lt lv_lv ms_my nl_nl no_no pl_pl pt_br ro_ro ru_ru sk_sk sl_si sq_al sr_sp sv_se ta_in th_th tr_tr uk_ua vi_vn zh_cn`

Added as complete modern locales for **1.0.1**: `af_za az_az be_by bs_ba el_gr eu_es fa_ir hy_am is_is ka_ge kk_kz sq_al ta_in`.

## Official upstream translation protection

Do not overwrite an official Catalogue key simply for stylistic consistency. The build strips protected upstream-owned keys where practical. Incomplete or stale upstream translations should be documented before any intentional override.

Historical upstream pattern: early branches include `de_de` and `it_it`; later G1 branches also include `pl_pl` and `zh_cn`; modern branches commonly include `de_de`, `pl_pl`, `zh_cn`, with `en_au` and later `ru_ru` appearing in newer versions.

## Release strategy — 15 JARs

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
| Fabric | 26.3 | dedicated, existing languages only |
| NeoForge | 26.3 | dedicated, existing languages only |

Important upstream facts:
- **Minecraft 1.21.5 is a genuine Catalogue target.** Repository history contains a real 1.21.5 update/release even though the current head of the old `multiloader/1.21.5` branch later points at 1.21.6. Historical target decisions must use commits/releases, not only the present branch head.
- Catalogue has **no published Minecraft 1.21.2 release**. Do not tag the grouped release files as 1.21.2 on CurseForge/Modrinth.
- 26.1+ actual Catalogue loaders are Fabric + NeoForge.
- Several upstream `pack.mcmeta` files are historically stale; do not copy their pack format blindly.

## Audited Minecraft resource formats

`1.16.5=6`, `1.17.1=7`, `1.18.2=8`, `1.19–1.19.2=9`, `1.19.3=12`, `1.19.4=13`, `1.20–1.20.1=15`, `1.20.4=22`, `1.20.5–1.20.6=32`, `1.21–1.21.1=34`, `1.21.3=42`, `1.21.4=46`, `1.21.5=55`, `1.21.6=63`, `1.21.7–1.21.8=64`, `1.21.9–1.21.10=69`, `1.21.11=75`, `26.1=84`, `26.2=88`, `26.3=97.1`.

Grouped modern packs include compatibility metadata for both the older `supported_formats` era and the newer `min_format` / `max_format` era.

## Licensing

Project policy for **1.0.1+ is MIT**, matching the repository `LICENSE` file and the public project metadata. Catalogue remains a separate upstream work; this project does not redistribute Catalogue's Java implementation code. Keep third-party attribution in `THIRD_PARTY_NOTICES.md`.

## Reproducible build

Requirements: Python 3.11+ and JDK 21+ (`javac` must support `--release 8` and `--release 17`).

```bash
python scripts/build_release.py
```

The script reads the translation JSON files, generates the six localization generations, compiles tiny loader entrypoints against local annotation stubs, builds all 13 JARs, validates JSON/placeholders/metadata, creates checksums and writes a combined ZIP. Archive timestamps are normalized so identical source input produces identical release archives. GitHub Actions performs two consecutive builds and compares JAR checksums, the build report and the combined ZIP hash.

## 1.0.1 scope

- bump all generated artifacts and metadata from 1.0.0 to **1.0.1**;
- align license declarations on **MIT**;
- raise complete modern-union coverage from **38 to 51 locales**;
- correct the historical 1.21.5 audit and include 1.21.5 in upload metadata;
- remove accidental 1.21.2 upload tagging where present;
- retain the 13 existing 1.0.1 release groups and add two dedicated 26.3 JARs, without any new language;
- make ZIP/JAR output genuinely reproducible by normalizing archive timestamps;
- update the CI workflow to current stable GitHub Actions majors and verify reproducibility automatically.

## Current QA status

The original **1.0.1** passed GitHub Actions as **13 artifacts**; the Minecraft 26.3 update produces **15 artifacts** with `LEGACY=91`, `CURRENT=101`, `MASTER=108` and `FULL_TRANSLATED=51`. JSON syntax, `%s` placeholders and loader/resource metadata are validated. Two consecutive CI builds produce identical JAR checksums, identical `build-report.json` and an identical combined ZIP hash.

Runtime testing remains useful for representative endpoints, especially Forge 1.16.5, Forge 1.20.4/1.21.11, Fabric 1.19.3/1.20.4/26.2, and NeoForge 1.20.4/26.2. If a grouped metadata range is rejected, split only that affected group.

## New-chat resume procedure

1. Read this file.
2. Read `docs/UPDATING.md` and `docs/RELEASE_MATRIX.md`.
3. Check upstream Catalogue releases newer than the audited 26.3.
4. Diff the upstream English localization against the six-generation model.
5. Reuse translations only for unchanged English meaning; translate new/changed strings.
6. Audit Minecraft's language list for new/removed locales and apply the real-language/primary-locale policy.
7. Run `python scripts/build_release.py`.
8. Review `dist/build-report.json` and `dist/SHA256SUMS.txt`.
9. Runtime-test representative endpoints before publishing stable artifacts.
10. Update this file after every support/matrix decision so GitHub remains the source of truth.
