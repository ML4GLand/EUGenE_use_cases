# scBasset
---
Code to work with scBasset models. This currently includes:
 - Preprocessing scATAC-seq datasets with code from scBasset and EUGENe
 - Training scBasset models from scratch with scBasset and EUGENe.

## Install
---
Follow the instructions in the `setup.ipynb` notebook to configure computational environments and get data needed to run the notebooks.

## Usage
---
1. Training scBasset models from scratch
scBasset is a framework that can be applied to any scATAC-seq dataset. We have chosen a few particular datasets:
- PBMC 3k multiome
- Buenrostro 2018
You can find numerically ordered notebooks in this directory for running the steps necessary to preprocess and train scBasset models on these datasets.
 
2. Benchmarking scBasset models
Coming soon!

3. Interpreting scBasset models
Coming soon!

## Acknowledgements
---
- Han Yuan: 
- Kipoi team: https://kipoi.org/

## TODO
---
- [ ] Add notebooks for benchmarking scBasset models against each other
- [ ] Add notebooks for interpreting scBasset models

## Citations
---
```bibtex
@ARTICLE{Yuan2022-gg,
  title    = "scBasset: sequence-based modeling of single-cell {ATAC-seq} using
              convolutional neural networks",
  author   = "Yuan, Han and Kelley, David R",
  abstract = "Single-cell assay for transposase-accessible chromatin using
              sequencing (scATAC) shows great promise for studying cellular
              heterogeneity in epigenetic landscapes, but there remain
              important challenges in the analysis of scATAC data due to the
              inherent high dimensionality and sparsity. Here we introduce
              scBasset, a sequence-based convolutional neural network method to
              model scATAC data. We show that by leveraging the DNA sequence
              information underlying accessibility peaks and the expressiveness
              of a neural network model, scBasset achieves state-of-the-art
              performance across a variety of tasks on scATAC and single-cell
              multiome datasets, including cell clustering, scATAC profile
              denoising, data integration across assays and transcription
              factor activity inference.",
  journal  = "Nat. Methods",
  month    =  aug,
  year     =  2022,
  language = "en"
}
```
