# Created by Alliance82
# Created on 01/01/2024
# This is a retirement planning calculator
# This program is not financial advice, this is intended for informational purposes only.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

# Savings
savings_p1 = []
savings_p2 = []

# Loop Values
i = 0
r = 0
compound_savings_p1 = 0
compound_savings_p2 = 0

# Using a range of interest rates to show projections based on reasonable return rates
pre_interest_rate = [0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12, 0.13, 0.14, 0.15]
post_interest_rate = [0.04, 0.05, 0.06, 0.07, 0.08]
income_growth = 0.03
end_age = 100

# Questions that will be asked to the user running the program
# Person 1 Questions
current_age_p1 = int(input("What is Person 1's age: "))
retirement_age_p1 = int(input("What is Person 1's retirment age: "))
start_savings_p1 = int(input("What is Person 1's current retirement savings: "))
income_p1 = int(input("What is Person 1's current income: "))
saving_pct_p1 = float(input("What is the savings rate for person 1 (use a decimal): "))
match_p1 = float(input("What company match percent does Person 1 receive (use a decimal): "))

# Person 2 Questions
current_age_p2 = int(input("What is Person 2's age: "))
retirement_age_p2 = int(input("What is Person 2's retirment age: "))
start_savings_p2 = int(input("What is Person 2's current retirement savings: "))
income_p2 = int(input("What is Person 2's current income: "))
saving_pct_p2 = float(input("What is the savings rate for person 2 (use a decimal): "))
match_p2 = float(input("What company match percent does Person 2 receive (use a decimal): "))

years_before_retire_p1 = retirement_age_p1 - current_age_p1
years_before_retire_p2 = retirement_age_p2 - current_age_p2
# Compound interest calculation A = P (1+r/n)^nt

# Loop for Person 1
age = current_age_p1
while age < end_age:
    
    i = i + 1
    age = current_age_p1 + i
    if age <= retirement_age_p1:
        
        if i == 1:
            savings_p1_float = (start_savings_p1 + income_p1*(saving_pct_p1+match_p1))
        else:
            savings_p1_float = (compound_savings_p1 + income_p1*(saving_pct_p1+match_p1))
        
        #for x in range(len(pre_interest_rate)):
        compound_savings_p1 = savings_p1_float * (1 + pre_interest_rate[4])
        income_p1 = income_p1 * (1 + income_growth)
        if age == retirement_age_p1:
            retirement_income_p1 = income_p1 * (1.00)
            print(f"Person 1's retirement income {retirement_income_p1}")
        else:
            pass
    else:        
        savings_p1_float = (compound_savings_p1 - retirement_income_p1)
        compound_savings_p1 = savings_p1_float * (1 + post_interest_rate[1])
        
    # Storing the persons age and savings
    savings_p1.append((age, round(compound_savings_p1,2)))


# Loop for Person 2
age = current_age_p2
while age < end_age:
    r = r + 1
    age = current_age_p2 + r
    
    if age <= retirement_age_p2:
        if i == 1:
            savings_p2_float = (start_savings_p2 + income_p2*(saving_pct_p2+match_p2))
        else:
            savings_p2_float = (compound_savings_p2 + income_p2*(saving_pct_p2+match_p2))
        
        #for x in range(len(pre_interest_rate)):
        compound_savings_p2 = savings_p2_float * (1 + pre_interest_rate[4])
        income_p2 = income_p2 * (1 + income_growth)
        if age == retirement_age_p2:
            retirement_income_p2 = income_p2 * (1.00)
            print(f"Person 2's retirement income {retirement_income_p2}")
        else:
            pass
    else:        
        savings_p2_float = (compound_savings_p2 - retirement_income_p2)
        compound_savings_p1 = savings_p2_float * (1 + post_interest_rate[1])
    
    # Storing the persons age and savings
    savings_p2.append((age, round(compound_savings_p2,2)))

total_savings = [(x[0], x[1] + y[1]) for x, y in zip(savings_p1, savings_p2)]
#total_at_retire = compound_savings_p1 + compound_savings_p2






# Create a DataFrame to plot
df = pd.DataFrame(total_savings, columns=['age', 'savings'])


total_income = df = pd.DataFrame(total_savings, columns=['age', 'savings'])
# Amount you are making at retirement
retirement_income = (.8) * total_income

# Outputting information to the user
print(f"At retirement Person 1 was making {retirement_income_p1} and Person 2 was making {retirement_income_p2} for a total of: {total_income}.")
print(f"In retirement most people spend 80% of pre-retirement income, so plan to withdraw: {retirement_income}.")
print(f"This is your total income: {total_income}.")




# Define the variables
total_at_retire = df.query(f'age == {retirement_age_p1}')['savings'].iloc[0]
print(f"At retirement age {retirement_age_p1}, you will have a total of: {total_at_retire}") 

# P: principal amount at retirement
# W: Max yearly withdrawl amount in retirement
# r: annual interest rate
# n: number of years
# t: number of times the interest is compounded per year
t = 1
P = total_at_retire
r = post_interest_rate[1] # annual interest rate
n = end_age - retirement_age_p1 # number of compounding periods per year

# Calculate the withdrawal amount
W = round(((((1+r)**n)*(r*P))/((1+r)**n-1)),2)
print(f"The maximum amount that you could withdraw every year to deplete the funds by {end_age} would be {W}")

# Setting the variables to be plotted and plotting the savings against age
x = df['age']
y = df['savings']
plt.plot(x, y, marker='o')
plt.xlabel('Age')
plt.ylabel('Savings')
plt.show()

# Will output to the location the Python file is in
save_file = 'Retirement_Savings_Calculator_Output.xlsx'
df.to_excel(save_file, sheet_name='Savings_Data', index=False)
os.startfile(save_file)
