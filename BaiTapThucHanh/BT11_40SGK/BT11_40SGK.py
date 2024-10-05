#Tìm UCLN của 2 số

#Hàm tìm ước số chung lớn nhất
def UCLN(a, b):
    ucln = 1
    for i in range (1, min(a, b) + 1):
        if a %i == 0 and b %i == 0:
            ucln = i
    return ucln

#Hàm Main()
def Main():
    a = int(input("Nhập vào số nguyên dương a = "))
    b = int(input("Nhập vào số nguyên dương b = "))
      
    ucln = UCLN(a, b)
    print(f"Ước chung lớn nhất của {a} và {b} là: {ucln} ")
    
    print()

Main()
