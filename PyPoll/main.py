# Author: Benoit Chamot
# Version: 1.0 (submission, revision)
# Date: 19 June 2023
#
# Description of process:
# - read the entire input CSV file
# - for each row, add vote count (one line = one vote) to candidate
# - for each candidate, calculate % of vote = # vote / total votes
# - select the candidate with higher % of vote as winner
# - print output on termainal and to file Analysis/vote_results.txt

# Import all necessary modules
import os
import csv

# Navigate to election data CSV file
csvpath = os.path.join('Resources','election_data.csv')

# Open CSV file for read with UTF-8 encoding
with open(csvpath, 'r', encoding = 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Save header to a variable
    csv_header = next(csvreader)

    # Variables used for the analysis
    total_votes = 0     # Total number of votes
    candidates = []     # List of all candidates (no duplicate)
    votes = {}     # Dictionaries of votes, format: "Candidate": votes (int)

    # Loop through the CSV file to collect data
    for row in csvreader:
        # Add 1 vote to the vote counter (total number of votes)
        total_votes += 1

        # Get the candidate name
        # If it is not already in the list, ...
        if row[2] not in candidates:
            # ... then add their name to the list of candidates 
            candidates.append(row[2])

            # ... then create a new key in the votes dictionary and count one vote
            votes[row[2]] = 1

        # Else (if the candidate is already in the list) ...
        else:
            # ... then add one count to their name (key)
            votes[row[2]] += 1

# Get results and save to strings to be printed
max_vote = 0        # Index 
results_line = []

results_line.append('Election Results')
results_line.append('----------------------------')
results_line.append(f"Total Votes: {total_votes}")
results_line.append('----------------------------')

for candidate in candidates:
    # Loop through candidates to get the percent of vote...
    percent_vote = 100*votes[candidate]/total_votes
    results_line.append(f"{candidate}: {percent_vote:.3f}% ({votes[candidate]} votes)")

    # ... and get the max number of votes
    if votes[candidate] > max_vote:
        max_vote = votes[candidate]
        winner = candidate

results_line.append('----------------------------')
results_line.append(f"Winner: {winner}")
results_line.append('----------------------------')

# Print to terminal
print() # Print empty line for clarity in the terminal
for line in results_line:
    print(line)

# Print to file
filepath = os.path.join('Analysis','election_results.txt')

with open(filepath,'w') as filename:
    for line in results_line:
        filename.write(line + '\n')
print()
print(f"File saved: {filepath}")
    