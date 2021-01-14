from utils import new_make_action_space, make_action_space
import time
# print(len(new_make_action_space()))
action_space=make_action_space()
for new in new_make_action_space():
    if not new in action_space:
        print(new)

a=time.time()
make_action_space()
b=time.time()
new_make_action_space()
c=time.time()
print(c-b)
print(b-a)