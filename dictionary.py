
# dictionary with tkinter


from PyDictionary import PyDictionary                           # importing the python dictionary module
from tkinter import *                                           # importing all the modules of tkinter
root=Tk()                                                      # making window
root.title("my search application")                            # giving title of window
root.geometry("550x550")                                       # giving size of the window


# function for using dictionary
def fxn():
    entry_val=e1.get()
    answer.delete(1.0,END)
    try:
        dictionary=PyDictionary()
        answer_val=dictionary.meaning(entry_val)
        #answer_val.get()
        answer.insert(INSERT,answer_val)
    except:
        answer.insert(INSERT,"please enter a valid value or check internet connection")

# Frame1
topframe=Frame(root)
topframe.pack(side=TOP)

# create a heading named my dictionary app:-
l1=Label(topframe,text="my dictionary app:-",fg="red",font=("times new roman",26,"bold"))
l1.pack(padx=10,pady=10)

# create an entry box where use can enter a keyword
e1=Entry(topframe,borderwidth=6)
e1.pack(padx=15,pady=15)

# create a search button
b1=Button(topframe,text="find meaning ",bg="cyan",fg="red",font=("times new roman",14,"bold"),command=fxn)
b1.pack(padx=15,pady=15)

# Frame 2
bottomframe=Frame(root,relief='solid',borderwidth=8)
bottomframe.pack()


answer=Text(bottomframe,width=100,height=100,wrap=WORD,fg="red",font=("times new roman",14,"bold"))
answer.pack()

# start the gui
root.mainloop()

