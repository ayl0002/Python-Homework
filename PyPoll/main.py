import os
import csv

totalVote = 0
canName = []
canVote = [0,0,0,0]
canDict = {}
canPercent = {}
canWin = 0
winName = ' '

def rowcount(csvreader):
    global totalVote
    global canDict
    for row in csvreader:
        totalVote += 1
        if row[2] not in canDict:
            canName.append(row[2])
            canDict.update({row[2]:0})
            
            
            
def votecount(csvreader):
    global canDict
    global canVote
    for row in csvreader:
        for i in canDict:
            if row[2] == i:
                canDict.update({i:canDict[i]+1})                
                

                 
def votepercent(csvreader):
    global canDict
    global canPercent
    global totalVote
    global canWin
    global canVote
    global canName
    for j in canDict:
        if j in canName:
            canPercent.update({j:round((canDict[j]/totalVote)*100,2)})
            canVote[int(canName.index(j))] = canDict[j]       
   
     
def winCan(csvreader):
    global canWin
    global canVote
    global canName
    global winName
    for m in canVote:
        if int(m) > canWin:
            canWin = m
            winName = canName[canVote.index(m)]         
          



csvpath = os.path.join("Resources\election_data.csv")

with open (csvpath,newline ='') as csvElect:

    csvreader = csv.reader(csvElect,delimiter =',')

    csv_header = next(csvreader)

    rowcount(csvreader)

with open (csvpath,newline ='') as csvElect:

    csvreader = csv.reader(csvElect,delimiter =',')

    csv_header = next(csvreader)
    
    votecount(csvreader)

with open (csvpath,newline ='') as csvElect:

    csvreader = csv.reader(csvElect,delimiter =',')

    csv_header = next(csvreader)
    
    votepercent(csvreader)

with open (csvpath,newline ='') as csvElect:

    csvreader = csv.reader(csvElect,delimiter =',')

    csv_header = next(csvreader)
    
    winCan(csvreader)

print(totalVote)
print(canDict)
print(canPercent)
print(canName)
print(canVote)
print(winName)
print(canWin)




 


        


   
  