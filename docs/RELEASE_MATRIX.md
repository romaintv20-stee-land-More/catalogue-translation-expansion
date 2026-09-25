# Release matrix

Current planned project version: **1.0.1**.

| Artifact group | Loader | Minecraft | Catalogue baseline | Content |
|---|---|---|---|---|
| forge-mc1.16.5 | Forge | 1.16.5 | 1.6.1 | G1 |
| forge-mc1.17.1 | Forge | 1.17.1 | 1.5.0 | G1 |
| forge-mc1.18.2 | Forge | 1.18.2 | 1.6.1 | G1 |
| forge-mc1.19.2 | Forge | 1.19.2 | 1.7.0 | G1 |
| forge-mc1.19.3 | Forge | 1.19.3 | 1.7.0 | G1 |
| forge-mc1.19.4 | Forge | 1.19.4 | 1.7.1 | G3 |
| forge-mc1.20.1 | Forge | 1.20.1 | 1.8.1 | G3 |
| forge-mc1.20.4-1.21.11 | Forge | 1.20.4 → 1.21.11 | 1.9.1 → 1.12.3 | modern union |
| fabric-mc1.19.3 | Fabric | 1.19.3 | 1.7.0 | G2 |
| fabric-mc1.19.4 | Fabric | 1.19.4 | 1.7.1 | G3 |
| fabric-mc1.20.1 | Fabric | 1.20.1 | 1.8.1 | G3 |
| fabric-mc1.20.4-26.2 | Fabric | 1.20.4 → 26.2 | 1.9.1 → 1.12.3 | modern union |
| neoforge-mc1.20.4-26.2 | NeoForge | 1.20.4 → 26.2 | 1.9.1 → 1.12.3 | modern union |
| fabric-mc26.3 | Fabric | 26.3 | 1.12.3 | G6 + 34-key Catalogue Marathi + 8,559-key embedded Minecraft Marathi |
| neoforge-mc26.3 | NeoForge | 26.3 | 1.12.3 | G6 + 34-key Catalogue Marathi + 8,559-key embedded Minecraft Marathi |

## Upload metadata notes

The two 26.3 artifacts are separate from the 1.20.4–26.2 grouped JARs so the complete 26.3 vanilla Marathi resource does not override earlier Minecraft text. Each is **one JAR per loader**, with no accompanying resource-pack ZIP. Upstream Catalogue 26.3 is available for Fabric and NeoForge from its GitHub release; do not tag Forge 26.3.

The grouped JAR dependency ranges are intentionally broader than the exact set of Catalogue releases. CurseForge/Modrinth game-version tags must follow versions for which Catalogue actually has a compatible release.

- **Minecraft 1.21.5 is a real Catalogue target** and must be included for the grouped Forge, Fabric and NeoForge files. Catalogue's repository history contains a genuine 1.21.5 target even though the current head of the old `multiloader/1.21.5` branch was later moved to 1.21.6.
- **Minecraft 1.21.2 must not be tagged** for the grouped files because Catalogue has no published 1.21.2 file. The upstream release list jumps from 1.21.1 to 1.21.3.
- The audited resource-pack format for Minecraft **1.21.5 is 55**.
- 26.1+ Catalogue releases use Fabric and NeoForge; do not tag Forge for those versions.

Do not infer historical target versions from the current contents of an old branch alone. Check release files, commits and `gradle.properties` together.
