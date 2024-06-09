# GUI-Maintenance.py
from tkinter import *
from tkinter import messagebox  # เพื่อเอามาทำ popup
from tkinter import ttk  # ย่อมาจาก Theme of TK มีหลาย widget ที่จะเอามาใช้

import csv
from datetime import datetime  # ต้องการนำ datetime มาเป็น transaction ID (tsid)

# เรียกไฟล์ที่เก็บ function ที่ทำงานกับ DATABASE
from db_maintenance import * # เพื่อไปดึง function ที่สร้างเตรียมไว้ใน db_maintenance มาใช้งาน

# def writecsv(record_list):
#     with open('data.csv','a',newline='',encoding='utf-8') as file:
#     # 'a'  คือ append  ถ้าเป็น 'w' คือ write ทับไฟล์เดิม (ข้อมูลเดิมหายหมด)
#         fw = csv.writer(file)
#         fw.writerow(record_list) 

############# ENVIRONMENT ###################
GUI = Tk()
GUI.title("โปรแกรมซ่อมบำรุง by vpac")
GUI.geometry("800x600+50+50")

######### กำหนดค่า FONT ไว้เรียกใช้ #############
FONT1 = ("Angsana New",20,"bold")
FONT2 = ("Angsana New",15)

############# สร้าง Tab
Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)
Tab.add(T1,text='ใบแจ้งซ่อม')
Tab.add(T2,text='ดูใบแจ้งซ่อม')
Tab.add(T3,text='สรุป')
Tab.pack(fill=BOTH,expand=1)



#####################


############## SCREEN DESIGN ################
L = Label(T1,text="ใบแจ้งซ่อม",font=FONT1)
# L.place(x=20,y=100)
# L.grid(row=0,column=0)
# L.pack()
L.place(x=80,y=10)
#--------
L = Label(T1,text="ชื่อผู้แจ้ง",font=FONT2)
L.place(x=30,y=50)
v_name = StringVar()      #กำหนดตัวแปรเพื่อรับค่า
E1=ttk.Entry(T1,textvariable=v_name,font=FONT2)
E1.place(x=150,y=50)
#--------
L = Label(T1,text="แผนก",font=FONT2)
L.place(x=30,y=100)
v_department = StringVar()      #กำหนดตัวแปรเพื่อรับค่า
E2=ttk.Entry(T1,textvariable=v_department,font=FONT2)
E2.place(x=150,y=100)
#--------
L = Label(T1,text="อุปกรณ์",font=FONT2)
L.place(x=30,y=150)
v_machine = StringVar()      #กำหนดตัวแปรเพื่อรับค่า
E3=ttk.Entry(T1,textvariable=v_machine,font=FONT2)
E3.place(x=150,y=150)
#--------
L = Label(T1,text="อาการเสีย",font=FONT2)
L.place(x=30,y=200)
v_problem = StringVar()      #กำหนดตัวแปรเพื่อรับค่า
E4=ttk.Entry(T1,textvariable=v_problem,font=FONT2)
E4.place(x=150,y=200)
#--------
L = Label(T1,text="หมายเลข",font=FONT2)
L.place(x=30,y=250)
v_number = StringVar()      #กำหนดตัวแปรเพื่อรับค่า
E5=ttk.Entry(T1,textvariable=v_number,font=FONT2)
E5.place(x=150,y=250)
#--------
L = Label(T1,text="เบอร์โทร",font=FONT2)
L.place(x=30,y=300)
v_tel = StringVar()      #กำหนดตัวแปรเพื่อรับค่า
E6=ttk.Entry(T1,textvariable=v_tel,font=FONT2)
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
    tsid = str(int(datetime.now().strftime('%y%m%d%H%M%S')) +114152147165) # gen tsid จากวันที่เวลา
    insert_mtworkorder(tsid,name,department,machine,problem,number,tel)

    # clear ค่าในช่อง Entry เมื่อ save เรียบร้อยแล้ว
    v_name.set('')
    v_department.set('')
    v_machine.set('')
    v_problem.set('')
    v_number.set('')
    v_tel.set('')
    update_table()


    #datalist = [dt,name,department,machine,problem,number,tel]
    #writecsv(datalist)
    #messenger.sendtext(text)   #ส่งไปไลน์
    #messagebox.showinfo("กำลังบันทึกข้อมูล...",text)

B=ttk.Button(T1,text="บันทึกใบแจ้งซ่อม",command=save)  #ทำปุ่มกด
B.place(x=200,y=350)

#สร้าง Tab 2
########################## TAB 2 ##############
header = ['TSID','ชื่อ','แผนก','อุปกรณ์','อาการเสีย','หมายเลข','เบอร์โทรผู้แจ้ง']
headerw = [50,100,100,150,200,100,100]

mtworkorderlist = ttk.Treeview(T2,column=header,show='headings',height=10)
mtworkorderlist.pack()

for h,w in zip(header,headerw) :  # ทำให้ค่าของ header ส่งไปพร้อมกับค่าของ headerw:
    # h คือตัวแปรเก็บ header w คือตัวแปรเก็บ hederw
    mtworkorderlist.heading(h,text=h)  # ชื่อหัว col
    mtworkorderlist.column(h,width=w,anchor='center')  # ความกว้างของ col ที่กำหนดไว้
mtworkorderlist.column('TSID',anchor='e')

#mtworkorderlist.insert('','end',values=['A','B','C','D','E','F','G'])

def update_table() :
    # clear ข้อมูลเก่าก่อน update
    mtworkorderlist.delete(*mtworkorderlist.get_children())
    data = view_mtworkorder()
    #print(data)
    for d in data:
        d = list(d)
        del d[0]
        mtworkorderlist.insert('','end',values=d)


###############################################
########## Start up ###############
update_table()

GUI.mainloop()

