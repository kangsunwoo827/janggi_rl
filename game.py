import numpy as np
import logging
from utils import form_to_board, coord_to_action, action_to_coord, can_move, make_action_space
from visualize import Visualize
#게임 보드판과 턴을 받고 다양한 함수 실행
#보드판은 row 10에 col9인 array (shape = 10,9 )
# Cho turn: +1, Han turn: -1
# No mark: 0, Cho mark: Plus, Han mark = minus

class GameState():
	def __init__(self, board, num_turn):
		#홀수면 Cho'turn -> +1
		if num_turn%2 :
			self.playerTurn=+1
		else:
			self.playerTurn=-1
		self.board = board
		self.num_turn=num_turn
		self.pieces = [None,'졸','사','상','마','포','차','왕']
		self.score_lst=[0,2,3,3,5,7,13,0]
		self.board_memory=np.zeros((6,10,9))

		self.playerScore=0
		self.oppoScore=0
		if self.playerTurn>0:
			self.oppoScore+=1.5
		else:
			self.playerScore+=1.5

		self.BoardToArray = self._convertBoardToArr()
		self.id = self._convertStateToId()
		self.score = self._getScore()
		self.allowedActions = self._allowedActions()
		self.isEndGame,self.who_win = self._checkForEndGame()


	#Action 중 가능한 Action return
	def _allowedActions(self):
		allowed = []
		
		#player_piece는 살아있는 아군 기물의 위치와 번호를 담은 리스트
		player_pieces=[]
		for piece in range(1,8):
			y_coord=np.where(self.board==piece*self.playerTurn)[0]
			x_coord=np.where(self.board==piece*self.playerTurn)[1]
			for i,y in enumerate(y_coord):
				coord=[y, x_coord[i]]
				player_pieces.append([piece,coord])

		for pp in player_pieces:
			piece=pp[0]
			before=pp[1]
			after_list=can_move(piece, before, self.board, self.playerTurn)
			
			for after in after_list:

				allowed.append([before,after])

		allowed=self.check_repetition(allowed)
		#coord 형태로 되어있기 때문에 action 형태로 변환
		allowed=[coord_to_action(coord) for coord in allowed]

		return allowed

	def check_turn(self):
		if self.num_turn%2 :
			self.playerTurn=+1
		else:
			self.playerTurn=-1

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

	#게임이 끝났는지 확인
	def _checkForEndGame(self):
		isEnd=False
		who_win=0

		#본인의 왕이 죽었다면 게임 끝 (패배)
		king_position=np.isin(self.board,7*self.playerTurn)
		if not np.any(king_position):
			print('king_die')
			isEnd=True
			who_win= -self.playerTurn

		playerScore,oppoScore=self.score
		#본인의 점수가 10점보다 적다면 게임 끝 (패배)
		if playerScore<10:
			print('score<10')
			isEnd=True
			who_win= -self.playerTurn
		

		#200턴안에 안끝나면 종료
		if self.num_turn > 200:
			print('turn>200')
			isEnd=True
			if playerScore>oppoScore :
				who_win=self.playerTurn
			else:
				who_win= -self.playerTurn		

		return isEnd,who_win


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


	#ban repetition
	def memorize_board(self):
		for i in range(len(self.board_memory)-1):
			self.board_memory[i]=self.board_memory[i+1]
		self.board_memory[-1]=self.board

	def check_repetition(self,allowedCoord):
		if (
			np.all(self.board_memory[0]==self.board_memory[4])
		 and np.all(self.board_memory[1]==self.board_memory[5])
		  and np.all(self.board_memory[2]==self.board)
		  ):
			for coord in allowedCoord:
				dummy_board=self.board
				before=allowedCoord[0]
				after=allowedCoord[1]
				dummy_board[after[0],after[1]]=dummy_board[before[0],before[1]]
				dummy_board[before[0],before[1]]=0
				
				if dummy_board==self.board_memory[3]:
					allowedCoord.remove(coord)
		return allowedCoord



	#action을 주면 action을 취한 상태의 state 와 value 등을 반환
	def takeAction(self, action):
		self.check_turn
		#memory_board
		self.memorize_board()
		coord=action_to_coord(action)
		before=coord[0]
		after=coord[1]
		newBoard = self.board
		newBoard[after[0],after[1]]=newBoard[before[0],before[1]]
		newBoard[before[0],before[1]]=0
		newState = GameState(newBoard, self.num_turn+1)
	
		

		value = 0
		done = 0

		if newState.isEndGame:
			#winner and turn is same      -> +1
			#winner and turn is different -> -1
			value = newState.who_win * newState.playerTurn
			done = 1

		state=self
		window=Visualize(state)	
		window.show(state)
		return (newState, value, done) 


	def render(self, logger):

		for row in self.board:
			logger.info([self.pieces[cell] for cell in row])
		logger.info('--------------')
		
	



