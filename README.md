# python-challenge
Repository for Monash University Bootcamp Module 3

## File structure
### PyBank
Files used for the first part of the assignment

### PyPoll
Files used for the second part of the assignment:
- main.py is the sole python script used to read the CSV file in Resources and output the results in the text file in Analysis
- Resources (dir): folder containing the input CSV file
- Resources/election_data.csv: CSV file as provided with the assignment
- Analysis (dir): folder containing the output TXT files created by the python script (main.py)
- Analysis/election_results.txt: output TXT file (generated py main.py)

## Questions, challenges and solutions
### PyBank

### PyPoll
In PyPoll/main.py, I use a list to store all the candidates names without duplicates. This is used to then check whether a candidate has already been added to the votes dictionary as a key. I could have used a check on votes.items() based on what I could find on Stack Overflow but the code seemed clearer the way I have done it and more logical to me. I'd be interested in knowing whether my solution is optimal or if there is a more elegant way?

To print the percent, I have used code found on Stack Overflow to print only the first two digits after the decimal point, i.e. use ":.2f" with the variable. 

I have decided to save the strings to be printed in the terminal and written in the output file in a list to be able to easily change the way they are printed without having to change the code twice (once for the terminal and once for the file.)