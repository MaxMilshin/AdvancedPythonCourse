import numpy as np

from matrix import Matrix

def main():
    np.random.seed(0)
    matrix1 = np.random.randint(0, 10, (10, 10))
    matrix2 = np.random.randint(0, 10, (10, 10))

    matrix1_obj = Matrix(matrix1)
    matrix2_obj = Matrix(matrix2)

    artifact_dir_path = '../artifacts/3.1/'

    try:
        result_add = matrix1_obj + matrix2_obj
        result_add.save_to_file(artifact_dir_path + "matrix+.txt")
    except ValueError as e:
        print("Error occurred during addition:", e)

    try:
        result_mul = matrix1_obj * matrix2_obj
        result_mul.save_to_file(artifact_dir_path + "matrix*.txt")
    except ValueError as e:
        print("Error occurred during element-wise multiplication:", e)

    try:
        result_matmul = matrix1_obj @ matrix2_obj
        result_matmul.save_to_file(artifact_dir_path + "matrix@.txt")
    except ValueError as e:
        print("Error occurred during matrix multiplication:", e)

if __name__ == "__main__":
    main()
