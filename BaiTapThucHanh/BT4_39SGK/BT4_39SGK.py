#Nhập vào 4 số nguyên in ra số nguyên lớn nhất

#Hàm Main
def Main():
    a = int(input("Nhập vào số nguyên thứ nhất: "))
    b = int(input("Nhập vào số nguyên thứ hai: "))
    c = int(input("Nhập vào số nguyên thứ ba: "))
    d = int(input("Nhập vào số nguyên thứ tư: "))

    SoLonNhat = max(a, b, c, d)
    print("Số lớn nhất là: ", SoLonNhat)

#Gọi hàm Main
Main()
