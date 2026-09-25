# Catalogue Translation Expansion 1.0.1

Maintenance, new Marathi language and Minecraft 26.3 compatibility update (candidate; not yet published).

## Changes

- Added complete modern 36-key translations for 13 additional locales:
  - Afrikaans (`af_za`)
  - Azerbaijani (`az_az`)
  - Belarusian (`be_by`)
  - Bosnian (`bs_ba`)
  - Greek (`el_gr`)
  - Basque (`eu_es`)
  - Persian (`fa_ir`)
  - Armenian (`hy_am`)
  - Icelandic (`is_is`)
  - Georgian (`ka_ge`)
  - Kazakh (`kk_kz`)
  - Albanian (`sq_al`)
  - Tamil (`ta_in`)
- Increased complete modern-union coverage from **38 to 52 locales**, including Marathi (`mr_in`) with all 36 union keys.
- Kept the historical G1 translations unchanged for older Catalogue versions.
- Bumped every generated artifact and embedded manifest from **1.0.0 to 1.0.1**.
- Aligned repository, loader metadata and packaged license declaration on **MIT**.
- Corrected the historical Catalogue audit: **Minecraft 1.21.5 is a real upstream target**.
- Added Minecraft **1.21.5** to the upload-version guidance for grouped Forge/Fabric/NeoForge files.
- Removed Minecraft **1.21.2** from upload-version guidance because Catalogue has no published 1.21.2 release.
- Added the audited Minecraft 1.21.5 resource-pack format (**55**).
- Added dedicated Minecraft **26.3** Fabric and NeoForge builds following the upstream GitHub release of Catalogue 1.12.3 (September 17). Its **34 English localization keys are identical** to those in 26.2, so G6 is reused without introducing or renaming Catalogue keys.
- Embedded the Marathi custom-language registration and **8,559 Minecraft 26.3 Marathi strings** inside each new 26.3 JAR. The source is derived directly from Beyond & More, with 722 machine-assisted new/changed entries pending native-language review. No separate resource pack is required.

## Packaging

The update produces **15 JARs**:

- 8 Forge artifacts
- 5 Fabric artifacts (including dedicated 26.3)
- 2 NeoForge artifacts (including dedicated 26.3)

All 15 are rebuilt for 1.0.1 because the version and license metadata are embedded in every JAR.

## Upload metadata warning

Do not simply tag every Minecraft version numerically contained inside a grouped dependency range. Use versions for which Catalogue itself has a compatible published release. In particular:

- include **1.21.5**;
- do **not** include **1.21.2**;
- do not tag Forge for Catalogue 26.1+ releases;
- add **26.3** only to the two dedicated Fabric/NeoForge artifacts; their embedded vanilla Marathi resource is audited for 26.3.

## QA

Run:

```bash
python scripts/build_release.py
```

A successful release build must report:

- 15 JARs;
- `LEGACY=91`;
- `CURRENT=102`;
- `MASTER=109`;
- `FULL_TRANSLATED=52`;
- valid JSON and preserved `%s` placeholders;
- generated SHA-256 checksums and combined ZIP.
