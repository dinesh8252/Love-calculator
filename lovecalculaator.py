# import tkinter
from tkinter import *
# import random module
import random
# Creating GUI window
root = Tk()
# Defining the container size, width=400, height=240
root.geometry('400x240')
# Title of the container
root.title('Love Calculator????')

# Function to calculate love percentage
# between the user and partner
def calculate_love():
    # Get the values from the input fields
    user_name = name1.get()
    partner_name = name2.get()
    
    # Check if any slot is empty
    if not user_name or not partner_name:
        # Show an error message if any field is empty
        error_message = "Please enter both your name and your partner's name."
        result.config(text=error_message)
        return  # Exit the function if validation fails
    
    # value will contain digits between 0-9
    st = '0123456789'
    # result will be in double digits
    digit = 2
    temp = "".join(random.sample(st, digit))
    result.config(text=temp)

# Heading on Top
heading = Label(root, text='Love Calculator - How much is he/she into you')
heading.pack()

# Slot/input for the first name
slot1 = Label(root, text="Enter Your Name:")
slot1.pack()
name1 = Entry(root, border=5)
name1.pack()

# Slot/input for the partner name
slot2 = Label(root, text="Enter Your Partner Name:")
slot2.pack()
name2 = Entry(root, border=5)
name2.pack()

bt = Button(root, text="Calculate", height=1,
            width=7, command=calculate_love)
bt.pack()

# Text on result slot
result = Label(root, text='Love Percentage between both of You:')
result.pack()

# Starting the GUI
root.mainloop()
