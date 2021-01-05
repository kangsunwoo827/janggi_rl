import numpy as np
import logging
from utils import coord_to_action, action_to_coord

#게임 보드판과 턴을 받고 다양한 함수 실행
#보드판은 row 10에 col9인 array (shape = 10,9 )
# Cho turn: +1, Han turn: -1
# No mark: 0, Cho mark: Plus, Han mark = minus

class GameState():
	def __init__(self, board, playerTurn, num_turn):
		self.board = board
		self.playerTurn = playerTurn
		self.num_turn=num_turn
		self.pieces = [None,'jol','sa','sang','ma','po','cha','wang']
		self.score_lst=[0,2,3,3,5,7,13,None]
		
		self.BoardToArray = self._convertBoardToArr()
		self.id = self._convertStateToId()
	
		self.score = self._getScore()
		self.playerScore=0
		self.oppoScore=0
		if playerTurn>0:
			self.oppoScore+=1.5
		else:
			self.playerScore+=1.5

		# self.allowedActions = self._allowedActions()
		# self.isEndGame = self._checkForEndGame()
		# self.value = self._getValue()



	#Action 중 가능한 Action return
	def _allowedActions(self):
		allowed = []
		# can_start =
		for i in range(len(self.board)):
			if i >= len(self.board) - 7:
				if self.board[i]==0:
					allowed.append(i)
			else:
				if self.board[i] == 0 and self.board[i+7] != 0:
					allowed.append(i)

		return allowed

	#state를 position array들로 변환 
	def _convertBoardToArr(self):
		position=np.zeros((14,*np.shape(self.board)))
		for i in range(7):
			#해당되는 값이 아닌 곳은 0으로 
			mark=(i+1)*self.playerTurn
			position[i]=np.where(self.board!=mark,0,self.board)
			position[i+7]=np.where(self.board!=-mark,0,self.board)
		return position

	#state를 id로 변환
	def _convertStateToId(self):
		position = self.BoardToArray
		id = ''.join(map(str,position))
		return id

	def _checkForEndGame(self):
		if num_turn >= 200:
			return True

		for x,y,z,a in self.winners:
			if (self.board[x] + self.board[y] + self.board[z] + self.board[a] == 4 * -self.playerTurn):
				return 1
		return 0


	def _getValue(self):
		# This is the value of the state for the current player
		# i.e. if the previous player played a winning move, you lose
		for x,y,z,a in self.winners:
			if (self.board[x] + self.board[y] + self.board[z] + self.board[a] == 4 * -self.playerTurn):
				return (-1, -1, 1)
		return (0, 0, 0)


	def _getScore(self): 
		for i in range(np.shape(self.board)[0]):
			for j in range(np.shape(self.board)[1]):
				piece=self.board[i,j]
				score=self.score_lst[abs(piece)]
				if piece*self.playerTurn>0:
					self.playerScore+=score
				else:
					self.oppoScore +=score

		return self.playerScore, self.oppoScore



	#action을 주면 action을 취한 상태의 state 반환
	def takeAction(self, action):
		coord=coord_to_action(action)
		before=coord[0]
		after=coord[1]
		newBoard = self.board
		newBoard[after]=newBoard[before]
		newBoard[before]=0
		newState = GameState(newBoard, -self.playerTurn)

		value = 0
		done = 0

		if newState.isEndGame:
			value = newState.value[0]
			done = 1

		return (newState, value, done) 




	def render(self, logger):
		for r in range(6):
			logger.info([self.pieces[str(x)] for x in self.board[7*r : (7*r + 7)]])
		logger.info('--------------')



class Game:

	def __init__(self):		
		self.currentPlayer = 1
		self.gameState = GameState(np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], dtype=np.int), 1)
		self.actionSpace = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], dtype=np.int)
		self.pieces = {'1':'X', '0': '-', '-1':'O'}
		self.grid_shape = (6,7)
		self.input_shape = (2,6,7)
		self.name = 'connect4'
		self.state_size = len(self.gameState.binary)
		self.action_size = len(self.actionSpace)

	def reset(self):
		self.gameState = GameState(np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], dtype=np.int), 1)
		self.currentPlayer = 1
		return self.gameState

	def step(self, action):
		next_state, value, done = self.gameState.takeAction(action)
		self.gameState = next_state
		self.currentPlayer = -self.currentPlayer
		info = None
		return ((next_state, value, done, info))


	def identities(self, state, actionValues):
		identities = [(state,actionValues)]

		currentBoard = state.board
		currentAV = actionValues

		currentBoard = np.array([
			  currentBoard[6], currentBoard[5],currentBoard[4], currentBoard[3], currentBoard[2], currentBoard[1], currentBoard[0]
			, currentBoard[13], currentBoard[12],currentBoard[11], currentBoard[10], currentBoard[9], currentBoard[8], currentBoard[7]
			, currentBoard[20], currentBoard[19],currentBoard[18], currentBoard[17], currentBoard[16], currentBoard[15], currentBoard[14]
			, currentBoard[27], currentBoard[26],currentBoard[25], currentBoard[24], currentBoard[23], currentBoard[22], currentBoard[21]
			, currentBoard[34], currentBoard[33],currentBoard[32], currentBoard[31], currentBoard[30], currentBoard[29], currentBoard[28]
			, currentBoard[41], currentBoard[40],currentBoard[39], currentBoard[38], currentBoard[37], currentBoard[36], currentBoard[35]
			])

		currentAV = np.array([
			currentAV[6], currentAV[5],currentAV[4], currentAV[3], currentAV[2], currentAV[1], currentAV[0]
			, currentAV[13], currentAV[12],currentAV[11], currentAV[10], currentAV[9], currentAV[8], currentAV[7]
			, currentAV[20], currentAV[19],currentAV[18], currentAV[17], currentAV[16], currentAV[15], currentAV[14]
			, currentAV[27], currentAV[26],currentAV[25], currentAV[24], currentAV[23], currentAV[22], currentAV[21]
			, currentAV[34], currentAV[33],currentAV[32], currentAV[31], currentAV[30], currentAV[29], currentAV[28]
			, currentAV[41], currentAV[40],currentAV[39], currentAV[38], currentAV[37], currentAV[36], currentAV[35]
					])

		identities.append((GameState(currentBoard, state.playerTurn), currentAV))

		return identities
