import os
import csv

canName = []
totalVote = 0
canVote = []
canCount = 0
canDict = {}

def rowcount(csvreader):
    global totalVote
    global canName
    global canCount
    for row in csvreader:
        totalVote += 1
        if row[2] not in canName:
            canName.append(row[2])
            canCount += 1
            canDict = {canName : 0}

        

""" def votecount(csvreader):
    global canName
    for row in csvreader:
        for i in canName:
            if row[2] == i: """
                
   

csvpath = os.path.join("Resources\election_data.csv")

with open (csvpath,newline ='') as csvElect:

    csvreader = csv.reader(csvElect,delimiter =',')

    csv_header = next(csvreader)

    rowcount(csvreader)

with open (csvpath,newline ='') as csvElect:

    csvreader = csv.reader(csvElect,delimiter =',')

    csv_header = next(csvreader)
    
    votecount(csvreader)
    
print(totalVote)
print(canName)
print(canVote)
    
  



 


        


   
  