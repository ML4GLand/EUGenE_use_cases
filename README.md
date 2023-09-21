# Use cases
This repository contains *attempts* to reproduce foundational research in machine learning for genomics using EUGENe and other ML4GLand tools. It also lends itself nicely for aggregating interesting analyses and visualizations of data that extend beyond the scope of the original research. We hope to encourage others to contribute their own use cases and analyses to this repository.

# Organization
The repository is split into subdirectories by model (e.g. Basset). Inside each subdirectory, you will find a README.md file that outlines what has implemented to date, and potentially exciting next steps. You will also find a `setup.ipynb` notebook that is meant to serve as a guide to getting your computational environment set-up for working with those notebooks. *Note*, for many of these use cases, both these files are works in progress.

The actual analysis notebooks will vary depending on the use case. For instance, most people don't have the computational resources available to retrain Basenji2, so the notebooks in that subdirectory are currently limited to inference. The scBasset subdirectory, on the other hand, can effectively be run on any scATAC-seq dataset, and is therefore organized by dataset.

# Contributing
We will be setting up more formal contribution guidelines in the future. For now, we are accepting many different forms of contribution. 

- If one of your models is represented here, I'm guessing I haven't done it justice, so please feel free to submit a pull request with your own notebooks and/or analyses. 
- If you have a use case or analysis that you would like to see implemented or have already completed, please open an issue and we can discuss how to get it added to the repository.
- If you find issues with any of the notebooks (guessing there will be plenty), please open an issue!

# Contact
If you have any questions, please feel free to reach out to me at `aklie@ucsd.edu`.

# TODO
- [ ] Create a script to run that generates all the files for a new use case that someone can use to get started with a new ones