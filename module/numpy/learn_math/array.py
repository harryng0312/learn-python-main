import numpy as np

# array
arr = np.array([1, 2, 3, 4], dtype='S4')

randArr = np.random.randint(0, 100, 100)
print(f"NP Array: {arr} ID: {id(arr)}")
print(f"NP Array type:{arr.dtype}")
print(f"Py Array:{arr.astype(dtype=int)} ID: {id(arr.astype(int))}")

sortedArr = np.sort(a=randArr, kind='quicksort', order=None)
print(f"RandArr: {sortedArr}")
print(f"RandArr reverted: {sortedArr[::-1]}")


# filter
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)