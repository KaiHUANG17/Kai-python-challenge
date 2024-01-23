import os
import csv

# set path
pypoll_path = os.path.join('..','Resources','election_data.csv')

# Intialization values for store
total_vote_number = 0
candidates = []
candidates_set = set()
percentage_of_won_Charles = 0
percent_of_won_Diana = 0
percent_of_won_Anthony = 0
candidate_Charles_votes = 0
candidate_Diana_votes = 0
candidate_Anthony_votes = 0
vote_data =[]

# read file
with open(pypoll_path, 'r') as csvfile:
    pypoll_reader = csv.reader(csvfile, delimiter=',')
    next(pypoll_reader)

    next_candidate = 0
    
#loop
    for i in pypoll_reader :
        total_vote_number += 1

        previous_candidate = i[2]

        if next_candidate != previous_candidate:
             candidates_set.add(previous_candidate)

        next_candidate = previous_candidate
        vote_data.append(i)

    candidates_set.add(previous_candidate)
    candidates = list(candidates_set)

        

# find total numbers of votes

for i in vote_data:
    if i[2] == 'Charles Casper Stockham':
        candidate_Charles_votes += 1
    elif i[2] == 'Diana DeGette':
        candidate_Diana_votes += 1
    else:
        candidate_Anthony_votes += 1

# percentage
percent_of_won_Charles = (candidate_Charles_votes / total_vote_number)*100
percent_of_won_Diana = (candidate_Diana_votes / total_vote_number)*100
percent_of_won_Anthony = (candidate_Anthony_votes / total_vote_number)*100

# find name
winner = max(candidate_Charles_votes, candidate_Diana_votes, candidate_Anthony_votes)

if winner == candidate_Charles_votes:
    winner_name = 'Charles Casper Stockham'

elif winner == candidate_Diana_votes:
    winner_name = 'Diana DeGette'

else:
    winner_name = 'Raymon Anthony Doane'

#print on terminal
print(f'Election Results')
print(f'--------------------------')
print(f'Total Votes : {total_vote_number}')
print(f'--------------------------')
print(f'{candidates[0]} : {percent_of_won_Charles:.3f}% ({candidate_Charles_votes})')
print(f'{candidates[1]} : {percent_of_won_Diana:.3f}% ({candidate_Diana_votes})')
print(f'{candidates[2]} : {percent_of_won_Anthony:.3f}% ({candidate_Anthony_votes})')
print(f'--------------------------')
print(f'Winner : {winner_name}')
print(f'--------------------------')

# make txt
output_file_path = 'election_data.txt'

with open(output_file_path, 'w')as output_file:
    output_file.write('Election Results\n')
    output_file.write('--------------------------\n')
    output_file.write(f'Total Votes : {total_vote_number}\n')
    output_file.write(f'--------------------------\n')
    output_file.write(f'{candidates[0]} : {percent_of_won_Charles:.3f}% ({candidate_Charles_votes})\n')
    output_file.write(f'{candidates[1]} : {percent_of_won_Diana:.3f}% ({candidate_Diana_votes})\n')
    output_file.write(f'{candidates[2]} : {percent_of_won_Anthony:.3f}% ({candidate_Anthony_votes})\n')
    output_file.write(f'--------------------------\n')
    output_file.write(f'Winner : {winner_name}\n')
    output_file.write(f'--------------------------\n')

