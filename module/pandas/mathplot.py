import matplotlib.pyplot as plt
import numpy as np


def create_sin_func() -> None:
    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    # plt.plot(x, y)
    plt.show()
    return


if __name__ == "__main__":
    create_sin_func()
    pass



