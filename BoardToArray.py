import numpy as np
# Cho turn: 0, Han turn: 1
# No mark: 0, Cho mark: Plus, Han mark = minus
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
def BoardToArray(board,turn):
    #board는 10*9사이즈의 array 우리의 목적은 각 말의 위치 정보를 담은 array를 뽑는 것.
    #14개의 array가 나오며 1~7까지는 아군, 이후는 적군
    arr=np.zeros((14,10,9))
    sign=(-1)**turn
    print(sign)
    for i in range(7):
        #해당되는 값이 아닌 곳은 0으로 
        mark=(i+1)*sign
        arr[i]=np.where(board!=mark,0,board)
        arr[i+7]=np.where(board!=-mark,0,board)
    
    return arr

a=BoardToArray(test_board,0)
print(a[3])