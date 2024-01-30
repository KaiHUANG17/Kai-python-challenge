{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "d84a57c4-f98e-4609-86b2-26d9d7c9464e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "----------------------------\n",
      "Total Months : 86\n",
      "Net Total: $22564198\n",
      "Average Change: $-8311.11\n",
      "Greatest Increase in Profits : Aug-16 ($1862002)\n",
      "Greatest Decrease in Profits : Feb-14 ($-1825558)\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import csv\n",
    "\n",
    "# Initialize variables to store financial analysis results\n",
    "total_months = 0\n",
    "net_amounts = 0\n",
    "previous_profit_change = 0\n",
    "total_changes = []\n",
    "dates = []\n",
    "\n",
    "#path\n",
    "pybank_path = os.path.join(\"..\",\"Resources\",\"budget_data.csv\")\n",
    "\n",
    "#read path\n",
    "with open(pybank_path, 'r') as csvfile:\n",
    "    pybank_reader = csv.reader(csvfile, delimiter = ',')\n",
    "    #skip header row\n",
    "    next(pybank_reader)\n",
    "    \n",
    "    for i in pybank_reader :\n",
    "        date = i[0]\n",
    "        profit_loss = int(i[1])\n",
    "\n",
    "        #calculate total number and net \n",
    "        total_months += 1\n",
    "        net_amounts += int(i[1])\n",
    "\n",
    "        #calculate change\n",
    "        if total_months > 1:\n",
    "            change = profit_loss - previous_profit_change\n",
    "            total_changes.append(change)\n",
    "            dates.append(date)\n",
    "\n",
    "        previous_profit_change = profit_loss\n",
    "\n",
    "#calculate average\n",
    "average_change = sum(total_changes)/(total_months - 1)\n",
    "\n",
    "#find the greatest_increase & greatest_decrease\n",
    "greatest_increase = max(total_changes)\n",
    "greatest_decrease = min(total_changes)\n",
    "\n",
    "#find dates\n",
    "index_greatest_increase = total_changes.index(greatest_increase)\n",
    "index_greatest_decrease = total_changes.index(greatest_decrease)\n",
    "\n",
    "date_greatest_increase = dates[index_greatest_increase]\n",
    "date_greatest_decrease = dates[index_greatest_decrease]\n",
    "\n",
    "#print thr analysis to the terminal\n",
    "print(\"Financial Analysis\")\n",
    "print(\"----------------------------\")\n",
    "print(f\"Total Months : {total_months}\")\n",
    "print(f\"Net Total: ${net_amounts}\")\n",
    "print(f\"Average Change: ${average_change:.2f}\")\n",
    "print(f\"Greatest Increase in Profits : {date_greatest_increase} (${greatest_increase})\")\n",
    "print(f\"Greatest Decrease in Profits : {date_greatest_decrease} (${greatest_decrease})\")\n",
    "\n",
    "#set new file\n",
    "output_file_path = 'financial_analysis.txt'\n",
    "\n",
    "with open(output_file_path, 'w')as output_file:\n",
    "    output_file.write(\"Financial Analysis\\n\")\n",
    "    output_file.write(\"------------------\\n\")\n",
    "    output_file.write(f\"Total Months: {total_months}\\n\")\n",
    "    output_file.write(f\"Net Total: ${net_amounts}\\n\")\n",
    "    output_file.write(f\"Average Change: ${average_change:.2f}\\n\")\n",
    "    output_file.write(f\"Greatest Increase in Profits: {date_greatest_increase} (${greatest_increase})\\n\")\n",
    "    output_file.write(f\"Greatest Decrease in Profits: {date_greatest_decrease} (${greatest_decrease})\\n\")\n",
    "\n",
    "\n",
    "        \n",
    "            \n",
    "\n",
    "        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9346b2ce-0b3c-4130-8050-5fa0d2ca2ae0",
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
