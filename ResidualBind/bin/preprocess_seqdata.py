# Imports
import os
import sys
import numpy as np
import h5py
import xarray as xr

sys.path.append("/cellar/users/aklie/projects/ML4GLand/use_cases/ResidualBind/bin")
from dataload import load_rnacompete_data, get_experiment_names, find_experiment_index


# Paths
input_path = "/cellar/users/aklie/data/ml4gland/pubs/koo21_gia/rnacompete2013.h5"
outdir_path = "/cellar/users/aklie/data/ml4gland/pubs/koo21_gia/"

exp_accession = get_experiment_names(input_path)
exp_index = [find_experiment_index(input_path, i) for i in exp_accession]

for norm in ["log_norm", "clip_norm"]:
    print("Making directory", os.path.join(outdir_path, norm))
    if not os.path.exists(os.path.join(outdir_path, norm)):
        os.makedirs(os.path.join(outdir_path, norm))

    print("Processing", norm)
    train, valid, test = load_rnacompete_data(
        file_path=input_path,
        ss_type="seq",
        normalization=norm,
        rbp_index=None,
        dataset_name=None
    )

    for dset_name, dset in zip(["train", "valid", "test"], [train, valid, test]):
        print("Saving", dset_name)
        ohe_seq = xr.DataArray(dset["inputs"], dims=("_sequence", "_length", "_ohe"))
        targets = xr.DataArray(dset["targets"], dims=("_sequence", "_target"))
        rbp_id = xr.DataArray(exp_accession, dims=("_target"))
        rbp_index = xr.DataArray(exp_index, dims=("_target"))
        sdata = xr.Dataset({"inputs": ohe_seq, "targets": targets, "rbp_id": rbp_id, "rbp_index": rbp_index})
        sdata.to_zarr(os.path.join(outdir_path, norm, f"rnacompete2013_{dset_name}.zarr"), mode="w")
