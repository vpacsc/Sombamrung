# basicsql.py
import sqlite3

#  สร้าง connection เพื่อเขื่อต่อฐานข้อมูล
conn = sqlite3.connect('maintenance.sqlite3')
# สร้าง cursor คือตัวที่เอาไว้สั่งคำสั่ง sql
c= conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS mt_workorder (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                tsid TEXT,
                name TEXT,
                department TEXT,
                machine TEXT,
                problem TEXT,
                number TEXT,
                tel TEXT) """)

def insert_mtworkorder(tsid,name,department,machine,problem,number,tel):
    #CREATE
    with conn:
        command = 'INSERT INTO mt_workorder VALUES (?,?,?,?,?,?,?,?)'
        c.execute(command,(None,tsid,name,department,machine,problem,number,tel))
    conn.commit()  # save database
    print('saved')


def view_mtworkorder():
    with conn:
        command = 'SELECT * FROM mt_workorder'
        c.execute(command)
        result = c.fetchall()
    print(result)
    return result

def update_mtworkorder(tsid,field,newvalue):
    with conn:
        command = 'UPDATE mt_workorder SET {} = (?) WHERE tsid=(?)'.format(field)
        c.execute(command,(newvalue,tsid))
    conn.commit()
    print('updated')



def delete_mtworkorder(tsid):
    with conn:
        command = "DELETE FROM mt_workorder WHERE tsid =(?)"
        c.execute(command,([tsid]))
    conn.commit()
    print('deleted')

#insert_mtworkorder('TS1002','Adinant','Sale','Printer','Hang','PT1999','084825469')
#update_mtworkorder('TS1002','tel','0840261748')
#delete_mtworkorder('TS1001')

result = view_mtworkorder()
#print(result[1][1])





