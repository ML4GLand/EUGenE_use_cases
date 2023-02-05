import os
import numpy as np
import pandas as pd
import seqdata as sd


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
        seq_tbl_wt = seq_tbl_filt[seq_tbl_filt["Element_id"].str.contains("Genomic")]
        exp_summary = pd.read_excel(paths[0], sheet_name=7)
        merged = pd.merge(seq_tbl_wt, exp_summary, on="Element_id", how="left")
        bc_grouped = merged.groupby("Element_id").agg("mean")
        CRE_norm_expression_WT_all = bc_grouped[["Rep1_Element_normalized", "Rep2_Element_normalized","Rep3_Element_normalized"]].mean(axis=1)
        bc_grouped["CRE_norm_expression_WT_all"] = CRE_norm_expression_WT_all
        bc_grouped["Sequence"] = merged.groupby("Element_id").agg({"Sequence": lambda x: x.iloc[0]})["Sequence"]
        merged_tbl = bc_grouped.reset_index()[["Sequence", "Element_id", "CRE_norm_expression_WT_all"]]
        merged_tbl["Element_id"] = merged_tbl["Element_id"].str.replace("_Genomic", "")
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