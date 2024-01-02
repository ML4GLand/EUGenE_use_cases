import os
import torch
import numpy as np
import pandas as pd 
import seqdata as sd
import xarray as xr
from eugene import models
from eugene.models import zoo
from eugene import train


# Model log directory
log_dir = "/cellar/users/aklie/projects/ML4GLand/use_cases/ResidualBind/models/2024_01_02/ResidualBind/log_norm"

# Load the dataset
sdata_train = sd.open_zarr("/cellar/users/aklie/data/ml4gland/pubs/koo21_gia/log_norm/rnacompete2013_train.zarr")
sdata_train["train_val"] = xr.DataArray([True] * sdata_train.dims["_sequence"], dims=["_sequence"])
sdata_valid = sd.open_zarr("/cellar/users/aklie/data/ml4gland/pubs/koo21_gia/log_norm/rnacompete2013_valid.zarr")
sdata_valid["train_val"] = xr.DataArray([False] * sdata_valid.dims["_sequence"], dims=["_sequence"])
sdata = xr.concat([sdata_train, sdata_valid], dim="_sequence", data_vars="minimal")
sdata["ohe_seq"] = sdata["inputs"]
sdata.load()

# Loop through and train each model
for index in range(sdata.dims["_target"]):
    sdata["target"] = sdata["targets"][:, index]
    rbp_id = sdata["rbp_id"].values[index]
    print("Training", rbp_id)

    # Instantiate an architecture
    arch = zoo.ResidualBind(
        input_len=41,
        output_dim=1
    )

    # Initialize the weights
    models.init_weights(arch)

    # Instantiate a sequence module
    module = models.SequenceModule(
        arch=arch,
        task="regression",
        loss_fxn="mse",
        optimizer_lr=0.001,
        scheduler="reduce_lr_on_plateau",
        scheduler_monitor="val_pearson_epoch",
        metric="pearson",
        seed=1234,
    )

    # Grab the training data for this RBP
    sdata_training = sdata.sel(_sequence=sdata["target"].notnull()).copy()

    # Train the model
    trainer = train.fit_sequence_module(
        model=module,
        sdata=sdata_training,
        seq_var="ohe_seq",
        target_vars=["target"],
        train_var="train_val",
        in_memory=True,
        transforms={"ohe_seq": lambda x: torch.tensor(x.transpose(0, 2, 1), dtype=torch.float32)},
        epochs=100,
        batch_size=100,
        early_stopping_patience=20,
        early_stopping_monitor="val_pearson_epoch",
        early_stopping_mode="max",
        model_checkpoint_monitor="val_pearson_epoch",
        model_checkpoint_mode="max",
        model_checkpoint_k=5,
        logger="csv",
        log_dir=os.path.join(log_dir, rbp_id),
        name="",
        version="",
        seed=1234,
        return_trainer=True
    )

    # Move best model to log directory
    print("Copying best model to log directory")
    best_model_path = trainer.checkpoint_callback.best_model_path
    copy_path = os.path.join(log_dir, rbp_id, "best_model.ckpt")
    os.system(f"cp {best_model_path} {copy_path}")

    # Clean up
    del module
    del trainer
    del sdata_training
    del arch
    