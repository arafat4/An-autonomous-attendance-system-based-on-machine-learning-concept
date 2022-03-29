from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x500")
        self.root.title("face Recognition System")


        
        title_lbl=Label(self.root,text="HELP DESK", font=("times new roman",30,"bold"),bg="white",fg="blue")
        title_lbl.place(x=-0,y=0,width=1420,height=30)


        # img_top=Image.open(r"C:\Users\arafat\Desktop\picture\college.jpg")
        # img_top=img_top.resize((1420,700),Image.ANTIALIAS)
        # self.photoimg_top=ImageTk.PhotoImage(img_top)

        # f_lbl=Label(self.root,image=self.photoimg_top)
        # f_lbl.place(x=0,y=55,width=1420,height=700)


        # Developer info
        dev_label=Label(self.root,text="Email:arafathoss28@gmail.com", font=("times new roman",14,"bold"),bg="blue")
        dev_label.place(x=500,y=150)

        dev_label=Label(self.root,text="Phone Number:+86-13211694428", font=("times new roman",14,"bold"),bg="blue")
        dev_label.place(x=500,y=190)

        dev_label=Label(self.root,text="Whatsapp: +86-13211694428", font=("times new roman",14,"bold"),bg="blue")
        dev_label.place(x=500,y=230)




if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()