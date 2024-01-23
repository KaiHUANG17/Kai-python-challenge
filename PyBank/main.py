<<<<<<< HEAD
#!/usr/bin/env python
# coding: utf-8

# In[51]:


import os
import csv

# Initialize variables to store financial analysis results
total_months = 0
net_amounts = 0
previous_profit_change = 0
total_changes = []
dates = []

#path
pybank_path = os.path.join("..","Resources","budget_data.csv")

#read path
with open(pybank_path, 'r') as csvfile:
    pybank_reader = csv.reader(csvfile, delimiter = ',')
    #skip header row
    next(pybank_reader)
    
    for i in pybank_reader :
        date = i[0]
        profit_loss = int(i[1])

        #calculate total number and net 
        total_months += 1
        net_amounts += int(i[1])

        #calculate change
        if total_months > 1:
            change = profit_loss - previous_profit_change
            total_changes.append(change)
            dates.append(date)

        previous_profit_change = profit_loss

#calculate average
average_change = sum(total_changes)/(total_months - 1)

#find the greatest_increase & greatest_decrease
greatest_increase = max(total_changes)
greatest_decrease = min(total_changes)

#find dates
index_greatest_increase = total_changes.index(greatest_increase)
index_greatest_decrease = total_changes.index(greatest_decrease)

date_greatest_increase = dates[index_greatest_increase]
date_greatest_decrease = dates[index_greatest_decrease]

#print thr analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months : {total_months}")
print(f"Net Total: ${net_amounts}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits : {date_greatest_increase} (${greatest_increase})")
print(f"Greatest Decrease in Profits : {date_greatest_decrease} (${greatest_decrease})")

#set new file
output_file_path = 'financial_analysis.txt'

with open(output_file_path, 'w')as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Net Total: ${net_amounts}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {date_greatest_increase} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {date_greatest_decrease} (${greatest_decrease})\n")


        
            

        


# In[ ]:




=======
import os
import csv

# Initialize variables to store financial analysis results
total_months = 0
net_amounts = 0
previous_profit_change = 0
total_changes = []
dates = []

#path
pybank_path = os.path.join("..","Resources","budget_data.csv")

#read path
with open(pybank_path, 'r') as csvfile:
    pybank_reader = csv.reader(csvfile, delimiter = ',')
    #skip header row
    next(pybank_reader)
    
    for i in pybank_reader :
        date = i[0]
        profit_loss = int(i[1])

        #calculate total number and net 
        total_months += 1
        net_amounts += int(i[1])

        #calculate change
        if total_months > 1:
            change = profit_loss - previous_profit_change
            total_changes.append(change)
            dates.append(date)

        previous_profit_change = profit_loss

#calculate average
average_change = sum(total_changes)/(total_months - 1)

#find the greatest_increase & greatest_decrease
greatest_increase = max(total_changes)
greatest_decrease = min(total_changes)

#find dates
index_greatest_increase = total_changes.index(greatest_increase)
index_greatest_decrease = total_changes.index(greatest_decrease)

date_greatest_increase = dates[index_greatest_increase]
date_greatest_decrease = dates[index_greatest_decrease]

#print thr analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months : {total_months}")
print(f"Net Total: ${net_amounts}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits : {date_greatest_increase} (${greatest_increase})")
print(f"Greatest Decrease in Profits : {date_greatest_decrease} (${greatest_decrease})")

#set new file
output_file_path = 'financial_analysis.txt'

with open(output_file_path, 'w')as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Net Total: ${net_amounts}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {date_greatest_increase} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {date_greatest_decrease} (${greatest_decrease})\n")
>>>>>>> origin/main
