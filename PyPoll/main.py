{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "1fa90083-74e5-4bf6-80f8-430fdd41b275",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "--------------------------\n",
      "Total Votes : 369711\n",
      "--------------------------\n",
      "Raymon Anthony Doane : 23.049% (85213)\n",
      "Charles Casper Stockham : 73.812% (272892)\n",
      "Diana DeGette : 3.139% (11606)\n",
      "--------------------------\n",
      "Winner : Diana DeGette\n",
      "--------------------------\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import csv\n",
    "\n",
    "# set path\n",
    "pypoll_path = os.path.join('..','Resources','election_data.csv')\n",
    "\n",
    "# Intialization values for store\n",
    "total_vote_number = 0\n",
    "candidates = []\n",
    "candidates_set = set()\n",
    "percentage_of_won_Charles = 0\n",
    "percent_of_won_Diana = 0\n",
    "percent_of_won_Anthony = 0\n",
    "candidate_Charles_votes = 0\n",
    "candidate_Diana_votes = 0\n",
    "candidate_Anthony_votes = 0\n",
    "vote_data =[]\n",
    "\n",
    "# read file\n",
    "with open(pypoll_path, 'r') as csvfile:\n",
    "    pypoll_reader = csv.reader(csvfile, delimiter=',')\n",
    "    next(pypoll_reader)\n",
    "\n",
    "    next_candidate = 0\n",
    "    \n",
    "#loop\n",
    "    for i in pypoll_reader :\n",
    "        total_vote_number += 1\n",
    "\n",
    "        previous_candidate = i[2]\n",
    "\n",
    "        if next_candidate != previous_candidate:\n",
    "             candidates_set.add(previous_candidate)\n",
    "\n",
    "        next_candidate = previous_candidate\n",
    "        vote_data.append(i)\n",
    "\n",
    "    candidates_set.add(previous_candidate)\n",
    "    candidates = list(candidates_set)\n",
    "\n",
    "        \n",
    "\n",
    "# find total numbers of votes\n",
    "\n",
    "for i in vote_data:\n",
    "    if i[2] == 'Charles Casper Stockham':\n",
    "        candidate_Charles_votes += 1\n",
    "    elif i[2] == 'Diana DeGette':\n",
    "        candidate_Diana_votes += 1\n",
    "    else:\n",
    "        candidate_Anthony_votes += 1\n",
    "\n",
    "# percentage\n",
    "percent_of_won_Charles = (candidate_Charles_votes / total_vote_number)*100\n",
    "percent_of_won_Diana = (candidate_Diana_votes / total_vote_number)*100\n",
    "percent_of_won_Anthony = (candidate_Anthony_votes / total_vote_number)*100\n",
    "\n",
    "# find name\n",
    "winner = max(candidate_Charles_votes, candidate_Diana_votes, candidate_Anthony_votes)\n",
    "\n",
    "if winner == candidate_Charles_votes:\n",
    "    winner_name = 'Charles Casper Stockham'\n",
    "\n",
    "elif winner == candidate_Diana_votes:\n",
    "    winner_name = 'Diana DeGette'\n",
    "\n",
    "else:\n",
    "    winner_name = 'Raymon Anthony Doane'\n",
    "\n",
    "#print on terminal\n",
    "print(f'Election Results')\n",
    "print(f'--------------------------')\n",
    "print(f'Total Votes : {total_vote_number}')\n",
    "print(f'--------------------------')\n",
    "print(f'{candidates[0]} : {percent_of_won_Charles:.3f}% ({candidate_Charles_votes})')\n",
    "print(f'{candidates[1]} : {percent_of_won_Diana:.3f}% ({candidate_Diana_votes})')\n",
    "print(f'{candidates[2]} : {percent_of_won_Anthony:.3f}% ({candidate_Anthony_votes})')\n",
    "print(f'--------------------------')\n",
    "print(f'Winner : {winner_name}')\n",
    "print(f'--------------------------')\n",
    "\n",
    "# make txt\n",
    "output_file_path = 'election_data.txt'\n",
    "\n",
    "with open(output_file_path, 'w')as output_file:\n",
    "    output_file.write('Election Results\\n')\n",
    "    output_file.write('--------------------------\\n')\n",
    "    output_file.write(f'Total Votes : {total_vote_number}\\n')\n",
    "    output_file.write(f'--------------------------\\n')\n",
    "    output_file.write(f'{candidates[0]} : {percent_of_won_Charles:.3f}% ({candidate_Charles_votes})\\n')\n",
    "    output_file.write(f'{candidates[1]} : {percent_of_won_Diana:.3f}% ({candidate_Diana_votes})\\n')\n",
    "    output_file.write(f'{candidates[2]} : {percent_of_won_Anthony:.3f}% ({candidate_Anthony_votes})\\n')\n",
    "    output_file.write(f'--------------------------\\n')\n",
    "    output_file.write(f'Winner : {winner_name}\\n')\n",
    "    output_file.write(f'--------------------------\\n')\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ab028900-3abb-4187-9d4d-bf4829ccb0ba",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "369711"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "total_vote_number"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "98c1179c-452b-49ea-b4d7-ea346c96d300",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Raymon Anthony Doane', 'Charles Casper Stockham', 'Diana DeGette']"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "candidates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "d549c5e9-ca84-45a7-952b-15c71de99e99",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "272892"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "candidate_Diana_votes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "2662212f-d5bc-4578-a2f0-87d94ccf39fd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11606"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "candidate_Anthony_votes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "d0d9975f-c567-43ce-92ff-d20eed123770",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "85213"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "candidate_Charles_votes "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "225e368b-c32a-4bf3-8b38-12946b89ac7c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "23.04854332167558"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "percent_of_won_Charles"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "7819e786-4568-4dbf-bc89-0058ff7ef23e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "73.81224794501652"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "percent_of_won_Diana"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "23b19c03-9159-4ec3-8754-2823d9397794",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "272892"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "winner"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "2f26f614-e14e-4462-83c2-343551e181ce",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Diana DeGette'"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "winner_name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "451b4dee-eff5-4bad-a4de-e5f45c21f9f7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
