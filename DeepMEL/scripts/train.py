import argparse
import os
import sys

import seqpro as sp
import torch
from eugene import dataload as dl
from eugene import models
from eugene import plot as pl
from eugene import train

sys.path.append("/cellar/users/aklie/projects/ML4GLand/collabs/er_stress_regulation/scripts")
from DeepMEL import DeepMEL


def main(args):
    print("Loading train data")
    train_sdata = dl.read_h5sd(os.path.join(args.data_dir, args.dataset_name + ".train.h5sd"))
    if args.n_topics is not None:
        cols = train_sdata.seqs_annot.columns
        topic_nums = [int(col.split("Topic")[-1]) for col in cols if col.startswith("Topic")]
        n_topics = max(topic_nums)
    else:
        n_topics = args.n_topics 
    topic_names = [f"Topic{i+1}" for i in range(n_topics)]
    print(f"Number of topics: {n_topics}")
    print("Initializing model")
    model = DeepMEL(
        input_len=500, 
        output_dim=n_topics, 
        metric_kwargs={"num_classes": n_topics},
        conv_kwargs={
            "conv_channels": [1024],  
        },
    )
    print("Model summary")
    print(model)
    test_output = model(torch.from_numpy(train_sdata.ohe_seqs[:128]).float()).shape
    print(f"Test output shape: {test_output}")
    models.init_weights(model)
    trainer = train.fit(
        model,
        train_sdata,
        target_keys=topic_names,
        train_key="train_val",
        gpus=1,
        epochs=50,
        batch_size=128,
        num_workers=4,
        log_dir=os.path.join(args.output_dir),
        name="DeepSTRESS",
        version=args.dataset_name,
        model_checkpoint_k = 3,
        return_trainer=True,
    )
    log_dir = os.path.join(args.output_dir, "DeepSTRESS", args.dataset_name)
    print(f"Plotting training summary to {log_dir}")
    pl.training_summary(
        log_dir,
        metric="auroc",
        save=os.path.join(log_dir, "training_summary.png")
    )
    print(f"Copying best model to {log_dir}")
    best_model_path = trainer.checkpoint_callback.best_model_path
    copy_path = os.path.join(log_dir, "best_model.ckpt")
    os.system(f"cp {best_model_path} {copy_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Train a DeepMEL model on binarized topics")
    parser.add_argument("--dataset_name", type=str, required=True)
    parser.add_argument("--data_dir", type=str, required=True)
    parser.add_argument("--output_dir", type=str, required=True)
    parser.add_argument("--n_topics", type=int, default=None)
    args = parser.parse_args()
    main(args)
