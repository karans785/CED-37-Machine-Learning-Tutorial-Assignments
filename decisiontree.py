import numpy
import pandas as pd
import math

dataset=pd.read_csv('playtennis.csv')
outlook = list(dataset['outlook'])
temperature = list(dataset['temperature'])
humidity = list(dataset['humidity'])
wind = list(dataset['wind'])
answer = list(dataset['answer'])

def calculate_entropy(answer):
    entropy = 0.0
    count = 0
    for i in range(len(answer)):
        if answer[i] == "yes":
            count = count + 1

    size = len(answer)
    p1 = count/size
    p2 = (size-count)/size
    if p1==0 and p2==0:
        entropy=0
    elif p1==0:
        entropy=p2*math.log(p2,2)
    elif p2==0:
        entropy=p1*math.log(p1,2)
    else:
        entropy = p1*math.log(p1,2) + p2*math.log(p2,2)
    entropy = entropy * -1
    return entropy


def calculate_gain(column,answer,entropy_decision):

    gain = 0.0
    values={}
    for i in range(len(column)):
        type=column[i]
        if type in values:
            values[type].append(answer[i])
        else:
            values[type]=[]
            values[type].append(answer[i])
    temp=0.0
    for i in values:
        p=len(values[i])/len(column)
        e=calculate_entropy(values[i])
        temp=temp+p*e

    gain=entropy_decision-temp
    return gain


def get_max_attribute(data):

    ans = data[len(data)-1]
    entropy_decision = calculate_entropy(ans)
    maxgain = 0
    index = -1
    for i in range(len(data)-1):
        gain = calculate_gain(data[i],ans,entropy_decision)
        if gain > maxgain:
            maxgain = gain
            index = i

    return index,entropy_decision

table = {'outlook':outlook,'temperature':temperature,'humidity':humidity,'wind':wind,'answer':answer}
name=['outlook','temperature','humidity','wind','answer']
branch=[]

def id3(temp,name,branch):
    table=[]
    for key in temp:
        table.append(temp[key])

    index,entropy_decision = get_max_attribute(table)
    if entropy_decision == 0:
        print(branch, "->",table[len(table)-1][0])
        print()
        return
    column = table[index]
    branch.append(name[index])
    values={}
    tempname = []

    for i in range(len(name)):
        if i != index:
            tempname.append(name[i])

    for i in range(len(column)):
        type=column[i]
        if type in values:
            for j in range(len(table)):
                if j != index:
                    values[type][name[j]].append(table[j][i])
        else:
            values[type]={}
            for j in range(len(table)):
                if j !=index:
                    values[type][name[j]]=[]
                    values[type][name[j]].append(table[j][i])

    for i in values:
        branch.append(i)
        id3(values[i],tempname,branch)
        branch.pop()

    branch.pop()

id3(table, name, branch)
