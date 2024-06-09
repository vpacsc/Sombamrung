def hello():
    print('Hello, My name is Loong')

# hello()

def hellofriend(name):
    print(f'Hello, My name is {name}.')

# hellofriend('Uncle')

def checkNameAge(name,age=20):    # สามารถกำหนค่า default ให้กับ parameter ได้
    print(f'Hello, My name is {name}.') # f คือการทำให้ดึงค่า agumennt มาใส่ในตัวแปร
    print(f'I am {age} years old')

# checkNameAge('Adinant',29)
# checkNameAge(age=70,name='Chai') # agument สลับที่ได้ แต่ต้องระบุชื่อ parameter
# checkNameAge('Nong')  # ระบบจะใช้ age ที่เป็นค่า default

def addNumber(x,y):  # ตัวอย่าง function ที่ส่งค่ากลับ
    return x+y   # return คือการส่งค่ากลับ

#sum = addNumber(10,20) #ต้องมีตัวแปรคอยรับข้อมูลที่ส่งกลับมา
#print(sum)

# leap year
#  - หาร 4 ลงตัว หรือ หาร 100 ไม่ลงตัว
#  - หาร 400 ลงตัว
#year = int(input('ปี ค.ศ. :'))   # input ประกาศตัวแปรเพื่อรอรับค่าลงในตัวแปร year  int() เพื่อให้ค่าที่รับเป็นตัวเลข
#if year % 4 == 0 and year % 400 == 0 or year % 100 != 0 :      # %คือการหารเอาเศษ
#    print(f'ค.ศ.{year} เป็น Leap year')
#else :
#    print(f'ค.ศ.{year} ไม่เป็น Leap year')  
#

color=['red','green','blue']      # กำหนดค่าชุดข้อมูลให้กับตัวแปร แบบ List อ้างอิงนับ 0,1,2
#print(color[0])
#print(color[-1])  #ค่า index ใส่ค่าติดลบ หมายถึงให้อ่านจากหลังไปหน้า


# for c in color:  # คือการวนลูปภายใน list color
#     print(c)

color.append('yellow')  # คือการเพิ่มค่าลงใน List ที่ชื่อว่า color
for c in color:  # คือการวนลูปภายใน list color
    print(c)