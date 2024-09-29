#Tính tiền Taxi

def TienTaxi(km):
    TongTien = 0
    for i in range(1, km+1):
        if i <= 1:
            TongTien += 5000
        if i >= 2 and i <= 5:
            TongTien += 4500
        if i > 5:
            TongTien += 3500

    if km > 120:
        TongTien = int(TongTien - TongTien / 100 * 10)

    print("Tổng tiền mà quý khách phải trả cho " +str(km)+ "km là: " +str(TongTien)+ "đ")


#Hàm Main
def Main():
    km = int(input("Mời quý khách nhập số km đi Taxi: "))
    while km <= 0:
        print("Vui lòng nhập số km là 1 số nguyên dương!")
        km = int(input("Vui lòng nhập lại số km đi Taxi: "))

    TienTaxi(km)

#Gọi lại hàm Main
Main()
