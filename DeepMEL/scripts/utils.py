import os
import pickle

import pandas as pd
from pycisTopic.cistopic_class import CistopicLDAModel


def load_cisTopic_model(
        dataset_dir, 
        dataset_name
    ):
    metrics = None
    coherence = None
    marg_topic = None
    topic_ass = None
    cell_topic_path = os.path.join(dataset_dir, dataset_name + ".cellMat.feather")
    region_topic_path = os.path.join(dataset_dir, dataset_name + ".regionMat.feather")
    cell_topic = pd.read_feather(cell_topic_path)
    cell_topic.index = ["Topic" + str(x) for x in range(1, cell_topic.shape[0] + 1)]
    topic_region = pd.read_feather(region_topic_path)
    topic_region.index = ["Topic" + str(x) for x in range(1, topic_region.shape[0] + 1)]
    topic_region = topic_region.T
    parameters = None
    model = CistopicLDAModel(
            metrics, 
            coherence, 
            marg_topic, 
            topic_ass, 
            cell_topic, 
            topic_region, 
            parameters
    )
    return model

def load_cisTopic_obj(file_name):
    """Load a cisTopic object from a pickle file"""
    with open(file_name, "rb") as f:
        cisTopic_obj = pickle.load(f)
    cisTopic_obj.selected_model.topic_ass = {}
    return cisTopic_obj