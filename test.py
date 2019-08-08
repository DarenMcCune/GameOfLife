import numpy as np
import algorithm as algo

x=np.array([[0,0,0,0,0], [0,0,1,0,0], [0,0,1,0,0], [0,0,1,0,0],[0,0,0,0,0]], dtype=np.bool)
for i in range(10):
    print x
    x=algo.tick(x)