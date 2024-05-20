import numpy as np
import pyopencl as cl
import datetime as dt
import io

KERNEL_PATH = r"D:/training/python/learn-python/module/learn_math/kernels/opencl/matrixmultiplication.cl"
FILE_MAT_NAME_1 = "data/matrix/mat1"
FILE_MAT_NAME_2 = "data/matrix/mat2"
FILETXT_MAT_NAME_1 = "data/matrix/mat1.txt"
FILETXT_MAT_NAME_2 = "data/matrix/mat2.txt"
MAT_SIZE = 2048

LOCAL_WORKGROUP_SIZE = 32
LOCAL_WORKGROUP: tuple
CONTEXT: cl.Context = None
PROGRAM: cl.Program = None
CMD_QUEUE: cl.CommandQueue = None


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


def initCl() -> None:
    # sets the local work group x,y
    global LOCAL_WORKGROUP
    global CONTEXT
    global CMD_QUEUE
    global PROGRAM
    # block, thread
    LOCAL_WORKGROUP = (LOCAL_WORKGROUP_SIZE, LOCAL_WORKGROUP_SIZE)
    # mf = cl.mem_flags
    # gets platform list and takes first
    platforms = cl.get_platforms()
    platform = platforms[0]
    # gets device list and takes first in my case intel xeon
    devices = platform.get_devices()
    device = devices[0]
    # creates context and command queue
    CONTEXT = cl.Context([device])
    cpq = cl.command_queue_properties
    CMD_QUEUE = cl.CommandQueue(CONTEXT, device, properties=cpq.PROFILING_ENABLE)
    # loads and builts the kernel
    PROGRAM = cl.Program(CONTEXT, open(KERNEL_PATH).read()).build()


def mulMatrix(mat1: np.ndarray, mat2: np.ndarray, mat1Buff: cl.Buffer, mat2Buff: cl.Buffer,
              resultBuff: cl.Buffer, mat1WBuff: cl.Buffer, mat2WBuff: cl.Buffer) -> None:
    # rs: np.ndarray = mat1 * mat2
    PROGRAM.matrixMulInt(CMD_QUEUE, (mat1.shape[0], mat2.shape[1]), LOCAL_WORKGROUP, mat1Buff, mat2Buff, resultBuff, mat1WBuff, mat2WBuff)
    CMD_QUEUE.finish()


if __name__ == "__main__":
    # mat1 = generate_square_maxtrix(MAT_SIZE)
    # save_matrix(filepath=FILE_MAT_NAME_1, mat=mat1)
    # savetxt_matrix(filepath=FILETXT_MAT_NAME_1, mat=mat1)

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

    initCl()
    mat1Arr: np.ndarray = np.array(copy=False, dtype=int, object=mat1)
    mat2Arr: np.ndarray = np.array(copy=False, dtype=int, object=mat2)
    mat3Arr: np.ndarray = np.random.rand(MAT_SIZE, MAT_SIZE).astype(dtype=int)
    # setes memory buffers
    mat1Buff = cl.Buffer(context=CONTEXT, flags=(cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR), hostbuf=mat1Arr)
    mat2Buff = cl.Buffer(context=CONTEXT, flags=(cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR), hostbuf=mat2Arr)
    # sets with of matrix
    mat1WBuff = cl.Buffer(context=CONTEXT, flags=(cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR),
                        hostbuf=np.int32(mat1Arr.shape[1]))
    mat2WBuff = cl.Buffer(context=CONTEXT, flags=(cl.mem_flags.READ_ONLY | cl.mem_flags.COPY_HOST_PTR),
                        hostbuf=np.int32(mat2Arr.shape[1]))
    # resulting buffer
    resultBuff = cl.Buffer(context=CONTEXT, flags=(cl.mem_flags.READ_WRITE), size=mat3Arr.nbytes)

    startTime: dt.datetime = dt.datetime.now()
    mulMatrix(mat1Arr, mat2Arr, mat1Buff, mat2Buff, resultBuff, mat1WBuff, mat2WBuff)
    endTime: dt.datetime = dt.datetime.now()

    # mat3Arr = np.empty_like(mat3Arr)
    cl.enqueue_copy(queue=CMD_QUEUE, dest=mat3Arr, src=resultBuff)
    matRs = np.matrix(data=mat3Arr, copy=False)

    print(f"Result by OpenCL GPU:\n{str(matRs)}")
    print(f"Run on OpenCL GPU time:{(endTime - startTime)}")
    pass
