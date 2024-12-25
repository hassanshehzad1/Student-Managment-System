from tkinter import*
from PIL import Image, ImageTk  #install pillow
from tkinter import ttk, messagebox
import sqlite3
class reportClass:
    def __init__(self,root):
        self.root = root
        self.root.title("CS50-final project: Student Result Managment System ")
        self.root.geometry("1200x480+90+190")
        self.root.config(bg="white")
        self.root.focus_force()
        
             # title
        title = Label(self.root,text=" View Result", font=("old style", 20,"bold"), bg="red", fg="white").place(x=0,y=0,relwidth=1, height=62)
        
        # Search
        self.var_search = StringVar()
        self.var_id=""
        lbl_select=Label(self.root,text="Search by Roll Number", font=("goudy old style",20,"bold"), bg="white").place(x=220, y=100)     
        txt_select=Entry(self.root,textvariable=self.var_search, font=("goudy old style",20,"bold"), bg="white").place(x=500, y=100, width=200)
        btn_search=Button(self.root, text="Search", font=("goudy old style", 17, "bold"), bg="#ff5733", fg="white", cursor="hand2", command=self.search).place(x=740,y=100,width=130,height=35)   
        btn_clear=Button(self.root, text="Clear", font=("goudy old style", 17, "bold"), bg="#ff5733", fg="white", cursor="hand2", command=self.clear).place(x=900,y=100,width=130,height=35)
           
        
        # Label
        lbl_roll=Label(self.root,text="Roll no", font=("goudy old style",15,"bold"), bg="white", bd=2,relief=GROOVE).place(x=150,y=230,width=150, height=50)
        lbl_name=Label(self.root,text="Name", font=("goudy old style",15,"bold"), bg="white", bd=2,relief=GROOVE).place(x=300,y=230,width=150, height=50)     
        lbl_course=Label(self.root,text="Course", font=("goudy old style",15,"bold"), bg="white", bd=2,relief=GROOVE).place(x=450,y=230,width=150, height=50)
        lbl_marks=Label(self.root,text="Marks obtained", font=("goudy old style",15,"bold"), bg="white", bd=2,relief=GROOVE).place(x=600,y=230,width=150, height=50)
        lbl_full=Label(self.root,text="Total Marks", font=("goudy old style",15,"bold"), bg="white", bd=2,relief=GROOVE).place(x=750,y=230,width=150, height=50)
        lbl_per=Label(self.root,text="Percentage", font=("goudy old style",15,"bold"), bg="white", bd=2,relief=GROOVE).place(x=900,y=230,width=150, height=50)
     
        self.roll=Label(self.root, font=("goudy old style",15,"bold"), bg="white", bd=2,relief=GROOVE)
        self.roll.place(x=150,y=280,width=150, height=50)
        self.name=Label(self.root, font=("goudy old style",15,"bold"), bg="white", bd=2,relief=GROOVE)
        self.name.place(x=300,y=280,width=150, height=50)     
        self.course=Label(self.root, font=("goudy old style",15,"bold"), bg="white", bd=2,relief=GROOVE)
        self.course.place(x=450,y=280,width=150, height=50)
        self.marks=Label(self.root, font=("goudy old style",15,"bold"), bg="white", bd=2,relief=GROOVE)
        self.marks.place(x=600,y=280,width=150, height=50)
        self.full=Label(self.root, font=("goudy old style",15,"bold"), bg="white", bd=2,relief=GROOVE)
        self.full.place(x=750,y=280,width=150, height=50)
        self.per=Label(self.root, font=("goudy old style",15,"bold"), bg="white", bd=2,relief=GROOVE)
        self.per.place(x=900,y=280,width=150, height=50)
     
        btn_delete=Button(self.root, text="Delete", font=("goudy old style", 17, "bold"), bg="#ff5733", fg="white", cursor="hand2", command=self.delete).place(x=900,y=350,width=130,height=35)
        #    Search
        
    def search(self):
          con = sqlite3.connect(database="rms.db")
          cur = con.cursor()
          try:
               if self.var_search.get()=="":
                   messagebox.showerror("Error","Roll no. should be required ", parent=self.root)
               else:    
                   cur.execute("Select * FROM result WHERE roll=?", (self.var_search.get(), ))
                   row=cur.fetchone()
                   if row!=None: 
                     self.var_id=row[0]    
                     self.roll.config(text=row[1])    
                     self.name.config(text=row[2])    
                     self.course.config(text=row[3])    
                     self.marks.config(text=row[4])    
                     self.full.config(text=row[5])    
                     self.per.config(text=row[6])    
                   else:     
                     messagebox.showerror("Error","No record found ", parent=self.root)                         
                
          except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")    
    
    
    def clear(self):
        self.var_id=""
        self.roll.config(text="")    
        self.name.config(text="")    
        self.course.config(text="")    
        self.marks.config(text="")    
        self.full.config(text="")    
        self.per.config(text="")    
        self.var_search.set("")   
     
      
    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
             if  self.var_id=="":
                 messagebox.showerror("Error","Search Student result first", parent=self.root)
             else:
                 cur.execute("Select * from result where rid =?", (self.var_id))
                 row=cur.fetchone()
                 if row==None:
                      messagebox.showerror("Error","Invalid Student Result", parent=self.root)
                 else:
                      op=messagebox.askyesno("Confirm","Do you really want to delete", parent=self.root)
                      if op==True:
                          cur.execute("delete from result where rid=?", (self.var_id,))
                          con.commit()
                          messagebox.showinfo("Delete","Students result deleted successfully", parent=self.root)
                          self.clear()
                        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")    
       
    

if __name__ =="__main__":
    root = Tk()
    obj  = reportClass(root)
    root.mainloop()    