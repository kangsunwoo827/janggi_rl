import numpy as np
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


#말번호와 위치를 넣으면 도착 가능한 coord 반환

def can_move(piece,before,gameboard,turn):
    #move_list는 행마를 이용해 이동 가능한 위치 
    move_list=[]
    #in_gung은 기물이 궁성안에 있는가 여부
    in_gung=False
    
    #사와 왕은 원래 궁성에 있음.
    if piece==2 or piece==7:
        in_gung=True
        
    if(before[0]>=7 and 3<=before[1] and before[1] <=5) or(before[0]<=2 and 3<=before[1] and before[1] <=5):
        in_gung=True
    
    if piece==1:
        move_list=[
                [before[0]-turn, before[1]],
                [before[0], before[1]-1],
                [before[0], before[1]+1]
                ]

        #궁안에 있으면 대각선 추가 (졸)
        if in_gung:
            move_list.append([before[0]-turn, before[1]-1])
            move_list.append([before[0]-turn, before[1]+1])
        
    if piece ==2:
            move_list=[
                [before[0]+1, before[1]],
                [before[0]-1, before[1]],
                [before[0], before[1]-1],
                [before[0], before[1]+1],
                [before[0]+1, before[1]+1],
                [before[0]-1, before[1]-1],
                [before[0]+1, before[1]-1],
                [before[0]-1, before[1]+1]
                ]
            
    if piece ==3:
        move_list=[[before[0]+3, before[1]+2]
                    ,[before[0]+2, before[1]+3]
                    ,[before[0]+3, before[1]-2]
                    ,[before[0]+2, before[1]-3]
                    ,[before[0]-3, before[1]+2]
                    ,[before[0]-2, before[1]+3]
                    ,[before[0]-3, before[1]-2]
                    ,[before[0]-2, before[1]-3]]
        
    if piece ==4:
        move_list=[[before[0]+1, before[1]+2]
                ,[before[0]+2, before[1]+1]
                ,[before[0]+1, before[1]-2]
                ,[before[0]+2, before[1]-1]
                ,[before[0]-1, before[1]+2]
                ,[before[0]-2, before[1]+1]
                ,[before[0]-1, before[1]-2]
                ,[before[0]-2, before[1]-1]]
        
    if piece ==5:
        move_list.append([9,before[1]])
        for i in range(9):
            move_list.append([before[0],i])
            move_list.append([i,before[1]])

        #궁안에 있으면 대각선 추가 (포)  
        if in_gung:
            #아래쪽 궁에 있을 때
            if (before[0]>=7 and 3<=before[1] and before[1] <=5) :
                if before[0]%2==1 and before[1]%2==1:
                    if gameboard[8,4]!=0 and abs(gameboard[8,4])!=5:
                        move_list.append([16-before[0],8-before[1]])
            else:
                if (before[1]%2)!=(before[0]%2):
                    if gameboard[1,4]!=0 and abs(gameboard[1,4])!=5:
                            move_list.append([2-before[0],8-before[1]])
                
        

    #궁안에 있으면 대각선 추가 (차)          
    if piece == 6:
        for i in range(9):
            move_list.append([before[0],i])
            move_list.append([i,before[1]])
        move_list.append([9,before[1]])
                
        if in_gung:
            #아래쪽에 있을 때
            if (before[0]>=7 and 3<=before[1] and before[1] <=5):
                if before[1]==4 and before[0]==8:
                    move_list.append([before[0]+1,before[1]+1])
                    move_list.append([before[0]+1,before[1]-1])
                    move_list.append([before[0]-1,before[1]+1])
                    move_list.append([before[0]-1,before[1]-1])
                
                elif before[0]%2==1 and before[1]%2==1:
                    move_list.append([8,4])
                    if gameboard[8,4]==0:
                        move_list.append([16-before[0],8-before[1]])
                    
            #위쪽 궁에 있을 때
            else:
                
                if (before[1]%2)!=(before[0]%2):
                    if before[1]==4:
                        move_list.append([before[0]+1,before[1]+1])
                        move_list.append([before[0]+1,before[1]-1])
                        move_list.append([before[0]-1,before[1]+1])
                        move_list.append([before[0]-1,before[1]-1])
                
                    else:
                        move_list.append([1,4])
                        if gameboard[1,4]==0:
                            move_list.append([2-before[0],8-before[1]])
            
            
    if piece ==7:
            move_list=[[before[0]+1,before[1]]
                    ,[before[0]-1,before[1]]
                    ,[before[0],before[1]-1]
                    ,[before[0],before[1]+1]
                    ,[before[0]+1,before[1]+1]
                    ,[before[0]-1,before[1]-1]
                    ,[before[0]+1,before[1]-1]
                    ,[before[0]-1,before[1]+1]]

    #================================================#
    #move_list를 만들었으니, 규칙에 어긋나는 부분 제거 #
    #================================================#
    can_list=[]
    for after in move_list:
        #판 밖으로 나가는 것 제외
        if after[0]<0 or after[0]>9 or after[1]<0 or after[1]>8:
            continue
        #같은 팀 말 위로 나가는 거 제외
        if turn * gameboard[after[0],after[1]]>0:
            continue
            
        #궁밖으로 못나감, 대각선으로 이동할 수 없는 곳이 있음
        if in_gung:
            if(before[0]>=7 and 3<=before[1] and before[1] <=5):
                
                if (after[0]<7 or after[1]<3 or after[1]>5)  and (piece==2 or piece==7):
                    continue
                    
                if before[0]==8 or before[1]==4:
                    if before[0]==8 and before[1]==4:
                        pass
                    else:
                        if after[0]-before[0]!=0 and after[1]-before[1]!=0:
                            continue
                    
                
            else:
                if (after[0]>2 or after[1]<3 or after[1]>5) and (piece==2 or piece==7):
                    continue
                
                if before[0]==1 or before[1]==4:
                    if before[0]==1 and before[1]==4:
                        pass
                    else:
                        if after[0]-before[0]!=0 and after[1]-before[1]!=0:
                            continue
                    
                
            
        #가는 길에 막히면 못움직임 (상)
        if piece==3 :
            move_y=np.sign(after[0]-before[0])
            move_x=np.sign(after[1]-before[1])
            if  gameboard[after[0]+1*(-move_y),after[1]+1*(-move_x)]==0 and gameboard[after[0]+2*(-move_y),after[1]+2*(-move_x)]==0:
                pass
            else:
                continue
        
            
        #가는 길에 막히면 못움직임 (마)      
        if piece==4 :
            
            move_y=np.sign(after[0]-before[0])
            move_x=np.sign(after[1]-before[1])
            if  gameboard[after[0]+1*(-move_y),after[1]+1*(-move_x)]==0:
                pass
            else:
                continue
                
        #포 사이에 하나 있어야 함 이 때 포면 안됨
        
        if piece==5:
            
            count=0
            jump_po=False
            
            if after[0]-before[0]!=0 and after[1]-before[1]!=0:
                count=1
            elif after[0]-before[0]==0 and after[1]-before[1]==0:
                continue
            
            elif after[0]-before[0]==0:
                d=after[1]-before[1]
                if d>0:
                    for i in range(1,d):
                        if gameboard[after[0],before[1]+i]!=0:
                            if abs(gameboard[after[0],before[1]+i])==5:
                                jump_po=True
                            count+=1
                            
                else:
                    for i in range(-1,d,-1):
                        if gameboard[after[0],before[1]+i]!=0:
                            
                            if abs(gameboard[after[0],before[1]+i])==5:
                                jump_po=True
                            count+=1
            
            elif after[1]-before[1]==0:
                d=after[0]-before[0]
                if d>0:
                    for i in range(1,d):
                        if gameboard[before[0]+i,after[1]]!=0:
                            if abs(gameboard[before[0]+i,after[1]])==5:
                                jump_po=True
                            count+=1
                else:
                    for i in range(-1,d,-1):
                        if gameboard[before[0]+i,after[1]]!=0:
                            if abs(gameboard[before[0]+i,after[1]])==5:
                                jump_po=True
                            count+=1
            
                
            if count!=1:
                continue
                
            if jump_po or abs(gameboard[after[0],after[1]])==5:
                continue
            
        
        #차 막히면 못감
        if piece==6:
            block=False
            if after[0]-before[0]!=0 and after[1]-before[1]!=0:
                pass
            elif after[0]-before[0]==0 and after[1]-before[1]==0:
                continue
            elif after[0]-before[0]==0:
                d=after[1]-before[1]
                if d>0:
                    for i in range(1,d):
                        if gameboard[after[0],before[1]+i]!=0:
                            block=True
                            
                else:
                    for i in range(-1,d,-1):
                        if gameboard[after[0],before[1]+i]!=0:
                            block=True
            
            elif after[1]-before[1]==0:
                d=after[0]-before[0]
                if d>0:
                    for i in range(1,d):
                        if gameboard[before[0]+i,after[1]]!=0:
                            block=True
                else:
                    for i in range(-1,d,-1):
                        if gameboard[before[0]+i,after[1]]!=0:
                            block=True
            else:
                continue
                
            if block:
                continue
    
        can_list.append(after)
        


    return can_list
