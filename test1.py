from game import Game
from funcs import playMatchesBetweenVersions
import loggers as lg

env = Game()
# playMatchesBetweenVersions(
# env
# , 1  # 컴퓨터 플레이어가 위치한 실행 버전 번호
# , -1 # 첫번째 플레이어의 버전 번호 (사람의 경우 1번)
# , 12 # 두번째 플레이어의 버전 번호 (사람의 경우 1번)
# , 10 # 플레이할 게임의 수
# , lg.logger_tourney # 게임 로그를 저장할 곳
# , 0  # 게임 시작 시 누가 먼저 둘 것인지 - 랜덤일 경우 0
# )
print(env.gameState.board)
print('memory')
print(env.gameState.board_memory)
newState,_ ,_ = env.gameState.takeAction([[0,1],[9,1]])
print(newState.board)
print('memory')
print(newState.board_memory)
newState,_ ,_ = newState.takeAction([[1,1],[2,1]])
print(newState.board)
newState,_ ,_ = env.gameState.takeAction([[9,1],[0,1]])
print(newState.board)
newState,_ ,_ = newState.takeAction([[2,1],[1,1]])
print(newState.board)
newState,_ ,_ = env.gameState.takeAction([[0,1],[9,1]])
print(newState.board)
newState,_ ,_ = newState.takeAction([[1,1],[2,1]])
print(newState.board)
print(newState.allowedActions)