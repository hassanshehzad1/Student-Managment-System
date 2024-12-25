from tkinter import*
from PIL import Image, ImageTk  #install pillow
from course import CourseClass
from student import StudentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox
import sqlite3
import os
class RMS:
    def __init__(self,root):
        self.root = root
        self.root.title("CS50-final project: Student Result Managment System ")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        # Icons
        self.logo_dash = ImageTk.PhotoImage(file="Images/logo.png")
        # title
        title = Label(self.root,text="Students Managments system",padx=10, compound=LEFT, image=self.logo_dash, font=("old style", 20,"bold"), bg="blue", fg="white").place(x=0,y=0,relwidth=1, height=50)
        # Menu
        M_Frame=LabelFrame(self.root,text="Services", font=("times new roman", 15), bg="white")
        M_Frame.place(x=10,y=70,width=1340,height=80)
        
        # button
        btn_course=Button(M_Frame,text="Course", font=("Goudy oldy style", 15 ,"bold"), command=self.add_course, bg="#242352", fg="white", cursor="hand1").place(x=20,y=5,width=140,height=40)        
        btn_student=Button(M_Frame,text="Student", font=("Goudy oldy style", 15 ,"bold"), command=self.add_student, bg="#242352", fg="white", cursor="hand1").place(x=220,y=5,width=140,height=40)        
        btn_result=Button(M_Frame,text="Result", font=("Goudy oldy style", 15 ,"bold"), bg="#242352", fg="white", command=self.add_result, cursor="hand1").place(x=440,y=5,width=140,height=40)
        btn_view=Button(M_Frame,text="View Result", font=("Goudy oldy style", 15 ,"bold"), bg="#242352", fg="white", cursor="hand1",command=self.add_report).place(x=660,y=5,width=140,height=40)
        btn_logout=Button(M_Frame,text="Logout", font=("Goudy oldy style", 15 ,"bold"), bg="#242352", fg="white", cursor="hand1", command=self.logout).place(x=880,y=5,width=140,height=40)
        btn_exist=Button(M_Frame,text="Exit", font=("Goudy oldy style", 15 ,"bold"), bg="#242352", fg="white", cursor="hand1", command=self.exit_).place(x=1100,y=5,width=140,height=40)
        
        # Content of window
        self.bg_image = Image.open("Images/bg.png")
        self.bg_image = self.bg_image.resize((420,250))
        self.bg_img=ImageTk.PhotoImage(self.bg_image)
        
        self.lbl_bg=Label(self.root, image=self.bg_img).place(x=400,y=180, width=920,height=350)
        
        # Update labels
        self.lbl_course=Label(self.root,text="Total Courses\n[ 0 ]", font=("goudy old style ", 20), bd=10, relief=RIDGE,bg="#2ff5f2",fg="white")
        self.lbl_course.place(x=200, y=530, width=300, height=100)      
        
        self.lbl_student=Label(self.root,text="Total Students\n[ 0 ]", font=("goudy old style ", 20), bd=10, relief=RIDGE,bg="#2995f2",fg="white")
        self.lbl_student.place(x=550, y=530, width=300, height=100)
      
        self.lbl_result=Label(self.root,text="Total Results\n[ 0 ]", font=("goudy old style ", 20), bd=10, relief=RIDGE,bg="#1114f2",fg="white")
        self.lbl_result.place(x=900, y=530, width=300, height=100)
      
        # Footer
        footer = Label(self.root,text="CS50-Students Managments system\nContact for any queries",  font=("old style", 20,"bold"), bg="blue", fg="white").pack(side=BOTTOM, fill=X)
  
        self.update_details()
    
    def update_details(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
             cur.execute("Select * FROM course")
             cr=cur.fetchall()
             self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")
             self.lbl_course.after(200,self.update_details)   
             
             cur.execute("Select * FROM student")
             cr=cur.fetchall()
             self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")
             self.lbl_student.after(200,self.update_details)   
             
             cur.execute("Select * FROM result")
             cr=cur.fetchall()
             self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")
             self.lbl_result.after(200,self.update_details)   
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")   
     
     
     
    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)
         
    
    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = StudentClass(self.new_win)
         
    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)
         
    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)
         
    def logout(self):
        op=messagebox.askyesno("Confirm","Are you sure to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("pyhton login.py")
   
    def exit_(self):
        op=messagebox.askyesno("Confirm","Are you sure to Exit?",parent=self.root)
        if op==True:
            self.root.destroy()
       
if __name__ =="__main__":
    root = Tk()
    obj  = RMS(root)
    root.mainloop()    