# ResidualBind
---
Code to work with ResidualBind models. This includes:
 - Training ResidualBind models from scratch on RNACompete2013 data
 - Comparing performances of ResidualBind models to those reported in the paper
 - Interpreting ResidualBind models using attributions, filters, evolution, and global importance analysis (GIA)

## Install
---
Follow the instructions in the `setup.ipynb` notebook to configure computational environments.

## Usage
---
1. 

## RNACompete2013
This dataset represents an in vitro RNA-binding protein assay of 244 RNA binding proteins. The dataset is downloaded as a single TSV file with RNA probes as rows and RNA binding proteins (RBP) as columns. Each entry in the table is an intensity measurement (can be normalized or raw) of the binding of each protein to each probe. There are over 244 RBP columns and 241,357 sequences spanning two sets (SetA and SetB)

https://hugheslab.ccbr.utoronto.ca/supplementary-data/RNAcompete_eukarya/


## Acknowledgements
---
- Peter Koo: https://github.com/p-koo/residualbind

## TODO
---
- [x] Prepare SeqDatas RNACompete2013 dataset
- [x] Train ResidualBind models from scratch 
- [] Compare performance of ResidualBind model to those reported in the Koo2021
- [] Basic interpretaion functionality on RBFOX2 ('RNCMPT00168')
- [] GIA interpretation on RBFOX2 ('RNCMPT00168')
- [] GIA interpretation on VTS1 ('RNCMPT00168')
- [] GC bias analysis

## Citations
---
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
