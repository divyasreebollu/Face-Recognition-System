from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import tkinter

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #first img
        img=Image.open(r"college_images\clge.jpg")
        img=img.resize((400,140),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1=Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=400,height=140)

        #second image
        img1=Image.open(r"college_images\fr.jpg")
        img1=img1.resize((400,140),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lb1=Label(self.root,image=self.photoimg1)
        f_lb1.place(x=400,y=0,width=400,height=140)

        #third image
        img2=Image.open(r"college_images\stu.jpg")
        img2=img2.resize((500,140),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lb1=Label(self.root,image=self.photoimg2)
        f_lb1.place(x=800,y=0,width=500,height=140)

        #backgroud image
        img3=Image.open(r"college_images\green.jpg")
        img3=img3.resize((1350,700),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1300,height=700)

        #title
        title_lb1=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",25,"bold"),bg="pink",fg="darkblue")
        title_lb1.place(x=0,y=0,width=1350,height=40)

        #=========================time=============================
        def time():
            string = strftime('%H:%M:%S %p')
            lb1.config(text = string)
            lb1.after(1000, time)
        
        lb1=Label(title_lb1,font=('times new romam',14,'bold'),background='white',foreground='blue')
        lb1.place(x=0,y=0,width=117,height=35)
        time()
        
        #student details BUTTON
        img4=Image.open(r"college_images\STUDENT DETAILS.png")
        img4=img4.resize((200,140),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=70,y=50,width=200,height=150)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=70,y=190,width=200,height=30)

        #face detection BUTTON
        img5=Image.open(r"college_images\FACE RECOGNITION.jpg")
        img5=img5.resize((200,140),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=50,width=200,height=150)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=190,width=200,height=30)

        #attendance BUTTON
        img6=Image.open(r"college_images\ATTENDANCE.jpg")
        img6=img6.resize((200,140),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=700,y=50,width=200,height=150)

        b1_1=Button(bg_img,text="Attendance",command=self.attendance_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=190,width=200,height=30)

        #HELP DESK BUTTON
        img7=Image.open(r"college_images\HELP.png")
        img7=img7.resize((200,140),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1050,y=50,width=200,height=150)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1050,y=190,width=200,height=30)

        #Train data
        img8=Image.open(r"college_images\TRAIN DATA.jpg")
        img8=img8.resize((200,140),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=70,y=300,width=200,height=150)

        b1_1=Button(bg_img,text="Train data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=70,y=430,width=200,height=30)

        #photos Button
        img9=Image.open(r"college_images\PHOTOS.jpg")
        img9=img9.resize((200,140),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=300,width=200,height=150)

        b1_1=Button(bg_img,text="photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=430,width=200,height=30)

        #developer
        img10=Image.open(r"college_images\DEVELOPER.png")
        img10=img10.resize((200,140),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=700,y=300,width=200,height=150)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=430,width=200,height=30)

        #exit button
        img11=Image.open(r"college_images\EXIT.jpg")
        img11=img11.resize((200,140),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1050,y=300,width=200,height=150)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1050,y=430,width=200,height=30)
    
    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

    #============function====================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)


if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
