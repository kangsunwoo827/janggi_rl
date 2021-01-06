from game import GameState
from visualize import Visualize
import random 
import numpy as np
from utils import action_to_coord
from time import sleep

game=Visualize('mssm','mssm')

num_turn=1
board,check,win,turn=game.step()
sleep(5)
while True:
    sleep(1)
    env=GameState(board,num_turn)
    action_lst=env.allowedActions
    action=random.sample(action_lst,1)[0]
    print(action[0],'에서',action[1])
    action=action_to_coord(action)
    board,check,win,turn=game.step(action)
    num_turn+=1
    
    