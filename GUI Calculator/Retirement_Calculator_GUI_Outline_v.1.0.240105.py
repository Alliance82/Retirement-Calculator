# Created By Alliance82
# Created On 1/5/2024
# This is a basic form that will be used as the GUI outline for a retirement calculator
# Tkinter is used as the framework for this GUI interface
# This is just a base form that is being updated to have the retirement savings calculator integrated into
import tkinter as tk
from tkinter import ttk, messagebox

# Class that captures each user entry in a text box and appends all their entries to a dictonairy
def display_entries():
    entry_dict = {label_texts[i]: entry.get() for i, entry in enumerate(entries)}
    entries_list.append(entry_dict)

    paragraph = "\n".join([f"{key}: {value}" for entry_dict in entries_list for key, value in entry_dict.items()])
    result_text.config(height=len(entries_list) + 10)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, paragraph)

    # Ask the user if they want to enter information for another person
    answer = messagebox.askyesno("Another Person", "Do you want to enter information for another person?")
    
    # Resets the form for the user to enter their next savings detail
    if answer:
        reset_form()

# Class to clear out the entries
def reset_form():
    for entry in entries:
        entry.delete(0, tk.END)

# Initiates and names to GUI window
root = tk.Tk()
root.title("Retirement Calculator")

# The list of items the program will iterate through to ask the user questions about their savings
label_texts = [
    "What is the name of this investment:",
    "Current Age:",
    "Retirement Age:",
    "Current Savings:",
    "Current Income:",
    "Savings Rate (use a decimal):",
    "Company Match (use a decimal):"
]

# Defines the entries as lists
# entries is appended with each answer the user types in the text boxes
# entries_list will be appended with an object for each full savings when the user clicks the button 
entries = []
entries_list = []

label = ttk.Label(root, text="This program will calculate your retirement savings based on your below inputs.")
label.grid(row=0, column=1)

# Loops through the label_texts and generates the form of questions and text boxes for the user
for row, label_text in enumerate(label_texts, start=0):
    # Defines the labels and label position, row iterates by 1 for each length of label_text
    label = ttk.Label(root, text=label_text)
    label.grid(row=row+3, column=1, pady=10)
    # Defines the user input boxes, row iterates by 1 for each length of label_text
    entry = ttk.Entry(root)
    entry.grid(row=row+3, column=2, pady=10)
    
    # Appends the entries list with all the user entered values
    entries.append(entry)

# Set the window state to 'zoomed' for full screen
root.wm_state('zoomed')

# Button to display the entered values in a paragraph and ask the user if they want to reset the form
display_button = ttk.Button(root, text="Display Entries", command=display_entries)
display_button.grid(row=len(label_texts) + 5, column=2, columnspan=2, pady=10)

# Displays the entries_list in the text box and resizes the text box for additional entries
result_text = tk.Text(root, wrap="word", height=len(entries_list) + 10, width=40)
result_text.grid(row=len(label_texts) + 5, column=1, columnspan=2, pady=10)

root.mainloop()
