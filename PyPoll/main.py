import os
import csv

totalVote = 0
canName = []
canVote = []
canDict = {}
canPercent = {}
canWin = 0

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
    print(totalVote)
    for j in canDict:
        canPercent.update({j:round((canDict[j]/totalVote)*100,2)})


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

print(totalVote)
print(canDict)
print(canPercent)
print(canWin)    
  



 


        


   
  