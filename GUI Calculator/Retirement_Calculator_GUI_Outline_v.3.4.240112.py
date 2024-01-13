# Created By Alliance82
# Updated On 1/7/2024
# The GUI has been partially updated to incorporated functionality capturing the user inputs and calcualting
# This is a basic form that will be used as the GUI outline for a retirement calculator
# Tkinter is used as the framework for this GUI interface
# This is just a base form that is being updated to have the retirement savings calculator integrated into
import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

compound_savings = 0
savings = []
savings_test = []

class BeforeRetire:
    
    def save_progress():
        response = messagebox.askyesno("Confirmation", "Do you want to continue with the calculation?")
        if response:
            print("Continuing entering investments")
            cont = 'continue'
            
        else:
            print("Done Calculating.")
            cont = 'stop'
            
        return cont    
    
    def clear_form():
        entries = [entry1, entry2, entry3, entry4, entry5, entry6, entry7]
        for entry in entries:
            entry.delete(0, tk.END)

    def calc_invest():
        i = 0
        r = 0
        inv_nam = i_nam.get() # Unused currently, will be used as an identifier once this is dynamic
        current_age = float(c_age.get())
        retirement_age = float(r_age.get())
        start_savings = float(c_sav.get())
        income = float(c_inc.get())
        saving_pct = float(sav_rt.get())
        match = float(c_mat.get())
        
        # Using a range of interest rates to show projections based on reasonable return rates
        pre_interest_rate = [0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12, 0.13, 0.14, 0.15]
        post_interest_rate = [0.04, 0.05, 0.06, 0.07, 0.08]
        income_growth = 0.03
        end_age = 100

        # Loop for Person 1
        age = current_age
        while age < end_age:
            
            i = i + 1
            age = current_age + i
            if age <= retirement_age:
                
                if i == 1:
                    savings__float = (start_savings + income*(saving_pct+match))
                else:
                    savings__float = (compound_savings + income*(saving_pct+match))
                
                #for x in range(len(pre_interest_rate)):
                compound_savings = savings__float * (1 + pre_interest_rate[2])
                income = income * (1 + income_growth)
                
                if age == retirement_age:
                    if (compound_savings - income) > 0:
                        retirement_income = income * (1.00)
                        print(f"Total retirement income: {retirement_income}")
                        
                elif age == end_age:
                    # Reset the variables for the next loop
                    income = 0
                    compound_savings = 0
                    savings__float = 0
                    
                else:
                    pass
                
            else:
                if (compound_savings - retirement_income) > 0:
                    savings__float = (compound_savings - retirement_income)
                    compound_savings = savings__float * (1 + post_interest_rate[1])
                else:
                    retirement_income = compound_savings
                    savings__float = (compound_savings - retirement_income)
                    compound_savings = savings__float * (1 + post_interest_rate[1])  
                
            # Storing the persons age and savings
            savings.append((age, round(compound_savings,2)))
            savings_test.append((inv_nam, age, round(compound_savings,2)))
            print(savings_test)
        # NEED TO UPDATE THE BELOW WHEN Loop is complete
        #total_savings = [(x[0], x[1]) for x in zip(savings_)]
        total_savings = savings

        # Create a DataFrame to plot
        df = pd.DataFrame(total_savings, columns=['age', 'savings'])
        # Info
        #print(df.info())
        # Describe
        #print(df.describe())
        
        df = df.groupby(['age'])['savings'].sum().reset_index()
        #print(df)
        total_income = pd.DataFrame(total_savings, columns=['age', 'savings'])
        # Amount you are making at retirement
        retirement_income = (.8) * total_income

        # Outputting information to the user
        #print(f"At retirement Person 1 was making {retirement_income}.")
        #print(f"In retirement most people spend 80% of pre-retirement income, so plan to withdraw: {retirement_income}.")
        #print(f"This is your total income: {total_income}.")

        # Define the variables
        total_at_retire = df.query(f'age == {retirement_age}')['savings'].iloc[0]
        #print(f"At retirement age {retirement_age}, you will have a total of: {total_at_retire}") 
       
        t = 1 # t: number of times the interest is compounded per year
        P = total_at_retire # P: principal amount at retirement
        r = post_interest_rate[1] # annual interest rate
        n = end_age - retirement_age # number of compounding periods per year

        # Calculate the max withdrawal amount
        W = round(((((1+r)**n)*(r*P))/((1+r)**n-1)),2)
        print(f"The maximum amount that you could withdraw every year to deplete the funds by {end_age} would be {W}")
        return df

    def plot_sav(df):
        # Setting the variables to be plotted and plotting the savings against age
        x = df['age']
        y = df['savings']
        plt.plot(x, y, marker='o')
        plt.xlabel('Age')
        plt.ylabel('Savings')
        plt.show()

    def output_excel(df, cont):
        # Output the Excel file when the user no longer wants to enter more investment information
        print(cont)
        if cont == 'stop':
            # Will output to the location the Python file is in
            save_file = 'Retirement_Savings_Calculator_Output.xlsx'
            df.to_excel(save_file, sheet_name='Savings_Data', index=False)
            os.startfile(save_file)
            
    def call_all():
        # Calling the calculation, passing the DataFrame, then clearing the form
        df_result = BeforeRetire.calc_invest()
        BeforeRetire.plot_sav(df_result)
        cont = BeforeRetire.save_progress()
        BeforeRetire.clear_form()
        BeforeRetire.output_excel(df_result, cont)

