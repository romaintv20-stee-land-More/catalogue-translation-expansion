# Catalogue Translation Expansion 1.0.1

Maintenance and translation-coverage release.

## Changes

- Added complete modern 36-key translations for 12 additional locales:
  - Afrikaans (`af_za`)
  - Azerbaijani (`az_az`)
  - Belarusian (`be_by`)
  - Greek (`el_gr`)
  - Basque (`eu_es`)
  - Persian (`fa_ir`)
  - Armenian (`hy_am`)
  - Icelandic (`is_is`)
  - Georgian (`ka_ge`)
  - Kazakh (`kk_kz`)
  - Albanian (`sq_al`)
  - Tamil (`ta_in`)
- Increased complete modern-union coverage from **38 to 50 locales**.
- Kept the historical G1 translations unchanged for older Catalogue versions.
- Bumped every generated artifact and embedded manifest from **1.0.0 to 1.0.1**.
- Aligned repository, loader metadata and packaged license declaration on **MIT**.
- Corrected the historical Catalogue audit: **Minecraft 1.21.5 is a real upstream target**.
- Added Minecraft **1.21.5** to the upload-version guidance for grouped Forge/Fabric/NeoForge files.
- Removed Minecraft **1.21.2** from upload-version guidance because Catalogue has no published 1.21.2 release.
- Added the audited Minecraft 1.21.5 resource-pack format (**55**).
- Re-audited upstream Catalogue: latest remains **Catalogue 1.12.3 / Minecraft 26.2**; no new English localization keys are required for 1.0.1.

## Packaging

The release remains **13 JARs**:

- 8 Forge artifacts
- 4 Fabric artifacts
- 1 NeoForge artifact

All 13 are rebuilt for 1.0.1 because the version and license metadata are embedded in every JAR.

## Upload metadata warning

Do not simply tag every Minecraft version numerically contained inside a grouped dependency range. Use versions for which Catalogue itself has a compatible published release. In particular:

- include **1.21.5**;
- do **not** include **1.21.2**;
- do not tag Forge for Catalogue 26.1+ releases.

## QA

Run:

```bash
python scripts/build_release.py
```

A successful release build must report:

- 13 JARs;
- `LEGACY=91`;
- `CURRENT=101`;
- `MASTER=108`;
- `FULL_TRANSLATED=50`;
- valid JSON and preserved `%s` placeholders;
- generated SHA-256 checksums and combined ZIP.
