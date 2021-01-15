from utils import  make_action_space
import time

a=time.time()
print(len(make_action_space()))
b=time.time()
print(b-a)