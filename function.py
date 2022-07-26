#การสร้างฟังก์ชัน
from tkinter import Y


def hello():
    print("Hello world")
    print("Wisanu")
#เรียกใช้งานฟังก์ชัน
hello()
#ส่งค่าผ่านparameter
def sum(x,y):
    ans = x+y
    print(ans)
sum(7,8)
sum(5,9)
#ส่งค่าผ่านparameter+return
def sum(x,y):
    return x + y
ans = sum(8,6)/2
print(ans)
def sum(x,y):
    x+y
    return "hello"
print (sum(5,6))