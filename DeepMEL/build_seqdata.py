import argparse
import os

import numpy as np
import pandas as pd
import seqdata as sd
from eugene import preprocess as pp


def main(args):
    print("Loading targets, names, and seqs from npy files")
    targets = np.load(os.path.join(args.data_dir, args.dataset_name + ".labels.npy"))
    names = np.load(os.path.join(args.data_dir, args.dataset_name + ".regions.npy"), allow_pickle=True)
    seqs = np.load(os.path.join(args.data_dir, args.dataset_name + ".seqs.npy"), allow_pickle=True)
    topic_names = [f"Topic{i+1}" for i in range(targets.shape[1])]
    topic_df = pd.DataFrame(data=targets, index=names, columns=topic_names)
    sdata = sd.SeqData(
        seqs=seqs,
        names=names,
        seqs_annot=topic_df
    )

    print("Preprocessing")
    pp.sanitize_seqs_sdata(sdata)
    mask = np.array([False if "N" in seq else True for seq in sdata.seqs])
    sdata = sdata[mask]
    print(f"Removed {np.sum(~mask)} sequences with N")
    pp.add_ranges_sdata(sdata)
    pp.ohe_seqs_sdata(sdata)
    pp.train_test_split_sdata(sdata, train_key="train_test", chr="chr2")
    train_sdata = sdata[sdata["train_test"]]
    test_sdata = sdata[~sdata["train_test"]]
    print("Split into train and test")
    print(f"Train: {train_sdata.n_obs}")
    print(f"Test: {test_sdata.n_obs}")
    pp.train_test_split_sdata(train_sdata, train_key="train_val", chr="chr3")
    train_sdata.write_h5sd(os.path.join(args.output_dir, args.dataset_name + ".train.h5sd"))
    test_sdata.write_h5sd(os.path.join(args.output_dir, args.dataset_name + ".test.h5sd"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Build SeqData object for from binarized topics")
    parser.add_argument("--dataset_name", type=str, required=True)
    parser.add_argument("--data_dir", type=str, required=True)
    parser.add_argument("--output_dir", type=str, required=True)
    args = parser.parse_args()
    main(args)
