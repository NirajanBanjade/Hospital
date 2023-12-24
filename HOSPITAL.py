from tkinter import *
from tkinter import ttk
import time
import datetime
import random
import mysql.connector
from tkcalendar import DateEntry
from tkinter import messagebox

class hospital:
    def __init__(self):
        self.root = Tk()
        self.root.title("Hospital Management system")
        self.root.geometry("1250x800+10+10")
        
        self.disease=StringVar() 
        self.namePatient=StringVar() 
        self.agePatient=StringVar() 
        self.weightPatient=StringVar() 
        self.Bp=StringVar() 
        self.nameofTablet=StringVar() 
        self.numDoses=StringVar() 
        self.cabinNum=StringVar() 
        self.patientId=StringVar() 
        self.entryDate=StringVar() 
        self.exitDate=StringVar() 
        self.dob=StringVar() 
        self.address=StringVar() 
        self.prescribedBy=StringVar() 


        label=Label(self.root,bd=25,relief=RIDGE,text="Online Doctor's Prescription",font=("times new roman",25,"italic"),fg="red")
        label.pack(side=TOP,fill=X)
        #---------------------dataframe---------
        dataframe=Frame(self.root,bd=20, relief=RIDGE)
        dataframe.place(width=1250, height=350,x=0,y=100)
        dataframeleft= LabelFrame(dataframe,bd=5,text="Patient Info", font=("times new roman",25,"bold"),relief=RIDGE)
        dataframeleft.place(width=950, height=300,x=0,y=0)

        dataframeright=LabelFrame(dataframe,bd=5,text="Prescription", font=("times new roman",25,"bold"),relief=RIDGE)
        dataframeright.place(width=300, height=300,x=700,y=0)
        
        #=======================buttons==================
        buttonframe=Frame(bd=20,relief=RIDGE)
        buttonframe.place(width=1250,height=70,x=0,y=425)

        lastframe=Frame(bd=5,relief=RIDGE)
        lastframe.place(width=1250,height=140,x=0,y=489)

        #====================leftframedata==================
        
  

        nameofdis=Label(dataframeleft,text="Illness detected",font=("times new roman",10,"bold","italic"))
        nameofdis.grid(row=0,column=0)

        comtabfirst=ttk.Combobox(dataframeleft,font=("times new roman",10,"bold"),width=27, textvariable=self.disease)
        comtabfirst["values"]=("Jaundice","Fever","Cholera","Heart disease","Headache","Diabetes")
        comtabfirst.grid(row=0,column=1)
        
        nameofpat=Label(dataframeleft, text="Name of patient : ",font=("times new roman",10,"bold","italic"),padx=2,pady=2)
        nameofpat.grid(row=1,column=0)
        nameEntry=Entry(dataframeleft,font=("times new roman",10,"bold","italic"),width=29,bd=5,textvariable=self.namePatient)
        nameEntry.grid(row=1,column=1)

        age=Label(dataframeleft, text="Age of patient: ",font=("times new roman",10,"bold","italic"),padx=2,pady=2)
        age.grid(row=2,column=0)
        ageEntry=Entry(dataframeleft,font=("times new roman",10,"bold","italic"),width=29,bd=5,textvariable=self.agePatient)
        ageEntry.grid(row=2,column=1)

        weight=Label(dataframeleft, text="Weight of patient: ",font=("times new roman",10,"bold","italic"),padx=2,pady=2)
        weight.grid(row=3,column=0)
        weightEntry=Entry(dataframeleft,font=("times new roman",10,"bold","italic"),width=29,bd=5,textvariable=self.weightPatient)
        weightEntry.grid(row=3,column=1)

        Bloodpressure=Label(dataframeleft, text="Blood Pressure : ",font=("times new roman",10,"bold","italic"),padx=2,pady=2)
        Bloodpressure.grid(row=4,column=0)
        bpEntry=Entry(dataframeleft,font=("times new roman",10,"bold","italic"),width=29,bd=5,textvariable=self.Bp)
        bpEntry.grid(row=4,column=1)   
        
        nameoftablet=Label(dataframeleft, text="Immediate Tablet: ",font=("times new roman",10,"bold","italic"),padx=2,pady=2)
        nameoftablet.grid(row=5,column=0)
        tabletEntry=Entry(dataframeleft,font=("times new roman",10,"bold","italic"),width=29,bd=5, textvariable=self.nameofTablet)
        tabletEntry.grid(row=5,column=1)

        
        numDoses=Label(dataframeleft, text="Number of doses: ",font=("times new roman",10,"bold","italic"),padx=2,pady=2)
        numDoses.grid(row=6,column=0)
        dosesEntry=Entry(dataframeleft,font=("times new roman",10,"bold","italic"),width=29,bd=5,textvariable=self.numDoses)
        dosesEntry.grid(row=6,column=1)    

        cabinNum=Label(dataframeleft, text="Cabin Number: ",font=("times new roman",10,"bold","italic"),padx=2,pady=2)
        cabinNum.grid(row=7,column=0)
        cabinEntry=Entry(dataframeleft,font=("times new roman",10,"bold","italic"),width=29,bd=5,textvariable=self.cabinNum)
        cabinEntry.grid(row=7,column=1)  

        #==========================================next column ========================
        PatientID=Label(dataframeleft, text="Patient ID:   ",font=("times new roman",10,"bold","italic"),padx=2,pady=2)
        PatientID.grid(row=0,column=2)
        IDEntry=Entry(dataframeleft,font=("times new roman",10,"bold","italic"),width=29,bd=5,textvariable=self.patientId)
        IDEntry.grid(row=0,column=3)  

        dateofEntry=Label(dataframeleft, text="Entry Date:    ",font=("times new roman",10,"bold","italic"),padx=2,pady=2)
        dateofEntry.grid(row=1,column=2)
        dateEntry=DateEntry(dataframeleft,font=("times new roman",10,"bold","italic"),width=27,bd=5, textvariable=self.entryDate)
        dateEntry.grid(row=1,column=3)  

        dateofExit=Label(dataframeleft, text="Exp Checkout: ",font=("times new roman",10,"bold","italic"),padx=2,pady=2)
        dateofExit.grid(row=2,column=2)
        dateExit=DateEntry(dataframeleft,font=("times new roman",10,"bold","italic"),width=27,bd=5,textvariable=self.exitDate)
        dateExit.grid(row=2,column=3)  

        dateofbirth=Label(dataframeleft, text="Date of birth: ",font=("times new roman",10,"bold","italic"),padx=2,pady=2)
        dateofbirth.grid(row=3,column=2)
        datebirth=DateEntry(dataframeleft,font=("times new roman",10,"bold","italic"),width=27,bd=5,textvariable=self.dob)
        datebirth.grid(row=3,column=3)  

        address=Label(dataframeleft, text="Patient Address:   ",font=("times new roman",10,"bold","italic"),padx=2,pady=2)
        address.grid(row=4,column=2)
        addressEntry=Entry(dataframeleft,font=("times new roman",10,"bold","italic"),width=29,bd=5,textvariable=self.address)
        addressEntry.grid(row=4,column=3)  

        doctor=Label(dataframeleft, text="Prescribed by :   ",font=("times new roman",10,"bold","italic"),padx=2,pady=2)
        doctor.grid(row=5,column=2)
        doctorEntry=Entry(dataframeleft,font=("times new roman",10,"bold","italic"),width=29,bd=5,textvariable=self.prescribedBy)
        doctorEntry.grid(row=5,column=3)  
        
        

        #====================prescription=======================


        self.prescription= Text(dataframeright,font=("ariel",9,"italic"), width=40,height=16)
        self.prescription.grid(row=0,column=0)

        #===============button==================================

        butprescrip=Button(buttonframe, text="Prescription",font=("arial",10,"bold"),bg="red",fg="white",width=24,command=self.iprescription)
        butprescrip.grid(row=0,column=0)

        butprescripdata=Button(buttonframe, text="Prescription Data",font=("arial",10,"bold"),bg="red",fg="white",width=24, command=self.iPrescriptiondata)
        butprescripdata.grid(row=0,column=1)

        update=Button(buttonframe, text="Update",font=("arial",10,"bold"),bg="red",fg="white",width=24,command=self.update_data)
        update.grid(row=0,column=2)

        Delete=Button(buttonframe, text="Delete",font=("arial",10,"bold"),bg="red",fg="white",width=24,command=self.idelete)
        Delete.grid(row=0,column=3)

        clear=Button(buttonframe, text="Clear",font=("arial",10,"bold"),bg="red",fg="white",width=24)
        clear.grid(row=0,column=4)

        exit=Button(buttonframe, text="Exit",font=("arial",10,"bold"),bg="red",fg="white",width=24)
        exit.grid(row=0,column=5)

       
        #=======================scroll==========================
        scrollX=ttk.Scrollbar(lastframe,orient=HORIZONTAL)
        scrollY=ttk.Scrollbar(lastframe,orient=VERTICAL)



        self.hospital_table=ttk.Treeview(lastframe,columns=("Illness","Patient Name","Age","Weight","Blood Pressure", "Tablet","Doses","Cadbin Num"," Patient Id","Entry","Exit","DOB","Address","Prescribed by"),xscrollcommand=scrollX.set,yscrollcommand=scrollY.set)
        
        scrollX.pack(side=BOTTOM,fill=X,expand=True)
        scrollY.pack(side=RIGHT,fill=Y,expand=True)



        scrollX=ttk.Scrollbar(command=self.hospital_table.yview)
        scrollX=ttk.Scrollbar(command=self.hospital_table.xview)




        for col in self.hospital_table["columns"]:
            self.hospital_table.heading(col, text=col)
        
        self.hospital_table["show"]="headings"

      
        for col in self.hospital_table["columns"]:
            self.hospital_table.column(col, width=150)     

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.cursor_focus)
        
                
        self.fetch()




