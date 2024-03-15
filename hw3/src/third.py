import numpy as np

from matrix import Matrix

def main():
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[5, 6], [7, 8]])
    C = Matrix([[1, 2], [3, 4]])
    D = Matrix([[8, 7], [6, 5]])

    artifact_dir_path = '../artifacts/3.3/'

    A.save_to_file(artifact_dir_path + "A.txt")
    B.save_to_file(artifact_dir_path + "B.txt")
    C.save_to_file(artifact_dir_path + "C.txt")
    D.save_to_file(artifact_dir_path + "D.txt")

    AB = A @ B
    CD = C @ D

    AB.save_to_file(artifact_dir_path + "AB.txt")
    CD.save_to_file(artifact_dir_path + "CD.txt")

    hashes_filename = 'hashes_file'

    with open(artifact_dir_path + hashes_filename, 'w') as f:
        f.write(f'hash(A)={hash(A)}\n')
        f.write(f'hash(C)={hash(C)}\n')
        f.write(f'hash(AB)={hash(AB)}\n')
        f.write(f'hash(CD)={hash(CD)}\n')
        
if __name__ == "__main__":
    main()
