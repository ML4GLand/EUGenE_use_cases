import os
import numpy as np
import pandas as pd
import seqdata as sd
import matplotlib.pyplot as plt

def king20(
    dataset = "SYN", 
    return_sdata=True, 
    download_mouse=False,
    dataset_dir="./",
    **kwargs: dict
):
    urls_list = [
        "https://elifesciences.org/download/aHR0cHM6Ly9jZG4uZWxpZmVzY2llbmNlcy5vcmcvYXJ0aWNsZXMvNDEyNzkvZWxpZmUtNDEyNzktc3VwcDEtdjIueGxzeA--/elife-41279-supp1-v2.xlsx?_hash=nX7V5q5UXEGDbCoqhF23ru1RNUI14CBnHk27Cxlpgr4%3D",
        "https://elifesciences.org/download/aHR0cHM6Ly9jZG4uZWxpZmVzY2llbmNlcy5vcmcvYXJ0aWNsZXMvNDEyNzkvZWxpZmUtNDEyNzktc3VwcDItdjIueGxzeA--/elife-41279-supp2-v2.xlsx?_hash=V%2FARKgB5fn%2FUe1zKqVdBFHuq7na8rU%2BuFcWIQQwnAPM%3D",
        "https://elifesciences.org/download/aHR0cHM6Ly9jZG4uZWxpZmVzY2llbmNlcy5vcmcvYXJ0aWNsZXMvNDEyNzkvZWxpZmUtNDEyNzktc3VwcDQtdjIuZmFzdGE-/elife-41279-supp4-v2.fasta?_hash=HEFd7o2rJQ5Be4CHpN3L9SnE0zbrhhJah%2Fgao0poWG0%3D",
        "http://hgdownload.cse.ucsc.edu/goldenpath/mm10/bigZips/mm10.fa.gz"
    ]
    paths = [
        os.path.join(dataset_dir, "king20", "design.xlsx"),
        os.path.join(dataset_dir, "king20", "models.xlsx"),
        os.path.join(dataset_dir, "king20", "GEN.fasta"),
        os.path.join(dataset_dir, "king20", "mm10.fa.gz")
    ]
    
    # Design excel
    if not os.path.exists(paths[0]):
        print(f"Downloading king20 design spreadsheet to {paths[0]}")
        os.system("wget -q -O {0} {1}".format(paths[0], urls_list[0]))
        print(f"Finished downloading king20 design spreadsheet to {paths[0]}")
    else:
        print(f"Design spreadsheet already exists at {paths[0]}")
    
    # Model excel
    if not os.path.exists(paths[1]):
        print(f"Downloading king20 model spreadsheet to {paths[1]}")
        os.system("wget -q -O {0} {1}".format(paths[1], urls_list[1]))
        print(f"Finished downloading king20 spreadsheet to {paths[1]}")
    else:
        print(f"Model spreadsheet already exists at {paths[1]}")
    
    # Load in the synthetic dataset
    if dataset == "SYN":
        seq_tbl = pd.read_excel(paths[0], sheet_name=1)
        seq_tbl_filt = seq_tbl[~seq_tbl["Sequence"].duplicated()]
        model_tbl = pd.read_excel(paths[1], sheet_name=4)
        merged_tbl = pd.merge(seq_tbl_filt, model_tbl, on="Element_id", how="outer")
    
    # Load in the genomic dataset
    elif dataset == "GEN":
        seq_tbl = pd.read_excel(paths[0], sheet_name=6)
        seq_tbl_filt = seq_tbl[~seq_tbl["Element_id"].duplicated()]
        seq_tbl_wt = seq_tbl_filt[(seq_tbl_filt["Element_id"].str.contains("Genomic")) | (seq_tbl_filt["Element_id"].str.contains("All_Mutated"))]
        exp_summary = pd.read_excel(paths[0], sheet_name=7)
        merged = pd.merge(seq_tbl_wt, exp_summary, on="Element_id", how="left")
        bc_grouped = merged.groupby("Element_id").agg("mean")
        CRE_norm_expression_WT_all = bc_grouped[["Rep1_Element_normalized", "Rep2_Element_normalized","Rep3_Element_normalized"]].mean(axis=1)
        bc_grouped["CRE_norm_expression_WT_all"] = CRE_norm_expression_WT_all
        bc_grouped["Sequence"] = merged.groupby("Element_id").agg({"Sequence": lambda x: x.iloc[0]})["Sequence"]
        merged_tbl = bc_grouped.reset_index()[["Sequence", "Element_id", "CRE_norm_expression_WT_all"]]
        merged_tbl["range"] = merged_tbl["Element_id"].str.replace("_Genomic", "").str.replace("_All_Mutated", "")
        merged_tbl["Barcode"] = "NA"
        
        if not os.path.exists(paths[2]):
            print(f"Downloading king20 gkmsvm fasta to {paths[2]}")
            os.system("wget -q -O {0} {1}".format(paths[2], urls_list[2]))
            print(f"Finished downloading king20 gkmsvm fasta to {paths[2]}")
        else:
            print(f"Gkmsvm fasta already exists at {paths[2]}")
        
        if download_mouse:
            if not os.path.exists(paths[3]):
                print(f"Downloading mm10 fasta to {paths[2]}")
                os.system("wget -q -O {0} {1}".format(paths[3], urls_list[3]))
                print(f"Finished downloading mm10 fasta to {paths[0]}")
            else:
                print(f"mm10 fasta already exists at {paths[3]}")
    else:
        raise ValueError("dataset must be either 'SYN' or 'GEN'.")
    if return_sdata:
        sdata = sd.SeqData(
            seqs=merged_tbl["Sequence"].values,
            names=merged_tbl["Element_id"].values,
            seqs_annot=merged_tbl.drop(["Barcode", "Sequence"], axis=1).set_index("Element_id")
        )
        return sdata
    else:
        return paths