#====================================database and functionality
    def iPrescriptiondata(self):
        if self.nameofTablet.get() =="" or self.patientId.get()=="":
            messagebox.showerror("Error","All fields are not filled!!")
        else:
            try: 
            
                db=mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="Nirajan@#1829",
                    database="tester"
                )
                mycursor=db.cursor()
                mycursor.execute("insert into Hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                 
                                  (  
                                    self.disease.get(),
                                    self.namePatient.get(), 
                                    self.agePatient.get(), 
                                    self.weightPatient.get(), 

                                    self.Bp.get(), 
                                    self.nameofTablet.get(), 
                                    self.cabinNum.get(), 
                                    self.numDoses.get(), 
                                    self.patientId.get(), 
                                    self.entryDate.get(), 
                                    self.exitDate.get(), 
                                    self.dob.get(), 
                                    self.address.get(), 
                                    self.prescribedBy.get()
                                 )
                 )
                 
                db.commit()
                db.close()
                self.fetch()
                messagebox.showinfo("Successfully added!!")
            except Exception as e:
                messagebox.showerror(f"Error {e}")
    def fetch(self):

        query="select * from hospital"
        db=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Nirajan@#1829",
            database="tester"
        )
        cur=db.cursor()
        cur.execute(query)
        rows=cur.fetchall()
        for i in rows:
            self.hospital_table.insert("",END,values=i)
            db.commit()
        db.close()
        
    def cursor_focus(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        if cursor_row:
            self.disease.set(row[0])
            self.namePatient.set(row[1]) 
            self.agePatient.set(row[3])
            self.weightPatient.set(row[2])
            self.Bp.set(row[4])
            self.nameofTablet.set(row[5])
            self.cabinNum.set(row[6])
            self.numDoses.set(row[7])
            self.patientId.set(row[8])
            self.entryDate.set(row[9])
            self.exitDate.set(row[10])
            self.dob.set(row[11])
            self.address.set(row[12])
            self.prescribedBy.set(row[13])
    

    def update_data(self):

        db=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Nirajan@#1829",
            database="tester"
        )
        mycursor=db.cursor()
        try:    
            mycursor.execute("update Hospital set Nameofdisease=%s,Patient=%s,Age=%s,Weight=%s,BP=%s,Tablets=%s,CabinNum=%s, Doses=%s,Entry=%s,Exitdate=%s,DOB=%s,Address=%s,Prescribedby=%s where PatientId=%s",(
                                        self.disease.get(),
                                        self.namePatient.get(), 
                                        self.agePatient.get(), 
                                        self.weightPatient.get(), 
                                        self.Bp.get(), 
                                        self.nameofTablet.get(), 
                                        self.cabinNum.get(), 
                                        self.numDoses.get(),                                    
                                        self.entryDate.get(), 
                                        self.exitDate.get(), 
                                        self.dob.get(), 
                                        self.address.get(), 
                                        self.prescribedBy.get(),  
                                        self.patientId.get()          
    
    
            ))
            db.commit()
            db.close()
            self.fetch()  # R:efresh the displayed data
            messagebox.showinfo("Success", "Record updated successfully!")
        except Exception as e:
            print(f"Error {e}")
    
    def iprescription(self):
        self.prescription.insert(END,"Disease:   "+self.disease.get()+"\n")
        self.prescription.insert(END,"Name of patient:   "+self.namePatient.get()+"\n")
        self.prescription.insert(END,"Age of patient:   "+self.agePatient.get()+"\n")
        self.prescription.insert(END,"Weight of patient:   "+self.weightPatient.get()+"\n")
        self.prescription.insert(END,"Blood pressure:   "+self.Bp.get()+"\n")
        self.prescription.insert(END,"Patient Id:   "+self.patientId.get()+"\n")
        self.prescription.insert(END,"Name of tablet:   "+self.nameofTablet.get()+"\n")
        self.prescription.insert(END,"Cabin Number:   "+self.cabinNum.get()+"\n")
        self.prescription.insert(END,"Number of doses:   "+self.numDoses.get()+"\n")
        self.prescription.insert(END,"Entry date:   "+self.entryDate.get()+"\n")
        self.prescription.insert(END,"Exit date:   "+self.exitDate.get()+"\n")
        self.prescription.insert(END,"Date of birth:   "+self.dob.get()+"\n")
        self.prescription.insert(END,"Address:   "+self.address.get()+"\n")
        self.prescription.insert(END,"Prescribed by:   "+self.prescribedBy.get()+"\n")
    
    def idelete(self):
        db=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Nirajan@#1829",
            database="tester"
        )
        mycursor=db.cursor()
        query="delete from Hospital where PatientId=%s"
        value=(self.patientId.get(),)
        if self.patientId.get() !="":
            mycursor.execute(query,value)
            db.commit()
            db.close()
            self.fetch()
            messagebox.showinfo("","Deleted","Successfully!!")
        else:
            messagebox.showerror("","Empty data!")



                


                                     
                                 

        

hosp=hospital()
mainloop()



        
    




