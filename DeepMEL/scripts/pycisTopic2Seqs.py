import os
import argparse

import numpy as np
import pandas as pd
import pyranges as pr
from pycisTopic.topic_binarization import binarize_topics
from utils import load_cisTopic_obj


def get_per_regions_topic_membership(region_dict):
    topic_regions_pd = pd.Index([])
    topic_regions_lst = []
    topic_region_mp = {}
    for topic, regions in region_dict.items():
        topic_regions_lst += list(regions.index)
        topic_regions_pd = pd.Index.union(topic_regions_pd, regions.index)
        for region in regions.index:
            topic_region_mp.setdefault(region, []).append(topic)
    return topic_regions_pd, topic_region_mp, topic_regions_lst

def get_nontopic_regions(all_regions, topic_regions_pd):
    non_topic_regions = all_regions[~all_regions.isin(topic_regions_pd)]
    return non_topic_regions

def create_binarized_matrix(all_regions, topic_region_mp, n_topics):
    arr = np.zeros((len(all_regions), n_topics))
    for i, row in enumerate(all_regions):
        if row in topic_region_mp:
            topic_nums = []
            for topic in topic_region_mp[row]:
                topic_nums.append(int(topic.split("Topic")[-1])-1)
            arr[i, topic_nums] = 1
    return arr

def check_topic_binarization(region_dict, arr, all_regions, non_topic_regions, topic_regions_pd, topic_regions_lst):
    for topic, regions in region_dict.items():
        assert non_topic_regions.isin(regions.index).sum() == 0, f"Topic {topic} contains a non-topic regions"
    assert np.all(np.array([len(regions) for _, regions in region_dict.items()]) == arr.sum(axis=0)), "Number of regions per topic does not match the number of 1s in the matrix"
    assert np.all(all_regions[arr.sum(axis=1) == 0].isin(non_topic_regions)), "Number of regions that are 0 across all topics does not match the number of non-topic regions"
    assert np.all(~all_regions[arr.sum(axis=1) == 0].isin(topic_regions_pd)), "Number of regions that are not 0 across all topics does not match the number of topic regions"
    assert arr.sum() == len(topic_regions_lst), "Number of 1s in the matrix does not match the number of topic regions"

def save_seqdata_files(
    bin_mtx, 
    regions, 
    output_dir, 
    dataset_name
):
    region_split = [region.split("-") for region in regions.str.replace(":", "-")]
    region_df = pd.DataFrame(region_split, columns=["Chromosome", "Start", "End"])
    pr_obj = pr.PyRanges(region_df)
    seqs = pr.get_fasta(pr_obj, "/cellar/users/aklie/data/ml4gland/genomes/hg38/hg38.fa")
    np.save(os.path.join(output_dir, dataset_name + ".labels.npy"), bin_mtx)
    np.save(os.path.join(output_dir, dataset_name + ".regions.npy"), regions)
    np.save(os.path.join(output_dir, dataset_name + ".seqs.npy"), seqs)

def main(args):
    print("Loading cisTopic object")
    cisTopic_obj = load_cisTopic_obj(os.path.join(args.dataset_dir, args.dataset_name + ".pycisTopic_obj.pkl"))
    print("Binarizing topics")
    region_dict = binarize_topics(cisTopic_obj, method='otsu', plot=True, num_columns=5, save=os.path.join(args.output_dir, "region_topic_binarization.pdf"))
    all_regions = cisTopic_obj.selected_model.topic_region.index
    all_regions = all_regions[all_regions.str.contains("chr")]
    print("Creating binarized matrix")
    topic_regions_pd, topic_region_mp, topic_regions_lst = get_per_regions_topic_membership(region_dict)
    non_topic_regions = get_nontopic_regions(all_regions, topic_regions_pd)
    arr = create_binarized_matrix(all_regions, topic_region_mp, cisTopic_obj.selected_model.topic_region.shape[1])
    print("Checking binarized matrix")
    check_topic_binarization(region_dict, arr, all_regions, non_topic_regions, topic_regions_pd, topic_regions_lst)
    print("Saving output files")
    save_seqdata_files(arr, all_regions, args.output_dir, args.dataset_name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert saved cisTopic objects into sequences and labels for training')
    parser.add_argument('--dataset_dir', type=str, help='Path to directory containing cisTopic output files')
    parser.add_argument('--dataset_name', type=str, help='Name of dataset')
    parser.add_argument('--output_dir', type=str, help='Path to directory to save output files')
    args = parser.parse_args()
    main(args)
    