import numpy as np
import h5py
import xarray as xr


def prepare_data(train, ss_type=None):

        seq = train['inputs'][:,:,:4]

        if ss_type == 'pu':
            structure = train['inputs'][:,:,4:9]
            paired = np.expand_dims(structure[:,:,0], axis=2)
            unpaired = np.expand_dims(np.sum(structure[:,:,1:], axis=2), axis=2)
            seq = np.concatenate([seq, paired, unpaired], axis=2)

        elif ss_type == 'struct':
            structure = train['inputs'][:,:,4:9]
            paired = np.expand_dims(structure[:,:,0], axis=2)
            HIME = structure[:,:,1:]
            seq = np.concatenate([seq, paired, HIME], axis=2)

        train['inputs']  = seq
        return train


def normalize_data(data, normalization):
    if normalization == 'clip_norm':
        # standard-normal transformation
        significance = 4
        std = np.nanstd(data)
        index = np.where(data > std*significance)[0]
        data[index] = std*significance
        mu = np.nanmean(data)
        sigma = np.nanstd(data)
        data_norm = (data-mu)/sigma
        params = [mu, sigma]

    elif normalization == 'log_norm':
        # log-standard-normal transformation
        MIN = np.nanmin(data)
        data = np.log(data-MIN+1)
        mu = np.nanmean(data)
        sigma = np.nanstd(data)
        data_norm = (data-mu)/sigma
        params = [MIN, mu, sigma]
    return data_norm, params


def load_rnacompete_data(file_path, ss_type='seq', normalization='log_norm', rbp_index=None, dataset_name=None):

    # open dataset
    dataset = h5py.File(file_path, 'r')
    if not dataset_name:  
        # load data from RNAcompete 2013
        X_train = np.array(dataset['X_train']).astype(np.float32)
        Y_train = np.array(dataset['Y_train']).astype(np.float32)
        X_valid = np.array(dataset['X_valid']).astype(np.float32)
        Y_valid = np.array(dataset['Y_valid']).astype(np.float32)
        X_test = np.array(dataset['X_test']).astype(np.float32)
        Y_test = np.array(dataset['Y_test']).astype(np.float32)

        # expand dims of targets
        if rbp_index is not None:
            Y_train = Y_train[:,rbp_index]
            Y_valid = Y_valid[:,rbp_index]
            Y_test = Y_test[:,rbp_index]
    else:
        # necessary for RNAcompete 2009 dataset
        X_train = np.array(dataset['/'+dataset_name+'/X_train']).astype(np.float32)
        Y_train = np.array(dataset['/'+dataset_name+'/Y_train']).astype(np.float32)
        X_valid = np.array(dataset['/'+dataset_name+'/X_valid']).astype(np.float32)
        Y_valid = np.array(dataset['/'+dataset_name+'/Y_valid']).astype(np.float32)
        X_test = np.array(dataset['/'+dataset_name+'/X_test']).astype(np.float32)
        Y_test = np.array(dataset['/'+dataset_name+'/Y_test']).astype(np.float32)

    # expand dims of targets if needed
    if len(Y_train.shape) == 1:
        Y_train = np.expand_dims(Y_train, axis=1)
        Y_valid = np.expand_dims(Y_valid, axis=1)
        Y_test = np.expand_dims(Y_test, axis=1)

    # transpose to make (N, L, A)
    X_train = X_train.transpose([0, 2, 1])
    X_test = X_test.transpose([0, 2, 1])
    X_valid = X_valid.transpose([0, 2, 1])

    # normalize intenensities
    Y_train, params_train = normalize_data(Y_train, normalization)
    Y_valid, params_valid = normalize_data(Y_valid, normalization)
    Y_test, params_test = normalize_data(Y_test, normalization)

    # dictionary for each dataset
    train = {'inputs': X_train, 'targets': Y_train}
    valid = {'inputs': X_valid, 'targets': Y_valid}
    test = {'inputs': X_test, 'targets': Y_test}

    # parse secondary structure profiles
    train = prepare_data(train, ss_type)
    valid = prepare_data(valid, ss_type)
    test = prepare_data(test, ss_type)

    return train, valid, test


def get_experiment_names(file_path):
    """Get the name of a given RNAcompete experiment"""
    dataset = h5py.File(file_path, 'r')
    return [i.decode('UTF-8') for i in np.array(dataset['experiment'])]


def find_experiment_index(data_path, experiment):
    """Find the index for a given RNAcompete experiment"""
    experiments = get_experiment_names(data_path)
    return experiments.index(experiment)


def build_seqdata(dataset):
    """Build a sequence dataset from a dataeset dictionary"""
    ohe_seqs = dataset["inputs"]
    targets = dataset["targets"].squeeze()
    nan_index = np.where(np.isnan(targets))
    print(f"Removing {len(nan_index[0])} sequences with NaN targets")
    ohe_seqs = np.delete(ohe_seqs, nan_index, axis=0)
    targets = np.delete(targets, nan_index, axis=0)    
    sdata = xr.Dataset({
        "ohe_seq": xr.DataArray(ohe_seqs, dims=("_sequence", "_length", "_ohe")),
        "target": xr.DataArray(targets, dims=("_sequence")),
    })
    return sdata