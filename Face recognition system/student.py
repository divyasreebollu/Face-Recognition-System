from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root,bg="blue"):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #=================variables===============
        
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone_no=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


        #first img
        img=Image.open(r"C:\Users\B Divya sreee\Desktop\Face recognition system\college_images\stu.jpg")
        img=img.resize((400,140),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1=Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=400,height=140)

        #second image
        img1=Image.open(r"C:\Users\B Divya sreee\Desktop\Face recognition system\college_images\s.jpg")
        img1=img1.resize((400,140),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lb1=Label(self.root,image=self.photoimg1)
        f_lb1.place(x=400,y=0,width=400,height=140)

        #third image
        img2=Image.open(r"C:\Users\B Divya sreee\Desktop\Face recognition system\college_images\st.jpg")
        img2=img2.resize((500,140),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lb1=Label(self.root,image=self.photoimg2)
        f_lb1.place(x=800,y=0,width=500,height=140)

        #backgroud image
        img3=Image.open(r"C:\Users\B Divya sreee\Desktop\Face recognition system\college_images\green.jpg")
        img3=img3.resize((1350,700),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1300,height=700)

        #title
        title_lb1=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="light pink",fg="dark blue")
        title_lb1.place(x=0,y=0,width=1300,height=30)

        main_frame=Frame(bg_img,bd=2,bg="light blue")
        main_frame.place(x=3,y=32,width=1350,height=500)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=6,y=6,width=615,height=450)

        img_left=Image.open(r"C:\Users\B Divya sreee\Desktop\Face recognition system\college_images\s.jpg")
        img_left=img_left.resize((650,100),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lb1=Label(Left_frame,image=self.photoimg_left)
        f_lb1.place(x=5,y=0,width=600,height=90)

         #current course information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=6,y=90,width=600,height=100)

        #Department
        dept_label=Label(current_course_frame,text="Department",font=("times new roman",10,"bold"),bg="white")
        dept_label.grid(row=0,column=0,padx=2,pady=1,sticky=W)

        dept_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),state="read only",width=20)
        dept_combo["values"]=("Select Department","CSE","CSD","CSM","CIVIL","EEE","ECE","MECH")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,padx=2,pady=1,sticky=W)

        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",10,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,pady=1,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",10,"bold"),state="read only",width=20)
        course_combo["values"]=("Select course","CD","AAD","AI-ML","MS","LSE","UHV")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=5,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",10,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=5,sticky=W)

        year_label_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",10,"bold"),state="read only",width=20)
        year_label_combo["values"]=("Select Year","2021-2022","2022-2023","2023-2024","2024-2025")
        year_label_combo.current(0)
        year_label_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        #semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",10,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=5,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",10,"bold"),state="read only",width=20)
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #class student information
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=190,width=600,height=230)
            #studentname
        studentName_label=Label(class_Student_frame,text="Student Name:",font=("times new roman",10,"bold"),bg="white")
        studentName_label.grid(row=0,column=0,padx=10,sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_std_name,font=("times new roman",10,"bold"))
        studentName_entry.grid(row=0,column=1,padx=10,sticky=W)

        #student id
        studentId_label=Label(class_Student_frame,text="Student Id:",font=("times new roman",10,"bold"),bg="white")
        studentId_label.grid(row=0,column=2,padx=5,sticky=W)

        studentId_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_std_id,font=("times new roman",10,"bold"))
        studentId_entry.grid(row=0,column=3,padx=5,sticky=W)

        #Teacher
        teacher_label=Label(class_Student_frame,text="Teacher:",font=("times new roman",10,"bold"),bg="white")
        teacher_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_teacher,font=("times new roman",10,"bold"))
        teacher_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #gender
        gender_label=Label(class_Student_frame,text="Gender:",font=("times new roman",10,"bold"),bg="white")
        gender_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        gender_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_gender,font=("times new roman",10,"bold"))
        gender_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",10,"bold"),state="read only",width=18)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=5,pady=5,sticky=W)


        #place
        place_label=Label(class_Student_frame,text="Address:",font=("times new roman",10,"bold"),bg="white")
        place_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        place_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_address,font=("times new roman",10,"bold"))
        place_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #dob
        dob_label=Label(class_Student_frame,text="DOB:",font=("times new roman",10,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_dob,font=("times new roman",10,"bold"))
        dob_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        #email
        email_label=Label(class_Student_frame,text="Email:",font=("times new roman",10,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_email,font=("times new roman",10,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone no
        phone_no_label=Label(class_Student_frame,text="Phone no:",font=("times new roman",10,"bold"),bg="white")
        phone_no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_no_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_phone_no,font=("times new roman",10,"bold"))
        phone_no_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)

        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=4,column=0)

        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio2,text="No Photo Sample",value="Yes")
        radiobtn2.grid(row=4,column=1)

        #button frame   save,update,delete,reset
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=140,width=590,height=30)

        save_button=Button(btn_frame,text="Save",command=self.add_data,width=20,font=("times new roman",10,"bold"),bg="green",fg="white")
        save_button.grid(row=0,column=0)

        update_button=Button(btn_frame,text="Update",command=self.update_data,width=20,font=("times new roman",10,"bold"),bg="green",fg="white")
        update_button.grid(row=0,column=1)

        delete_button=Button(btn_frame,text="Delete",command=self.delete_data,width=20,font=("times new roman",10,"bold"),bg="green",fg="white")
        delete_button.grid(row=0,column=2)

        reset_button=Button(btn_frame,text="Reset",command=self.reset_data,width=20,font=("times new roman",10,"bold"),bg="green",fg="white")
        reset_button.grid(row=0,column=3)


        #button frame
        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=170,width=590,height=30)
    
        take_photo_button=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=45,font=("times new roman",10,"bold"),bg="green",fg="white")
        take_photo_button.grid(row=1,column=0)

        update_photo_button=Button(btn_frame1,text="Update Photo Sample",width=45,font=("times new roman",10,"bold"),bg="green",fg="white")
        update_photo_button.grid(row=1,column=1)


        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=630,y=6,width=630,height=450)

            #image
        img_right=Image.open(r"C:\Users\B Divya sreee\Desktop\Face recognition system\college_images\s.jpg")
        img_right=img_right.resize((650,100),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lb1=Label(Right_frame,image=self.photoimg_right)
        f_lb1.place(x=5,y=0,width=610,height=90)

            #-----------------Search system-------------------------
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=90,width=610,height=60)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",10,"bold"),bg="brown",fg="white")
        search_label.grid(row=0,column=0,padx=10,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",10,"bold"),state="read only",width=15)
        search_combo["values"]=("Select","Student_Id","Phone_no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",10,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)


        search_button=Button(search_frame,text="Search",width=12,font=("times new roman",10,"bold"),bg="green",fg="white")
        search_button.grid(row=0,column=3,padx=4)

        search_button=Button(search_frame,text="Show All",width=12,font=("times new roman",10,"bold"),bg="green",fg="white")
        search_button.grid(row=0,column=4,padx=4)

        # ==================table frame=================
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=6,y=170,width=610,height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","name","id","teacher","gender","address","dob","email","phone","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)     
        scroll_x.config(command=self.student_table.xview)  
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Departmet") 
        self.student_table.heading("course",text="Course") 
        self.student_table.heading("year",text="Year") 
        self.student_table.heading("sem",text="Semester") 
        self.student_table.heading("name",text="StudentName")  
        self.student_table.heading("id",text="StudentId")  
        self.student_table.heading("teacher",text="Teacher") 
        self.student_table.heading("gender",text="Gender") 
        self.student_table.heading("address",text="Address")
        self.student_table.heading("dob",text="DOB") 
        self.student_table.heading("email",text="Email") 
        self.student_table.heading("phone",text="Phone") 
        self.student_table.heading("photo",text="Photo") 
        self.student_table["show"]="headings"

        self.student_table.column("dep",width="100") 
        self.student_table.column("course",width="100") 
        self.student_table.column("year",width="100") 
        self.student_table.column("sem",width="100") 
        self.student_table.column("name",width="100")  
        self.student_table.column("id",width="100") 
        self.student_table.column("teacher",width="100") 
        self.student_table.column("gender",width="100") 
        self.student_table.column("address",width="100") 
        self.student_table.column("dob",width="100") 
        self.student_table.column("email",width="100") 
        self.student_table.column("phone",width="100")  
        self.student_table.column("photo",width="100")

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #==========Function button==============================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="sree",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_semester.get(),
                                                                                                self.var_std_name.get(),
                                                                                                self.var_std_id.get(),
                                                                                                self.var_teacher.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone_no.get(),
                                                                                                self.var_radio1.get()                                                                             
                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)    

    #==================================fetch data============================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="sree",database="face_recognizer")            
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()    

        #==================get cursor====================================
    def get_cursor(self,event):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_name.set(data[4]),
        self.var_std_id.set(data[5]),
        self.var_teacher.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_address.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone_no.set(data[11]),
        self.var_radio1.set(data[12])

    #================update function=====================
        
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="sree",database="face_recognizer")            
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set dep=%s,course=%s,year=%s,sem=%s,std_id=%s,teacher=%s,gender=%s,address=%s,dob=%s,email=%s,phone=%s,photo=%s where std_name=%s",(
                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_semester.get(),
                                                                                                self.var_std_id.get(),
                                                                                                self.var_teacher.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone_no.get(),
                                                                                                self.var_radio1.get(),  
                                                                                                self.var_std_name.get(),               
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details Successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)   
    #delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="sree",database="face_recognizer")            
                    my_cursor=conn.cursor()
                    sql="delete from student where std_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Succesfully deleted student details",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    #reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_name.set("")
        self.var_std_id.set("")
        self.var_teacher.set("")
        self.var_gender.set("Male")
        self.var_address.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone_no.set("")
        self.var_radio1.set("")



#========================= Generate data set or take photo sample =====================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="sree",database="face_recognizer")            
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set dep=%s,course=%s,year=%s,sem=%s,std_name=%s,teacher=%s,gender=%s,address=%s,dob=%s,email=%s,phone=%s,photo=%s where std_id=%s",(
                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_semester.get(),
                                                                                                self.var_std_name.get(),
                                                                                                self.var_teacher.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone_no.get(),
                                                                                                self.var_radio1.get(),  
                                                                                                self.var_std_id.get()==id+1             
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #===============Load predefined data on facefrontals from opencv=========

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    # conver gary sacle
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,2.5,10)
                    #Scaling factor 1.3
                    # Minimum naber 5
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(200,200))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(30,30),cv2.FONT_HERSHEY_COMPLEX,2,(0,200,0),2)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(img_id)==20:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed!!!!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)




if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()