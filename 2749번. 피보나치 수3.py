import numpy as np
from sys import stdin
import math

n = int(stdin.readline())
exp = np.array( [[1,1,1], [1,0,0],[0,1,0]] )
base = np.array([[1], [1], [0] ] )

exps = exp ** (n-2)
ans = np.dot(exps, base)
print(exps)
