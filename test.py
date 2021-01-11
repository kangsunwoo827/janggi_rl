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

# from game import GameState,Game
# env=Game()
# print(env.gameState.allowedActions)

# action_space=make_action_space()
# id_index=identity_space_index()
# import random
# for i in range(10):
#     r=random.randint(1,len(action_space))
#     print(action_space[r-1])
#     print(action_space[id_index[r-1]])

# current_player.model.viewLayers()

import numpy as np
np.set_printoptions(suppress=True)

from shutil import copyfile
import random
from importlib import reload


from keras.utils import plot_model

from game import Game, GameState
from agent import Agent
from memory import Memory
from model import Residual_CNN
from funcs import playMatches, playMatchesBetweenVersions

import loggers as lg

from settings import run_folder, run_archive_folder
import initialise
import pickle
import config

env=Game()
current_NN = Residual_CNN(config.REG_CONST, config.LEARNING_RATE, (15,) + env.grid_shape,   env.action_size, config.HIDDEN_CNN_LAYERS)
best_NN = Residual_CNN(config.REG_CONST, config.LEARNING_RATE, (15,) +  env.grid_shape,   env.action_size, config.HIDDEN_CNN_LAYERS)

current_player = Agent('current_player', env.state_size, env.action_size, config.MCTS_SIMS, config.CPUCT, current_NN)

gs = GameState(test_board, 1)

preds = current_player.get_preds(gs)

# # print(preds)
# # # current_player.model.viewLayers()
# # from keras.utils import plot_model
# # plot_model(current_NN.model, to_file=run_folder + 'models/model.png', show_shapes = True)
# best_player = Agent('best_player', env.state_size, env.action_size, config.MCTS_SIMS, config.CPUCT, best_NN)
# env = Game()
# player1=best_player
# player2=best_player
# scores = {player1.name:0, "drawn": 0, player2.name:0}
# sp_scores = {'sp':0, "drawn": 0, 'nsp':0}
# points = {player1.name:[], player2.name:[]}

   
# state = env.reset()

# done = 0
# turn = 0
# player1.mcts = None
# player2.mcts = None

# player1Starts = random.randint(0,1) * 2 - 1

# if player1Starts == 1:
#     players = {1:{"agent": player1, "name":player1.name}
#             , -1: {"agent": player2, "name":player2.name}
#             }
   
# else:
#     players = {1:{"agent": player2, "name":player2.name}
#             , -1: {"agent": player1, "name":player1.name}
#             }

# print(env.gameState.board)

# while done == 0:
#     print('done:0')
#     turn = turn + 1

#     #### Run the MCTS algo and return an action
#     if turn < 10:
#         action, pi, MCTS_value, NN_value = players[state.playerTurn]['agent'].act(state, 1)
#     else:
#         action, pi, MCTS_value, NN_value = players[state.playerTurn]['agent'].act(state, 0)
#     print(turn)
#     # print(action)/