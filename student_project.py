import tkinter as tk
#from tkinter import *
#from tkinter.ttk import*
from tkinter import ttk
from pymysql import *
from student_project1 import Login
#import mysql.connector

def next():
    r=int(roll_enterybox.get())
    p=password_enterybox.get()
    con=connect(host='localhost',user='root',password='incorrect',port=3306,database='student_inst')
    cursor=con.cursor()
    count=cursor.execute(f"select * from student where Roll={r} and Password='{p}'")
    if(count>0):
        win.destroy()
        import student_project1 as st
        st.Login(cursor.fetchone())
    else:
        pass

win = tk.Tk()
win.geometry('600x600')
win.title('Student')
win.configure(background='gray')

# title of the page
#heading


heading=tk.Label(win,text="STUDENT INSTRUCTIONS", font='Helvetica 18 bold',background='gold')

#heading.config(font=100,width =0,background='gray') config ki separately need ni h
heading.pack(pady=30)


# label frame

label_frame = ttk.Labelframe(win)

label_frame.pack(fill='both',padx=20,pady=20)
#frame1= tk.Frame(win,height=100,width =100,background='black',borderwidth=2)
#frame1.pack()
# roll number
roll = tk.Label(label_frame,text='Enter your Roll no. :',font='arial 16 bold',bg='light blue')
roll.pack()

roll_enterybox = ttk.Entry(label_frame,font=('arial',16,'bold'),background="powder blue",justify='left')
roll_enterybox.focus_set()
roll_enterybox.pack(pady=30)

# password 
password = tk.Label(label_frame,text='Enter your password: ',font='arial 16 bold',bg='light blue')
password.pack()

password_enterybox = tk.Entry(label_frame,show='*',font=('arial',16,'bold'),background="powder blue",justify='left')
password_enterybox.pack(pady = 30)
# create button

login_button= tk.Button(win,text='login',command=next,activebackground='red',bd=5,activeforeground='yellow',bg='powder blue', width=15,font=('arial',14,'bold'),relief='sunken')
login_button.pack(padx=20,pady=20)

win.mainloop()


def student_project1(win,data):
    win.destroy()
    Login(data)