'''
number = int(input("Nhập một số nguyên: "))
if number > 0:
    print("Đây là số dương")
elif number < 0:
    print("Đây là số âm")
else:
    print("Số bạn nhập bằng 0")
'''
print("------------Bài 1-------------")

age = int(input("Nhập số tuổi của bạn: "))
if age >= 18:
    print("Bạn đã đủ tuổi trưởng thành")
else:
    print("Bạn chưa đủ tuổi trưởng thành")

print("------------Bài 2-------------")

number = int(input("Nhập một số nguyên: "))
if number % 2 == 0:
    print("Đây là số chẵn")
else:
    print("Đây là số lẻ")

print("------------Bài 3-------------")

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
if a > b:
    print(f"Số lớn nhất là: {a}")
elif a < b:
    print(f"Số lớn nhất là: {b}")
else: 
    print("Hai số bằng nhau")

print("------------Bài 4-------------")

score = float(input("Nhập điểm: "))
if score < 0 or score > 10:
    print("Điểm không hợp lệ")
elif score >= 8:
    print("Giỏi")
elif score >= 6.5:
    print("Khá")
elif score >= 5:
    print("Trung bình")
else:
    print("Chưa đạt")