# Catalogue Translation Expansion 1.0.1

Maintenance, translation-coverage and Minecraft 26.3 compatibility release. The 26.3 extension adds no languages.

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
- Increased complete modern-union coverage from **38 to 51 locales**.
- Kept the historical G1 translations unchanged for older Catalogue versions.
- Bumped every generated artifact and embedded manifest from **1.0.0 to 1.0.1**.
- Aligned repository, loader metadata and packaged license declaration on **MIT**.
- Corrected the historical Catalogue audit: **Minecraft 1.21.5 is a real upstream target**.
- Added Minecraft **1.21.5** to the upload-version guidance for grouped Forge/Fabric/NeoForge files.
- Removed Minecraft **1.21.2** from upload-version guidance because Catalogue has no published 1.21.2 release.
- Added the audited Minecraft 1.21.5 resource-pack format (**55**).
- Added dedicated **Minecraft 26.3** Fabric and NeoForge JARs for the official Catalogue 1.12.3 release of September 17. All 34 upstream English keys and values are identical to 26.2, so no new translations are required.

## Packaging

The release contains **15 JARs**:

- 8 Forge artifacts
- 5 Fabric artifacts (including Minecraft 26.3)
- 2 NeoForge artifacts (including Minecraft 26.3)

The 13 existing 1.0.1 groups are preserved; two dedicated 26.3 variants reuse the existing G6 translations.

## Upload metadata warning

Do not simply tag every Minecraft version numerically contained inside a grouped dependency range. Use versions for which Catalogue itself has a compatible published release. In particular:

- include **1.21.5**;
- do **not** include **1.21.2**;
- do not tag Forge for Catalogue 26.1+ releases;
- tag Minecraft 26.3 only on the new Fabric and NeoForge variants.

## QA

Run:

```bash
python scripts/build_release.py
```

A successful release build must report:

- 15 JARs;
- `LEGACY=91`;
- `CURRENT=101`;
- `MASTER=108`;
- `FULL_TRANSLATED=51`;
- valid JSON and preserved `%s` placeholders;
- generated SHA-256 checksums and combined ZIP.
