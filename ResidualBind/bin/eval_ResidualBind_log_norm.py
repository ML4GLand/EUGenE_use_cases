import os
import sys
import torch
import numpy as np
import pandas as pd
import seqdata as sd
from eugene import models
from eugene.models import zoo
from eugene import plot as pl
import matplotlib.pyplot as plt

sys.path.append("/cellar/users/aklie/projects/ML4GLand/use_cases/ResidualBind/bin")
from plot import training_summary, scatter


# Model log directory
date = "2023_12_16"
rbp = "RNCMPT00100"
normalization = "log_norm"
log_dir = f"/cellar/users/aklie/projects/ML4GLand/use_cases/ResidualBind/models/{date}/ResidualBind/{normalization}/{rbp}"

# Check if log directory exists
if not os.path.isdir(log_dir):
    print(f"Log directory {log_dir} does not exist")

# Check if model exists
best_path = os.path.join(log_dir, "best_model.ckpt")
if not os.path.isfile(best_path):
    print(f"Model {best_path} does not exist")

# Get device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device: {}".format(device))


training_summary(log_dir, metrics=["pearson"], logger="csv", save=os.path.join(log_dir, "training_summary.png"))

# Load the dataset
sdata = sd.open_zarr("/cellar/users/aklie/data/ml4gland/pubs/koo21_gia/log_norm/rnacompete2013_test.zarr")
sdata.load()

# Get target vector
target_ind = np.where(sdata["rbp_id"].values == rbp)[0]
targets = sdata["targets"][:, target_ind].values.squeeze()

# Instantiate an architecture
arch = zoo.ResidualBind(
    input_len=41,
    output_dim=1
)

module = models.SequenceModule.load_from_checkpoint(
    os.path.join(log_dir, "best_model.ckpt"),
    arch=arch,
)

module.to(device).eval();


preds = module.predict(
    sdata["inputs"].values.transpose(0, 2, 1),
    batch_size=128
).cpu().numpy().squeeze()


# Make output directory if it doesn't exist
outdir = os.path.join(log_dir, "performance")
if not os.path.exists(outdir):
    os.makedirs(outdir)

df = pd.DataFrame({
    "target": targets,
    "pred": preds
})
df.to_csv(os.path.join(outdir, "test_predictions.csv"), index=False)


# Plot a nice blue color
scatter(
    x=targets,
    y=preds,
    c="#4682B4",
    alpha=0.8,
    xlabel="Experimental binding scores",
    ylabel="Predicted binding scores",
    density=False,
    rasterized=True,
    s=5,
    save=os.path.join(outdir, "test_scatter.png"),
)
