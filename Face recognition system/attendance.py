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
    def __init__(self,root,bg="blue"):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Attendance System")

        #==================================variables========================
        self.var_atten_id=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_email=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        #first img
        img=Image.open(r"college_images\stu.jpg")
        img=img.resize((635,140),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lb1=Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=635,height=140)

        #second img
        img1=Image.open(r"college_images\st.jpg")
        img1=img1.resize((636,140),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lb1=Label(self.root,image=self.photoimg1)
        f_lb1.place(x=636,y=0,width=636,height=140)

        #bg image
        img3=Image.open(r"college_images\green.jpg")
        img3=img3.resize((1350,700),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1300,height=700)

        #title
        title_lb1=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="light pink",fg="dark blue")
        title_lb1.place(x=0,y=0,width=1300,height=30)

        main_frame=Frame(bg_img,bd=2,bg="light blue")
        main_frame.place(x=3,y=32,width=1350,height=500)

        #left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="skyblue",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=6,y=6,width=615,height=450)

        img_left=Image.open(r"college_images\s.jpg")
        img_left=img_left.resize((650,100),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lb1=Label(Left_frame,image=self.photoimg_left)
        f_lb1.place(x=5,y=0,width=600,height=90)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="pink")
        left_inside_frame.place(x=0,y=105,width=605,height=320)

        #label and entry
        #attendance Id
        attendanceId_label=Label(left_inside_frame,text="Attendance Id:",font=("times new roman",10,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=5,pady=8)


        attendanceId_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,font=("times new roman",10,"bold"),state="read only",width=20)
        attendanceId_entry.grid(row=0,column=1,padx=5,pady=8)

        #name
        name_label=Label(left_inside_frame,text="Name:",font=("times new roman",10,"bold"),bg="white")
        name_label.grid(row=0,column=2,padx=5,pady=8)


        atten_name_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,font=("times new roman",10,"bold"),state="read only",width=20)
        atten_name_entry.grid(row=0,column=3,padx=5,pady=8)

        #dept
        dept_label=Label(left_inside_frame,text="Department:",font=("times new roman",10,"bold"),bg="white")
        dept_label.grid(row=1,column=0,padx=5,pady=8)


        attendept_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,font=("times new roman",10,"bold"),state="read only",width=20)
        attendept_entry.grid(row=1,column=1,padx=5,pady=8)

        #email
        attenemail_label=Label(left_inside_frame,text="Email:",font=("times new roman",10,"bold"),bg="white")
        attenemail_label.grid(row=1,column=2,padx=5,pady=8)


        attendemail_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_email,font=("times new roman",10,"bold"),state="read only",width=20)
        attendemail_entry.grid(row=1,column=3,padx=5,pady=8)

        #time
        attentime_label=Label(left_inside_frame,text="Time:",font=("times new roman",10,"bold"),bg="white")
        attentime_label.grid(row=2,column=0,padx=5,pady=8)


        attentime_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,font=("times new roman",10,"bold"),state="read only",width=20)
        attentime_entry.grid(row=2,column=1,padx=5,pady=8)

        #date
        attendate_label=Label(left_inside_frame,text="Date:",font=("times new roman",10,"bold"),bg="white")
        attendate_label.grid(row=2,column=2,padx=5,pady=8)


        attendate_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,font=("times new roman",10,"bold"),state="read only",width=20)
        attendate_entry.grid(row=2,column=3,padx=5,pady=8)

        #Attendance status
        attenstatus_label=Label(left_inside_frame,text="Attendance status:",font=("times new roman",10,"bold"),bg="white")
        attenstatus_label.grid(row=3,column=0,padx=5,pady=8)

        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=("times new roman",10,"bold"),state="read only",width=20)
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,padx=5,pady=8)

        #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=250,width=600,height=30)

        import_button=Button(btn_frame,text="Import csv",command=self.importCsv,width=20,font=("times new roman",10,"bold"),bg="green",fg="white")
        import_button.grid(row=0,column=0)

        export_button=Button(btn_frame,text="Export csv",command=self.exportCsv,width=20,font=("times new roman",10,"bold"),bg="green",fg="white")
        export_button.grid(row=0,column=1)

        update_button=Button(btn_frame,text="Update",width=20,font=("times new roman",10,"bold"),bg="green",fg="white")
        update_button.grid(row=0,column=2)

        reset_button=Button(btn_frame,text="Reset",command=self.reset_data,width=20,font=("times new roman",10,"bold"),bg="green",fg="white")
        reset_button.grid(row=0,column=3)
        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="skyblue",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=630,y=6,width=630,height=450)

        table_frame=Frame(Right_frame,bd=2,bg="pink",relief=RIDGE)
        table_frame.place(x=5,y=5,width=610,height=420)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","name","dept","email","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)     
        scroll_x.config(command=self.AttendanceReportTable.xview)  
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("dept",text="Dept")
        self.AttendanceReportTable.heading("email",text="Email")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance Status")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=150)
        self.AttendanceReportTable.column("name",width=150)
        self.AttendanceReportTable.column("dept",width=150)
        self.AttendanceReportTable.column("email",width=150)
        self.AttendanceReportTable.column("time",width=150)
        self.AttendanceReportTable.column("date",width=150)
        self.AttendanceReportTable.column("attendance",width=150)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
    
    # ===================fetch data==========================================
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    #===============import cssv======================
    def importCsv(self):
        global mydata
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    
    #===============import cssv======================
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfuly","Export Data Successfully!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

        #=============Cursur Function for CSV========================

    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content["values"]

        self.var_atten_id.set(rows[0]),
        self.var_atten_name.set(rows[1]),
        self.var_atten_dep.set(rows[2]),
        self.var_atten_email.set(rows[3]),
        self.var_atten_time.set(rows[4]),
        self.var_atten_date.set(rows[5]),
        self.var_atten_attendance.set(rows[6])  

     #=============Cursur Function for mysql========================
    def reset_data(self):

        self.var_atten_id.set(""),
        self.var_atten_name.set(""),
        self.var_atten_dep.set(""),
        self.var_atten_email.set(""),
        self.var_atten_time.set(""),
        self.var_atten_date.set(""),
        self.var_atten_attendance.set("")

        
if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()