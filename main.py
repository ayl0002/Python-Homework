#import resources
import os
import csv

#Read CSV File
csvpath = os.path.join ("PyBank/Resources/budget_data.csv")

with open (csvpath,newline ='') as csvBudget:

    csvreader = csv.reader(csvBudget,delimiter =',')

    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    month_count = 0
    revenue_total = 0
    Great_Increase = 0
    Great_Inc_Date = str('Jan-1900')
    Great_Decrease = 900
    Great_Dec_Date = str('Jan-1900')
   

   #read row by row and check for variable increase / decreases 
    for row in csvreader:
        month_count = month_count + 1
        revenue_total +=int(row[1])
        if float(row[1]) > Great_Increase:
            Great_Increase = float(row[1])    
            Great_Inc_Date = str(row[0])
        if float(row[1]) < Great_Decrease:
            Great_Decrease = float(row[1])    
            Great_Dec_Date = str(row[0])
        elif float(row[1]) == Great_Decrease:
            Great_Decrease = float(row[1])    
            Great_Dec_Date = str(row[0])
        

        

        #print(row)
       
print('Financial Analysis')
print('........................................................................')
print(f'Total Months: {month_count}')
print(f'Total: {revenue_total}')
print(f'Average Change: '+ str(round(revenue_total/month_count,2)))
print(f'Greatest Increase in Profits: {Great_Inc_Date}  (${Great_Increase})')
print(f'Greatest Descrease in Profits: {Great_Dec_Date} (${Great_Decrease})')

output_path = os.path.join("PyBank","PyBank.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['.....................'])
    csvwriter.writerow([f'Total Months: {str(month_count)}'])
    csvwriter.writerow([f'Greatest Increase in Profits: {Great_Inc_Date}  (${Great_Increase})'])
    csvwriter.writerow([f'Greatest Descrease in Profits: {Great_Dec_Date} (${Great_Decrease})'])







