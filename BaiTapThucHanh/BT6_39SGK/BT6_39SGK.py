#Tạo menu cộng trừ nhân chia 

#Khai báo thư viện để thoát chương trình
import sys

def Cong(a, b):
    return a + b

def Tru(a, b):
    return a - b

def Nhan(a, b):
    return a * b

def Chia(a, b):
    return a / b
        

def Main():
    a = int(input("Nhập vào số nguyên a = "))
    b = int(input("Nhập vào số nguyên b = "))

    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("5. Thoát")

    while True: 
        LuaChon = int(input("Nhập vào lựa chọn: "))
        while LuaChon < 1 or LuaChon > 5:
            print("Vui lòng nhập lựa chọn từ 1 - 5!")
            LuaChon = int(input("Nhập lại lựa chọn: "))

        if LuaChon == 1:
            Tong = Cong(a, b)
            print(f"{a} + {b} = {Tong}")

        elif LuaChon == 2:
            Hieu = Tru(a, b)
            print(f"{a} - {b} = {Hieu}")

        elif LuaChon == 3:
            Tich = Nhan(a, b)
            print(f"{a} * {b} = {Tich}")

        elif LuaChon == 4:
            if b == 0:
                print("Không thể chia cho 0!")
            else:
                Thuong = Chia(a, b)
                print(f"{a} / {b} = {Thuong}")

        else:
            return sys.exit() #Thoát chương trình

Main()