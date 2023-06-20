import os
import csv

data_path=os.path.join('Resources','budget_data.csv')

Total_Months = 0
Total_profit_loss = 0
value = 0
change = 0
 
Dates = []
Profits =[]

with open(data_path, newline="") as budget_file:
    csvreader = csv.reader(budget_file, delimiter = ",")
    csv_header = next(csvreader)

    first_row= next(csvreader)

    Total_Months += 1

    Total_profit_loss += int(first_row[1])
    value = int(first_row(1))

for row in csvreader:

    dates.append(row[0])
    
        