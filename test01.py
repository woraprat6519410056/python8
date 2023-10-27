#---------- set คือ ข้อมูลหลายข้อมูล คนละชนิด ซ้ำกันไม่ได้(ถ้าซ้ำกันถือว่าเป็นตัวเดียวกัน) และไม่มีลำดับ และแก้ไขไม่ได้ แต่เพิ่ม -------
my_setl = {10, 20, True, 10, 'SAU', (20, 'Iot')}

#ไม่สามารภที่จะเข้าถึงข้อมูลใดข้อมูลหนึ่งได้
# เข้าถึงทุกข้อมูลใน Set
for data in my_setl :
    print(data)

# แก้ไขข้อมูล Set ทำไม่ได้โดยตรง แต่ทำได้โดยอ้อมเหมือนกัน Tuple
my_list = list( my_setl )
print(my_list)
my_list[2] = 'IOT'
print(my_list)
my_setl= set (my_list)
print(my_setl)

# Set Metod
my_setl.add(999)
my_setl.add('Wow')
print(my_setl)
my_setl.pop()
print(my_setl)
my_setl.remove(999)
print(my_setl)