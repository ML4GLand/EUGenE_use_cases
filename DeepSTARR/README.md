# BPNet
---
Code to work with DeepSTARR models. This includes:
 - Training and interpreting BPNet models from scratch with [EUGENe].
 - Testing the Kipoi DeepSTARR model
 - Testing Bernardo's DeepSTARR model in keras

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
- Bernardo de Almeida:
- Kipoi team: https://kipoi.org/

## TODO
---
- [ ] Train new DeepSTARR model with EUGENe update
- [ ] Run inference on test set with Zenodo model
- [ ] Run inference on test set with Kipoi model
- [ ] Notebook comparing inference results
- [ ] Attributions across models

## Citations
---
```bibtex
@ARTICLE{De_Almeida2022-aa,
  title     = "{DeepSTARR} predicts enhancer activity from {DNA} sequence and
               enables the de novo design of synthetic enhancers",
  author    = "de Almeida, Bernardo P and Reiter, Franziska and Pagani,
               Michaela and Stark, Alexander",
  abstract  = "Enhancer sequences control gene expression and comprise binding
               sites (motifs) for different transcription factors (TFs).
               Despite extensive genetic and computational studies, the
               relationship between DNA sequence and regulatory activity is
               poorly understood, and de novo enhancer design has been
               challenging. Here, we built a deep-learning model, DeepSTARR, to
               quantitatively predict the activities of thousands of
               developmental and housekeeping enhancers directly from DNA
               sequence in Drosophila melanogaster S2 cells. The model learned
               relevant TF motifs and higher-order syntax rules, including
               functionally nonequivalent instances of the same TF motif that
               are determined by motif-flanking sequence and intermotif
               distances. We validated these rules experimentally and
               demonstrated that they can be generalized to humans by testing
               more than 40,000 wildtype and mutant Drosophila and human
               enhancers. Finally, we designed and functionally validated
               synthetic enhancers with desired activities de novo. A
               deep-learning model called DeepSTARR quantitatively predicts
               enhancer activity on the basis of DNA sequence. The model learns
               relevant motifs and syntax rules, allowing for the design of
               synthetic enhancers with specific strengths.",
  journal   = "Nat. Genet.",
  publisher = "Nature Publishing Group",
  volume    =  54,
  number    =  5,
  pages     = "613--624",
  month     =  may,
  year      =  2022,
  language  = "en"
}
```
