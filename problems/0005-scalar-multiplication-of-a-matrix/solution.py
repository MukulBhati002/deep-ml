import numpy as np

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    npa = np.array(matrix)
    res = np.multiply(npa, scalar)
    return res.tolist()