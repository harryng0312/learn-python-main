import numpy as np
import cupy as cp
import cupyx as cpx
import datetime as dt
import io

FILE_MAT_NAME_1 = "data/matrix/mat1"
FILE_MAT_NAME_2 = "data/matrix/mat2"
FILETXT_MAT_NAME_1 = "data/matrix/mat1.txt"
FILETXT_MAT_NAME_2 = "data/matrix/mat2.txt"
MAT_SIZE = 1440 #6_144

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


def mulMatrix(mat1: cp.ndarray, mat2: cp.ndarray) -> cp.ndarray:
    rs: cp.ndarray = cp.matmul(mat1, mat2)
    return rs


def computeByGPU(deviceIndex:int = 0) -> None:
    # mat1 = generate_square_maxtrix(MAT_SIZE)
    # save_matrix(filepath=FILE_MAT_NAME_1, mat=mat1)
    # savetxt_matrix(filepath=FILETXT_MAT_NAME_1, mat=mat1)

    # mat2 = generate_square_maxtrix(MAT_SIZE)
    # save_matrix(filepath=FILE_MAT_NAME_2, mat=mat2)
    # savetxt_matrix(filepath=FILETXT_MAT_NAME_2, mat=mat2)

    startLoadTime = dt.datetime = dt.datetime.now()
    # mat1 = load_matrix(FILE_MAT_NAME_1)
    # mat2 = load_matrix(FILE_MAT_NAME_2)
    mat1 = loadtxt_matrix(FILETXT_MAT_NAME_1)
    mat2 = loadtxt_matrix(FILETXT_MAT_NAME_2)
    endLoadTime = dt.datetime = dt.datetime.now()
    print(f"Load done in {endLoadTime - startLoadTime}...")
    print(f"mat1 {type(mat1)}:\n{mat1}\nmat2 {type(mat2)}:\n{mat2}")
    print(f"runtime info: \n{cpx.get_runtime_info()}")
    # mat1cpArr = cp.array(obj=mat1Arr, dtype=int)
    # mat2cpArr = cp.array(obj=mat2Arr, dtype=int)
    
    # startTime: dt.datetime = dt.datetime.now();
    # matRs = mat1 * mat2
    # endTime: dt.datetime = dt.datetime.now();
    # print(f"Result by CPU:\n{str(matRs)}")
    # print(f"Run on CPU time:{(endTime - startTime)}")
    mat1Arr: np.ndarray = np.array(copy=False, dtype=int, object=mat1)
    mat2Arr: np.ndarray = np.array(copy=False, dtype=int, object=mat2)
    startTime: dt.datetime = dt.datetime.now()
    # matRs = mat1 * mat2
    N = 100
    CN = 20
    mempool = cp.get_default_memory_pool()
    pinned_mempool = cp.get_default_pinned_memory_pool()
    # mempool.set_limit(size = 2 * 1024**3)
    for i in range(N):
        if i > 0 and i % CN == 0:
            print(f"Round {i}: {mempool.used_bytes()} + {mempool.free_bytes()} = {mempool.total_bytes()} | {pinned_mempool.n_free_blocks()} | {pinned_mempool.n_free_blocks()}")
            start_clean_time: dt.datetime = dt.datetime.now()
            mempool.free_all_blocks()
            pinned_mempool.free_all_blocks()
            end_clean_time: dt.datetime = dt.datetime.now()
            print(f"Free in: {(end_clean_time - start_clean_time).total_seconds()}")
            pass
        # mat1cpArr = cp.asarray(a=mat1Arr, dtype=float)
        # mat2cpArr = cp.asarray(a=mat2Arr, dtype=float)
        mat1cpArr = cp.asarray(a=mat1, dtype=float)
        mat2cpArr = cp.asarray(a=mat2, dtype=float)
        matRs1 = mulMatrix(mat1cpArr, mat2cpArr)
        # del mat1Arr, mat2Arr, mat1cpArr, mat2cpArr
        del mat1cpArr, mat2cpArr        

    endTime: dt.datetime = dt.datetime.now()
    matRs = np.matrix(data=cp.asnumpy(a=matRs1), copy=False)

    print(f"Result by CUDA GPU:\n{str(matRs)}")
    print(f"Run on CUDA GPU time:{(endTime - startTime).total_seconds()/N}")
    return None


def showDevice(deviceInd: int = 0) -> None:
    with cp.cuda.Device(deviceInd) as device:
        mempool = cp.get_default_memory_pool()
        pinned_mempool = cp.get_default_pinned_memory_pool()
        mempool.set_limit(1024 * 1024**2)
        # cupy.get_default_memory_pool().get_limit()
        print(f"Device{deviceInd} info: {cpx.get_runtime_info()}")
        print(f"Device{deviceInd} attributes: {device.attributes}")
        print(f"Device{deviceInd} mempool limit: {mempool.get_limit()}")
    return None


if __name__ == "__main__":
    # showDevice()
    computeByGPU()
    pass
