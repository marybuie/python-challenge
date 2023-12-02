#import dependencies
import os
import csv

#path to csv
poll_path = os.path.join("Resources", "election_data.csv")

#initializing variables
total_votes = 0
candidates = {}
winner = {'name': '', 'votes': 0}

#calculating total number of votes for each candidate
with open(poll_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)
    for row in csv_reader:
        candidate = row[2]

        total_votes += 1

        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

        #calculate winner
        if candidates[candidate] > winner['votes']:
            winner['name'] = candidate
            winner['votes'] = candidates[candidate]

#calculating percentage of votes cast for each candidate
percentages = {name: (votes / total_votes) * 100 for name, votes in candidates.items()}

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    print(f"{candidate}: {percentages[candidate]:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner['name']}")
print("-------------------------")

#debugging output text file
output_dir = "Analysis"
os.makedirs(output_dir, exist_ok=True)

#creating output text file
output_path = os.path.join("Analysis", "election_results.txt")
with open(output_path, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        output_file.write(f"{candidate}: {percentages[candidate]:.3f}% ({votes})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner['name']}\n")
    output_file.write("-------------------------\n")