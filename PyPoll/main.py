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

print('Election Results')
print('...................................')
print(f'Total Votes: {totalVote}')
print('...................................')
print(f'{canName[0]}: {canPercent[canName[0]]}% ({canDict[canName[0]]})')
print(f'{canName[1]}: {canPercent[canName[1]]}% ({canDict[canName[1]]})')
print(f'{canName[2]}: {canPercent[canName[2]]}% ({canDict[canName[2]]})')
print(f'{canName[3]}: {canPercent[canName[3]]}% ({canDict[canName[3]]})')
print('...................................')
print(f'Winner: {winName}')
print('...................................')

output_path = os.path.join("PyPoll.csv")

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['...................................'])
    csvwriter.writerow([f'Total Votes: {totalVote}'])
    csvwriter.writerow(['...................................'])
    csvwriter.writerow([f'{canName[0]}: {canPercent[canName[0]]}% ({canDict[canName[0]]})'])
    csvwriter.writerow([f'{canName[1]}: {canPercent[canName[1]]}% ({canDict[canName[1]]})'])
    csvwriter.writerow([f'{canName[2]}: {canPercent[canName[2]]}% ({canDict[canName[2]]})'])
    csvwriter.writerow([f'{canName[3]}: {canPercent[canName[3]]}% ({canDict[canName[3]]})'])
    csvwriter.writerow(['...................................'])
    csvwriter.writerow([f'Winner: {winName}'])
    csvwriter.writerow(['...................................'])
 


        


   
  