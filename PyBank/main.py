import csv 
import os

csvpath = os.path.join("Resources","budget_data.csv")


print("Financial Analysis")
print('----------------------------')

#define variables as integer
rowcount = 0
total = 0
change = 0
totalchange = 0
oldvalue = 0
#create a list to store the change in proft/loss
profit = []
#create a string to store the value of the year of greatest increase in profits
maxyear = ""
#create a string to store the value of the year of greatest decrease in profits
minyear = ""

with open(csvpath, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csv_reader)
    #loop through each row of data after the header
    for row in csv_reader:
        #total number of rows looped equals to the total number of months
        rowcount = rowcount + 1
        #add up the total profit/losses from each row and store the value in the variable total
        total = total + int(row[1])
        #we can only calculate the change starting from the second month
        if oldvalue != 0:
            #calculate the change by subtracting the value of the current month (row) by the value of previous month (row-1)
            change = int(row[1]) - oldvalue
            #add up the changes and store the value in the variable totalchange
            totalchange = (int(row[1]) - oldvalue) + totalchange
            #store each value of change in the list profit
            profit.append(change)
        #define the value of oldvalue as row[1] after looping a row so oldvalue becomes the value of the previous row    
        oldvalue = int(row[1])

oldvalue = 0
#using the max fuction to find the largest value in the list profit, store it as the variable maxprofit
maxprofit = max(profit)
#using the min fuction to find the smallest value in the list profit, store it as the variable minprofit
minprofit = min(profit)
with open(csvpath, newline='') as csvfile: 
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csv_reader)
    for row in csv_reader:
            #looping each row to check if the change in profits equals to the largest value of change stored in maxprofit
            if int(row[1]) - oldvalue == maxprofit:
                #then store the year value on the same row into the string maxyear
                maxyear = row[0]
            #looping each row to check if the change in profits equals to the smallest value of change stored in minprofit
            if int(row[1]) - oldvalue == minprofit:
                #then store the year value on the same row into the string mixyear
                minyear = row[0]
            oldvalue = int(row[1])
    

print(f'Total Months: {rowcount}')
print(f'Total: ${total}')
print(f'Average Change: ${(totalchange/(rowcount-1)):.2f}')
print(f'Greatest Increase in Profits: {maxyear} (${maxprofit})')
print(f'Greatest Decrease in Profits: {minyear} (${minprofit})')

#set variable for output file
output_file = os.path.join("budgetdata.txt")
#open the output file
with open(output_file, 'w') as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write('----------------------------\n')
    text_file.write(f'Total Months: {rowcount}\n')
    text_file.write(f'Total: ${total}\n')
    text_file.write(f'Average Change: ${(totalchange/(rowcount-1)):.2f}\n')
    text_file.write(f'Greatest Increase in Profits: {maxyear} (${maxprofit})\n')
    text_file.write(f'Greatest Decrease in Profits: {minyear} (${minprofit})\n')
text_file.close
    
            
    