def seq_len(seq, ohe=False):
    if ohe:
        return seq.shape[1]
    else:
        return len(seq)

def seq_lens(seqs, ohe=False):
    if ohe:
        return np.array([seq.shape[1] for seq in seqs])
    else:
        return np.array([len(seq) for seq in seqs])

def seq_len_sdata(sdata, copy=False):
    if sdata.seqs is not None:
        sdata["seq_len"] = seq_lens(sdata.seqs, ohe=False)
    elif sdata.ohe_seqs is not None:
        sdata["seq_len"] = seq_lens(sdata.ohe_seqs, ohe=True)
    else:
        raise ValueError("No sequences found in sdata")
        
        
from sklearn.ensemble import RandomForestRegressor
from eugene._settings import settings
import threading

def fit(
    model,
    sdata,
    target_keys,
    train_key="train_val",
    features_cols = None,
    seqsm_key = None,
    threads=None,
    log_dir=None,
    name=None,
    version="",
    seed=None,
    verbosity=1
):
    # Set-up the run
    threads = threads if threads is not None else threading.active_count()
    log_dir = log_dir if log_dir is not None else settings.logging_dir
    model_name = model.__class__.__name__
    name = name if name is not None else model_name
    np.random.seed(seed) if seed is not None else np.random.seed(settings.seed)
    model.verbose = verbosity

    # Remove seqs with NaN targets
    targs = sdata.seqs_annot[target_keys].values  
    if len(targs.shape) == 1:
        nan_mask = np.isnan(targs)
    else:
        nan_mask = np.any(np.isnan(targs), axis=1)
    print(f"Dropping {nan_mask.sum()} sequences with NaN targets.")
    sdata = sdata[~nan_mask]
    targs = targs[~nan_mask]
    print(np.isnan(targs).sum())
    
    # Get train and val indeces
    train_idx = np.where(sdata.seqs_annot[train_key] == True)[0]
    val_idx = np.where(sdata.seqs_annot[train_key] == False)[0]
    
    # Get train and val targets
    train_Y = targs[train_idx].squeeze()
    val_Y = targs[val_idx].squeeze()
    
    # Get train adn val features
    if feature_cols is not None:
        sdata.seqsm[f"{model_name}_features" if seqsm_key is None else seqsm_key] = sdata.seqs_annot[feature_cols].values
    else:
        assert seqsm_key is not None
    features = sdata.seqsm[seqsm_key]
    train_X = features[train_idx]
    val_X = features[val_idx]
    model.fit(train_X, train_Y)
    
    if not os.path.exists(os.path.join(log_dir, name, version)):
        os.makedirs(os.path.join(log_dir, name, version))
        
    pd.DataFrame(pd.Series(model.get_params())).T.to_csv(os.path.join(log_dir, name, version, "hyperparams.tsv"), index=False, sep="\t")
    
def predictions(
    model,
    sdata,
    target_keys,
    features_cols = None,
    seqsm_key = None,
    threads=None,
    store_only=False,
    out_dir=None,
    name=None,
    version="",
    file_label="",
    prefix="",
    suffix="",
    copy=False
):
    threads = threads if threads is not None else threading.active_count()
    target_keys = [target_keys] if type(target_keys) == str else target_keys
    out_dir = out_dir if out_dir is not None else settings.output_dir
    model_name = model.__class__.__name__
    name = name if name is not None else model_name
    out_dir = os.path.join(out_dir, name, version)
    
    if feature_cols is not None:
        sdata.seqsm[f"{model_name}_features"] = sdata.seqs_annot[feature_cols].values
    else:
        assert seqsm_key is not None
    features = sdata.seqsm[seqsm_key]
    ps = model.predict(features)
    ts = sdata.seqs_annot[target_keys].values.squeeze()
    inds = sdata.seqs_annot.index
    new_cols = [f"{prefix}{lab}_predictions{suffix}" for lab in target_keys]
    sdata.seqs_annot[new_cols] = np.expand_dims(model.predict(features), axis=1)
    if not store_only:
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        df = pd.DataFrame(index=inds, data={"targets": ts, "predictions": ps})
        df.to_csv(os.path.join(out_dir, f"{file_label}_predictions.tsv"), sep="\t")
    return sdata if copy else None

def _impurity_decrease(
    model, 
    feature_names,
    plot=True,
    prefix="",
    suffix="",
    copy=False
):
    importances = model.feature_importances_
    std = np.std([tree.feature_importances_ for tree in model.estimators_], axis=0)
    descending_ord = np.argsort(importances)
    importances = importances[descending_ord]
    std = std[descending_ord]
    names = feature_names[descending_ord]
    forest_importances = pd.DataFrame(data={"importances": importances, "std": std}, index=names)
    if plot:
        fig, ax = plt.subplots()
        forest_importances["importances"].plot.barh(yerr=std, ax=ax)
        ax.set_title("Feature importances using MDI")
        ax.set_ylabel("Mean decrease in impurity")
        plt.show()
    return forest_importances

def feature_attribution_sdata(
    sdata,
    model,
    method = "mean_impurity",
    uns_key=None,
    feature_names=None,
    copy=False
):
    if method == "mean_impurity":
        uns_key if uns_key is not None else "mean_impurity_imps"
        forest_importances = _impurity_decrease(model, feature_names, plot=False)
        sdata.uns[f"{prefix}uns_key{suffix}"] = forest_importances
    return sdata if copy else None