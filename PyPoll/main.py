"""
Your task is to create a Python script that analyzes the votes and calculates each of the following:

    The total number of votes cast

    A complete list of candidates who received votes

    The percentage of votes each candidate won

    The total number of votes each candidate won

    The winner of the election based on popular vote
"""

import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

total_votes = 0
candidates = []
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley__votes = 0


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    csvheader = next(csvreader)
    
    for row in csvreader:
        total_votes = total_votes + 1
        
        if row[2] not in candidates:
            candidates.append(row[2])

        if row[2] == candidates[0]:
            Khan_votes = Khan_votes + 1
        elif row[2] == candidates[1]:
            Correy_votes = Correy_votes + 1
        elif row[2] == candidates[2]:
            Li_votes = Li_votes + 1
        else: 
            OTooley__votes = OTooley__votes + 1

    Khan_percent = Khan_votes/total_votes
    Correy_percent = Correy_votes/total_votes
    Li_percent = Li_votes/total_votes
    OTooley_percent = OTooley__votes/total_votes

    winner = max(Khan_votes, Correy_votes, Li_votes, OTooley__votes)

    if winner == Khan_votes:
        winner_name = "Khan"
    elif winner == Correy_votes:
        winner_name = "Correy"
    elif winner == Li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley"

print("Election Results")
print("----------------")
print(f"Total Votes: {total_votes}")
print("----------------")
print(f"Khan: {Khan_percent:.3%} ({Khan_votes})")
print(f"Correy: {Correy_percent:.3%} ({Correy_votes})")
print(f"Li: {Li_percent:.3%} ({Li_votes})")
print(f"O'Tooley: {OTooley_percent:.3%} ({OTooley__votes})")
print("----------------")
print(f"Winner: {winner_name}")

output_file = os.path.join("Analysis", "election_data_analysis.text")

with open(output_file, 'w',) as txtfile:
    txtfile.write("Election Results")
    txtfile.write("----------------")
    txtfile.write(f"Total Votes: {total_votes}")
    txtfile.write("----------------")
    txtfile.write(f"Khan: {Khan_percent:.3%} ({Khan_votes})")
    txtfile.write(f"Correy: {Correy_percent:.3%} ({Correy_votes})")
    txtfile.write(f"Li: {Li_percent:.3%} ({Li_votes})")
    txtfile.write(f"O'Tooley: {OTooley_percent:.3%} ({OTooley__votes})")
    txtfile.write("----------------")
    txtfile.write(f"Winner: {winner_name}")