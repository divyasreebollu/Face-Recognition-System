from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self,root,bg="blue"):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        #title
        title_lb1=Label(self.root,text="HELP DESK",font=("times new roman",25,"bold"),bg="violet",fg="dark blue")
        title_lb1.place(x=0,y=0,width=1300,height=30)

        #backgroud image
        img3=Image.open(r"college_images\green.jpg")
        img3=img3.resize((1350,700),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1300,height=700)

        #top photo
        img_top=Image.open(r"college_images\lap.jpg")
        img_top=img_top.resize((1300,600),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lb1=Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=0,y=37,width=1300,height=600)

        dev_label=Label(f_lb1,text="Email:shivangijoshi@123gmail.com",font=("times new roman",12,"bold"),bg="white")
        dev_label.place(x=500,y=250)




if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()