from game import GameState,Game
from visualize import Visualize
import random 
import numpy as np
from utils import action_to_coord
from time import sleep

janggi=Game()
state=janggi.gameState
window=Visualize(state)
while True:
    sleep(0.1)
    window.show(state)
    action_lst=janggi.gameState.allowedActions
    action=random.sample(action_lst,1)[0]
    print(action[0],'에서',action[1])
    new_state,v,done,i=janggi.step(action)
    state=new_state
    if done:
        window.show(state)
        sleep(5)
        break
    