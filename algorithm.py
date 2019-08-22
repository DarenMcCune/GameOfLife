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

    def flip_physical_board_cell(self, cell):
        if(cell>=self.PHYSICAL_BOARD_HEIGHT*self.PHYSICAL_BOARD_WIDTH):
            raise ValueError("cell falls out of bounds of the physical")
        row, col=self._get_physical_board_indices_from_cell(cell)
        self.board[row, col]=int(not self.board[row, col])

    def _get_physical_board_indices_from_cell(self, cell):
        if (cell >= self.PHYSICAL_BOARD_HEIGHT * self.PHYSICAL_BOARD_WIDTH):
            raise ValueError("cell falls out of bounds of the physical")
        row = cell // self.PHYSICAL_BOARD_WIDTH
        col = cell % self.PHYSICAL_BOARD_HEIGHT
        return row, col

    def update_virtual_board(self):
        #This function needs to do 3 things(None of them if virtual board size doesn't change: Update virtual board size
        #move the location of the physical board's top left corner, and copy the former board's data values to the correct
        #location

        #Check if their are any active cells on any of the borders.
        row_sum=np.sum(self.board, axis=1)
        col_sum=np.sum(self.board, axis=0)
        # The only thing that matters is whether or not their are active cells on the border, not how many their are,
        # so we reduce these to bools to make later calculations simple
        top_row=bool(row_sum[0])
        bottom_row=bool(row_sum[row_sum.shape[0]])
        left_col=bool(col_sum[0])
        right_col=bool(col_sum[col_sum.shape[0]])
        # If their are no active cells on any border, return
        if(top_row+bottom_row+left_col+right_col==0):
            return

        # Grow each side there is an active cell on by width/height. In other words, if their are no active cells on
        # the left or right, stay the same width, if their is one, append an entire self.width's amount of space that
        # side for 2x growth, and if there are active cells in both append an entire self.width's amount of space on
        # both sides for a total of 3x growth
        new_board_width=(1+left_col+right_col)*self.width
        new_board_height=(1+top_row+bottom_row)*self.height
        new_board=np.zeros((new_board_width, new_board_height))

        # if space was added to the left or above the physical board's location, increment it's coordinates to reflect
        # that
        if(left_col):
            self.physical_board_top_left[0]+=self.width
        if(top_row):
            self.physical_board_top_left[1]+=self.height

        #finally, embed the old board in the new board and update self.board, self.width and self.height
        old_board_x=self.width*left_col
        old_board_y=self.height*top_row
        new_board[old_board_x:old_board_x+self.width, old_board_y: old_board_y+self.height]=self.board
        self.width=new_board_width
        self.height=new_board_height
        self.board=new_board
