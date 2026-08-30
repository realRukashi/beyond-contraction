# Reproducibility guide

## Scope

The three paper-facing notebooks are executed and self-contained enough to show the full analysis logic and reported outputs. They download third-party data/models on demand and create local embedding caches that are intentionally excluded from version control.

## Environment

The supplied executed notebooks report Python 3.12.13. Their setup cells install `datasets>=2.18,<4`, `transformers>=4.43,<5`, `accelerate`, SciPy, scikit-learn, pandas, PyArrow, tqdm, SentencePiece, and (for Experiment C) `concept-erasure`. `requirements.txt` mirrors these dependencies but does not claim an exact lockfile because exact installed package versions were not preserved in the supplied artifacts.

A GPU is strongly recommended for the resource profile.

## Run order

1. `notebooks/paper/03_experiment_a_controlled_evidence.ipynb`
2. `notebooks/paper/04_experiment_b_nested_update.ipynb`
3. `notebooks/paper/05_experiment_c_validation.ipynb`

The two notebooks under `notebooks/development/` document the earlier pilot progression and are not required for paper results.

## Main fixed settings

- Random seed used for global setup: `2026`.
- Encoders: `bert-base-uncased`, `roberta-base`, `microsoft/deberta-v3-base`.
- Layers: 4, 8, 12; LEACE validation uses layers 8 and 12 in the resource profile.
- CoarseWSD-20 is balanced within lexical item/sense subject to notebook-specific caps.
- Experiment A diagnostic ordering is training-only token-sense PMI; five random reveal seeds are used in the resource run.
- Experiment B base context sizes are 2, 4, 8 tokens with three matched control seeds.
- Natural validation uses 2, 4, 8, 16 nearest context tokens.

## Statistical unit

The lexical item is the primary statistical unit for CoarseWSD analyses. Repeated token pairs and aggregate model/layer/evidence cells are not treated as independent replications. The paper avoids naive pair-level significance claims for clustered natural-transition and RAW-C observations.

## Outputs not bundled

The original notebook runs create larger cache and per-word result directories. Those directories were not among the supplied files used to assemble this repository package, so only the executed notebooks, curated figures, and paper-facing summary CSVs are included here.
