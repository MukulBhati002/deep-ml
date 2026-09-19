import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	rlen = len(a[0])
	clen = len(a)
	if rlen*clen != new_shape[0]*new_shape[1]:
		return []
	npa = np.array(a)
	ans = npa.reshape(new_shape)
	return ans.tolist()