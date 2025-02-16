import csv
import matplotlib.pyplot as plt

darwin=[]
lamarck=[]
baldwin=[]
with open('max_his_darwin.csv', 'r') as f:
    reader = csv.reader(f)
    i=0
    for row in reader:
        i+=1
        if(i==1):
            darwin=[0 for _ in range(len(row))]
        for j in range(len(row)):
            darwin[j]+=int(row[j])
    for j in range(len(darwin)):
        darwin[j]=darwin[j]/i            
with open('max_his_lamarck.csv', 'r') as f:
    reader = csv.reader(f)
    i=0
    for row in reader:
        i+=1
        if(i==1):
            lamarck=[0 for _ in range(len(row))]
        for j in range(len(row)):
            lamarck[j]+=int(row[j])
    for j in range(len(lamarck)):
        lamarck[j]=lamarck[j]/i   
with open('max_his_baldwin.csv', 'r') as f:
    reader = csv.reader(f)
    i=0
    for row in reader:
        i+=1
        if(i==1):
            baldwin=[0 for _ in range(len(row))]
        for j in range(len(row)):
            baldwin[j]+=int(row[j])
    for j in range(len(baldwin)):
        baldwin[j]=baldwin[j]/i   


x_values = [i for i in range(len(darwin))]

# プロット
plt.plot(x_values, darwin, label='darwin')
plt.plot(x_values, lamarck, label='lamarck')
plt.plot(x_values, baldwin, label='baldwin')

# 各種設定
plt.xlabel('generation')
plt.ylabel('max fittness')
plt.title('Line plot')
plt.legend()

# 表示
plt.show()
