import os
import csv

data_path=os.path.join('Resources','election_data.csv')

Candidates = []
num_of_votes = []
percenatge_votes = []
Total_votes = 0
 
with open(data_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
    
        Total_votes += 1
        if row[2] not in Candidates:
            Candidates.append(row[2])
            index= Candidates.index(row[2])
            num_of_votes.append(1)

        else:    
             index=Candidates.index(row[2])
             num_of_votes[index] += 1

    for votes in num_of_votes:
         percentage=(votes/Total_votes)*100
         percentage="%.3f%%" % percentage
         percenatge_votes.append(percentage)

    winner=max(num_of_votes)
    index=num_of_votes.index(winner)
    winning_candidate = Candidates[index]

print("Election Results")     
print("---------------------")
print(f"Total Votes : {str(Total_votes)}")
print("---------------------")

for i in range(len(Candidates)):
    print(f"{Candidates[i]}: {str(percenatge_votes[i])} ({str(num_of_votes[i])})")
print("---------------------")
print(f"Winner : {winning_candidate}")
print("---------------------")

output_file =os.path.join('Analysis','output.txt')  

polloutput = open(output_file,"w")
line1 = "Election Results"
line2 = "---------------------"
line3 = str(f"Total Votes : {str(Total_votes)}")
line4 = "---------------------"
polloutput.write('{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4))
for i in range(len(Candidates)):
    line=str(f"{Candidates[i]}: {str(percenatge_votes[i])} ({str(num_of_votes[i])})")
    polloutput.write('{}\n'.format(line))
line5 = "---------------------"
line6 = str(f"Winner : {winning_candidate}")
line7 = "---------------------"
polloutput.write('{}\n{}\n{}\n'.format(line5,line6,line7))
