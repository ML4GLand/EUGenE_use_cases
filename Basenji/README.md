# Basenji
---
Code to work with pretrained Basenji models from multiple sources:

- David Kelley's [Basenji]() repository
- David Laub's [basenji2-pytorch]() repository
- Kipoi's [Basenji]() model

## Install
---
Follow the instructions in the `setup.ipynb` notebook to configure computational environments for each pretrained model.

## Usage
---
1. Testing
 - See the `test_inference*.ipynb` notebooks for examples of how to use the pretrained models for inference.

## Fine-tuning
---
Coming soon!

## Acknowledgements
---
- David Kelley: https://github.com/calico/basenji
- David Laub: https://github.com/d-laub/basenji2-pytorch
- Kipoi team: https://kipoi.org/

## TODO
---
- [x] Get DL's model working for inference
- [x] Get Kipoi's model working for inference
- [ ] Get DRKs basenji model working
- [ ] Notebook comparing inference across models
- [ ] Add fine-tuning example for PyTorch
- [ ] Reproduce an analysis from Alex Karollus's paper: https://github.com/Karollus/SequenceModelBenchmark
- [ ]

## Citations
---
```bibtex
@ARTICLE{Kelley2018-if,
  title    = "Sequential regulatory activity prediction across chromosomes with
              convolutional neural networks",
  author   = "Kelley, David R and Reshef, Yakir A and Bileschi, Maxwell and
              Belanger, David and McLean, Cory Y and Snoek, Jasper",
  abstract = "Models for predicting phenotypic outcomes from genotypes have
              important applications to understanding genomic function and
              improving human health. Here, we develop a machine-learning
              system to predict cell-type-specific epigenetic and
              transcriptional profiles in large mammalian genomes from DNA
              sequence alone. By use of convolutional neural networks, this
              system identifies promoters and distal regulatory elements and
              synthesizes their content to make effective gene expression
              predictions. We show that model predictions for the influence of
              genomic variants on gene expression align well to causal variants
              underlying eQTLs in human populations and can be useful for
              generating mechanistic hypotheses to enable fine mapping of
              disease loci.",
  journal  = "Genome Res",
  volume   =  28,
  number   =  5,
  pages    = "739--750",
  month    =  may,
  year     =  2018,
  language = "en"
}
```

```bibtex
@ARTICLE{Kelley2020-tp,
  title    = "Cross-species regulatory sequence activity prediction",
  author   = "Kelley, David R",
  abstract = "Machine learning algorithms trained to predict the regulatory
              activity of nucleic acid sequences have revealed principles of
              gene regulation and guided genetic variation analysis. While the
              human genome has been extensively annotated and studied, model
              organisms have been less explored. Model organism genomes offer
              both additional training sequences and unique annotations
              describing tissue and cell states unavailable in humans. Here, we
              develop a strategy to train deep convolutional neural networks
              simultaneously on multiple genomes and apply it to learn sequence
              predictors for large compendia of human and mouse data. Training
              on both genomes improves gene expression prediction accuracy on
              held out and variant sequences. We further demonstrate a novel
              and powerful approach to apply mouse regulatory models to analyze
              human genetic variants associated with molecular phenotypes and
              disease. Together these techniques unleash thousands of non-human
              epigenetic and transcriptional profiles toward more effective
              investigation of how gene regulation affects human disease.",
  journal  = "PLoS Comput. Biol.",
  volume   =  16,
  number   =  7,
  pages    = "e1008050",
  month    =  jul,
  year     =  2020,
  language = "en"
}
```
