import numpy as np
import datetime as dt
import io

FILE_MAT_NAME_1 = "data/matrix/mat1"
FILE_MAT_NAME_2 = "data/matrix/mat2"
FILETXT_MAT_NAME_1 = "data/matrix/mat1.txt"
FILETXT_MAT_NAME_2 = "data/matrix/mat2.txt"
MAT_SIZE = 2048


def generate_square_maxtrix(n: int) -> np.matrix:
    m1 = np.random.randint(low=-128, high=127, size=(n, n))
    return m1


def save_matrix(filepath: str, mat: np.matrix) -> None:
    # np.savetxt(fname=filepath, X=mat, fmt="%d")
    file: io.FileIO = None
    try:
        file = open(file=filepath, mode="bw")
        np.save(file=file, arr=np.array(object=mat, dtype=int))
    finally:
        if file is not None:
            file.close()


def load_matrix(filepath: str) -> np.matrix:
    result: np.matrix = None
    file: io.FileIO = None
    try:
        file = open(file=filepath, mode="br")
        result = np.matrix(data=np.load(file=filepath, fix_imports=True), dtype=int)
    finally:
        if file is not None:
            file.close()
    return result


def savetxt_matrix(filepath: str, mat: np.matrix) -> None:
    np.savetxt(fname=filepath, X=mat, fmt="%d")


def loadtxt_matrix(filepath: str) -> np.matrix:
    return np.matrix(data=np.loadtxt(fname=filepath, dtype=int), dtype=int)


def mulMatrix(mat1: np.ndarray, mat2: np.ndarray) -> np.ndarray:
    rs: np.ndarray = np.ndarray(shape=(mat1.shape[0], mat2.shape[1]), dtype=int)
    for i in range(0, len(mat1)):
        for j in range(0, len(mat2[0])):
            s = 0
            for k in range(0, len(mat1[0])):
                s += mat1[i][k]*mat2[k][j]
            rs[i, j] = s
    return rs


if __name__ == "__main__":
    # mat1 = generate_square_maxtrix(MAT_SIZE)
    # save_matrix(filepath=FILE_MAT_NAME_1, mat=mat1)
    # savetxt_matrix(filepath=FILETXT_MAT_NAME_1, mat=mat1)
    #
    # mat2 = generate_square_maxtrix(MAT_SIZE)
    # save_matrix(filepath=FILE_MAT_NAME_2, mat=mat2)
    # savetxt_matrix(filepath=FILETXT_MAT_NAME_2, mat=mat2)

    startLoadTime = dt.datetime = dt.datetime.now();
    # mat1 = load_matrix(FILE_MAT_NAME_1)
    # mat2 = load_matrix(FILE_MAT_NAME_2)
    mat1 = loadtxt_matrix(FILETXT_MAT_NAME_1)
    mat2 = loadtxt_matrix(FILETXT_MAT_NAME_2)
    endLoadTime = dt.datetime = dt.datetime.now();
    print(f"Load done in {endLoadTime - startLoadTime}...")
    print(f"mat1 {type(mat1)}:\n{mat1}\nmat2 {type(mat2)}:\n{mat2}")

    mat1Arr: np.ndarray = np.array(copy=False, dtype=int, object=mat1)
    mat2Arr: np.ndarray = np.array(copy=False, dtype=int, object=mat2)
    # startTime: dt.datetime = dt.datetime.now();
    # matRs = mulMatrix(mat1Arr, mat2Arr)
    # endTime: dt.datetime = dt.datetime.now();
    # print(f"{str(matRs)}")
    # print(f"python time:{(endTime - startTime)}")

    startTime: dt.datetime = dt.datetime.now();
    # matRs = mat1 * mat2
    matRs = mulMatrix(mat1Arr, mat2Arr)
    endTime: dt.datetime = dt.datetime.now();

    print(f"Result by CPU:\n{str(matRs)}")
    print(f"Run on CPU time:{(endTime - startTime)}")
    pass
