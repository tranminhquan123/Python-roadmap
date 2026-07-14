# ------- Phần A - and, or, not ---------
# and - Và
'''age = 20
has_id_card = True

if age > 18 and has_id_card:
    print("Được vào")
else:
    print("Không được vào")

# or - Hoặc
is_student = True
has_discount_code = False

if is_student or has_discount_code:
    print("Được giảm giá")
else:
    print("Không được giảm giá")

# not - Phủ định
is_raining = False

if not is_raining:
    print("Có thể đi chơi")
else:
    print("Nên ở nhà")

# -------------- Phần B - Vòng Lặp -----------

for number in range(1, 6):
    print(number)

total = 0
for number in range(1, 6):
    total += number
print(total)'''

# ------------- Thực hành bài 4 và 5 -----------

# ------- Bài 1 --------
username = input("Nhập tên người dùng: ")
password = (input("Nhập mật khẩu: "))

if username == "admin" and password == "123456":
    print("Đăng nhập thành công")
else:
    print("Sai tài khoản hoặc mật khẩu")

# -------- Bài 2 -----------

score = float(input("Nhập điểm: "))
if score < 0 or score > 10:
    print("Điểm không hợp lệ")
else:
    print("Điểm hợp lệ")

# ------- Bài 3 --------
age = int(input("Nhập tuổi: "))
if age < 6 or age > 60:
    print("Miễn phí vé")
else:
    print("Phải mua vé")

# --------- Bài 4 ------------

for number in range (1, 11):
    print(number)

# --------- Bài 5 -----------

n = int(input("Nhập n: "))
total = 0 
for number in range (1, n + 1):
    total += number
print (total)

# ------- Bài 6 ---------

x = int(input("Nhập x: "))
count = 0

for number in range(1, x + 1):
    if number % 2 == 0:
        count += 1
print(f"Có {count} số chẵn từ 1 đến {x}") 