window = tk.Tk()
window.title("Investment Calculator")
# Set the window state to 'zoomed' for full screen
window.wm_state('zoomed')

# This will store each of the variables
inv_list = []

# Creating the form with labels and entry boxes. Creating the variables for the user entry.
label1 = ttk.Label(window, text="Investment Name")
label1.grid(row=1, column=0, pady=10)

i_nam = tk.StringVar()
entry1 = ttk.Entry(window, textvariable=i_nam)
entry1.grid(row=1, column=2, pady=10)

label2 = ttk.Label(window, text="Current Age")
label2.grid(row=2, column=0, pady=10)

c_age = tk.StringVar()
entry2 = ttk.Entry(window, textvariable=c_age)
entry2.grid(row=2, column=2, pady=10)

label3 = ttk.Label(window, text="Retirement Age")
label3.grid(row=3, column=0, pady=10)

r_age = tk.StringVar()
entry3 = ttk.Entry(window, textvariable=r_age)
entry3.grid(row=3, column=2, pady=10)

label4 = ttk.Label(window, text="Current Savings")
label4.grid(row=4, column=0, pady=10)

c_sav = tk.StringVar()
entry4 = ttk.Entry(window, textvariable=c_sav)
entry4.grid(row=4, column=2, pady=10)

label5 = ttk.Label(window, text="Curremt Income")
label5.grid(row=5, column=0, pady=10)

c_inc = tk.StringVar()
entry5 = ttk.Entry(window, textvariable=c_inc)
entry5.grid(row=5, column=2, pady=10)

label6 = ttk.Label(window, text="Savings Rate")
label6.grid(row=6, column=0, pady=10)

sav_rt = tk.StringVar()
entry6 = ttk.Entry(window, textvariable=sav_rt)
entry6.grid(row=6, column=2, pady=10)

label7 = ttk.Label(window, text="Company Match")
label7.grid(row=7, column=0, pady=10)

c_mat = tk.StringVar()
entry7 = ttk.Entry(window, textvariable=c_mat)
entry7.grid(row=7, column=2, pady=10)

my_app_instance = BeforeRetire()

btn_convert = tk.Button(
    master=window,
    text="Calculate",
    command=BeforeRetire.call_all
)
btn_convert.grid(column=9, row=9)

window.mainloop()