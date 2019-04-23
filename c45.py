import numpy
import pandas as pd
import math

dataset=pd.read_csv('playtennisC4.csv')

outlook = list(dataset['outlook'])
temperatureC = list(dataset['temperature'])
humidityC = list(dataset['humidity'])
wind = list(dataset['wind'])
answer = list(dataset['answer'])

temperature = []
humidity = []

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


def calculate_splitinfo(column):
    splitinfo = 0.0
    values={}
    for i in range(len(column)):
        type=column[i]
        if type in values:
            t = values[type]
            values[type] = t+1
        else:
            values[type]=1

    for i in values:
        p=(values[i])/len(column)
        l=math.log(p,2)
        splitinfo = splitinfo + (p*l)

    splitinfo = -1 * splitinfo
    return splitinfo

def calculate_gainratio(column,answer,entropy_decision):

    gain = calculate_gain(column,answer,entropy_decision)
    splitinfo = calculate_splitinfo(column)

    if splitinfo == 0:
        return 0
    return (gain/splitinfo)


def conTOdis(entropy_decision):

    global temperature,humidity

    maxgain = 0
    value = 0
    for i in range(len(humidityC)):

        threshold = humidityC[i]
        temp = []
        for j in range(len(humidityC)):
            if humidityC[j]>threshold:
                temp.append("high")
            else:
                temp.append("low")

        currgain = calculate_gain(temp,answer,entropy_decision)
        if currgain>maxgain:
            maxgain = currgain
            value = threshold
            humidity = temp

    print(humidityC)
    print(value)
    print(humidity,"\n")

    maxgain = 0
    value = 0
    for i in range(len(temperatureC)):

        threshold = temperatureC[i]

        if threshold != 83 and threshold != 85:
            temp = []
            for j in range(len(temperatureC)):
                if temperatureC[j]>threshold:
                    temp.append("high")
                else:
                    temp.append("low")
            currgain = calculate_gain(temp,answer,entropy_decision)
            if currgain>maxgain:
                maxgain = currgain
                value = threshold
                temperature = temp

    print(temperatureC)
    print(value)
    print(temperature,"\n")


def get_max_attribute(data):

    ans = data[len(data)-1]
    entropy_decision = calculate_entropy(ans)
    maxgain = 0
    index = -1
    for i in range(len(data)-1):
        gain = calculate_gainratio(data[i],ans,entropy_decision)
        if gain > maxgain:
            maxgain = gain
            index = i

    return index,entropy_decision

ed = calculate_entropy(answer)
conTOdis(ed)

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

# main function call
id3(table, name, branch)
