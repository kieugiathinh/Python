#Tiền thuê khách sạn

#Hàm tính tiền thuê khách sạn
def TienPhongA(SoNgay, LoaiPhong):
    tienphong = SoNgay * 250000

    if SoNgay > 10:
        tienphong = tienphong - tienphong / 100 * 10;
    print(f"Tiền phòng cho {SoNgay} ngày, loại phòng A là: {int(tienphong)}đ")

def TienPhongB(SoNgay, LoaiPhong):
    tienphong = SoNgay * 200000

    if SoNgay > 10:
        tienphong = tienphong - tienphong / 100 * 10;
    print(f"Tiền phòng cho {SoNgay} ngày, loại phòng B là: {int(tienphong)}đ")

def TienPhongC(SoNgay, LoaiPhong):
    tienphong = SoNgay * 150000

    if SoNgay > 10:
        tienphong = tienphong - tienphong / 100 * 10;
    print(f"Tiền phòng cho {SoNgay} ngày, loại phòng C là: {int(tienphong)}đ")

#Hàm Main
def Main():
    n = int(input("Bạn muốn thuê khách sạn bao nhiêu ngày: "))
    while n <= 0:
        print("Vui lòng nhập số ngày là 1 số dương")
        n = int(input("Nhập lại số ngày muốn thuê phòng: "))

    print("Mời bạn chọn loại phòng!")
    print("1. Loại A - 250.000 đ/ngày")
    print("2. Loại B - 200.000 đ/ngày")
    print("3. Loại C - 150.000 đ/ngày")

    LuaChon = int(input("Mời bạn nhập loại phòng muốn thuê: "))
    
    if LuaChon == 1:
        TienPhongA(n, LuaChon)
    elif LuaChon == 2:
        TienPhongB(n, LuaChon)
    elif LuaChon == 3:
        TienPhongC(n, LuaChon)
    else:
        print("Vui lòng nhập loại phòng từ 1 - 3!")
        
Main()


