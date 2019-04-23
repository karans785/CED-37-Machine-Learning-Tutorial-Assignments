"""Find S"""
#import numpy as np
data = [['S','W','N','S','W','S','Y'],['S','W','H','S','W','S','Y'],['R','C','H','S','W','C','N'],['S','W','H','S','C','C','Y']]

def findS(data):
    H=[]
    
    print("Initialising the hypothesis with 1st training example.")
    for i in range(len(data[0])-1):
        H.append(data[0][i])
    print(H)
    #print(H)
    for i in range(len(data)):
        if i==0:
            continue
        if data[i][6]=='Y' : 
            for j in range(len(H)):
                if not data[i][j] == H[j] :
                    H[j] = '?'
            print("After round ",i+1," the hypothesis is : ", H)

        else :
            print("Negative training example is ignored.")
            
findS(data)