from utils import *
import numpy as np
# import loggers as lg/

# test_board=np.array([
#                     [-6,-3,-4,-2, 0,-2,-4,-3,-6],
#                     [ 0, 0, 0, 0,-7, 0, 0, 0, 0],
#                     [ 0,-5, 0, 0, 0, 0, 0,-5, 0],
#                     [-1, 0,-1, 0,-1, 0,-1, 0,-1],
#                     [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                     [ 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                     [ 1, 0, 1, 0, 1, 0, 1, 0, 1],
#                     [ 0, 5, 0, 0, 0, 0, 0, 5, 0],
#                     [ 0, 0, 0, 0, 7, 0, 0, 0, 0],
#                     [ 6, 4, 3, 2, 0, 2, 3, 4, 6]])

# from game import GameState,Game

# janggi=Game()
# print(janggi.step([[0,9],[2,9]]))
a=np.ones((6,10,9))
for i in range(len(a)):
    a[i]+=i
for i in range(len(a)-1):
    a[i]=a[i+1]
a[-1]=np.zeros((10,9))
print(a)
