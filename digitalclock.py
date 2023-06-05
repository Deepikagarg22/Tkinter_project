import tkinter as tk                          # importing all the  odules and widgets from tkinter
from datetime import datetime as dt           # importing the time module


root = tk.Tk()
root.title('My self')                              # setting the title of window
root.geometry('600x300')                           # for giving size of window
root.config(padx=20,bg='#ADD8E6')                  # configuring the background color 
root.resizable(0.0,0.0)                            # disabling the resizable option




# function for showing time
def show_time():
    current_time = dt.now().strftime("%I: %M :%S %p")
    time.config(text=current_time)
    root.after(1000,show_time)

# function for showing the date
def show_date():
    current_date = dt.now().strftime("%A : %d - %B - %Y")
    day_date.config(text=current_date)



# defining label to display the heading
heading = tk.Label(text='CLOCK',font=('Courier',60,'bold'),fg='WHITE',bg='#ADD8E6')
heading.grid(row=1,column=1,columnspan=2)



# showing time
time = tk.Label(text='12:30 PM',font=('radioland',60),bg='#ADD8E6',fg='black',pady=10)
time.grid(row=2,column=1)

# showing date
day_date = tk.Label(text='MONDAY : 12-MARCH-2020',font=('onyx',20),bg='#ADD8E6',fg='#28485B')
day_date.place(x=90,y=220)

# calling functions
show_time()
show_date()

# start the gui
root.mainloop()
