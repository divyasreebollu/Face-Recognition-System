from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root,bg="blue"):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        #title
        title_lb1=Label(self.root,text="DEVELOPER",font=("times new roman",25,"bold"),bg="light pink",fg="dark blue")
        title_lb1.place(x=0,y=0,width=1300,height=30)

        #backgroud image
        img3=Image.open(r"college_images\green.jpg")
        img3=img3.resize((1350,700),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1300,height=700)

        #top photo
        img_top=Image.open(r"college_images\pix.jpg")
        img_top=img_top.resize((1300,600),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lb1=Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=37,width=1300,height=600)

        #frame
        main_frame=Frame(f_lb1,bd=2,bg="white")
        main_frame.place(x=900,y=0,width=600,height=500)

        img_top1=Image.open(r"college_images\sivangi.jpg")
        img_top1=img_top1.resize((180,180),Image.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lb1=Label(main_frame,image=self.photoimg_top1)
        f_lb1.place(x=190,y=0,width=180,height=180)

        #Developer info
        dev_label=Label(main_frame,text="hello my name,Shivagi Joshi",font=("times new roman",11,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="I am actress",font=("times new roman",12,"bold"),bg="white")
        dev_label.place(x=0,y=30)

        img3=Image.open(r"college_images\hd.jpg")
        img3=img3.resize((500,320),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lb1=Label(main_frame,image=self.photoimg3)
        f_lb1.place(x=0,y=185,width=500,height=320)







if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
