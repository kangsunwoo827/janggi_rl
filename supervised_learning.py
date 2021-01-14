from game import Game, GameState
from visualize import Visualize
from time import sleep

def gib_to_data(path='gibo2020.txt'):

    with open(path, 'r',encoding='utf-8') as file:
        data = file.read()
        data = data.split('\n\n')
        
    data = data[:-1]

    data=['\n\n'.join([data[2*i],data[2*i+1]]) for i in range(1163)]
    data = [match for match in data if  '완승' in match]
    data = [match for match in data if not  '. i' in match]
    num=0
    discount_ratio=0.9
    tot_input=[]
    tot_score=[]
    tot_action=[]
    for match in data:
        num+=1
        cho_form_idx=match.find('초차림')
        cho_form=match[cho_form_idx+5:cho_form_idx+9]
        han_form_idx=match.find('한차림')
        han_form=match[han_form_idx+5:han_form_idx+9]
        end_turn_idx=match.find('총수 "')
        win_idx=match.find('[대국결과')
        end_turn=match[end_turn_idx+4:win_idx-3]
        win=match[win_idx+7:win_idx+8]
        cho_form=''.join(['m' if i=='마' else 's' for i in cho_form])
        han_form=''.join(['m' if i=='마' else 's' for i in han_form])
        pan_lst=[]
        strend_idx=match.find('\n\n')
        action_str=match[strend_idx+2:]
        # print(action_str)
        env=Game(cho_form,han_form)
        # window=Visualize(env.gameState)
        action_lst=action_str.split('. ')
        action_lst=action_lst[1:]
        # action_lst=[action for action in action_lst]
        # print(action_lst)
        end_turn=int(end_turn)
        input_lst=[]
        score_lst=[]
        next_action=[]
        for num_turn in range(end_turn):
            action=action_lst[num_turn]
            action=action[:5]
            
            num_turn+=1
            if win=='초':
                win_constant=1
            else:
                win_constant=0
            if '한수쉼' in action:
                action=None
                continue
            else:
                before=[int(i) for i in action[0:2]]
                after=[int(i) for i in action[3:5]]
                action=[before,after]
            next_action.append(action)
            new_state, value, done, _=env.step(action)
            # window.show(new_state)
            input=new_state.BoardToInput
            score=discount_ratio**(end_turn-num_turn)
            score*=(-1)**(num_turn+win_constant)
            input_lst.append(input)
            score_lst.append(score)

        tot_input.append(input_lst)
        tot_score.append(score_lst)
        tot_action.append(next_action)
        if num%50==0:
            print('총 {}중 iter {}'.format(len(data),num))

    return [tot_input,tot_score,tot_action]


gib_2020_data=gib_to_data()
import pickle
pickle.dump(gib_2020_data, open( "gib2020.p", "wb" ) )

# data = pickle.load( open( "gib2020.p",   "rb" ) )
# input_data=[d[:-1] for d in data[0]]
# input_data=[y for x in input_data for y in x]
# value_data=[d[:-1] for d in data[1]]
# value_data=[y for x in value_data for y in x]
# policy_data=[d[1:] for d in data[2]]
# policy_data=[y for x in policy_data for y in x]

# print(input_data[0])
# print(policy_data[0])
# total_data=[input_data,value_data,policy_data]

# for i in range():
#     minibatch = random.sample(total_data, 256)
#     training_states = np.array([self.model.convertToModelInput(row['state']) for row in minibatch])
#     training_targets = {'value_head': np.array([row['value'] for row in minibatch])
#                         , 'policy_head': np.array([row['AV'] for row in minibatch])} 

#     fit = self.model.fit(training_states, training_targets, epochs=config.EPOCHS, verbose=1, validation_split=0, batch_size = 32)
#     lg.logger_mcts.info('NEW LOSS %s', fit.history)

#     self.train_overall_loss.append(round(fit.history['loss'][config.EPOCHS - 1],4))
#     self.train_value_loss.append(round(fit.history['value_head_loss'][config.EPOCHS - 1],4)) 
#     self.train_policy_loss.append(round(fit.history['policy_head_loss'][config.EPOCHS - 1],4)) 

# # plt.plot(self.train_overall_loss, 'k')
# # plt.plot(self.train_value_loss, 'k:')
# # plt.plot(self.train_policy_loss, 'k--')

# # plt.legend(['train_overall_loss', 'train_value_loss', 'train_policy_loss'], loc='lower left')

# # display.clear_output(wait=True)
# # display.display(pl.gcf())
# # pl.gcf().clear()
# # time.sleep(1.0)

# print('\n')
# self.model.printWeightAverages()