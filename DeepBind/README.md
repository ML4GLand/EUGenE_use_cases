# BPNet
---
Code to work with DeepBind models. This includes:
 - Training and interpreting DeepBind models from scratch with [EUGENe].
 - Testing the Kipoi DeepBind models
 - Training and interpreting ResidualBind models from scratch with [EUGENe].
 - Inference with ResidualBind models from Peter Koo
 - Fine-tuning?

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
- Kipoi team: https://kipoi.org/
- Peter Koo: 

## TODO
---
- [ ] Put up EUGENE_paper trained models on Zenodo, show how to download in setup.ipynb
- [ ] Notebook for training DeepBind models from scratch from SeqDatasets
- [ ] Notebook for training DeepBind and ResidualBind models from PK's data in ResidualBind
- [ ] Notebook training ResidualBind models with PKs code
- [ ] Test inference on DeepBind model from Kipoi
- [ ] Attributions across models

## Citations
---
```bibtex
@ARTICLE{Alipanahi2015-ef,
  title    = "Predicting the sequence specificities of {DNA-} and {RNA-binding}
              proteins by deep learning",
  author   = "Alipanahi, Babak and Delong, Andrew and Weirauch, Matthew T and
              Frey, Brendan J",
  abstract = "Knowing the sequence specificities of DNA- and RNA-binding
              proteins is essential for developing models of the regulatory
              processes in biological systems and for identifying causal
              disease variants. Here we show that sequence specificities can be
              ascertained from experimental data with 'deep learning'
              techniques, which offer a scalable, flexible and unified
              computational approach for pattern discovery. Using a diverse
              array of experimental data and evaluation metrics, we find that
              deep learning outperforms other state-of-the-art methods, even
              when training on in vitro data and testing on in vivo data. We
              call this approach DeepBind and have built a stand-alone software
              tool that is fully automatic and handles millions of sequences
              per experiment. Specificities determined by DeepBind are readily
              visualized as a weighted ensemble of position weight matrices or
              as a 'mutation map' that indicates how variations affect binding
              within a specific sequence.",
  journal  = "Nat. Biotechnol.",
  volume   =  33,
  number   =  8,
  pages    = "831--838",
  month    =  aug,
  year     =  2015,
  language = "en"
}
```

```bibtex

@ARTICLE{Koo2021-ly,
  title    = "Global importance analysis: An interpretability method to
              quantify importance of genomic features in deep neural networks",
  author   = "Koo, Peter K and Majdandzic, Antonio and Ploenzke, Matthew and
              Anand, Praveen and Paul, Steffan B",
  abstract = "Deep neural networks have demonstrated improved performance at
              predicting the sequence specificities of DNA- and RNA-binding
              proteins compared to previous methods that rely on k-mers and
              position weight matrices. To gain insights into why a DNN makes a
              given prediction, model interpretability methods, such as
              attribution methods, can be employed to identify motif-like
              representations along a given sequence. Because explanations are
              given on an individual sequence basis and can vary substantially
              across sequences, deducing generalizable trends across the
              dataset and quantifying their effect size remains a challenge.
              Here we introduce global importance analysis (GIA), a model
              interpretability method that quantifies the population-level
              effect size that putative patterns have on model predictions. GIA
              provides an avenue to quantitatively test hypotheses of putative
              patterns and their interactions with other patterns, as well as
              map out specific functions the network has learned. As a case
              study, we demonstrate the utility of GIA on the computational
              task of predicting RNA-protein interactions from sequence. We
              first introduce a convolutional network, we call ResidualBind,
              and benchmark its performance against previous methods on
              RNAcompete data. Using GIA, we then demonstrate that in addition
              to sequence motifs, ResidualBind learns a model that considers
              the number of motifs, their spacing, and sequence context, such
              as RNA secondary structure and GC-bias.",
  journal  = "PLoS Comput. Biol.",
  volume   =  17,
  number   =  5,
  pages    = "e1008925",
  month    =  may,
  year     =  2021,
  language = "en"
}
```
