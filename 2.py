import numpy as np
a=np.array([[8,2],[10,3],[12,1],[5,6]])
result=(a.sum(1)%2).astype(bool)
print(result)
