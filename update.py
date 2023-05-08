import tkinter as tk
from tkinter import ttk
from pymysql import*
from tkinter import messagebox


class Update:
    
    def __init__(self,data=None):
        self.data=data
        self.win = tk.Tk()
        self.win.geometry('600x600')
        self.win.title('Update')
        self.win.configure(background='sea green')

        self.heading=ttk.Label(self.win,text="STUDENT INSTRUCTIONS", font='Helvetica 24 bold',background='gold')
        self.heading.pack(pady=30)

#label frame
        self.label_frame = ttk.Labelframe(self.win) 
        self.label_frame.pack(fill='both',padx=20,pady=20)


        self.welcome = ttk.Label(self.label_frame,text='Welcome:'+str(data[1]),font='Helvetica 24 bold')
        self.welcome.pack(padx=20,pady=20)
        
        self.new_password = ttk.Label(self.label_frame,text='New Password',font='arial 16 bold')
        self.new_password.pack(pady=20)
        self.new_entrybox = ttk.Entry(self.label_frame,font=('arial',16,'bold'),background="powder blue",justify='left')
        self.new_entrybox.pack()

        self.confirm_password = ttk.Label(self.label_frame,text='Confirm Password',font='arial 16 bold')
        self.confirm_password.pack(pady=20)
        self.confirm_entrybox = ttk.Entry(self.label_frame,font=('arial',16,'bold'),background="powder blue",justify='left')
        self.confirm_entrybox.pack()

        self.update_btn = tk.Button(self.label_frame,text='Update',activebackground='red',bd=5,activeforeground='yellow',bg='powder blue', width=15,font=('arial',14,'bold'),command=lambda:change(self.new_entrybox,self.data))
        self.update_btn.pack(padx=20,pady=20)

        self.back_btn = tk.Button(self.label_frame,text='Back',activebackground='red',bd=5,activeforeground='yellow',bg='powder blue', width=15,font=('arial',14,'bold'),command= lambda:back(self.win,self.data))
        self.back_btn.pack(padx=20,pady=20)

        self.win.mainloop()

def back(win,data):
        win.destroy()
        import student_project1 as sp1
        sp1.Login(data)        
def change(e,data):
        password= e.get()
        print(password,data)
        con=connect(host='localhost',user='root',password='incorrect',port=3306,database='student_inst')
        cursor=con.cursor()
        cursor.execute(f"Update student set Password ='{password}' where Roll={data[0]} ")
        con.commit()
        con.close()
        messagebox.showinfo('Update','Password updated')