class Game:

	def __init__(self,cho_form='mssm',han_form='mssm'):		
		self.cho_form=cho_form
		self.han_form=han_form
		formation_cho=form_to_board(self.cho_form)
		formation_han=form_to_board(self.han_form)
		self.init_board=np.concatenate([np.flip(formation_han*(-1), axis=0),formation_cho])
		self.num_turn=1
		self.gameState = GameState(self.init_board, self.num_turn)
		
		self.currentPlayer = self.gameState.playerTurn
		self.actionSpace = np.array(make_action_space())
		self.pieces = [None,'졸','사','상','마','포','차','왕']
		self.grid_shape = (10,9)
		self.input_shape = None
		self.name = 'janggi'
		self.state_size = len(self.gameState.BoardToArray)
		self.action_size = len(self.actionSpace)

	def reset(self,cho_form='mssm',han_form='mssm'):
		self.num_turn=1
		formation_cho=form_to_board(cho_form)
		formation_han=form_to_board(han_form)
		self.init_board=np.concatenate([np.flip(formation_han*(-1), axis=0),formation_cho])
		self.gameState = GameState(self.init_board, 1)
		return self.gameState

	def step(self, action):
		next_state, value, done = self.gameState.takeAction(action)
		self.gameState = next_state
		
		state=self.gameState
		window=Visualize(state)	
		window.show(state)
		info = None
		return ((next_state, value, done, info))

	

	# def identities(self, state, actionValues):
	# 	identities = [(state,actionValues)]

	# 	currentBoard = state.board
	# 	currentAV = actionValues

	# 	currentBoard = np.array([
	# 		  currentBoard[6], currentBoard[5],currentBoard[4], currentBoard[3], currentBoard[2], currentBoard[1], currentBoard[0]
	# 		, currentBoard[13], currentBoard[12],currentBoard[11], currentBoard[10], currentBoard[9], currentBoard[8], currentBoard[7]
	# 		, currentBoard[20], currentBoard[19],currentBoard[18], currentBoard[17], currentBoard[16], currentBoard[15], currentBoard[14]
	# 		, currentBoard[27], currentBoard[26],currentBoard[25], currentBoard[24], currentBoard[23], currentBoard[22], currentBoard[21]
	# 		, currentBoard[34], currentBoard[33],currentBoard[32], currentBoard[31], currentBoard[30], currentBoard[29], currentBoard[28]
	# 		, currentBoard[41], currentBoard[40],currentBoard[39], currentBoard[38], currentBoard[37], currentBoard[36], currentBoard[35]
	# 		])

	# 	currentAV = np.array([
	# 		currentAV[6], currentAV[5],currentAV[4], currentAV[3], currentAV[2], currentAV[1], currentAV[0]
	# 		, currentAV[13], currentAV[12],currentAV[11], currentAV[10], currentAV[9], currentAV[8], currentAV[7]
	# 		, currentAV[20], currentAV[19],currentAV[18], currentAV[17], currentAV[16], currentAV[15], currentAV[14]
	# 		, currentAV[27], currentAV[26],currentAV[25], currentAV[24], currentAV[23], currentAV[22], currentAV[21]
	# 		, currentAV[34], currentAV[33],currentAV[32], currentAV[31], currentAV[30], currentAV[29], currentAV[28]
	# 		, currentAV[41], currentAV[40],currentAV[39], currentAV[38], currentAV[37], currentAV[36], currentAV[35]
	# 				])

	# 	identities.append((GameState(currentBoard, state.playerTurn), currentAV))

	# 	return identities
