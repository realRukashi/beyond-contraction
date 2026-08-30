# Publishing this research repository on GitHub

This package follows the repository elements GitHub itself recommends for understandable and reusable projects: a README, license, citation file, and contribution guidance. GitHub also recognizes `CITATION.cff` in the repository root and exposes a **Cite this repository** control.

## Minimal release path

1. Create a new **public** GitHub repository and upload the contents of this archive as the repository root.
2. Verify the publication identity is consistent: **Hồ Ngọc Huy**, ORCID **0009-0007-4156-352X**.
3. Run `python scripts/repo_check.py` locally once before pushing.
4. Create a tagged GitHub release such as `v0.1.0` after the repository looks correct.
5. Optional: connect the public repository to Zenodo. Zenodo can archive GitHub releases and mint a DOI, which is more stable to cite than a moving branch.
6. After a DOI is minted, add it to `CITATION.cff`, `README.md`, and the canonical paper metadata before the next release.

## Why these files are here

- `README.md`: first-page explanation and navigation.
- `LICENSE` / `paper/LICENSE.md`: reuse terms for code versus manuscript.
- `CITATION.cff`: machine-readable citation metadata supported by GitHub.
- `REPRODUCIBILITY.md`: environment, run order, and what is intentionally excluded.
- `AI_USE.md`: explicit provenance/disclosure rather than burying AI assistance.
- `THIRD_PARTY_DATA.md`: avoids silently redistributing data/models with separate terms.

## Official references consulted

- GitHub Docs, **Best practices for repositories**: https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories
- GitHub Docs, **About CITATION files**: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files
- GitHub Docs, **Adding a license to a repository**: https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository
- GitHub Docs, **Referencing and citing content** (Zenodo DOI workflow): https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content
- Zenodo Help, **Enable a repository / archive a GitHub release**: https://help.zenodo.org/docs/github/enable-repository/ and https://help.zenodo.org/docs/github/archive-software/github-upload/
