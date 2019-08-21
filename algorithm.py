import numpy as np

class Game:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.PHYSICAL_BOARD_WIDTH = width
        self.PHYSICAL_BOARD_HEIGHT = height
        self.physical_board_top_left=[0, 0]
        self.playing=False
        self.board=np.zeros((self.width, self.height))

    def _sum_neighbors(self):
        out=np.zeros(self.board.shape, dtype=np.ubyte)
        it = np.nditer(self.board, flags=['multi_index'], op_flags=['readonly'])
        for cells in it:
            out[it.multi_index]=np.sum(self.board[max([0, it.multi_index[0] - 1]):min([5, it.multi_index[0] + 2]),
                  max([0, it.multi_index[1] - 1]):min([5, it.multi_index[1] + 2])])
            out[it.multi_index]-=self.board[it.multi_index]
        return out

    def tick(self, grid):
        if(self.playing):
            neighbors=self._sum_neighbors(grid)
            survivors=(neighbors<4) & (neighbors>1) & grid
            newbies=(grid==0) & (neighbors==3)
            self.board=(survivors|newbies).astype(int)
            self.update_virtual_board()
        else:
            raise ValueError("Attempted to advance the game state when paused")

    def update_virtual_board(self):
        row_sum=np.sum(self.board, axis=1)
        col_sum=np.sum(self.board, axis=0)
        top_row=row_sum[0]
        bottom_row=row_sum[row_sum.shape[0]]
        left_col=col_sum[0]
        right_col=col_sum[col_sum.shape[0]]
        if(top_row+bottom_row+left_col+right_col==0):
            return
        #TODO update physical_board_top_left, update board