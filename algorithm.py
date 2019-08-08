import numpy as np

def sum_neighbors(in_):
    out=np.zeros(in_.shape, dtype=np.ubyte)
    it = np.nditer(in_, flags=['multi_index'], op_flags=['readonly'])
    for cells in it:
        out[it.multi_index]=np.sum(in_[max([0, it.multi_index[0] - 1]):min([5, it.multi_index[0] + 2]),
              max([0, it.multi_index[1] - 1]):min([5, it.multi_index[1] + 2])])
        out[it.multi_index]-=in_[it.multi_index]
    return out

def tick(grid):
    neighbors=sum_neighbors(grid)
    survivors=(neighbors<4) & (neighbors>1) & grid
    newbies=(grid==0) & (neighbors==3)
    return survivors|newbies