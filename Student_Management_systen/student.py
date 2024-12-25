from tkinter import*
from PIL import Image, ImageTk  #install pillow
from tkinter import ttk, messagebox
import sqlite3
class StudentClass:
    def __init__(self,root):
        self.root = root
        self.root.title("CS50-final project: Student Result Managment System ")
        self.root.geometry("1200x480+90+190")
        self.root.config(bg="white")
        self.root.focus_force()
        
             # title
        title = Label(self.root,text="Managing Students Details", font=("old style", 20,"bold"), bg="blue", fg="white").place(x=0,y=0,relwidth=1, height=50)
        # Variables
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_a_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()
        
        # Wigets
        lbl_roll = Label(self.root, text="Roll no",font=("old style", 20,"bold"), bg="white", ).place(x=10, y=60)
        lbl_Name = Label(self.root, text="Name",font=("old style", 20,"bold"), bg="white", ).place(x=10, y=100)
        lbl_Email = Label(self.root, text="Email",font=("old style", 20,"bold"), bg="white", ).place(x=10, y=140)
        lbl_gender= Label(self.root, text="Gender",font=("old style", 20,"bold"), bg="white", ).place(x=10, y=180)
        lbl_state= Label(self.root, text="State",font=("old style", 20,"bold"), bg="white", ).place(x=10, y=220)
        txt_state = Entry(self.root, textvariable=self.var_state, font=("old style", 20,"bold"), bg="lightblue", ).place(x=150, y=220, width=150)
     
        lbl_city= Label(self.root, text="City",font=("old style", 20,"bold"), bg="white", ).place(x=310, y=220)
        txt_city = Entry(self.root, textvariable=self.var_state, font=("old style", 20,"bold"), bg="lightblue", ).place(x=410, y=220, width=150)
     
        lbl_pin= Label(self.root, text="Pin",font=("old style", 20,"bold"), bg="white", ).place(x=380, y=220)
        txt_pin = Entry(self.root, textvariable=self.var_state, font=("old style", 20,"bold"), bg="lightblue", ).place(x=370, y=220, width=120)

        lbl_address= Label(self.root, text="Address",font=("old style", 20,"bold"), bg="white", ).place(x=10, y=260)

        # Entry fielsds
        self.txt_roll = Entry(self.root, textvariable=self.var_roll, font=("old style", 20,"bold"), bg="lightblue", )
        self.txt_roll.place(x=200, y=60, width=200)
        
        txt_name = Entry(self.root,textvariable=self.var_name, font=("old style", 20,"bold"), bg="lightblue", ).place(x=180, y=100, width=200)
        txt_email = Entry(self.root,textvariable=self.var_email,  font=("old style", 20,"bold"), bg="lightblue", ).place(x=180, y=140, width=200)
        self.txt_address= Text(self.root, font=("old style", 20,"bold"), bg="lightblue", )
       
        self.txt_gender = ttk.Combobox(self.root,textvariable=self.var_gender, values=("Male","Female","Other"), font=("old style", 20,"bold"), state="readonly", justify=CENTER )
        self.txt_gender.place(x=180, y=180,width=200)
        self.txt_gender.current(0)
        
        # Column 2
        lbl_dob = Label(self.root, text="DOB",font=("old style", 20,"bold"), bg="white", ).place(x=370, y=60)
        lbl_contact = Label(self.root, text="Contact",font=("old style", 20,"bold"), bg="white", ).place(x=370, y=100)
        lbl_admission = Label(self.root, text="Admission",font=("old style", 20,"bold"), bg="white", ).place(x=370, y=140)
        lbl_course= Label(self.root, text="Course",font=("old style", 20,"bold"), bg="white", ).place(x=370, y=180)
        
        # Fields
        self.course_list=["Empty"]
        # Function_call to update the list
        self.fetch_course()
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("old style", 20,"bold"), bg="lightblue", ).place(x=480, y=60, width=200)
        txt_contact = Entry(self.root,textvariable=self.var_contact, font=("old style", 20,"bold"), bg="lightblue", ).place(x=500, y=100, width=200)
        txt_admission = Entry(self.root,textvariable=self.var_a_date,  font=("old style", 20,"bold"), bg="lightblue", ).place(x=540, y=140, width=200)
        self.txt_address= Text(self.root, font=("old style", 20,"bold"), bg="lightblue", )
        self.txt_course = ttk.Combobox(self.root,textvariable=self.var_course, values=(self.course_list), font=("old style", 20,"bold"), state="readonly", justify=CENTER )
        self.txt_course.place(x=500, y=180,width=200)
        self.txt_course.set("Empty")
        
        
        
        self.txt_address= Text(self.root, font=("old style", 20,"bold"), bg="lightblue", )
        self.txt_address.place(x=180, y=270, width=500, height=100)
        
        # Buttons
        self.btn_add=Button(self.root, text="Save", font=("goudy old style", 17, "bold"), bg="#ff5733", fg="white", cursor="hand2", command=self.add)
        self.btn_add.place(x=180, y=450, width=110, height=40)
        self.btn_update=Button(self.root, text="Update", font=("goudy old style", 17, "bold"), bg="#ff3333", fg="white", cursor="hand2", command=self.update)
        self.btn_update.place(x=300, y=450, width=110, height=40)
        self.btn_delete=Button(self.root, text="Delete", font=("goudy old style", 17, "bold"), bg="#ff5710", fg="white", cursor="hand2" ,command=self.delete)
        self.btn_delete.place(x=420, y=450, width=110, height=40)       
        self.btn_clear=Button(self.root, text="Clear", font=("goudy old style", 17, "bold"), bg="#ff5983", fg="white", cursor="hand2", command=self.clear)
        self.btn_clear.place(x=550, y=450, width=110, height=40)
        # Search panel
        self.var_search = StringVar()
        lbl_search_roll = Label(self.root, text="Roll no", font=("old style", 20,"bold"), fg="black",bg="white" ).place(x=670, y=60)
        txt_search_roll= Entry(self.root, textvariable=self.var_roll, font=("old style", 20,"bold"), bg="lightblue", ).place(x=780, y=60, width=200)
        btn_search=Button(self.root, text="Search", font=("goudy old style", 17, "bold"), bg="#ff5733", fg="white", cursor="hand2",command=self.search).place(x=1000,y=60,width=130,height=30)
        
        # Content
        self.C_Frame=Frame(self.root,bd =2,relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=540, height=440)
        
        scrolly = Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx = Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("roll", "name","email","gender", "dob","contact","admission","course","state","city","pin","address"))
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        
        self.CourseTable.heading("roll",text="Roll no")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("email",text="Email")
        self.CourseTable.heading("gender",text="gender")
        self.CourseTable.heading("dob",text="D-O-B")
        self.CourseTable.heading("contact",text="Contact")
        self.CourseTable.heading("admission",text="Admission")
        self.CourseTable.heading("course",text="Course")
        self.CourseTable.heading("state",text="State")
        self.CourseTable.heading("city",text="City")
        self.CourseTable.heading("pin",text="Pin")
        self.CourseTable.heading("address",text="Address")
        self.CourseTable["show"]='headings'
        self.CourseTable.column("roll",width=80)
        self.CourseTable.column("name",width=120)
        self.CourseTable.column("email",width=150)
        self.CourseTable.column("gender",width=180)
        self.CourseTable.column("dob",width=100)
        self.CourseTable.column("contact",width=100)
        self.CourseTable.column("admission",width=100)
        self.CourseTable.column("course",width=100)
        self.CourseTable.column("state",width=100)
        self.CourseTable.column("city",width=100)
        self.CourseTable.column("pin",width=100)
        self.CourseTable.column("address",width=100)
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)
        self.show()
        self.fetch_course()
        # 
    
    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.txt_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_a_date.set("")
        self.var_course.set("Select")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("") 
        self.txt_address.delete("1.0",END)     
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")
    
    
    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
             if  self.var_roll.get()=="":
                 messagebox.showerror("Error","Roll No should be required ", parent=self.root)
             else:
                 cur.execute("Select * from student where roll =?", (self.var_roll.get(),))
                 row=cur.fetchone()
                 if row==None:
                      messagebox.showerror("Error","please Select a student from the list first", parent=self.root)
                 else:
                      op=messagebox.askyesno("Confirm","Do you really want to delete", parent=self.root)
                      if op==True:
                          cur.execute("delete from student where roll=?", (self.var_roll.get(),))
                          con.commit()
                          messagebox.showinfo("Delete","Studentm,mmnuuui deleted successfully", parent=self.root)
                          self.clear()
                        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")    
                   
                     
        
    def get_data(self,ev):
        self.txt_roll.config(state='readonly')
        r=self.CourseTable.focus()
        content= self.CourseTable.item(r)
        row = content.get("values", []) 
        if not row:
            messagebox.showerror("Error: ","No data selected")
            return   
        
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.txt_gender.set(row[3])
        self.var_dob.set(row[4])
        self.var_contact.set(row[5])
        self.var_a_date.set(row[6])
        self.var_course.set(row[7])
        self.var_state.set(row[8])
        self.var_city.set(row[9])
        self.var_pin.set(row[10]) 
        self.txt_address.delete("1.0",END)    
        self.txt_address.insert(END,row[11])    
        
    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
             if  self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No. should be required ", parent=self.root)
             else:
                 cur.execute("Select * from student where roll =?", (self.var_roll.get(),))
                 row=cur.fetchone()
                 if row==None:
                      messagebox.showerror("Error","Select student from list", parent=self.root)
                 else:
                      cur.execute("update student set name=?, email=?, gender=?, dob=?, contact=?, admission=?, course=?, state=?, city=?, pin=?, address=? where roll=?",( self.var_name.get(), self.var_email.get(), self.txt_gender.get(),self.var_dob.get(),self.var_contact.get(),self.var_a_date.get(),self.var_course.get(),self.var_state.get(),self.var_city.get(),self.var_pin.get(), self.txt_address.get("1.0",END),self.var_roll.get()))
                      con.commit()
                      messagebox.showinfo("Success","Student update successfully", parent=self.root)
                      self.show()                
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")    
        
    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
             if  self.var_roll.get()=="":
                messagebox.showerror("Error","Roll no should be required ",   parent=self.root)
             else:
                 cur.execute("Select * from student where roll =?", (self.var_roll.get(),))
                 row=cur.fetchone()
                 if row!=None:
                      messagebox.showerror("Error","Course name already present", parent=self.root)
                 else:
                      cur.execute("insert into student ( name, email, gender, dob, contact, admission, course, state, city, pin ,address) values(?,?,?,?,?,?,?,?,?,?,?)",(self.var_name.get(), self.var_email.get(), self.txt_gender.get(),self.var_dob.get(),self.var_contact.get(),self.var_a_date.get(),self.var_course.get(),self.var_state.get(),self.var_city.get(),self.var_pin.get(), self.txt_address.get("1.0",END)))
                      con.commit()
                      messagebox.showinfo("Success","Student added Successfully", parent=self.root)
                      self.show()                
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")    
        
    def fetch_course(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
             cur.execute("select name from course")
             rows = cur.fetchall()
             v=[]
             if len(rows)>0:
                 
                 for row in rows:
                     self.course_list.append(row[0])
            
             print(v)
        except Exception as ex:
                   messagebox.showerror("Error", f"Error due to {str(ex)}")    
        
   
    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
             cur.execute("Select * FROM student")
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
             cur.execute("Select * FROM student")
             row=cur.fetchone()
             if row!=None: 
                self.CourseTable.delete(*self.CourseTable.get_children()) 
                self.CourseTable.insert('',END, values=row)
             else:     
                 messagebox.showerror("Error","No record found ", parent=self.root)       
                  
                
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")    
        
if __name__ =="__main__":
    root = Tk()
    obj  = StudentClass(root)
    root.mainloop()    