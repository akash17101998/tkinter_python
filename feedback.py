import tkinter as tk
from tkinter import ttk

class Feedback:

    def __init__(self,data=None):
        self.data=data
        self.win = tk.Tk()
        self.win.geometry('600x600')
        self.win.title('Feedback')
        self.win.configure(background='sea green')

        self.heading=ttk.Label(self.win,text="STUDENT INSTRUCTIONS", font='Helvetica 24 bold',background='gold')
        self.heading.pack(pady=30)

#label frame
        self.label_frame = ttk.Labelframe(self.win) 
        self.label_frame.pack(fill='both',padx=20,pady=20)


        self.welcome = ttk.Label(self.label_frame,text='Welcome:',font='Helvetica 24 bold')
        self.welcome.pack(padx=20,pady=20)

### comment
        self.comment = ttk.Label(self.label_frame,text= 'Comment: ',font='Helvetica 12 bold')
        self.comment.pack()

        self.label_frame1 = ttk.Labelframe(self.label_frame) 
        self.label_frame1.pack(fill='both',padx=20,pady=20)

        self.fun = ttk.Label(self.label_frame1,text='Student Feedback: '+str(data[6]),font=('arial',12,'bold'))
        self.fun.pack()
        #self.fun.insert(0,self.data[5])

        self.back_btn = tk.Button(self.label_frame,text='Back',activebackground='red',bd=5,activeforeground='yellow',bg='powder blue', width=15,font=('arial',14,'bold'),command=lambda:back(self.win,self.data))
        self.back_btn.pack(padx=20,pady=20,side='bottom')

        self.win.mainloop()

def back(win,data):
    win.destroy()
    import student_project1 as sp1
    sp1.Login(data)        