import numpy as np

from mixin import NumpyHashMixin

class Matrix(NumpyHashMixin):
    def __init__(self, data):
        self.data = np.array(data)
    
    def __add__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Matrix dimensions do not match for addition.")
        return Matrix(self.data + other.data)
    
    def __mul__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Matrix dimensions do not match for element-wise multiplication.")
        return Matrix(self.data * other.data)
    
    def __matmul__(self, other):
        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError("Matrix dimensions do not match for matrix multiplication.")
        return Matrix(np.matmul(self.data, other.data))
    
    def save_to_file(self, filename):
        max_value = np.max(self.data)
        min_value = np.min(self.data)
        num_width = max(len(str(max_value)), len(str(min_value)))
        np.savetxt(filename, self.data, fmt=f'%{num_width}d', delimiter=' ')
