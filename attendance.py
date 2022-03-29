from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x500")
        self.root.title("face Recognition System")

        # **********variables*********
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        # #first image
        # img=Image.open(r"C:\Users\arafat\Desktop\picture\college.jpg")
        # img=img.resize((700,100),Image.ANTIALIAS)
        # self.photoimg=ImageTk.PhotoImage(img)

        # f_lbl=Label(self.root,image=self.photoimg)
        # f_lbl.place(x=0,y=0,width=700,height=100)


        # #second image
        # img1=Image.open(r"C:\Users\arafat\Desktop\picture\FR.jpg")
        # img1=img1.resize((700,100),Image.ANTIALIAS)
        # self.photoimg1=ImageTk.PhotoImage(img1)

        # f_lbl=Label(self.root,image=self.photoimg1)
        # f_lbl.place(x=650,y=0,width=800,height=100)


        
        #background image
        img3=Image.open(r"C:\Users\arafat\Desktop\picture\bg.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman",30,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=30)

        main_frame=Frame(bg_img,bd=2, bg="white")
        main_frame.place(x=5,y=0,width=1335, height=630)

        #left level frame
        left_frame=LabelFrame(main_frame,bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=0,width=600,height=450)

        
        # img_left=Image.open(r"C:\Users\arafat\Desktop\picture\college.jpg")
        # img_left=img_left.resize((640,60),Image.ANTIALIAS)
        # self.photoimg_left=ImageTk.PhotoImage(img_left)

        # f_lbl=Label(left_frame,image=self.photoimg3)
        # f_lbl.place(x=5,y=0,width=630,height=140)



        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE, bg="white")
        left_inside_frame.place(x=0,y=0,width=570, height=420)

        # Label and entry

        # attendance id
        attendanceId_label=Label(left_inside_frame,text="attendanceId:", font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0, column=0,padx=10,pady=5,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        # Roll
        Roll_label=Label(left_inside_frame,text="Roll:", font=("times new roman",12,"bold"),bg="white")
        Roll_label.grid(row=1, column=0,padx=10,pady=5,sticky=W)

        Roll_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        Roll_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        

        # Name
        Name_label=Label(left_inside_frame,text="Name:", font=("times new roman",12,"bold"),bg="white")
        Name_label.grid(row=2, column=0,padx=10,pady=5,sticky=W)

        Name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        Name_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # Department
        Depeartment_label=Label(left_inside_frame,text="Depeartment:", font=("times new roman",12,"bold"),bg="white")
        Depeartment_label.grid(row=3, column=0,padx=10,pady=5,sticky=W)

        Depeartment_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        Depeartment_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # Department
        Time_label=Label(left_inside_frame,text="Time:", font=("times new roman",12,"bold"),bg="white")
        Time_label.grid(row=4, column=0,padx=10,pady=5,sticky=W)

        Time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        Time_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # Date
        Date_label=Label(left_inside_frame,text="Date:", font=("times new roman",12,"bold"),bg="white")
        Date_label.grid(row=5, column=0,padx=10,pady=5,sticky=W)

        Date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        Date_entry.grid(row=5,column=1,padx=10,pady=5,sticky=W)


        #attendance
        Attendance_label=Label(left_inside_frame,text="Attendance Status:", font=("times new roman",12,"bold"),bg="white")
        Attendance_label.grid(row=6, column=0,padx=10,pady=5,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,width=18,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=6,column=1,pady=5)
        self.atten_status.current(0)


         # save buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=350,width=550,height=35)

        import_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)

        export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,text="Update csv",command=self.action,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=13,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)





        #right lavel frame
        right_frame=LabelFrame(main_frame,bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman",12,"bold"))
        right_frame.place(x=610,y=0,width=600,height=450)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=0,y=0,width=600,height=420)

        # **********Scroll bar Table****************
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)


        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        

# *************fetch data*****************

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)


    # export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow (i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
        
        except Exception as es:
                messagebox.showerror("Error",f"Due To{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")



        #export upadte
    def action(self):
        id=self.var_atten_id.get()
        roll=self.var_atten_roll.get()
        name=self.var_atten_name.get()
        dep=self.var_atten_dep.get()
        time=self.var_atten_time.get()
        date=self.var_atten_date.get()
        attendn=self.var_atten_attendance.get()

        # write to csv file
        try:
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="a",newline="\n") as f:
                dict_writer=csv.DictWriter(f,fieldnames=(["ID","Roll","Name","Department","Time","Date","Attendance"]))
                dict_writer.writeheader()
                dict_writer.writerow({
                "ID":id,
                "Roll":roll,
                "Name":name,
                "Department":dep,
                "Time":time,
                "Date":date,
                "Attendance":attendn 
                    })
            messagebox.showinfo("Data Exported","Your data exported to " +os.path.basename(fln)+ " Successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
        




if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()