# Basenji
---
Code to work with Basset models. This includes:
 - David Kelley's pretrained [Basset]() model. Can use this for benchmarking, inference and other downstream tasks.
 - Training and interpreting Basset models from scratch with [EUGENe].
 - Testing the Basset model trained in the [EvoAug paper](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-023-02941-w).

## Install
---
Follow the instructions in the `setup.ipynb` notebook to configure computational environments.

## Usage
---
1. Testing
 - See the `test_inference*.ipynb` notebooks for examples of how to use the pretrained models for inference.

2. Training
 - See the `train_*.ipynb` notebooks for examples of how to train Basset models from scratch with EUGENe.
 
## Fine-tuning
---
Coming soon!

## Acknowledgements
---
- David Kelley: https://github.com/davek44/Basset
- Peter Koo: https://genomebiology.biomedcentral.com/articles/10.1186/s13059-023-02941-w
- Kipoi team: https://kipoi.org/

## TODO
---
- [x] Get Kipoi's model working for inference
- [x] Train Basset model from scratch using EUGENe
- [ ] Get DRKs code running from GitHub
- [ ] Notebook comparing inference across models
- [ ] Add fine-tuning example for PyTorch
- [ ] Interpret all PyTorch models with EUGENe on examples from papers

## Citations
---
```bibtex
@ARTICLE{Kelley2016-oh,
  title    = "Basset: learning the regulatory code of the accessible genome
              with deep convolutional neural networks",
  author   = "Kelley, David R and Snoek, Jasper and Rinn, John L",
  abstract = "The complex language of eukaryotic gene expression remains
              incompletely understood. Despite the importance suggested by many
              noncoding variants statistically associated with human disease,
              nearly all such variants have unknown mechanisms. Here, we
              address this challenge using an approach based on a recent
              machine learning advance-deep convolutional neural networks
              (CNNs). We introduce the open source package Basset to apply CNNs
              to learn the functional activity of DNA sequences from genomics
              data. We trained Basset on a compendium of accessible genomic
              sites mapped in 164 cell types by DNase-seq, and demonstrate
              greater predictive accuracy than previous methods. Basset
              predictions for the change in accessibility between variant
              alleles were far greater for Genome-wide association study (GWAS)
              SNPs that are likely to be causal relative to nearby SNPs in
              linkage disequilibrium with them. With Basset, a researcher can
              perform a single sequencing assay in their cell type of interest
              and simultaneously learn that cell's chromatin accessibility code
              and annotate every mutation in the genome with its influence on
              present accessibility and latent potential for accessibility.
              Thus, Basset offers a powerful computational approach to annotate
              and interpret the noncoding genome.",
  journal  = "Genome Res",
  volume   =  26,
  number   =  7,
  pages    = "990--999",
  month    =  jul,
  year     =  2016,
  language = "en"
}

```

```bibtex

@ARTICLE{Lee2023-hk,
  title    = "{EvoAug}: improving generalization and interpretability of
              genomic deep neural networks with evolution-inspired data
              augmentations",
  author   = "Lee, Nicholas Keone and Tang, Ziqi and Toneyan, Shushan and Koo,
              Peter K",
  abstract = "Deep neural networks (DNNs) hold promise for functional genomics
              prediction, but their generalization capability may be limited by
              the amount of available data. To address this, we propose EvoAug,
              a suite of evolution-inspired augmentations that enhance the
              training of genomic DNNs by increasing genetic variation. Random
              transformation of DNA sequences can potentially alter their
              function in unknown ways, so we employ a fine-tuning procedure
              using the original non-transformed data to preserve functional
              integrity. Our results demonstrate that EvoAug substantially
              improves the generalization and interpretability of established
              DNNs across prominent regulatory genomics prediction tasks,
              offering a robust solution for genomic DNNs.",
  journal  = "Genome Biol.",
  volume   =  24,
  number   =  1,
  pages    = "105",
  month    =  may,
  year     =  2023,
  keywords = "Data augmentations; Deep learning; Model interpretability;
              Regulatory genomics",
  language = "en"
}
```
