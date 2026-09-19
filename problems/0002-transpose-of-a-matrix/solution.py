import numpy as np
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    npa = np.array(a)
    return npa.T
    