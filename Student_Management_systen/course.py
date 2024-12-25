from tkinter import*
from PIL import Image, ImageTk  #install pillow
from tkinter import ttk, messagebox
import sqlite3
class CourseClass:
    def __init__(self,root):
        self.root = root
        self.root.title("CS50-final project: Student Result Managment System ")
        self.root.geometry("1200x480+90+190")
        self.root.config(bg="white")
        self.root.focus_force()
        
             # title
        title = Label(self.root,text="Course Details", font=("old style", 20,"bold"), bg="blue", fg="white").place(x=0,y=0,relwidth=1, height=50)
        # Variables
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()
   
        # Wigets
        lbl_courseName = Label(self.root, text="Course name",font=("old style", 20,"bold"), bg="white", ).place(x=10, y=60)
        lbl_courseDuration = Label(self.root, text="Durations",font=("old style", 20,"bold"), bg="white", ).place(x=10, y=100)
        lbl_courseCharges = Label(self.root, text="Charges",font=("old style", 20,"bold"), bg="white", ).place(x=10, y=140)
        lbl_description= Label(self.root, text="Description",font=("old style", 20,"bold"), bg="white", ).place(x=10, y=180)

        # Entry fielsds
        self.txt_courseName = Entry(self.root, textvariable=self.var_course, font=("old style", 20,"bold"), bg="lightblue", )
        self.txt_courseName.place(x=200, y=60, width=200)
        
        txt_courseDuration = Entry(self.root,textvariable=self.var_duration, font=("old style", 20,"bold"), bg="lightblue", ).place(x=180, y=100, width=200)
        txt_courseCharges = Entry(self.root,textvariable=self.var_charges,  font=("old style", 20,"bold"), bg="lightblue", ).place(x=180, y=140, width=200)
        self.txt_description= Text(self.root, font=("old style", 20,"bold"), bg="lightblue", )
        self.txt_description.place(x=180, y=180, width=500, height=140)
        
        # Buttons
        self.btn_add=Button(self.root, text="Save", font=("goudy old style", 17, "bold"), bg="#ff5733", fg="white", cursor="hand2", command=self.add)
        self.btn_add.place(x=180, y=350, width=110, height=40)
        self.btn_update=Button(self.root, text="Update", font=("goudy old style", 17, "bold"), bg="#ff3333", fg="white", cursor="hand2", command=self.update)
        self.btn_update.place(x=300, y=350, width=110, height=40)
        self.btn_delete=Button(self.root, text="Delete", font=("goudy old style", 17, "bold"), bg="#ff5710", fg="white", cursor="hand2" ,command=self.delete)
        self.btn_delete.place(x=420, y=350, width=110, height=40)       
        self.btn_clear=Button(self.root, text="Clear", font=("goudy old style", 17, "bold"), bg="#ff5983", fg="white", cursor="hand2", command=self.clear)
        self.btn_clear.place(x=550, y=350, width=110, height=40)
        # Search panel
        self.var_search = StringVar()
        lbl_search_courseName = Label(self.root, text="Course name", font=("old style", 20,"bold"), fg="black",bg="white" ).place(x=670, y=60)
        self.txt_search_courseName = Entry(self.root, textvariable=self.var_course, font=("old style", 20,"bold"), bg="lightblue", ).place(x=850, y=60, width=200)
        self.btn_add=Button(self.root, text="Search", font=("goudy old style", 17, "bold"), bg="#ff5733", fg="white", cursor="hand2",command=self.search)
        self.btn_add.place(x=1070, y=60, width=140, height=30)
        # Content
        self.C_Frame=Frame(self.root,bd =2,relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=540, height=440)
        
        scrolly = Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("cid", "name","duration", "charges","description"))
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        
        self.CourseTable.heading("cid",text="Course ID")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("duration",text="Duration")
        self.CourseTable.heading("charges",text="Charges")
        self.CourseTable.heading("description",text="Description")
        self.CourseTable["show"]='headings'
        self.CourseTable.column("cid",width=50)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration",width=100)
        self.CourseTable.column("charges",width=100)
        self.CourseTable.column("description",width=100)
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()
        # 
    
    def clear(self):
        self.show()
        self.var_course.set("")    
        self.var_duration.set("")    
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete("1.0",END)
        self.txt_courseName.config(state=NORMAL)
        
    
    
    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
             if  self.var_course.get()=="":
                messagebox.showerror("Error","Course name should be required ", parent=self.root)
             else:
                 cur.execute("Select * from course where name =?", (self.var_course.get(),))
                 row=cur.fetchone()
                 if row==None:
                      messagebox.showerror("Error","please Select a course from the list first", parent=self.root)
                 else:
                      op=messagebox.askyesno("Confirm","Do you really want to delete", parent=self.root)
                      if op==True:
                          cur.execute("delete from course where name=?", (self.var_course.get(),))
                          con.commit()
                          messagebox.showinfo("Delete","Course deleted successfully", parent=self.root)
                          self.clear()
                        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")    
                   
                     
        
    def get_data(self,ev):
        self.txt_courseName.config(state='readonly')
        self.txt_courseName
        r=self.CourseTable.focus()
        content= self.CourseTable.item(r)
        row=content["values"]
        # print(row)    
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        # self.var_course.set(row[4])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[4])
        
    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
             if  self.var_course.get()=="":
                messagebox.showerror("Error","Course name should be required ", parent=self.root)
             else:
                 cur.execute("Select * from course where name =?", (self.var_course.get(),))
                 row=cur.fetchone()
                 if row==None:
                      messagebox.showerror("Error","Select a course from title", parent=self.root)
                 else:
                      cur.execute("update course set duration=?, charges=?, description=? where name=?",( self.var_charges.get(), self.var_duration.get(), self.txt_description.get("1.0",END),self.var_course.get(),))
                      con.commit()
                      messagebox.showinfo("Success","Course update successfully", parent=self.root)
                      self.show()                
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")    
        
    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
             if  self.var_course.get()=="":
                messagebox.showerror("Error","Course name should be required ", parent=self.root)
             else:
                 cur.execute("Select * from course where name =?", (self.var_course.get(),))
                 row=cur.fetchone()
                 if row!=None:
                      messagebox.showerror("Error","Course name already present", parent=self.root)
                 else:
                      cur.execute("insert into course (name, duration, charges, description) values(?,?,?,?)",(self.var_course.get(), self.var_charges.get(), self.var_duration.get(), self.txt_description.get("1.0",END)))
                      con.commit()
                      messagebox.showinfo("Success","Course added successfully", parent=self.root)
                      self.show()                
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")    
        
   
    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
             cur.execute("Select * FROM course")
             rows=cur.fetchall()
             self.CourseTable.delete(*self.CourseTable.get_children()) 
             for row in rows:
                 self.CourseTable.insert('',END, values=row)
                  
                
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")    
   
   
   
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
             cur.execute("Select * FROM course")
             rows=cur.fetchall()
             self.CourseTable.delete(*self.CourseTable.get_children()) 
             for row in rows:
                 self.CourseTable.insert('',END, values=row)
                  
                
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")    
        
if __name__ =="__main__":
    root = Tk()
    obj  = CourseClass(root)
    root.mainloop()    