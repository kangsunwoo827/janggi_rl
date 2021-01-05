
import logging

def setup_logger(name, log_file, level=logging.INFO):

    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.handlers:
        logger.addHandler(handler)

    return logger

#장기 좌표 표기법과 array의 index 사이의 변환
def coord_to_action(coord):
    before=coord[0]
    after=coord[1]
    action_before=[(before[1]+1)%10, before[0]+1]
    action_after=[(after[1]+1)%10, after[0]+1]

    return [action_before,action_after]

def action_to_coord(action):
    before=action[0]
    after=action[1]
    
    if not before[0]:
        before[0]=10
    if not after[0]:
        after[0]=10

    coord_before=[before[1]-1, before[0]-1]
    coord_after=[after[1]-1, after[0]-1]

    return [coord_before,coord_after]
