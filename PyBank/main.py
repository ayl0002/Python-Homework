#import resources
import os
import csv

#Read CSV File
csvpath = os.path.join ("resources","budget_data.csv")

with open (csvpath,newline ='') as csvBudget:

    csvreader = csv.reader(csvBudget,delimiter =',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    month_count = 0

    for row in csvreader:
        month_count = month_count + 1
    
print(month_count)





