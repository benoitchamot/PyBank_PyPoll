# Author: Benoit Chamot
# Version: 1.0 (submission 1, revision 0)
# Date: 19 June 2023
#
# Description of process:
# - read the entire input CSV file
# - for each row, increase month count (one line = one month)
# - for each row, calculate the change between current and previous month
# - calculate min/max and average of change
# - print output on terminal and to file Analysis/bank_results.txt

# Import all necessary modules
import os
import csv

# Navigate to election data CSV file
csvpath = os.path.join('Resources','budget_data.csv')

# Open CSV file for read with UTF-8 encoding
with open(csvpath, 'r', encoding = 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Save header to a variable
    csv_header = next(csvreader)
    
    # Variables for the analysis
    total_month = 0     # Number of month (counter, number of lines in the file)
    total_amount = 0    # Net total amount of "Profit/Losses" over the entire period
    profitlosses = {}   # Dictionary storing all the changes in profits and losses for further analysis, format: "Month": Change
    first_row = True    # Boolean variable to check whether we are on the first row with data

    for row in csvreader:
        total_month += 1                    # Count number of month (entry)
        total_amount += int(row[1])         # Add up all profits and losses

        if not first_row:
            profitlosses[row[0]] = int(row[1]) - previous_row   # Add profit/loss row to dictionary
        else:
            first_row = False # Skip first row

        # Save previous row for calculation of change
        previous_row = int(row[1])

# Find min and max profit and calculate average
min_change = 0
max_change = 0
avg_change = 0

for month in profitlosses:

    # Assign change for the month to a variable for clarity
    change = profitlosses[month]

    # Accummulate change into a variable
    avg_change += change

    # If the change for this month is greater than the current max change...
    if change > max_change:
        # ... Then save the current month and change to the maximum variables
        max_month = month
        max_change = change
    
    # Or, if the change for this month is lower than the current min change...
    elif change < min_change:
        # ... Then save the current month and change to the minimum variables
        min_month = month
        min_change = change

# Calculate average change by divinding sum of changes by number of month - 1
# (because the change could not be calculated for the first row of Jan-10 since Dec-09 is unknown) 
avg_change = avg_change/(total_month-1)

# Get results and save to strings to be printed
results_line = []

results_line.append("Financial Analysis")
results_line.append("------------------------")
results_line.append(f"Total Months: {total_month}")
results_line.append(f"Total: ${total_amount}")
results_line.append(f"Average Change: ${avg_change:.2f}")
results_line.append(f"Greatest Increase in Profits: {max_month} (${max_change})")
results_line.append(f"Greatest Decrease in Profits: {min_month} (${min_change})")

# Print to terminal
print() # Print empty line for clarity in the terminal
for line in results_line:
    print(line)

# Print to file
filepath = os.path.join('Analysis','bank_results.txt')

with open(filepath,'w') as filename:
    for line in results_line:
        filename.write(line + '\n')

print()  # Print empty line for clarity in the terminal
print(f"File saved: {filepath}")