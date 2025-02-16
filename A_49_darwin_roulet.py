import numpy as np
import random
import csv
import copy


G=1000
N=100
P=0.001

def adapt_score(ind,env):
    X=[0 for _ in range(20)]
    score=0
    for i in range(len(env)):
        if ind[i]==1:
            X[env[i][0]]+=1
            X[env[i][1]]+=1
            X[env[i][2]]+=1
        else:
            X[env[i][0]]-=1
            X[env[i][1]]-=1
            X[env[i][2]]-=1
        for i in range(len(X)):
            if(X[i]==0):
                score+=1
    return score

def next_gen_darwin(gen,env):
    score=[]
    for j in range(N):
        score.append(adapt_score(gen[j],env))
    next_gen=[]
    for _ in range(N):
        index1 = np.random.choice(len(gen), p=np.array(score)/np.sum(score))
        parent1 = copy.deepcopy(gen[index1])
        index2 = np.random.choice(len(gen), p=np.array(score)/np.sum(score))
        parent2 = copy.deepcopy(gen[index2])
        children=[0 for _ in range(len(env))]
        mix=random.sample(range(len(env)),1)
        for j in range(len(env)):
            if(j<mix[0]):
                if random.random() > P:
                    children[j]=parent1[j]
                else:
                    children[j]=1-parent1[j]
            else:
                if random.random() > P:
                    children[j]=parent1[j]
                else:
                    children[j]=1-parent2[j]
        next_gen.append(children)
    return next_gen
        
RED = '\033[31m'
DEFAULT = '\033[0m'        
def ga(env):
    global S
    global P
    gen_his=[]
    gen=[]
    max_his=[]
    for _ in range(N):
        ind=(np.random.randint(2, size=len(env))).tolist()
        gen.append(ind)
    for i in range(G):
        gen_his.append(copy.deepcopy(gen))
        score=[]
        for j in range(N):
            score.append(adapt_score(gen[j],env))
        max_his.append(max(score))
        gen=next_gen_darwin(gen,env)
        if(i%10==0):
            print('generation = {}, max = {}, P = {}'.format(i,max_his[i],P))
            data_with_colors = [f"{RED}{item}{DEFAULT}" if item == max(score) else str(item) for item in score]
            print(', '.join(data_with_colors)) 
    
        if(i>30):
            flag=max_his[i]-max_his[i-1]
            if(flag < 0 ):
                P-=0.001
            elif(flag==0):
                P+=0.001
        
    return max_his



env=[]
with open('data.csv', 'r') as f:
    n=0
    reader = csv.reader(f, delimiter=' ')
    for row in f:
        data = [[abs(int(j)-1) for j in i] for i in reader]
        env.append(data)
        n+=1
env=env[0]

D=5
max_his_ave=[0 for _ in range(G)]
for i in range(D):
    max_his=ga(env)
    for i in range(G):
        max_his_ave[i]+=max_his[i]/D
with open('score_his_ave_darwin.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(max_his_ave)
    

