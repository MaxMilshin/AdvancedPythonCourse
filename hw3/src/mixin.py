import numpy as np

def get_num_width(data):
    arr_str = data.astype(str)
    str_lengths = np.vectorize(len)(arr_str.flatten())
    max_length = np.max(str_lengths)

    return max_length


class NumpyArithmeticMixin:
    def __add__(self, other):
        return self.__class__(self.data + other.data)

    def __sub__(self, other):
        return self.__class__(self.data - other.data)

    def __mul__(self, other):
        return self.__class__(self.data * other.data)

    def __truediv__(self, other):
        return self.__class__(self.data / other.data)
        
class NumpyRepresentationMixin:
    def __str__(self):
        num_width = get_num_width(self.data)
        formatted_data = '\n'.join([''.join([f"{elem:<{num_width}} " for elem in row]) for row in self.data])
        return formatted_data

class NumpyIOMixin:
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))



class NumpyGetSetMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = np.array(new_data)


class NumpyHashMixin:
    def __hash__(self):
        return int(np.sum(self.data))