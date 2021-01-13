#### SELF PLAY
EPISODES = 5#25
MCTS_SIMS = 800 #50
MEMORY_SIZE = 30000 # 30000
TURNS_UNTIL_TAU0 = 30 # turn on which it starts playing deterministically
CPUCT = 1 #A hyperparameter determining the level of exploration.
EPSILON = 0.2
ALPHA = 0.8


#### RETRAINING
BATCH_SIZE = 256
EPOCHS = 1
REG_CONST = 0.0001
LEARNING_RATE = 0.1
MOMENTUM = 0.9
TRAINING_LOOPS = 5

HIDDEN_CNN_LAYERS = [
	{'filters':75, 'kernel_size': (4,4)}
	 , {'filters':75, 'kernel_size': (4,4)}
	 , {'filters':75, 'kernel_size': (4,4)}
	 , {'filters':75, 'kernel_size': (4,4)}
	 , {'filters':75, 'kernel_size': (4,4)}
	 , {'filters':75, 'kernel_size': (4,4)}
	]

#### EVALUATION
EVAL_EPISODES = 5
SCORING_THRESHOLD = 1.3