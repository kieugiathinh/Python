#Nhập vào 2 giờ in ra tổng và hiệu của 2 giờ đó

#Khai báo thư viên math
import math

#Hàm tổng thời gian
def TongThoiGian(gio1, phut1, gio2, phut2):
    ThoiGian1 = gio1 * 60 + phut1
    ThoiGian2 = gio2 * 60 + phut2

    TongTG = ThoiGian1 + ThoiGian2

    Gio = int(TongTG / 60)
    Phut = int(TongTG % 60)

    print("Tổng 2 thời gian là: " +str(Gio)+ " giờ " +str(Phut)+ " phút")

#Hàm hiệu thời gian
def HieuThoiGian(gio1, phut1, gio2, phut2):
    ThoiGian1 = gio1 * 60 + phut1
    ThoiGian2 = gio2 * 60 + phut2

    TongTG = math.fabs(ThoiGian1 - ThoiGian2)

    Gio = int(TongTG / 60)
    Phut = int(TongTG % 60)

    print("Hiệu 2 thời gian là: " +str(Gio)+ " giờ " +str(Phut)+ " phút")


#Hàm Main
def Main():
    #Nhập
    gio1 = int(input("Nhập vào giờ thứ nhất: "))
    while gio1 < 0:
        print("Vui lòng nhập giờ là 1 số nguyên dương!")
        gio1 = int(input("Nhập lại giờ thứ nhất: "))

    phut1 = int(input("Nhập vào phút thứ nhất: "))
    while phut1 < 0 or phut1 > 59:
        print("Vui lòng nhập phút từ 0 - 59!")
        phut1 = int(input("Nhập lại phút thứ nhất: "))


    gio2 = int(input("Nhập vào giờ thứ hai: "))
    while gio2 < 0:
        print("Vui lòng nhập giờ là 1 số nguyên dương!")
        gio2 = int(input("Nhập lại giờ thứ hai: "))

    phut2 = int(input("Nhập vào phút thứ hai: "))
    while phut2 < 0 or phut2 > 59:
        print("Vui lòng nhập phút từ 0 - 59!")
        phut2 = int(input("Nhập lại phút thứ hai: "))


    #Xuất
    print("Thời gian thứ nhất là: " +str(gio1)+ " giờ " +str(phut1)+ " phút")
    print("Thời gian thứ hai là: " +str(gio2)+ " giờ " +str(phut2)+ " phút")

    TongThoiGian(gio1, phut1, gio2, phut2)
    HieuThoiGian(gio1, phut1, gio2, phut2)

#Gọi lại hàm Main
Main()