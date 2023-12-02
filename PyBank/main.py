#import
import os
import csv

#path to csv
budget_path = os.path.join("Resources", "budget_data.csv")

#initialize variables
total_months = 0
net_total = 0
previous_profit = 0
profit_changes = []
greatest_increase = {'date': '', 'amount': float('-inf')}
greatest_decrease = {'date': '', 'amount': float('inf')}

#for loop that calculates net total, greatest increase, greatest decrease
with open(budget_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    for row in csv_reader:
        date = row[0]
        profit = int(row[1])
        net_total += profit

        change = profit - previous_profit
        profit_changes.append(change)

        if change > greatest_increase['amount']:
            greatest_increase['date'] = date
            greatest_increase['amount'] = change
        if change < greatest_decrease['amount']:
            greatest_decrease['date'] = date
            greatest_decrease['amount'] = change

        previous_profit = profit
        total_months += 1

#calculate average change
average_change = sum(profit_changes) / (total_months - 1)

#print results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

#debug output text file
output_dir = "Analysis"
os.makedirs(output_dir, exist_ok=True)

#create output text file
output_path = os.path.join("Analysis", "financial_analysis.txt")
with open(output_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")