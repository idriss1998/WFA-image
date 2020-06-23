import numpy as np
from scipy.linalg import svd
import sys
from PIL import Image
import math
def calculWeights(A,B):
	U, s, VT = svd(A,False)
	Sigma = np.zeros((len(A[0]), len(A[0])))
	for i in range(len(A[0])):
		Sigma[i][i] = s[i]
	V = np.transpose(VT)
	UT = np.transpose(U)
	if np.linalg.cond(Sigma) < 1/sys.float_info.epsilon:
		invS = np.linalg.inv(Sigma)
		M = V.dot(invS)
		M = M.dot(UT)
		x = M.dot(B)
		return x
	else:
		return 0