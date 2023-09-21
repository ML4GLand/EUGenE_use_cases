import os
import psutil
import h5py
import numpy as np
from scipy import sparse

# a generator to read examples from h5 file
# create a tf dataset
class generator:
    def __init__(self, file, m):
        self.file = file # h5 file for sequence
        self.m = m # csr matrix, rows as seqs, cols are cells
        self.n_cells = m.shape[1]
        self.ones = np.ones(1344)
        self.rows = np.arange(1344)

    def __call__(self):
        with h5py.File(self.file, 'r') as hf:
            X = hf['X']
            for i in range(X.shape[0]):
                x = X[i]
                x_tf = sparse.coo_matrix((self.ones, (self.rows, x)), 
                                               shape=(1344, 4), 
                                               dtype='int8').toarray()
                y = self.m.indices[self.m.indptr[i]:self.m.indptr[i+1]]
                y_tf = np.zeros(self.n_cells, dtype='int8')
                y_tf[y] = 1
                yield x_tf, y_tf

def print_memory():
    process = psutil.Process(os.getpid())
    print('cpu memory used: %.1fGB.'%(process.memory_info().rss/1e9))