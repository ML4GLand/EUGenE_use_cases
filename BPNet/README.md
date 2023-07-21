# BPNet
---
Code to work with BPNet models. This includes:
 - Training and interpreting models with Jacob Schreiber's bpnet-lite repo
 - Training and interpreting BPNet models from scratch with [EUGENe].
 - Testing the Kipoi BPNet model

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
- Jacob Schreiber: https://github.com/jmschrei/bpnet-lite
- Kipoi team: https://kipoi.org/

## TODO
---
- [x] Train BPNet model from scratch using bpnetlite
- [x] Train BPNet model from scratch using seqdata-bpnetlite combo
- [x] Train BPNet model from scratch using eugene
- [x] Notebook comparing training across models
- [ ] Fix transforms issues with EUGENe (new branch of SeqData)
- [ ] Test inference on BPNet model from Kipoi
- [ ] Attributions across models
- [ ] Extension to chrombpnet

## Citations
---
```bibtex
@ARTICLE{Avsec2021-sw,
  title    = "Base-resolution models of transcription-factor binding reveal
              soft motif syntax",
  author   = "Avsec, {\v Z}iga and Weilert, Melanie and Shrikumar, Avanti and
              Krueger, Sabrina and Alexandari, Amr and Dalal, Khyati and Fropf,
              Robin and McAnany, Charles and Gagneur, Julien and Kundaje,
              Anshul and Zeitlinger, Julia",
  abstract = "The arrangement (syntax) of transcription factor (TF) binding
              motifs is an important part of the cis-regulatory code, yet
              remains elusive. We introduce a deep learning model, BPNet, that
              uses DNA sequence to predict base-resolution chromatin
              immunoprecipitation (ChIP)-nexus binding profiles of pluripotency
              TFs. We develop interpretation tools to learn predictive motif
              representations and identify soft syntax rules for cooperative TF
              binding interactions. Strikingly, Nanog preferentially binds with
              helical periodicity, and TFs often cooperate in a directional
              manner, which we validate using clustered regularly interspaced
              short palindromic repeat (CRISPR)-induced point mutations. Our
              model represents a powerful general approach to uncover the
              motifs and syntax of cis-regulatory sequences in genomics data.",
  journal  = "Nat. Genet.",
  volume   =  53,
  number   =  3,
  pages    = "354--366",
  month    =  mar,
  year     =  2021,
  language = "en"
}
```
