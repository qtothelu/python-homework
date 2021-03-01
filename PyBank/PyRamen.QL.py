import numpy as np
import pandas as pd
from pathlib import Path
git pull uw-fintech-spring-21/Homework/02-Python/Instructions/Pybank/resources/budget_data.csv

#Testing directory
pd.read_csv(r'uw-fintech-spring-21/Homework/02-Python/Instructions/Pybank/resources/budget_data.csv')

budget_filepath = Path(r'uw-fintech-spring-21/Homework/02-Python/Instructions/Pybank/resources/budget_data.csv')

df = pd.read_csv(budget_filepath)

# The total number of months included in the dataset.

count_row = df.shape[0]
print(f"Total Months: ",count_row)

# The net total amount of Profit/Losses over the entire period.

total_PL = df['Profit/Losses'].sum()
print(f"Total: $",total_PL)

#The average of the changes in Profit/Losses over the entire period.

df2=df
df2['Profit/Losses']=df2['Profit/Losses'].shift(1)
df2 = df2.fillna(0)
df = pd.read_csv(budget_filepath)
df3 = df["Profit/Losses"]-df2["Profit/Losses"]
AveragePL=df3.sum[1:86].sum(axis=0)/(count_row-1)
print(f"Average  Change: $",AveragePL.round(2))

#The greatest increase in profits (date and amount) over the entire period.

df.drop('Profit/Losses',inplace=True,axis=1)
date=df["Date"]
df3 = df3.join(date)
Greatest_Profit = df3.loc[df3['Profit/Losses'].idxmax(())]
print(f"Greatest Increase in Profits: ",Greatest_Profit)

#The greatest decrease in losses (date and amount) over the entire period.

Worst_Profit = df3.loc[df3['Profit/Losses'].idxmax(())]
print(f"Greatest Decrease in Profits: ",Worst_Profit)