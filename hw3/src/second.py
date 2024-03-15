import numpy as np

from mixin import NumpyArithmeticMixin, NumpyIOMixin, NumpyRepresentationMixin, NumpyGetSetMixin

class NumpyClass(NumpyArithmeticMixin, NumpyIOMixin, NumpyRepresentationMixin, NumpyGetSetMixin):
    def __init__(self, data):
        self.data = data

def main():
    np.random.seed(0)
    data1 = np.random.randint(0, 10, (3, 3))
    data2 = np.random.randint(0, 10, (3, 3))

    obj1 = NumpyClass(data1)
    obj2 = NumpyClass(data2)

    print("Object 1:")
    print(obj1)
    print()

    print("Object 2:")
    print(obj2)
    print()

    result_add = obj1 + obj2
    print("Addition Result:")
    print(result_add)
    print()

    result_sub = obj1 - obj2
    print("Subtraction Result:")
    print(result_sub)
    print()

    result_mul = obj1 * obj2
    print("Multiplication Result:")
    print(result_mul)
    print()

    result_div = obj1 / obj2
    print("Division Result:")
    print(result_div)
    print()

    result_div.save_to_file("../artifacts/3.2/numpy_object.txt")


if __name__ == "__main__":
    main()
