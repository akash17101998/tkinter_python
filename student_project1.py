import tkinter as tk
from tkinter import ttk
#from tkinter import colorchooser
from view_profile import View
from update import Update
from feedback import Feedback

class Login:
    
    def __init__(self,data=None):
        self.data=data
        self.win = tk.Tk()
        self.win.geometry('600x600')
        #frame = tk.Frame(win,width=50,height=50)        #frame ki height or width deni ho to
        #frame.pack()
        self.win.title('Student')
        self.win.configure(background='sea green')
        self.heading=ttk.Label(self.win,text="STUDENT INSTRUCTIONS", font='Helvetica 24 bold',background='gold')
        self.heading.pack(pady=30)


        #label frame
        self.label_frame = ttk.Labelframe(self.win) 
        self.label_frame.pack(fill='both',padx=20,pady=20)

        self.welcome=ttk.Label(self.label_frame,text='Welcome:'+str(data[1]),font='Helvetica 18 bold')
        self.welcome.pack(padx=20,pady=20)

        self.update= tk.Button(self.label_frame,text='Update Password',activebackground='red',bd=5,activeforeground='yellow',bg='powder blue', width=15,font=('arial',14,'bold'),command=lambda:update(self.win,self.data))
        self.update.pack(padx=20,pady=20)
        #update.config(font = 'helvetica 20 bold')

        self.view = tk.Button(self.label_frame,text='View Profile',activebackground='red',bd=5,activeforeground='yellow',bg='powder blue', width=15,font=('arial',14,'bold'),command= lambda:view_profile(self.win,self.data))
        self.view.pack(padx=20,pady=20)

        self.feedback = tk.Button(self.label_frame,text='Feedback',activebackground='red',bd=5,activeforeground='yellow',bg='powder blue', width=15,font=('arial',14,'bold'),command= lambda:feedback(self.win,self.data))
        self.feedback.pack(padx=20,pady=20)
        
        self.back_btn = tk.Button(self.label_frame,text='Back',activebackground='red',bd=5,activeforeground='yellow',bg='powder blue', width=15,font=('arial',14,'bold'),command= lambda:back(self.win,self.data))
        self.back_btn.pack(padx=20,pady=20)
        self.win.mainloop()


def back(win,data):
    win.destroy()
    import student_project as sp
    sp.Student(data)        


def update(win,data):
    win.destroy()
    Update(data)

def view_profile(win,data):
    win.destroy()
    View(data)

def feedback(win,data):
    win.destroy()
    Feedback(data)