# DeepMEL
---
Code to work with DeepMEL models. This includes:
 - Training, evaluating, and interpreting DeepMEL models

## Install
---
Follow the instructions in the `setup.ipynb` notebook to configure computational environments.

## Usage
---
1. Consensus peak calling (optional) -- you can also skip this step if you just want to use CellRanger called peaks
2. pycisTopic analysis -- check out the https://github.com/IGVF-UCSD/cistopic_pipeline for a more thoroughly defined pipeline for running cisTopic (especially if you have big datasets)
3. Convert pycisTopic objects to training inputs
4. Build SeqData objects for training
5. Train DeepMEL models
6. Evaluate DeepMEL models
7. Interpret DeepMEL models

## Acknowledgements
---
- Ibrahim Taskiran: 
- Kipoi team: https://kipoi.org/

## TODO
---
- [ ] Add more documentation
- [ ]

## Citations
---
```bibtex
@ARTICLE{Minnoye2020-vz,
  title    = "Cross-species analysis of enhancer logic using deep learning",
  author   = "Minnoye, Liesbeth and Taskiran, Ibrahim Ihsan and Mauduit, David
              and Fazio, Maurizio and Van Aerschot, Linde and Hulselmans, Gert
              and Christiaens, Valerie and Makhzami, Samira and Seltenhammer,
              Monika and Karras, Panagiotis and Primot, Aline and Cadieu,
              Edouard and van Rooijen, Ellen and Marine, Jean-Christophe and
              Egidy, Giorgia and Ghanem, Ghanem Elias and Zon, Leonard and
              Wouters, Jasper and Aerts, Stein",
  abstract = "Deciphering the genomic regulatory code of enhancers is a key
              challenge in biology as this code underlies cellular identity. A
              better understanding of how enhancers work will improve the
              interpretation of noncoding genome variation, and empower the
              generation of cell type-specific drivers for gene therapy. Here
              we explore the combination of deep learning and cross-species
              chromatin accessibility profiling to build explainable enhancer
              models. We apply this strategy to decipher the enhancer code in
              melanoma, a relevant case study due to the presence of distinct
              melanoma cell states. We trained and validated a deep learning
              model, called DeepMEL, using chromatin accessibility data of 26
              melanoma samples across six different species. We demonstrate the
              accuracy of DeepMEL predictions on the CAGI5 challenge, where it
              significantly outperforms existing models on the melanoma
              enhancer of IRF4 Next, we exploit DeepMEL to analyse enhancer
              architectures and identify accurate transcription factor binding
              sites for the core regulatory complexes in the two different
              melanoma states, with distinct roles for each transcription
              factor, in terms of nucleosome displacement or enhancer
              activation. Finally, DeepMEL identifies orthologous enhancers
              across distantly related species where sequence alignment fails,
              and the model highlights specific nucleotide substitutions that
              underlie enhancer turnover. DeepMEL can be used from the Kipoi
              database to predict and optimise candidate enhancers, and to
              prioritise enhancer mutations. In addition, our computational
              strategy can be applied to other cancer or normal cell types.",
  journal  = "Genome Res.",
  month    =  jul,
  year     =  2020,
  language = "en"
}
```

```bibtex
@ARTICLE{Atak2021-sz,
  title     = "Interpretation of allele-specific chromatin accessibility using
               cell state-aware deep learning",
  author    = "Atak, Zeynep Kalender and Taskiran, Ibrahim Ihsan and
               Demeulemeester, Jonas and Flerin, Christopher and Mauduit, David
               and Minnoye, Liesbeth and Hulselmans, Gert and Christiaens,
               Valerie and Ghanem, Ghanem Elias and Wouters, Jasper and Aerts,
               Stein",
  abstract  = "Genomic sequence variation within enhancers and promoters can
               have a significant impact on the cellular state and phenotype.
               However, sifting through the millions of candidate variants in a
               personal genome or a cancer genome, to identify those that
               impact cis-regulatory function, remains a major challenge.
               Interpretation of noncoding genome variation benefits from
               explainable artificial intelligence to predict and interpret the
               impact of a mutation on gene regulation. Here we generate phased
               whole genomes with matched chromatin accessibility, histone
               modifications, and gene expression for 10 melanoma cell lines.
               We find that training a specialized deep learning model, called
               DeepMEL2, on melanoma chromatin accessibility data can capture
               the various regulatory programs of the melanocytic and
               mesenchymal-like melanoma cell states. This model outperforms
               motif-based variant scoring, as well as more generic deep
               learning models. We detect hundreds to thousands of
               allele-specific chromatin accessibility variants (ASCAVs) in
               each melanoma genome, of which 15-20\% can be explained by gains
               or losses of transcription factor binding sites. A considerable
               fraction of ASCAVs are caused by changes in AP-1 binding, as
               confirmed by matched ChIP-seq data to identify allele-specific
               binding of JUN and FOSL1. Finally, by augmenting the DeepMEL2
               model with ChIP-seq data for GABPA, the TERT promoter mutation
               as well as additional ETS motif gains can be identified with
               high confidence. In conclusion, we present a new integrative
               genomics approach and a deep learning model to identify and
               interpret functional enhancer mutations with allelic imbalance
               of chromatin accessibility and gene expression.",
  journal   = "Genome Res.",
  publisher = "Cold Spring Harbor Laboratory",
  pages     = "gr.260851.120",
  month     =  apr,
  year      =  2021,
  language  = "en"
}
```
