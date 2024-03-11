from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import numpy as np
import mysql.connector
import cv2

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Panel")

        title_lb1=Label(self.root,text="TRAIN DATA SET",font=("times new roman",25,"bold"),bg="light pink",fg="dark blue")
        title_lb1.place(x=0,y=0,width=1300,height=30)

        #backgroud image
        img3=Image.open(r"college_images\green.jpg")
        img3=img3.resize((1350,700),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1300,height=700)

        #top photo
        img_top=Image.open(r"college_images\face.jpg")
        img_top=img_top.resize((1300,400),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lb1=Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=55,width=1300,height=250)
        
        #button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",15,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=0,y=307,width=1300,height=40)

        #bottom photo
        img_bottom=Image.open(r"college_images\tr.jpg")
        img_bottom=img_bottom.resize((1300,400),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lb1=Label(self.root,image=self.photoimg_bottom)
        f_lb1.place(x=0,y=350,width=1300,height=250)
    
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #Gray scale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #=================Train Classifier=============
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("clf.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Completed!!!!!")



        

if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()