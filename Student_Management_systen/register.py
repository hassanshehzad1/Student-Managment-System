from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import sqlite3
import os
class Register:
    def __init__(self, root):
        self.root =root
        self.root.title("Registration window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        
    
        
        # Register frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,width=700,height=500)
        
        title=Label(frame1,text="REGISTER HERE", font=("times new roman",20,"bold"),bg="white")
        
        # Row 1
        f_name=Label(frame1,text="First Name", font=("times new roman",15,"bold"),bg="white")
        f_name.place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)
        
        l_name=Label(frame1,text="Last Name", font=("times new roman",15,"bold"),bg="white")
        l_name.place(x=350,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)
        
        # Row 2
        contact=Label(frame1,text="Contact", font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame1,text="email", font=("times new roman",15,"bold"),bg="white")
        email.place(x=350,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)
        
        # Row 3
        question=Label(frame1,text="Security Question", font=("times new roman",15,"bold"),bg="white")
        question.place(x=50,y=240)
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify="center")
        self.cmb_quest["values"]=("Select","Your First Pet name","Your Birth place")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)
        
        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="lightgray")
        answer.place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)
        
       
    #    Row 2
        password=Label(frame1,text="password",font=("times new roman",15,"bold"),bg="white",fg="lightgray")
        password.place(x=370,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=50,y=340,width=250)
        
        cpassword=Label(frame1,text="cpassword",font=("times new roman",15,"bold"),bg="white",fg="lightgray")
        cpassword.place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_cpassword.place(x=370,y=340,width=250)
        
        
        # Terms
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I agree the terms and conditions", variable=self.var_chk, bg="white",font=("times new roman",12))
        chk.place(x=50,y=380)
    
        btn_login=Button(self.root,text="Sign in",command=self.login_window,font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2")
        btn_login.place(x=200,y=500,width=180,height=35)
        
        btn_register=Button(self.root,text="Register Now",command=self.register_data,font=("times new roman",15,"bold"),bg="green",fg="white",cursor="hand2")
        btn_register.place(x=550,y=430,width=250,height=45)
        
    
    
    def login_window(self):
        self.root.destroy()
        os.system("python login.py")
        
    
    def clear(self):
        self.txt_fname.delete(0,END)        
        self.txt_lname.delete(0,END)        
        self.txt_contact.delete(0,END)        
        self.txt_email.delete(0,END)        
        self.txt_answer.delete(0,END)        
        self.txt_password.delete(0,END)        
        self.txt_cpassword.delete(0,END)        
        self.cmb_quest.current(0)
        
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.txt_answer.get()=="" or  self.      txt_lname.get()=="" or  self.txt_password.get()=="" or  self.txt_cpassword.get()=="":
          messagebox.showerror("Error","All Fields are required",parent=self.root) 
        elif self.txt_cpassword.get()!=self.txt_password.get():
                 messagebox.showerror("Error","Password and confirm password should be same",parent=self.root)
        elif self.var_chk.get()==0:
                 messagebox.showerror("Error","Terms and conditions required",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur =  con.cursor()
                cur.execute("Select * from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                if row!=None:
                   messagebox.showerror("Error","User already Reqgitered , Please try with another")
                else:
                  cur.execute("insert into employee (f_name,l_name,contact,email,question,answer,password) values(?, ?,?,?,?,?,? )",(self.txt_fname.get(),self.txt_lname.get(),self.txt_contact.get(),self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get(),self.txt_password.get()))
                  con.commit()
                  con.close()
                  messagebox.showinfo("Success", "Registration Successfully",parent=self.root)
                  self.clear()
                  self.login_window()
            
            except Exception as e:
                messagebox.showerror("Error",f"Error due to: {str(e)}",parent=self.root)    
                         
        
                  
        
                    
        
if __name__ =="__main__":
    root = Tk()
    obj  = Register(root)
    root.mainloop()            