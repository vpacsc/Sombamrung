from tkinter import *
from tkinter import messagebox  # เพื่อเอามาทำ popup

# Songlinne lib
from songline import Sendline
token = 'jxlEEP2tbOvR6Emu6xkl7RmXSC7E337zS7cyinHq6Nj'  ## token ไลน์ของ vpacsc
messenger= Sendline(token)

import csv
from datetime import datetime

def writecsv(record_list):
    with open('data.csv','a',newline='',encoding='utf-8') as file:
    # 'a'  คือ append  ถ้าเป็น 'w' คือ write ทับไฟล์เดิม (ข้อมูลเดิมหายหมด)
        fw = csv.writer(file)
        fw.writerow(record_list) 

############# ENVIRONMENT ###################
GUI = Tk()
GUI.title("โปรแกรมซ่อมบำรุง by vpac")
GUI.geometry("500x500+50+50")

######### กำหนดค่า FONT ไว้เรียกใช้ #############
FONT1 = ("Angsana New",20,"bold")
FONT2 = ("Angsana New",15)

############## SCREEN DESIGN ################
L = Label(GUI,text="ใบแจ้งซ่อม",font=FONT1)
# L.pack
# L.place(x=20,y=100)
# L.grid(row=0,column=0)
L.pack()
#--------
L = Label(GUI,text="ชื่อผู้แจ้ง",font=FONT2)
L.place(x=30,y=50)
v_name = StringVar()      #กำหนดตัวแปรเพื่อรับค่า
E1=Entry(GUI,textvariable=v_name,font=FONT2)
E1.place(x=150,y=50)
#--------
L = Label(GUI,text="แผนก",font=FONT2)
L.place(x=30,y=100)
v_department = StringVar()      #กำหนดตัวแปรเพื่อรับค่า
E2=Entry(GUI,textvariable=v_department,font=FONT2)
E2.place(x=150,y=100)
#--------
L = Label(GUI,text="อุปกรณ์",font=FONT2)
L.place(x=30,y=150)
v_machine = StringVar()      #กำหนดตัวแปรเพื่อรับค่า
E3=Entry(GUI,textvariable=v_machine,font=FONT2)
E3.place(x=150,y=150)
#--------
L = Label(GUI,text="อาการเสีย",font=FONT2)
L.place(x=30,y=200)
v_problem = StringVar()      #กำหนดตัวแปรเพื่อรับค่า
E4=Entry(GUI,textvariable=v_problem,font=FONT2)
E4.place(x=150,y=200)
#--------
L = Label(GUI,text="หมายเลข",font=FONT2)
L.place(x=30,y=250)
v_number = StringVar()      #กำหนดตัวแปรเพื่อรับค่า
E5=Entry(GUI,textvariable=v_number,font=FONT2)
E5.place(x=150,y=250)
#--------
L = Label(GUI,text="เบอร์โทร",font=FONT2)
L.place(x=30,y=300)
v_tel = StringVar()      #กำหนดตัวแปรเพื่อรับค่า
E6=Entry(GUI,textvariable=v_tel,font=FONT2)
E6.place(x=150,y=300)
#--------


################ FUNCTION ##############

def save():
    name = v_name.get()     # .get คือการดึงค่าออกมาจาก StringVar
    department = v_department.get()
    machine = v_machine.get()
    problem = v_problem.get()
    number = v_number.get()
    tel = v_tel.get()

    text =        "ชื่อผู้แจ้ง : "+ name + '\n'
    text = text + "แผนก  : "+department + '\n'
    text = text + "อุปกรณ์ : "+machine + '\n'   
    text = text + "อาการ  : "+problem + '\n'
    text = text + "หมายเลข : "+number + '\n'
    text = text + "เบอร์โทร : "+tel + '\n'
    dt = datetime.now().strftime('%y-%m-%d %H:%M:%S')
    datalist = [dt,name,department,machine,problem,number,tel]
    writecsv(datalist)
#    messenger.sendtext(text)   #ส่งไปไลน์
    messagebox.showinfo("กำลังบันทึกข้อมูล...",text)

B=Button(GUI,text="บันทึกใบแจ้งซ่อม",command=save)  #ทำปุ่มกด
B.place(x=200,y=350)



GUI.mainloop()

