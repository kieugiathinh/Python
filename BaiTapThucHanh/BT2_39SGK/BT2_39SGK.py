#Viết chương trình giải phương trình bậc 2

#khai báo thư viên math
import math

#Hàm Phương trình bậc 1
def PhuongTrinhBac1(a, b):
    if a == 0:
        if b == 0:
            print("Phương trình vừa nhập vô số nghiệm")
        else:
            print("Phương trình vừa nhập vô nghiệm")
    else:
        x = -b / a
        print("Phương trình vừa nhập có nghiệm x = ", x)

#Hàm Phương trình bậc 2
def PhuongTrinhBac2(a, b, c):
    if a == 0:
        PhuongTrinhBac1(b, c)
    else:
        Delta = b**2 - 4*a*c

        if Delta < 0:
            print("Vì Delta = " +str(Delta)+ " < 0. Nên phương trình vô nghiệm")
        elif Delta == 0:
            x = -b / (2*a)
            print("Vì Delta = 0. Nên phương trình có nghiệm kép x = ", x)
        else:
            x1 = (-b + math.sqrt(Delta)) / (2*a)
            x2 = (-b - math.sqrt(Delta)) / (2*a)
            print("Vì Delta = " +str(Delta)+ " > 0. Nên phương trình vừa nhập có 2 nghiệm phân biệt")
            print("x1 = " +str(x1)+ "\nx2 =", x2)

#Hàm Main
def Main():
    a = int(input("Nhập vào hệ số a = "))
    b = int(input("Nhập vào hệ số b = "))
    c = int(input("Nhập vào hệ số c = "))

    PhuongTrinhBac2(a, b, c)

#Gọi hàm main
Main()
