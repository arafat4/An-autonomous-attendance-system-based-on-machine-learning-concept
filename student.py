from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x500")
        self.root.title("face Recognition System")

        #######################variables#################
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


        self.searchTxt_var = StringVar()
        self.search_var = StringVar() 

        # #first image
        # img=Image.open(r"C:\Users\arafat\Desktop\picture\college.jpg")
        # img=img.resize((500,50),Image.ANTIALIAS)
        # self.photoimg=ImageTk.PhotoImage(img)

        # f_lbl=Label(self.root,image=self.photoimg)
        # f_lbl.place(x=0,y=0,width=450,height=50)


        # #second image
        # img1=Image.open(r"C:\Users\arafat\Desktop\picture\FR.jpg")
        # img1=img1.resize((500,50),Image.ANTIALIAS)
        # self.photoimg1=ImageTk.PhotoImage(img1)

        # f_lbl=Label(self.root,image=self.photoimg1)
        # f_lbl.place(x=450,y=0,width=450,height=50)

        # #third image
        # img2=Image.open(r"C:\Users\arafat\Desktop\picture\college.jpg")
        # img2=img2.resize((500,50),Image.ANTIALIAS)
        # self.photoimg2=ImageTk.PhotoImage(img2)

        # f_lbl=Label(self.root,image=self.photoimg2)
        # f_lbl.place(x=900,y=0,width=500,height=50)

        #background image
        img3=Image.open(r"C:\Users\arafat\Desktop\picture\bg.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM", font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=30)

        main_frame=Frame(bg_img,bd=2, bg="white")
        main_frame.place(x=5,y=0,width=1335, height=630)

        #left level frame
        left_frame=LabelFrame(main_frame,bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"))
        left_frame.place(x=0,y=0,width=645,height=450)


        # img_left=Image.open(r"C:\Users\arafat\Desktop\picture\college.jpg")
        # img_left=img_left.resize((640,30),Image.ANTIALIAS)
        # self.photoimg_left=ImageTk.PhotoImage(img_left)

        # f_lbl=Label(left_frame,image=self.photoimg2)
        # f_lbl.place(x=5,y=0,width=630,height=70)

        #current course information
        current_course_frame=LabelFrame(left_frame,bd=2, bg="white", relief=RIDGE, text="Current course information", font=("times new roman",12,"bold"))
        current_course_frame.place(x=0,y=0,width=630,height=110)

        #Department
        dep_label=Label(current_course_frame,text="Department", font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0, column=0,padx=10, sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly", width=20)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2,pady=10, sticky=W)


        #Course
        Course_label=Label(current_course_frame,text="Course", font=("times new roman",12,"bold"),bg="white")
        Course_label.grid(row=0, column=2,padx=10, sticky=W)

        Course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly", width=20)
        Course_combo["values"]=("Select Course","FE","SE","TE","BE")
        Course_combo.current(0)
        Course_combo.grid(row=0, column=3, padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(current_course_frame,text="Year", font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1, column=0,padx=10, sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly", width=20)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2,pady=10,sticky=W)

        #Semester
        semester_label=Label(current_course_frame,text="Semester", font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1, column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly", width=20)
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2,pady=10,sticky=W)


        #Class Student Information
        class_student_frame=LabelFrame(left_frame,bd=2, bg="white", relief=RIDGE, text="Class Student information", font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=125,width=630,height=300)

        #student id
        studentId_label=Label(class_student_frame,text="StudentID:", font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0, column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        studentName_label=Label(class_student_frame,text="StudentName:", font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0, column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division name
        class_div_label=Label(class_student_frame,text="Class Division:", font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1, column=0,padx=8,pady=5,sticky=W)

        # class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly", width=18)
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=8,pady=8,sticky=W)

        #Roll No
        roll_no_label=Label(class_student_frame,text="Roll No:", font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1, column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_student_frame,text="Gender:", font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2, column=0,padx=9,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly", width=18)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=9,pady=8,sticky=W)

        #Date of Birth
        dob_label=Label(class_student_frame,text="DOB:", font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2, column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        email_label=Label(class_student_frame,text="Email:", font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3, column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        #phone no
        phone_label=Label(class_student_frame,text="Phone No:", font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3, column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        #Address
        address_label=Label(class_student_frame,text="Address:", font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4, column=0,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        #Teacher name
        teacher_label=Label(class_student_frame,text="Teacher Name:", font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4, column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take photo sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radiobtn2.grid(row=6,column=1)

        # save buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=625,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=240,width=625,height=35)
        
        take_photo_btn=Button(btn_frame,text="Take photo sample",command=self.generate_dataset,width=31,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        
        update_photo_btn=Button(btn_frame,text="Update photo sample",width=31,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)
    














        #right lavel frame
        right_frame=LabelFrame(main_frame,bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"))
        right_frame.place(x=680,y=0,width=645,height=700)


        # img_right=Image.open(r"C:\Users\arafat\Desktop\picture\college.jpg")
        # img_right=img_right.resize((640,30),Image.ANTIALIAS)
        # self.photoimg_right=ImageTk.PhotoImage(img_right)

        # f_lbl=Label(right_frame,image=self.photoimg2)
        # f_lbl.place(x=5,y=0,width=630,height=60)

        # Search system

        search_frame=LabelFrame(right_frame,bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=0,width=630,height=70)

        search_label=Label(search_frame,text="Search By:", font=("times new roman",10,"bold"),bg="red",fg="white")
        search_label.grid(row=0, column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",10,"bold"),state="readonly", width=15,textvariable=self.search_var)
        search_combo["values"]=("Select","Roll","Phone")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=20,textvariable=self.searchTxt_var,font=("times new roman",10,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=15,command=self.search_data,font=("times new roman",8,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)



        showAll_btn=Button(search_frame,text="Show All",width=15,command=self.show_data,font=("times new roman",8,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        #table frame
        table_frame=Frame(right_frame,bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5,y=70,width=630,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #################function declaration##################

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_semester.get(),
                                                                                                self.var_std_id.get(),
                                                                                                self.var_std_name.get(),
                                                                                                self.var_div.get(),
                                                                                                self.var_roll.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_teacher.get(),
                                                                                                self.var_radio1.get()
                                                                                                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
# *************fetch data*************
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
        for i in data:
                self.student_table.insert("",END,values=i)
        conn.commit()
        conn.close()

# **************get cursor**************
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Upadate","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where StudentId=%s",(
                                                                    
                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                        self.var_std_id.get()
                                                                                                                                                                        ))
                    
                else:
                    if not Update:
                        return 
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To{str(es)}",parent=self.root)


                # *********delete function************

    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>=0:
                    conn=mysql.connector.connect(host="localhost",username="root",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where StudentId=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To{str(es)}",parent=self.root)

#reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_name.set("")
        self.var_std_id.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # ******************Generate data set or take photo sample*********************

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where StudentId=%s",(    
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get(),
                                                                                                            self.var_std_id.get()==id+1
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                # ************load predifined data on face frontal from opencv**************
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling faction=1.3
                    #Minimum Neighbour=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))       
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)      
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"      
                        cv2.imwrite(file_name_path,face)     
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Cropped Face",face)     

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!!")
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    
    def search_data(self):
        if self.searchTxt_var.get()=="" or self.search_var.get()=="Select Option":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student where " +str(self.search_var.get())+" LIKE '%"+str(self.searchTxt_var.get())+"%'")
                rows=my_cursor.fetchall()         
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    
    def show_data(self):

        conn=mysql.connector.connect(host="localhost",username="root",database="face_recognizer")
        my_cursor=conn.cursor()

        

        my_cursor.execute("SELECT * from student")
        rows = my_cursor.fetchall()

        if(len(rows)!=0):

            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values=row)

        conn.commit()
        conn.close()

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()