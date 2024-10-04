#Tính tiền lương cho công nhân

def TienLuong(LuongMoiNgay, SoNgayLamViec, SoGioTangCa, SoNgayDiTre):
    TienThuong = SoGioTangCa * 10000

    if SoNgayLamViec > 24:
        TienThuong += 15000 * (SoNgayLamViec - 24)

    TienPhat = SoNgayDiTre * 20000

    TongTienLuong = (LuongMoiNgay * SoNgayLamViec) + TienThuong - TienPhat

    print(f"Tiền lương: {int(TongTienLuong)}đ")


#Hàm Main
def Main():
    LuongMoiNgay = float(input("Nhập vào mức lương mỗi ngày: "))
    SoNgayLamViec = int(input("Nhập vào số ngày làm việc: "))
    SoGioTangCa = int(input("Nhập vào số giờ làm việc tăng ca: "))
    SoNgayDiTre = int(input("Nhập vào số ngày đi trễ: "))

    TienLuong(LuongMoiNgay, SoNgayLamViec, SoGioTangCa, SoNgayDiTre)

Main()
