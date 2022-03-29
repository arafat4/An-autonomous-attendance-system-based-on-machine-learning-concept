from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x500")
        self.root.title("Face Recognition System")


        
        title_lbl=Label(self.root,text="DEVELOPER", font=("times new roman",30,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1250,height=30)


        # img_top=Image.open(r"C:\Users\arafat\Desktop\picture\college.jpg")
        # img_top=img_top.resize((1420,700),Image.ANTIALIAS)
        # self.photoimg_top=ImageTk.PhotoImage(img_top)

        # f_lbl=Label(self.root,image=self.photoimg_top)
        # f_lbl.place(x=0,y=55,width=1420,height=700)

        # Frame
        # main_frame=Frame(self.root,bd=2, bg="white")
        # main_frame.place(x=0,y=30,width=1250, height=450)


        # img_top1=Image.open(r"C:\Users\arafat\Desktop\picture\college.jpg")
        # img_top1=img_top1.resize((150,150),Image.ANTIALIAS)
        # self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        # f_lbl=Label(main_frame)
        # f_lbl.place(x=0,y=0,width=150,height=500)

        
        # Developer info
        dev_label=Label(self.root,text="Mohammad Arafat Hossain", font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=495,y=130)

        dev_label=Label(self.root,text="Full Stack Web Developer", font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=495,y=170)

        dev_label=Label(self.root,text="BSC in Computer Science", font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=495,y=210)

        dev_label=Label(self.root,text="Southsest Forestry University", font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=495,y=250)


        # #third image
        # img2=Image.open(r"C:\Users\arafat\Desktop\picture\college.jpg")
        # img2=img2.resize((400,400),Image.ANTIALIAS)
        # self.photoimg2=ImageTk.PhotoImage(img2)

        # f_lbl=Label(main_frame,image=self.photoimg2)
        # f_lbl.place(x=0,y=220,width=400,height=400)


if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()