"""
Your task is to create a Python script that analyzes the records to calculate each of the following:

    The total number of months included in the dataset

    The net total amount of "Profit/Losses" over the entire period

    Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

    The greatest increase in profits (date and amount) over the entire period

    The greatest decrease in profits (date and amount) over the entire period
"""

import os
import csv

# designate resource file path
csvpath = os.path.join("Resources", "budget_data.csv")

# initialize variables & create lists
total_months = 0
total_profit = 0
profit_changes = []
months_count = []
greates_increase_profit = 0
greatest_increse_month = 0
greatest_decrease_profit = 0
greatest_decrease_month = 0

print("Financial Analysis")
print("------------------")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")

    csvheader = next(csvreader)
    row = next(csvreader)
    
    previous_row = int(row[1])
    
    # loop through rows to calculate values for anlysis
    for row in csvreader:
        total_months = total_months + 1

        total_profit = total_profit + int(row[1])

        profit_change = int(row[1]) - previous_row
        profit_changes.append(profit_change)
        previous_row = int(row[1])
        months_count.append(row[0])

        if int(row[1]) > greates_increase_profit:
            greates_increase_profit = int(row[1])
            greatest_increse_month = row[0]

        if int(row[1]) < greatest_decrease_profit:
            greatest_decrease_profit = int(row[1])
            greatest_decrease_month = row[0]
    
    average_change = sum(profit_changes)/len(profit_changes)

    highest = max(profit_changes)
    lowest = min(profit_changes)

    # print analysis
    print(f"Total Months: {total_months}") 
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increse_month}, (${highest})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month}, (${lowest})")

# export analysis to text fie
output_file = os.path.join("Analysis", "budget_data_analysis.text")

with open(output_file, 'w',) as txtfile:
    txtfile.write("Financial Analysis")
    txtfile.write("------------------")
    txtfile.write(f"Total Months: {total_months}")
    txtfile.write(f"Total: ${total_profit}")
    txtfile.write(f"Average Change: ${average_change:.2f}")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increse_month}, (${highest})")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month}, (${lowest})")