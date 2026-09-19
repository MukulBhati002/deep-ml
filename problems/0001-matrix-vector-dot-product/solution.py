import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	rlen = len(a[0])
	clen = len(b)
	if rlen != clen:
		return -1;
	npa = np.array(a)
	npb = np.array(b)
	res = npa @ npb
	return res.tolist()