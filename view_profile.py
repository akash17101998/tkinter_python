import tkinter as tk
from tkinter import ttk

class View:

    def __init__(self,data=None):
        self.data=data    
        self.win = tk.Tk()
        self.win.geometry('600x900')
        self.win.title('View Profile')
        self.win.configure(background='sea green')


        self.heading= ttk.Label(self.win,text='STUDENT INSTRUCTIONS', font='Helvetica 24 bold', background='gold')
        self.heading.pack(pady=30)


### label frame
        self.label_frame= ttk.LabelFrame(self.win)
        self.label_frame.pack(padx=20,pady=20,fill='both')

        self.scrollbar= tk.Scrollbar(self.label_frame)
        self.scrollbar.pack(side= tk.RIGHT,fill=tk.Y)


        self.welcome = ttk.Label(self.label_frame,text='Welcome:',font='Helvetica 24 bold')
        self.welcome.pack(padx=20,pady=20)



### roll no
        self.roll_no = ttk.Label(self.label_frame,text='Roll No.', font= 'arial 16 bold')
        self.roll_no.pack(padx=10,pady=10)
# roll no entrybox
        self.roll_no_entrybox= ttk.Entry(self.label_frame,font=('arial',16,'bold'),background="powder blue",justify='left')
        self.roll_no_entrybox.pack()
        self.roll_no_entrybox.insert(0,self.data[0])


#### name 
        self.name = ttk.Label(self.label_frame,text='Name', font= 'arial 16 bold')
        self.name.pack(padx=10,pady=10)
# name entrybox
        self.name_entrybox= ttk.Entry(self.label_frame,font=('arial',16,'bold'),background="powder blue",justify='left')
        self.name_entrybox.pack()
        self.name_entrybox.insert(0,self.data[1])

### batch
        self.batch = ttk.Label(self.label_frame,text='Batch', font='arial 16 bold')
        self.batch.pack(padx=10,pady=10)
# batch entrybox
        self.batch_entrybox = ttk.Entry(self.label_frame,text=self.data[2],font=('arial',16,'bold'),background="powder blue",justify='left')
        self.batch_entrybox.pack() 
        self.batch_entrybox.insert(0,self.data[2])






### course
        self.course = ttk.Label(   self.label_frame,text='Course',font = 'arial 16 bold')
        self.course.pack(padx=10,pady=10)
## course entrybox
        self.course_entrybox = ttk.Entry(  self.label_frame,text=self.data[3],font=('arial',16,'bold'),background="powder blue",justify='left')
        self.course_entrybox.pack()
        self.course_entrybox.insert(0,self.data[3])




### city
        self.city = ttk.Label( self.label_frame,text='City',font = 'arial 16 bold')
        self.city.pack(padx=10,pady=10)
# city entrybox
        self.city_entrybox = ttk.Entry(self.label_frame,text=self.data[4],font=('arial',16,'bold'),background="powder blue",justify='left')
        self.city_entrybox.pack()
        self.city_entrybox.insert(0,self.data[4])

        self.back_btn = tk.Button(self.label_frame,text='Back',activebackground='red',bd=5,activeforeground='yellow',bg='powder blue', width=15,font=('arial',14,'bold'),command=lambda:back(self.win,self.data))
        self.back_btn.pack(padx=20,pady=20)


        self.win.mainloop()

def back(win,data):
        win.destroy()
        import student_project1 as sp1
        sp1.Login(data)        