import numpy as np
from sklearn.metrics import average_precision_score, roc_auc_score
from sklearn.utils import class_weight, shuffle


def evaluate_model(y_test, pred, verbose=True): 
    auroc = calculate_auroc(y_test, pred) 
    aupr = calculate_aupr(y_test, pred) 
    if verbose:
        print("Test AUROC: %.4f +/- %.4f"%(np.nanmean(auroc), np.nanstd(auroc)))
        print("Test AUPR : %.4f +/- %.4f"%(np.nanmean(aupr), np.nanstd(aupr)))
    return auroc, aupr

def calculate_auroc(y_true, y_score):
    vals = []
    for class_index in range(y_true.shape[-1]):
        vals.append( roc_auc_score(y_true[:,class_index], y_score[:,class_index]) )    
    return np.array(vals)

def calculate_aupr(y_true, y_score):
    vals = []
    for class_index in range(y_true.shape[-1]):
        vals.append( average_precision_score(y_true[:,class_index], y_score[:,class_index]) )    
    return np.array(vals)

def shuffle_label(label):
    for i in range(len(label.T)):
        label.T[i] = shuffle(label.T[i])
    return label

def calculate_roc_pr(score, label):
    output = np.zeros((len(label.T), 2))
    for i in range(len(label.T)):
        roc_ = roc_auc_score(label.T[i], score.T[i])
        pr_ = average_precision_score(label.T[i], score.T[i])
        output[i] = [roc_, pr_]
    return output