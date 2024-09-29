#Bài tập tính điểm trung bình 3 môn: Toán, Lý, Hóa

#Hàm tính điểm trung bình 
def DiemTrungBinh(a, b, c):
    return (a + b + c) / 3

#Hàm Main
def Main():
    Toan = float(input("Nhập vào điểm môn Toán: "))
    while Toan < 0 or Toan > 10:
        print("Vui lòng nhập điểm từ 1 - 10!")
        Toan = float(input("Nhập lại điểm môn Toán: "))

    Ly = float(input("Nhập vào điểm môn Lý: "))
    while Ly < 0 or Ly > 10:
        print("Vui lòng nhập điểm từ 1 - 10!")
        Ly = float(input("Nhập lại điểm môn Lý: "))

    Hoa = float(input("Nhập vào điểm môn Hóa: "))
    while Hoa < 0 or Hoa > 10:
        print("Vui lòng nhập điểm từ 1 - 10!")
        Hoa = float(input("Nhập lại điểm môn Hóa: "))

    print("Điểm trung bình của bạn là: ", DiemTrungBinh(Toan, Ly, Hoa))

#Gọi lại hàm Main
Main()