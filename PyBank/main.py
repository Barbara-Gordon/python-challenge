import os
import csv

months = []

profitloss = 0
changes = []
changevalues = {}
averagechange = 0
changes = []
changevalues = []

bankpath = os.path.join("Resources/budget_data.csv") #Add Resources when moving to VSCode

with open (bankpath, newline ="") as bankcsv:
    bankfile = csv.reader(bankcsv, delimiter = ",")
    
    next(bankfile, None)
    
    for row in bankfile:        
        changevalues.append(int(row[1]))
        months.append(row[0])

for i in range(len(changevalues) -1):
    value = changevalues[i+1] - changevalues[i]
    changes.append((months[i+1],value))
    averagechange += value
    


profitloss = sum(changevalues)
g_increase = max(changes,key=lambda item:item[1])
g_decrease = min(changes,key=lambda item:item[1])

averagechange = format(averagechange/(len(changevalues) -1), '.2f')

outputtext = (f"Financial Analysis \n ---------------------- \nTotal Months: {len(changevalues)} \nTotal: ${profitloss}\nAverage Change: ${averagechange}\nGreatest Increase in Profits: {g_increase[0]} (${g_increase[1]})\nGreatest Decrease in Profits {g_decrease[0]} (${g_decrease[1]})")         


print(outputtext)

output_path = os.path.join("outputfile.txt")

with open(output_path, "w") as textfile:
    textfile.write(outputtext)