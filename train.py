from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x500")
        self.root.title("face Recognition System")


        title_lbl=Label(self.root,text="TRAIN DATASET", font=("times new roman",30,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1250,height=30)


        # img_top=Image.open(r"C:\Users\arafat\Desktop\picture\college.jpg")
        # img_top=img_top.resize((1420,700),Image.ANTIALIAS)
        # self.photoimg_top=ImageTk.PhotoImage(img_top)

        # f_lbl=Label(self.root,image=self.photoimg_top)
        # f_lbl.place(x=0,y=55,width=1420,height=100)

        #button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=160,width=220,height=40)


        # img_bottom=Image.open(r"C:\Users\arafat\Desktop\picture\college.jpg")
        # img_bottom=img_bottom.resize((1500,300),Image.ANTIALIAS)
        # self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        # f_lbl=Label(self.root,image=self.photoimg_bottom)
        # f_lbl.place(x=0,y=200,width=1500,height=100)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # =================== Train the classifier And save==================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")




if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()