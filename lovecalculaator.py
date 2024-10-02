# import tkinter
from tkinter import *
import random

# Creating GUI window
root = Tk()
# Defining the container size, width=400, height=240
root.geometry('400x240')
# Title of the container
root.title('Love Calculator 💖')

# Function to calculate love percentage between the user and partner
def calculate_love():
    # Get the values from the input fields
    user_name = name1.get()
    partner_name = name2.get()
    
    # Check if any slot is empty
    if not user_name or not partner_name:
        # Show an error message if any field is empty
        error_message = "Please enter both your name and your partner's name."
        result.config(text=error_message, fg='red')  # Red text for error
        return  # Exit the function if validation fails
    
    # value will contain digits between 0-9
    st = '0123456789'
    # result will be in double digits
    digit = 2
    temp = "".join(random.sample(st, digit))
    result.config(text=f'Love Percentage: {temp}%', fg='blue')  # Blue text for result

# Setting a colorful background
root.configure(bg='lightyellow')

# Heading on Top
heading = Label(root, text='Love Calculator - How much is he/she into you', bg='lightyellow', fg='purple', font=('Arial', 12, 'bold'))
heading.pack(pady=10)

# Slot/input for the first name
slot1 = Label(root, text="Enter Your Name:", bg='lightyellow', fg='black')
slot1.pack()
name1 = Entry(root, border=5, bg='white', fg='black')
name1.pack(pady=5)

# Slot/input for the partner name
slot2 = Label(root, text="Enter Your Partner Name:", bg='lightyellow', fg='black')
slot2.pack()
name2 = Entry(root, border=5, bg='white', fg='black')
name2.pack(pady=5)

# Button to calculate
bt = Button(root, text="Calculate", height=1, width=7, command=calculate_love, bg='lightblue', fg='black', font=('Arial', 10, 'bold'))
bt.pack(pady=10)

# Text on result slot
result = Label(root, text='Love Percentage between both of You:', bg='lightyellow', fg='green', font=('Arial', 10))
result.pack(pady=10)

# Starting the GUI
root.mainloop()
