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

# from game import GameState

# env=GameState(test_board,4)
# # y_coord=np.where(test_board==7)[0]
# # print(y_coord)
# env.render(lg.logger_tourney)

import random
lst=[1,3,3,4,6,3456,8,65,4,4,7,8,0,2]
for x in range(100):
    print(random.sample(lst,1))