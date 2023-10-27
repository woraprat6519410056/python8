# OOP

class IoTSAU :
   #data/property/field/attribute
   major = "SAU"
   name = ""

# method (มันคือ Funciton แต่เราไม่เรียกฟังก์ชัน)
def showHi(self) :
    print('Hi....')

def introduceMySelf(self) :
    print(f'My name is {self.major}')
    print(f'My major is {self.major}')

#-------------------
#สร้าง object
obA = IoTSAU( ) #เป็นการเรียกใช้ constructor ของคลาสให้ทำงาน (ถ้ามี) 
obB = IoTSAU( )


#การใช้งาน data ของ object คือ เอาคามันมาใช้ หรือเปลื่ยนคำให้มันใหม่
print( obA.major )
obA.major = "Wow"
obA.major =  "ฟ้าร้อง"
obB.name = "ฝนตกแล้ว"

# การใช้งาน data ของ object คือ สั่งให้เมธอตของ object นั้นๆ ทำงาน
obA.introduceMySelf()
obB.introduceMySelf()
