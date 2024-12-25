from tkinter import *
from tkinter import ttk,messagebox
from datetime import*
import time
from math import*
import sqlite3
import os
class Login_window:
    def __init__(self, root):
        self.root =root
        self.root.title("Login")    
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        
    

        
        
        
        title=Label(self.root,text="Login_window HERE", font=("times new roman",20,"bold"),bg="blue", fg="white")
        title.place(x=450,y=30)
        
        email=Label(self.root,text="email", font=("times new roman",15,"bold"),bg="white")
        email.place(x=350,y=170)
        self.txt_email=Entry(self.root,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)
        
        
       
    #    Row 2
        pass_=Label(self.root,text="pass_",font=("times new roman",15,"bold"),bg="white")
        pass_.place(x=350,y=310)
        self.txt_pass_=Entry(self.root,font=("times new roman",15),bg="lightgray")
        self.txt_pass_.place(x=370,y=340,width=250)
        
        btn_forget=Button(self.root,text="Forget password",command=self.forget_password_window,font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2", bd=0)
        btn_forget.place(x=300,y=500,width=180,height=35)
        
        btn_login=Button(self.root,text="Login",command=self.login,font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2")
        btn_login.place(x=500,y=500,width=180,height=35)
        
        btn_reg=Button(self.root,text="Register",command=self.register_window,font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2")
        btn_reg.place(x=700,y=500,width=180,height=35)
        
    
        
    
    
    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_pass_.delete(0,END)
        self.txt_email.delete(0,END)
            
    
    def clear(self):
        self.txt_fname.delete(0,END)        
        self.txt_lname.delete(0,END)        
        self.txt_contact.delete(0,END)        
        self.txt_email.delete(0,END)        
        self.txt_answer.delete(0,END)        
        self.txt_pass_.delete(0,END)        
        self.txt_cpass_.delete(0,END)        
        self.cmb_quest.current(0)
    
    def forget_password(self):
        if self.cmb_quest.get()=="Select" or self.txt_answer.get()==""or self.txt_new_pass.get()=="":
            messagebox.showerror("Error","All fields are required", parent=self.root2)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("Select * FROM employee where email=? and question=? and answer=?",(
                    self.txt_email.get(),
                    self.cmb_quest.get(),
                    self.txt_answer.get()
                ))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Security Question ",parent=self.root2)
                else:
                    cur.execute("Update employee set password=? where email=?",(self.txt_new_pass.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Your password has been reset, Please login with new password",parent=self.root2)
                        
                    
                
            except Exception as e:
                messagebox.showerror("Error",f"Error due to: {str(e)}",parent=self.root2)
                     
    
    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset your password",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("Select * from employee where email=? ",(self.txt_email.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter the valid email address",parent=self.root)
                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350X400+495+150")
                    self.root2.focus_force()
                    self.root2_grab_set()
                    
                    t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"))
                    t.pack(side=TOP,pady=10)
                    
                    
                    # Forget password
                    question=Label(self.root2,text="Security Question", font=("times new roman"))
                    question.place(x=50,y=80)
                    self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman",13),state='readonly')
                    self.cmb_quest["values"]=("Select","Your first Pet Name","Your Birth Place")
                    self.cmb_quest.place(x=50,y=130,width=250)
                    self.cmb_quest.current(0)
                    
                    
                    # Answer
                    answer = Label(self.root2,text="Answer", font=("times new roman ",15,"bold"))
                    answer.place(x=50,y=150)
                    self.txt_answer=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.txt_answer.place(x=50,y=210,width=250)
                        
                    # new password
                    new_password = Label(self.root2,text="New Password  ", font=("times new roman ",15,"bold"))
                    new_password.place(x=50,y=220)
                    self.txt_new_pass=Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.txt_new_pass.place(x=50,y=290,width=250)
                        
                    btn_change_password=Button(self.root2,text="Reset Password", command=self.forget_password,font=("times new roman",15,"bold"),bg="blue",fg="white")
                    btn_change_password.place(x=50,y=300,width=250)
                    
                
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to:{str(es)}",parent=self.root)         
   
   
    def login(self):
        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root) 
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur =  con.cursor()
                cur.execute("Select * from employee where email=? and password=?",(self.txt_email.get(),self.txt_pass_.get(),))
                row=cur.fetchone()
                if row==None:
                   messagebox.showerror("Error","Invalid Username and Password",parent=self.root)
                else:
                   messagebox.showerror("Success","Welcome",parent=self.root)
                   self.root.destroy()
                   os.system("python dashboard.py")
            except Exception as e:
                messagebox.showerror("Error",f"Error due to: {str(e)}",parent=self.root)    
                         
        
                  
    def register_window(self):
        self.root.destroy()

        
        
            
if __name__ =="__main__":
    root = Tk()
    obj  = Login_window(root)
    root.mainloop()            