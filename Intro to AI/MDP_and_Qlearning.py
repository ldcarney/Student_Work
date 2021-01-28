#Liam Carney
#Intro to AI

#MDP and Qlearning Algorithms 
#Excuse the formatting as it is taken from a jupyter notebook

import pandas as pd
import numpy as np
import random
import scipy.stats as stats
import matplotlib.pyplot as plt
from collections import defaultdict

# added packages
import heapq
from matplotlib import colors

walls = [(1,y) for y in range(2,15)] + [(2,y) for y in range(3,14)] + [(3,y) for y in range(4,13)] + \
        [(4,y) for y in range(5,12)] + [(x,1) for x in range(5,24)] + [(10,y) for y in range(9,13)] + \
        [(x,y) for x in range(11,14) for y in range(9,15)] + [(14,y) for y in range(11,15)] + \
        [(x,y) for x in range(21,26) for y in range(11,17)] + \
        [(x,y) for x in [0,26] for y in range(0,18)] + [(x,y) for x in range(0,26) for y in [0,17]]
        
states = [(x,y) for x in range(1,26) for y in range(1,17)]

# Your adjacency here
def adjacent_states(state):
    #N,W,S,E direction
    n = [(state[0], state[1]+1),1]
    s = [(state[0], state[1]-1),1]
    e = [(state[0]+1, state[1]),1]
    w = [(state[0]-1, state[1]),1]
    
    #diagonals 
    ne = [(state[0]+1, state[1]+1), np.sqrt(2)]
    nw = [(state[0]-1, state[1]+1), np.sqrt(2)]
    se = [(state[0]+1, state[1]-1), np.sqrt(2)]
    sw = [(state[0]-1, state[1]-1), np.sqrt(2)]
    
    #array of adjacent states 
    arr = [n, s, e, w, ne, nw, se, sw]
    arr2 = arr.copy()
    #remove invalid states
    for state in arr2:
        for wall in walls:
            if state[0] == wall:
                if state in arr:
                    arr.remove(state)
    
    return arr

def heuristic_cols(state, goal):
    num_cols = goal[0] - state[0]
    return num_cols
       
def heuristic_rows(state, goal):
    num_rows = goal[1] - state[1]
    return num_rows
   
def heuristic_eucl(state, goal):
    """
    num_cols = heuristic_cols(state, goal)
    num_rows = heuristic_rows(state, goal)
    dist = np.sqrt((num_cols**2)+(num_rows**2))
    """
    
    eucl_dist = np.linalg.norm(np.array(goal)-np.array(state))
    
    return eucl_dist

def heuristic_max(state, goal):
    arr = [heuristic_cols(state, goal), heuristic_rows(state,goal), heuristic_eucl(state, goal)]
    heur_max = max(arr)
    return heur_max

def Astar_search(state, goal):
    path = [(1,15)]
    
    while True:
        adj_arr = adjacent_states(state)
        heur_dict = {}
        
        for adj_state in adj_arr:
            f_val = heuristic_max(adj_state[0], goal) + adj_state[1]
            heur_dict[adj_state[0]] = f_val

        key_min = min(heur_dict.keys(), key=(lambda k: heur_dict[k]))
        state = key_min
        
        path.append(key_min)
        if key_min == goal:
            break
        
        
    return path

path = Astar_search((1,15),(25,9))
x = [coord[0] for coord in path]
y = [coord[1] for coord in path]

x_walls = [wall[0] for wall in walls]
y_walls = [wall[1] for wall in walls]

xlines = [0.5, 1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,
          11.5,12.5,13.5,14.5,15.5,16.5,17.5,
         18.5,19.5,20.5,21.5,22.5,23.5,24.5,26.5]
ylines = [0.5, 1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,
         11.5,12.5,13.5,14.5,15.5,16.5]
plt.figure(figsize=(13,8))
plt.plot(x_walls, y_walls, 's', color = 'b' )
plt.plot(x, y, 's', color = 'g')

plt.xticks(xlines)
plt.yticks(ylines)
plt.axis([.5,25.5,.5,16.5])
#plt.xticks([])
#plt.yticks([])

plt.grid(color='black', linestyle= '-', linewidth=2, fillstyle = 'full', ds = 'steps-pre')
plt.gca().patch.set_facecolor('0.9')


