
import mysql.connector
con=mysql.connector.connect(user='root',host='localhost')
mycursor=con.cursor()
mycursor.execute("use db1")
from tkinter import *
root=Tk()
root.title("my gui app")
root.geometry("450x450")
def fxn():
    def fxn1():
        a=int(e1.get())
        b=e2.get()
        c=int(e3.get())
        comm=f"insert into tb20 values({a},'{b}',{c})"
        mycursor.execute(comm)
        con.commit()
        l4.config(text="inserted successfully")
    mynew=Toplevel(root)
    mynew.title("insert")
    mynew.geometry("300x300")
    l1=Label(mynew,text="enter your id",fg="blue",font=("times new roman",14,"bold"))
    l1.grid(row=0,column=0)
    e1=Entry(mynew)
    e1.grid(row=0,column=1)
    l2=Label(mynew,text="enter your name",fg="blue",font=("times new roman",14,"bold"))
    l2.grid(row=1,column=0)
    e2=Entry(mynew)
    e2.grid(row=1,column=1)
    l3=Label(mynew,text="enter your marks",fg="blue",font=("times new roman",14,"bold"))
    l3.grid(row=2,column=0)
    e3=Entry(mynew)
    e3.grid(row=2,column=1)
    b2=Button(mynew,text="click to insert",bg="blue",fg="white",font=("italic",14,"bold"),command=fxn1)
    b2.grid(row=8,column=8)
    l4=Label(mynew,fg="blue",font=("italic",14,"bold"))
    l4.grid(row=12,column=12)
    mynew.mainloop()
def fxn3():
    def fxn5():
        d=int(e5.get())
        com=f"delete from tb20 where id={d}"
        mycursor.execute(com)
        con.commit()
        l6.config(text="deleted successfully")

    mynew2=Toplevel(root)
    mynew2.title("deletion")
    mynew2.geometry("200x200")
    l5=Label(mynew2,text="enter your id")
    l5.grid(row=0,column=0)
    e5=Entry(mynew2)
    e5.grid(row=0,column=1)
    b2=Button(mynew2,text="click to delete",bg="blue",fg="white",font=("italic",14,"bold"),command=fxn5)
    b2.grid(row=4,column=4)
    l6=Label(mynew2)
    l6.grid(row=7,column=7)
    mynew2.mainloop()
b1=Button(root,text="click to insert the data",bg="cyan",fg="blue",font=("italic",14,"bold"),command=fxn)
b1.grid(row=6,column=0)
b1=Button(root,text="click to delete the data",bg="cyan",fg="blue",font=("italic",14,"bold"),command=fxn3)
b1.grid(row=6,column=6)

root.mainloop()
mycursor.close()
 

 