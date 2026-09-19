import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	npa = np.array(matrix)
	if mode == "column":
	  return np.mean(npa,axis = 0)
	return np.mean(npa,axis = 1)