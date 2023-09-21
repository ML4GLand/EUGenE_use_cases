# Script to build a pycisTopic object from saved cisTopic files from R
# USAGE: python ${script_dir}/cisTopic2pycisTopic.py \
#   --directory /path/to/output/directory \
#   --dataset_name dataset_name

import argparse
import logging
import os
import pickle
import sys

import pandas as pd
from scipy import io

sys.path.append("/cellar/users/aklie/projects/ML4GLand/collabs/er_stress_regulation")
from pycisTopic.cistopic_class import create_cistopic_object
from utils import load_cisTopic_model


def convert_cistopic(directory, dataset_name):

    # Set default logging level to INFO
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"    
    )
    
    # Quick warning
    logging.warning("Make sure you've run cisTopic2pycisTopic.R first or formatted your data based on it's output")
    
    # Load the LDA model
    logging.info("Loading the cisTopic model")
    model = load_cisTopic_model(dataset_dir=directory, dataset_name=dataset_name)

    # Load the fragment count matrix (likely will take minutes if have a lot of cells and regions)
    logging.info("Loading the fragment count matrix, this will be the most time consuming step")
    fragment_matrix = io.mmread(os.path.join(directory, dataset_name + ".countMatrix.mtx"))
    fragment_matrix = fragment_matrix.tocsr()
    logging.info("Fragment count matrix loaded with size: {}".format(fragment_matrix.shape))

    # Load in cell and region metadata
    logging.info("Loading the cell and region metadata")
    cell_data = pd.read_csv(os.path.join(directory, dataset_name + ".cellData.tsv"), sep="\t")
    logging.info("Cell metadata loaded with size: {}".format(cell_data.shape))
    region_data = pd.read_csv(os.path.join(directory, dataset_name + ".regionData.tsv"), sep="\t")
    logging.info("Region metadata loaded with size: {}".format(region_data.shape))

    # Create a pycisTopic object
    logging.info("Creating the pycisTopic object")
    cisTopic_obj = create_cistopic_object(
        fragment_matrix=fragment_matrix, 
        cell_names=cell_data.index, 
        region_names=region_data.index, 
        split_pattern="", 
        project=""
    )

    # Also add the cell annotation
    logging.info("Adding the cell annotation")
    cisTopic_obj.add_cell_data(cell_data)
    
    # Add the cisTopic model to the pycisTopic object
    logging.info("Adding the cisTopic model to the pycisTopic object")
    cisTopic_obj.add_LDA_model(model)
    
    # Save the pycisTopic object
    logging.info("Saving the pycisTopic object")
    pickle.dump(
        cisTopic_obj,
        open(os.path.join(directory, dataset_name + ".pycisTopic_obj.pkl"), "wb")
    )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert saved cisTopic objects to pycisTopic')
    parser.add_argument('--directory', type=str, help='Directory where all the cisTopic objects are saved')
    parser.add_argument('--dataset_name', type=str, help='Name of the dataset')
    args = parser.parse_args()
    convert_cistopic(args.directory, args.dataset_name)