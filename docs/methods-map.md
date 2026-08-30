# Methods map: the paper without the jargon

The paper has one core observation and two layers of follow-up.

## 1. Core test: does disambiguation contract the cloud?

For each ambiguous noun, context tokens are revealed in two matched ways: a sense-diagnostic ordering chosen from **training-only** token-sense PMI, and random orderings with the same number of visible tokens. The target-token representation is then measured at layers 4, 8, and 12 in frozen BERT, RoBERTa, and DeBERTa-v3.

Two quantities are separated:

- **Within-sense dispersion (`W`)**: how spread out examples of the *same* sense are.
- **Between-sense separation (`B`)**: how far sense centroids are from the overall centroid.

The robust pattern is `B` increasing under diagnostic evidence. `W` can decrease, stay nearly unchanged, or increase. Therefore clearer sense information does not require universal within-sense contraction.

## 2. Same-starting-point test: what changes when one useful cue is added?

Experiment B starts from an identical base context and adds either one diagnostic cue or one matched control cue. It asks four different questions instead of treating them as one:

1. Does sense become easier for a linear probe to recover? **Yes.**
2. Does the update point more into a supervised sense-discriminative subspace? **Yes, descriptively.**
3. Does the rest of the representational structure remain identical? **No; CKA decreases relative to control.**
4. Is a fixed lexical summary of the old context still recoverable? **Mostly; a newly fit decoder does about as well as controls, while a base-trained decoder transfers worse.**

That combination motivates the word *reorganization*. It does not identify a unique mechanism.

## 3. Validation: try to make the story fail

- **Natural local context:** reveal nearest tokens without using the gold sense to choose them. Sense accessibility usually rises as context grows.
- **LEACE:** remove linearly accessible sense signal. Sense decoding drops strongly while the fixed old-context target drops only modestly.
- **RAW-C:** embedding similarity tracks graded human semantic relatedness descriptively.

## Misreadings the paper explicitly blocks

| Tempting reading | What the evidence actually supports |
|---|---|
| "The model's semantic entropy falls." | Not measured. The paper measures linear sense accessibility. |
| "The model has one true internal sense axis." | Not shown. The sense subspace is supervised with gold labels. |
| "All old context is preserved." | Not shown. Only a fixed low-dimensional lexical target is reconstructed. |
| "LEACE deletes the concept from the model." | Not shown. LEACE removes linear accessibility under the fitted setting. |
| "45/45 means 45 independent replications." | No. It is a descriptive robustness count over shared words/models/layers. |
| "Reorganization is a proved transformer mechanism." | No. It is a compact description of the observed geometry. |
