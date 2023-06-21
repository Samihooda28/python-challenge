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
    value = int(first_row[1])

    for row in csvreader:

         Dates.append(row[0])
         change = int(row[1])-value
         Profits.append(change)
         value=int(row[1])
         Total_Months += 1

         Total_profit_loss = Total_profit_loss + int(row[1])

         Average_Change = sum(Profits)/len(Profits)

    Greatest_Increase = max(Profits)
    Greatest_Increase_Index = Profits.index(Greatest_Increase)
    Greatest_Increase_Date = Dates[Greatest_Increase_Index]

    Greatest_Decrease = min(Profits)
    Greatest_Decrease_Index = Profits.index(Greatest_Decrease)
    Greatest_Decrease_Date = Dates[Greatest_Decrease_Index]

output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months : {str(Total_Months)}\n"
    f"Total : {str(Total_profit_loss)}\n"
    f"Average Change : ${str(round(Average_Change,2))}\n"
    f"Greatest Increase in Profits : {Greatest_Increase_Date} (${str(Greatest_Increase)})\n"
    f"Greatest Decrease in Profits : {Greatest_Decrease_Date} (${str(Greatest_Decrease)})\n" )

print(output)

output_file =os.path.join('Analysis','output.txt')

pybank_output = open(output_file,"w")

output_txt =[ (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months : {str(Total_Months)}\n"
    f"Total : {str(Total_profit_loss)}\n"
    f"Average Change : ${str(round(Average_Change,2))}\n"
    f"Greatest Increase in Profits : {Greatest_Increase_Date} (${str(Greatest_Increase)})\n"
    f"Greatest Decrease in Profits : {Greatest_Decrease_Date} (${str(Greatest_Decrease)})\n" )]

pybank_output.writelines(output_txt)
pybank_output.close
