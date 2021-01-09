from utils import *
import numpy as np
# import loggers as lg/

test_board=np.array([
                    [-6,-3,-4,-2, 0,-2,-4,-3,-6],
                    [ 0, 0, 0, 0,-7, 0, 0, 0, 0],
                    [ 0,-5, 0, 0, 0, 0, 0,-5, 0],
                    [-1, 0,-1, 0,-1, 0,-1, 0,-1],
                    [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [ 1, 0, 1, 0, 1, 0, 1, 0, 1],
                    [ 0, 5, 0, 0, 0, 0, 0, 5, 0],
                    [ 0, 0, 0, 0, 7, 0, 0, 0, 0],
                    [ 6, 4, 3, 2, 0, 2, 3, 4, 6]])

from game import GameState,Game
print(test_board[0,8])
action=[[1,9],[2,8]]
print(action_to_coord(action))


