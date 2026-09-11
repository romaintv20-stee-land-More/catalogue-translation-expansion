# G1 language scope (Minecraft 1.16.5)

Catalogue Translation Expansion starts from the Minecraft 1.16.5 language list.

## Selection rules

- `en_us` is the English source and is not a translation target.
- Novelty or fictional entries are excluded from the first pass.
- Direct regional/standard variants and clearly same-language dialect variants are deferred; one primary variant is kept for now.
- Distinct real regional languages remain eligible.
- Serious non-fictional constructed languages may remain eligible.
- Existing Catalogue translations for the exact target are not replaced.
- If a reliable translation cannot be produced with sufficient confidence, the file intentionally keeps the exact English source strings and is recorded as an English fallback in `audit/g1_language_scope.json`.

The first G1 source has only three keys, so every locale file must contain exactly those three keys. The scope manifest is the authoritative machine-readable list for this pass.
