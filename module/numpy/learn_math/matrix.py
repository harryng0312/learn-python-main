import numpy as np


def print_matrix():
    m1 = np.matrix([
        [1, 2, 3],
        [4, 5, 6],
        [4, 5, 6]
    ])
    m2 = np.matrix([
        [1],
        [4],
        [7]
    ])
    rs = m1 * m2
    print(f"Kết quả: \n{rs}")
    print(f"Dạng ma trận: {rs.shape}")
    print(f"Kiểu dữ liệu: {rs.dtype}")
    print(f"Số chiều: {rs.ndim}")
    print(f"Ma trận chuyển vị: {rs.T}")
    print(f"Phần ảo: {rs.imag}")
    print(f"Số lượng phần tử: {rs.size}")
    print(f"Kích thước mỗi phần tử (bytes): {rs.itemsize}")

