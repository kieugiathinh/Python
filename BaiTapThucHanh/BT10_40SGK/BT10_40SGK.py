#In ra tất cae các ước của N

def TatCaUoc(n):
    for i in range (1, n + 1):
        if n % i == 0:
            print(i, end=" ")

def Main():
    n = int(input("Nhập vào số nguyên dương n = "))
    print(f"Tất cả ước của {n} là: ", end="")
    TatCaUoc(n)

    print()

Main()
