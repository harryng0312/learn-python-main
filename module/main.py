# This is a sample Python script.
import sys
from basic.threads import thread_basic as tb
import numpy as np
# from learn_math import matrix as mt
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    arr1: (float) = (1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
    arr2: list[float] = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
    arr3: (float) = arr1
    arr4: list[float] = arr2
    a: float = 3.0
    print(f"size of int:{sys.getsizeof(a)} type:{type(a)} \narr1:{id(arr1)} arr2:{id(arr2)}\n" 
        + f"arr3:{id(arr3)} arr4:{id(arr4)}")
    # mt.print_matrix()
    print(f"Kích thước số: {sys.getsizeof(np.int8(6.0))}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