class MDP:
    def __init__(self, default_reward, discount):
        self.states = states
        self.default_reward = default_reward
        self.df = discount
        
    def actions(self, state):
        #print(state)
        arr = []
        arr2 = []
        n = ['N', (state[0], state[1]+1)]
        s = ['S', (state[0], state[1]-1)]
        e = ['E', (state[0]+1, state[1])]
        w = ['W', (state[0]-1, state[1])]

        ne = ['NE',(state[0]+1, state[1]+1)]
        nw = ['NW',(state[0]-1, state[1]+1)]
        se = ['SE',(state[0]+1, state[1]-1)]
        sw = ['SW',(state[0]-1, state[1]-1)]

        #array of adjacent states 
        arr = [n, s, e, w, ne, nw, se, sw]
        arr2 = arr.copy()

        #remove invalid states
        for wall in walls:
            for poss_state in arr2:
                #print(arr)
                if poss_state[1] == wall:
                    #print(poss_state)
                    if poss_state in arr:
                        arr.remove(poss_state)
        actions = []
        for new_state in arr:
            actions.append(new_state[0])
            
        return actions
    
    def reward(self, state):
        if state == (25,9):
            return 10
        else:
            return self.default_reward
    
    def result(self, state, action):
        
        assert action in self.actions(state), 'Error: action needs to be available in that state'
        
        action_results = {
            'N' : (state[0], state[1]+1),
            'S' : (state[0], state[1]-1),
            'E' : (state[0]+1, state[1]),
            'W' : (state[0]-1, state[1]),
            'NE': (state[0]+1, state[1]+1),
            'NW': (state[0]-1, state[1]+1),
            'SE': (state[0]+1, state[1]-1),
            'SW': (state[0]-1, state[1]-1)
        }
        for key in action_results:
            if key == action:
                return action_results[key]
        
    def transition(self, state, action):
        
        trans = []
        if action is None:
            return [(0, state)]
        else:
            trans.append((.75, self.result(state,action)))
            
            possAct = self.actions(state)
            possAct.remove(action)
            remain_prob = .25/len(possAct)
            for a in possAct:
                trans.append((remain_prob, self.result(state,a)))
                
            return trans

#accessible states
old_states = states.copy()
for state in old_states:
    for wall in walls:
        if wall == state:
            states.remove(state)
new_util = {}         
for item in states:        
    new_util[item] = 0


def value_iteration(mdp, states, new_util, tol):
    
    #new_util = {(x,y):x+y for x in range(1,mdp.ncol+1) for y in range(1,mdp.nrow+1)}
    
    while True:
        old_util = new_util.copy()
        
        max_change = 0
        for s in states:
            
            next_states = [mdp.transition(s, a) for a in mdp.actions(s)]
            best_util = -99

            for k in range(len(next_states)):
                newsum = sum([next_states[k][j][0]*old_util[next_states[k][j][1]] for j in range(len(next_states[k]))])
                best_util = max(best_util, newsum)
                if len(next_states)==1:
                    best_util = newsum
    
            new_util[s] = mdp.reward(s) + mdp.df*best_util
        
            max_change = max(max_change, abs(new_util[s]-old_util[s]))
            #print(max_change)
            #print('tol: ', tol*(1-mdp.df)/mdp.df)
            
        if (mdp.df==1 and max_change < tol) or max_change < tol*(1-mdp.df)/mdp.df:
            break
            
    return new_util

def find_policy(mdp, new_util, states):
    policy = {s : None for s in states}
    
    for s in states:
        best_util = (-99, None)
        
        for a in mdp.actions(s):
            
            # calculate the expected utility of action a from state s
            newsum = sum([p*new_util[s2] for p, s2 in mdp.transition(s,a)])
            if newsum > best_util[0]:
                best_util = (newsum, a)
                
        policy[s] = best_util[1]
        
    return policy
    
    
util_dict = value_iteration(mdp, states, new_util, tol=.1)
pol_dict = find_policy(mdp, util_dict, states)

newUtil = value_iteration(mdp, states, new_util, tol=.1)
lowest_util = min(newUtil.keys(), key=(lambda k: newUtil[k]))
hi_util = sorted(newUtil, key=newUtil.get, reverse=True)[:3]

print('Lowest Utility State: ', lowest_util)
print('Highest 3 Utility States: ', hi_util)


pol_dict[(25, 9)] = " "
data = {"x":[], "y":[], "label":[]}
for key, coord in pol_dict.items():
    data["x"].append(key[0])
    data["y"].append(key[1])
    data["label"].append(coord)


