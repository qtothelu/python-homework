#Setting up libraries Numpy, Pandas, and Pathlib
Python
import numpy as np
import pandas as pd
from pathlib import Path

#Pulling latest git version 
git pull uw-fintech-spring-21/Homework/02-Python/Instructions/Pybank/resources/budget_data.csv

#Testing directory before beginning homework
pd.read_csv(r'uw-fintech-spring-21/Homework/02-Python/Instructions/Pybank/resources/budget_data.csv')

#Assigning directory to variable
budget_filepath = Path(r'uw-fintech-spring-21/Homework/02-Python/Instructions/Pybank/resources/budget_data.csv')
df = pd.read_csv(budget_filepath)

# The total number of months included in the dataset. Counting all the rows since each row represent a unique month
count_row = df.shape[0]
print(f"Total Months: ",count_row)

# The net total amount of Profit/Losses over the entire period. Specifying the sum of the column title "Profit/Losses"
total_PL = df['Profit/Losses'].sum()
print(f"Total: $",total_PL)

"""
The average of the changes in Profit/Losses over the entire period. Created a second dataframe with the profit/loss data shifted down one row.
Also created third dataframe that subtracts the profit/loss column from data frame 1 from data frame 2. Used varaiable AveragePL to calculate average.
Since there are no prior date in row 1 of the data, I have excluded the first row in the calculation of the average p/l over entire period.
"""
df2=df
df = pd.read_csv(budget_filepath)
df2['Profit/Losses']=df2['Profit/Losses'].shift(1)
df2 = df2.fillna(0)
df2['Profit/Losses']=df["Profit/Losses"]-df2["Profit/Losses"]
AveragePL=df2.iloc[1:86,1].sum()/(count_row-1)
print(f"Average  Change: $",AveragePL.round(2))


"""
The greatest increase in profits (date and amount) over the entire period. Dropped Profit/loss data in dataframe 1 and merged data frame 1 and 3 to show dates along
the average change in p/l data. Specified which column I want the max value in data frame 3. Utilized idxmax function to pull entire row data of the max value data. 
"""
Greatest_Profit = df3.loc[df3['Profit/Losses'].idxmax(())]
int = Greatest_Profit
print(f"Greatest Increase in Profits: $",Greatest_Profit)

#The greatest decrease in losses (date and amount) over the entire period.
Worst_Profit = df3.loc[df3['Profit/Losses'].idxmin(())]
int = Worst_Profit
print(f"Greatest Decrease in Profits: $",Worst_Profit)
