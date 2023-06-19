# python-challenge
Repository for Monash University Bootcamp Module 3
- Exercise 1: PyBank
- Exercise 2: PyPoll

_Important note:_ Please run both main.py scripts from their own directories (PyRoll and PyBank) or the loading and saving of files may not work.

## File structure
### PyBank
Files used for the first part of the assignment
- main.py is the sole python script used to read the CSV file in Resources and output the results in the text file in Analysis
- Resources (dir): folder containing the input CSV file
- Resources/budget_data.csv: CSV file as provided with the assignment
- Analysis (dir): folder containing the output TXT files created by the python script (main.py)
- Analysis/bank_results.txt: output TXT file (generated py main.py)

### PyPoll
Files used for the second part of the assignment:
- main.py is the sole python script used to read the CSV file in Resources and output the results in the text file in Analysis
- Resources (dir): folder containing the input CSV file
- Resources/election_data.csv: CSV file as provided with the assignment
- Analysis (dir): folder containing the output TXT files created by the python script (main.py)
- Analysis/election_results.txt: output TXT file (generated py main.py)

## Questions, challenges and solutions
### PyBank
I am using a boolean to skip the first row of the profits and losses file to avoid an out-of-range error by substracting a row that doesn't contain data. The change in profit/loss for each line L is calculated like this: Change(L) = Profit(L) - Profit(L-1). Therefore the list of all changes has a length of 1 less than the total number of month since the first month will not have a known value (we cannot calculate the change for Jan-10 without knowing the Dec-09 value). This difference will mean that we need to divide by (number_of_months -1) instead of number_of_months when calculating the average.

I have decided to save the strings to be printed in the terminal and written in the output file in a list to be able to easily change the way they are printed without having to change the code twice (once for the terminal and once for the file.)

### PyPoll
In PyPoll/main.py, I use a list to store all the candidates names without duplicates. This is used to then check whether a candidate has already been added to the votes dictionary as a key. I could have used a check on votes.items() based on what I could find on Stack Overflow but the code seemed clearer the way I have done it and more logical to me. I'd be interested in knowing whether my solution is optimal or if there is a more elegant way?

As for PyBank, I have decided to save the strings to be printed in the terminal and written in the output file in a list to be able to easily change the way they are printed without having to change the code twice (once for the terminal and once for the file.)

As I am using the same code to print the results_line to the terminal and file between PyBank and PyPoll, I could have created a function in an external file (imported as a module) such as print_to_terminal(results_line) or print_to_file(results_line, filename) but it was cleaner to keep both assignments clean and separate without sharing any external custom modules.