plt.figure(figsize=(15,10))
plt.title('Optimal Policy', fontsize=20)
plt.xlabel('x', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.scatter(data["x"], data["y"], marker = 'o', color = 'w')
plt.plot(25, 9, marker = 's', ms = 30, color = 'y')

for label, x, y in zip(data["label"], data["x"], data["y"]):
    plt.annotate(label, xy = (x, y))

x_walls = [wall[0] for wall in walls]
y_walls = [wall[1] for wall in walls]

xlines = [0.5, 1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,
          11.5,12.5,13.5,14.5,15.5,16.5,17.5,
         18.5,19.5,20.5,21.5,22.5,23.5,24.5,26.5]
ylines = [0.5, 1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,
         11.5,12.5,13.5,14.5,15.5,16.5]

plt.plot(x_walls, y_walls, 's', color = 'b', ms = 30)


plt.xticks(xlines)
plt.yticks(ylines)
plt.axis([.5,25.5,.5,16.5])

plt.grid(color='black', linestyle= '-', linewidth=2, fillstyle = 'full', ds = 'steps-pre')

random.seed(30)
x = np.linspace(0,25,26)
y = np.linspace(0,25,26)
X,Y = np.meshgrid(x,y)
f1 = np.zeros(X.shape)
f2 = np.zeros(X.shape)
f3 = np.zeros(X.shape)
f4 = np.zeros(X.shape)

mu1, mu2, mu3, mu4=[17,12],[17,11],[11,8],[11,6]
covar1, covar2, covar3, covar4= [[16,8],[8,16]],[[12,.5],[.5,12]],[[4,.8],[.8,4]],[[.8,12],[.8,12]]
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        f1[i,j] = 6*stats.multivariate_normal.pdf(x=(X[i,j],Y[i,j]), mean=mu1, cov=covar1)
        f2[i,j] = 3*stats.multivariate_normal.pdf(x=(X[i,j],Y[i,j]), mean=mu2, cov=covar2)
        f3[i,j] = stats.multivariate_normal.pdf(x=(X[i,j],Y[i,j]), mean=mu3, cov=covar3)
        f4[i,j] = 1*stats.multivariate_normal.pdf(x=(X[i,j],Y[i,j]), mean=mu4, cov=covar4)
        
f =f1+f2+f3+f4    
f=1-(f/np.max(f))**(1/3)

#PLOTTING:
fig, ax = plt.subplots(1,1, figsize=(7,5))
my_levels = np.linspace(0, 1, 11)
labels = [str(lv) for lv in my_levels]
cp = ax.contour(X, Y, f, levels=my_levels)
plt.clabel(cp, inline=1, fontsize=10)
ax.set(xlim=(0, 25), ylim=(0, 16))
plt.title('Footing')

def footing(x,y):
    return f[y,x]

print("It's icy at (12,8), with almost no footing:", footing(12,8))
print("It's better at (8,12):", footing(8,12))


#create a Q, initialize all the Q-utilities as 0.
ending_state = (25,9)

# Initializing Q-Values
Q_dict = {}
for state in states:
    Q_dict[state] = 0

rewards_dict = {}
for state in states:
    if state == (25,9):
        rewards_dict[state] = 10
    else:
        rewards_dict[state] = -0.01        

#reward the exit/end location
#rewards_new = np.copy(rewards_dict)


def create_dict(state):
    diction = {}
    diction_2 = {}
    actions = mdp.actions(state)
    diction[(state, state)] = 'None', Q_dict[state], rewards_dict[state]
    for action in actions:
        result = mdp.result(state, action)

        diction[(state, result)] = action, Q_dict[result], rewards_dict[result]
        
        new_actions = mdp.actions(result)
        diction_2[(state, result)] = action, Q_dict[result], rewards_dict[result]
        diction_2[(result, result)] = 'None', Q_dict[result], rewards_dict[result]
        for new_act in new_actions:
            new_result = mdp.result(result, new_act)
            diction_2[(result, new_result)] = new_act, Q_dict[new_result], rewards_dict[new_result]
            
        
            
            
        #actions_next = adjacent_states(action[0])
        #for a_next in actions_next:
            #diction[action, a_next] = 0
            
    return diction, diction_2


#print(create_dict((4,4)))
create_dict((4,4))





