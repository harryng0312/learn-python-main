from concurrent.futures import ProcessPoolExecutor, Executor, ThreadPoolExecutor, wait, Future
from multiprocessing import get_context, Queue, Manager
from multiprocessing.context import BaseContext
import scipy

import numpy as np

def mul_matrix(mat1: np.ndarray, mat2: np.ndarray) -> np.ndarray:
    rs: np.ndarray = np.ndarray(shape=(mat1.shape[0], mat2.shape[1]), dtype=int)
    for i in range(0, len(mat1)):
        for j in range(0, len(mat2[0])):
            s = 0
            for k in range(0, len(mat1[0])):
                s += mat1[i][k]*mat2[k][j]
            rs[i, j] = s
    return rs

def calculate_mul_and_sum(rs: np.ndarray, m1: np.ndarray, m2: np.ndarray, row_no: int, col_no: int) -> None:
    total: int = 0
    for k in range(0, len(m1[0])):
        total += m1[row_no, k] * m2[k, col_no]
    # with ctx.Lock():
    #     queue.put((row_no, col_no, total))
    # return queue
    # rs = ctx.Value("b")
    rs[row_no, col_no] = total
    # print(f"Rs id:{id(rs)}\n{rs}")

def mul_matrix_parallel(mat1: np.ndarray, mat2: np.ndarray, threadCount: int = 4) -> np.ndarray:
    context = get_context('fork') # spawn, fork, forkserver
    with ProcessPoolExecutor(max_workers=threadCount, mp_context=context) as executor:
        rs: np.ndarray = np.ndarray(shape=(mat1.shape[0], mat2.shape[1]), dtype=int)
        # queue = context.Queue(mat1.shape[0] * mat2.shape[1])
        # queue = Queue(mat1.shape[0] * mat2.shape[1])
        # chunkSize = (mat1.shape[0] * mat2.shape[1]) // threadCount
        resultArr: list[Future] = []
        for i in range(0, len(mat1)):
            for j in range(0, len(mat2[0])):
                # calculateMulAndSum(rs, mat1, mat2, i, j)
                # fut = executor.map(calculateMulAndSum, [rs], [mat1], [mat2], [i], [j])
                with context.Lock():
                    fut: Future = executor.submit(calculate_mul_and_sum, rs, mat1, mat2, i, j)
                    resultArr.append(fut)
        wait(fs=resultArr)
    return rs


def print_matrix():
    m1 = np.matrix([
        [2, 3, 4],
        [1, 0, 0],
    ], copy=False, dtype=np.float64)
    m2 = np.matrix([
        [0, 1000],
        [1, 100],
        [0, 10]
    ], copy=False, dtype=np.float64)
    print(f"Ma trận chuyển vị:\n{m1.T}")
    # print(f"Ma trận giả nghịch đảo:\n{m1.I}\n{scipy.linalg.pinv(m1.I).astype(int)}")
    print(f"Ma trận giả nghịch đảo:\n{m1.I} \nnghịch đảo lại:\n{np.linalg.pinv(m1.I).astype(dtype=np.float64, copy=False)}")
    print(f"Ma trận chuyển vị:\n{m1.T} \nliên hợp:\n{m1.H}")
    print(f"Tích Ma trận giả nghịch đảo:\n{m1 * np.matrix(m1.I)}")
    # rs = m1 * m2
    rs = mul_matrix_parallel(mat1=np.array(copy=False, dtype=int, object=m1),
                   mat2=np.array(copy=False, dtype=int, object=m2))
    # rs = np.matrix(rs)
    print(f"Kết quả: \n{rs}")
    print(f"Dạng ma trận: {rs.shape}")
    print(f"Kiểu dữ liệu: {rs.dtype}")
    print(f"Số chiều: {rs.ndim}")
    print(f"Ma trận chuyển vị: {rs.T}")
    print(f"Phần ảo: {rs.imag}")
    print(f"Số lượng phần tử: {rs.size}")
    print(f"Kích thước mỗi phần tử (bytes): {rs.itemsize}")


if __name__ == "__main__":
    print_matrix()
    pass
