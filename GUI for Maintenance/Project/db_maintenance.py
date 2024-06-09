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


def view_mtworkorder():
    with conn:
        command = 'SELECT * FROM mt_workorder'
        c.execute(command)
        result = c.fetchall()
    return result

def update_mtworkorder(tsid,field,newvalue):
    with conn:
        command = 'UPDATE mt_workorder SET {} = (?) WHERE tsid=(?)'.format(field)
        c.execute(command,(newvalue,tsid))
    conn.commit()


def delete_mtworkorder(tsid):
    with conn:
        command = 'DELETE FROM mt_workorder WHERE tsid =(?)'
        c.execute(command,([tsid]))
    conn.commit()
