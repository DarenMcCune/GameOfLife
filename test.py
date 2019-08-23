from algorithm import Game
x=Game(8, 8)
for cell in [0,33, 34, 41, 42]:
    x.flip_physical_board_cell(cell)
print x.board.astype(int)

x.playing=True
for i in range(10):
    print "continue ##########################"
    #raw_input("continue? ")
    x.tick()
    print "virtual board:"
    print x.board.astype(int)
    print "Physical:"
    print x._get_physical_board().astype(int)
