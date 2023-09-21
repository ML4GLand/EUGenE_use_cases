# scBasset
---
Code to work with scBasset models. This includes:
 - Running inference on scBasset models from Han
 - Training a scBasset model from scratch with [EUGENe].
 - Testing the Kipoi scBasset model

## Install
---
Follow the instructions in the `setup.ipynb` notebook to configure computational environments.

## Usage
---
1. Testing
 - See the `test_inference*.ipynb` notebooks for examples of how to use the pretrained models for inference. TODO!

2. Training
 - See the `train_*.ipynb` notebooks for examples of how to train models from scratch
 
## Model interpretation
---
Coming soon!

## Acknowledgements
---
- Han Yuan: 
- Kipoi team: https://kipoi.org/

## TODO
---
- [x] Get something working for loading pbmc 3k ATAC data into a EUGENe scBasset
- [ ] Run inference with Kipoi model
- [ ] Get Han's keras implementation working

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
