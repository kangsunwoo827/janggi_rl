from game import GameState, Game
import numpy as np
test_board=np.array([
            [6,4,3,2,0,2,3,4,6]],
            [0,0,0,0,7,0,0,0,0],
            [0,5,0,0,0,0,0,5,0],
            [1,0,1,0,1,0,1,0,1],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [1,0,1,0,1,0,1,0,1],
            [0,5,0,0,0,0,0,5,0],
            [0,0,0,0,7,0,0,0,0],
            [6,4,3,2,0,2,3,4,6]],
            
])

print(GameState(test_board,1).allowedActions)