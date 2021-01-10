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
current_NN = Residual_CNN(config.REG_CONST, config.LEARNING_RATE, (14,) + env.grid_shape,   env.action_size, config.HIDDEN_CNN_LAYERS)
best_NN = Residual_CNN(config.REG_CONST, config.LEARNING_RATE, (14,) +  env.grid_shape,   env.action_size, config.HIDDEN_CNN_LAYERS)

current_player = Agent('current_player', env.state_size, env.action_size, config.MCTS_SIMS, config.CPUCT, current_NN)

gs = GameState(test_board, 1)

# preds = current_player.get_preds(gs)

# print(preds)
current_player.model.viewLayers()