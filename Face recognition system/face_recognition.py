from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import os
import numpy as np
import mysql.connector #pip install mysql.connector-python
import cv2         #pip install opencv-python

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lb1=Label(self.root,text="FACE RECOGNITION",font=("times new roman",25,"bold"),bg="light pink",fg="dark blue")
        title_lb1.place(x=0,y=0,width=1300,height=30)

        #1st image
        img_top=Image.open(r"college_images\f_det.jpg")
        img_top=img_top.resize((550,570),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lb1=Label(self.root,image=self.photoimg_top)
        f_lb1.place(x=5,y=55,width=550,height=570)

        #2nd image
        img_bottom=Image.open(r"college_images\FACE RECOGNITION.jpg")
        img_bottom=img_bottom.resize((720,570),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lb1=Label(self.root,image=self.photoimg_bottom)
        f_lb1.place(x=550,y=55,width=720,height=570)

        b1_1=Button(f_lb1,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",15,"bold"),bg="red",fg="white")
        b1_1.place(x=300,y=500,width=200,height=30)
        #========================attendance==========
    def mark_attendance(self,r,n,d,e):
        with open("divya.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))  
                name_list.append(entry[0])
            if((r not in name_list) and (n not in name_list) and (d not in name_list) and (e not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{r},{n},{d},{e},{dtString},{d1},Present")


        #face recognition
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="sree",database="face_recognizer")            
                my_cursor=conn.cursor()

                my_cursor.execute("select std_id from student where std_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select std_name from student where std_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select dep from student where std_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select email from student where std_id="+str(id))
                e=my_cursor.fetchone()
                e="+".join(e)


                if confidence > 77:
                    cv2.putText(img,f"roll no:{r}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"name:{n}",(x,y-50),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"dep:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"email:{e}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(r,n,d,e)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)    

                coord=[x,y,w,y]
            
            return coord    


        #==========
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf= cv2.face.LBPHFaceRecognizer_create() #pip install opencv-contrib-python
        clf.read("clf.xml")

        videoCap=cv2.VideoCapture(0)

        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Detector",img)

            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()