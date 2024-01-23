# Kai-python-challenge

In this Challenge, I created two Python scripts to analyse the financial records of the company and helping a small, rural U.S. town modernise its vote-counting process.

## Table of Contents

- Paybank challenge
- Paypoll challenge


## Description

### Paybank
- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period

### Paypoll
- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won

## Reference
- date_greatest_increase = dates[index_greatest_increase]
date_greatest_decrease = dates[index_greatest_decrease]
https://chat.openai.com/c/c29a6b0a-b978-4a55-b36f-2cb0893b672f

- with open(output_file_path, 'w')as output_file:
    output_file.write('Election Results\n')
    output_file.write('--------------------------\n')
    output_file.write(f'Total Votes : {total_vote_number}\n')
    output_file.write(f'--------------------------\n')
