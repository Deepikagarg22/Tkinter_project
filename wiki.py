# importing module
import tkinter as tk
import wikipedia as wk



window = tk.Tk()                                     # creating a normal window
window.title("Wikipedia")                            # giving the title of window
window.geometry("650x700")                           # giving size of the window
window.resizable(0.0,0.0)                            # getting window can not be resizable


# creating a function which will show all summary
def result():
    query = user_search.get()
    print(query)

    # if summary will be fetch from the wikipedia
    try:
        # show summary in text area
        result = wk.summary(query,sentences = 2)
        result_label.config(text=result,font=('Georgia',17),wraplength=600,relief='ridge',padx=20,pady=20,fg='black')
    
    # if summary will not fetch from wikipedia , it shows error
    except:
        result_label.config(text='No data found',font=('Georgia',17),wraplength=600,relief='ridge',padx=20,pady=20)




# create a heading named wikipedia
heading = tk.Label(text='WikipediA',font=('Georgia',80),fg='#2E8B57')
heading.pack()


# create a search bar
search = tk.Label(text='Search here',font=('Georgia',20))
search.pack(pady=15)


# create an entry box where use can enter a keyword
user_search = tk.Entry(font=('Georgia',18),width= 35)
user_search.pack()


# create a search button
search_button = tk.Button(text='Search',font=('Georgia',18,'bold'),padx=170,bg='#2E8B57',fg='white',relief='ridge',command=result)
search_button.pack()


result_label = tk.Label(text='')
result_label.pack(pady=20)



# start the gui
window.mainloop()

