'''
name = input("Nhập tên của bạn: ")
print(f"Xin chào {name}")

#-----------------------------------------------

first_number = input("Nhập số thứ nhất: ")
second_number = input("Nhập số thứ hai: ")

print (first_number + second_number)

#-----------------------------------------------

first_number = int(input("Nhập số thứ nhất: "))
second_number = int(input("Nhập số thứ hai: "))

total = first_number + second_number
print(f"Tổng là: {total}")


#------------------------------------------------

name = input("Nhập tên của bạn: ")
birth_year = int(input("Năm sinh của bạn: "))

current_year = 2026
age = current_year - birth_year

print(f"Xin chào {name}")
print(f"Năm nay bạn {age} tuổi")
'''

#---------------------Bài tập-----------
# Bài tập 1
name = input("Nhập họ và tên: ")
country = input("Nhập thành phố bạn đang sống: ")

print(f"Họ và tên: {name}")
print(f"Thành phố đang sinh sống: {country}")

# Bài tập 2
first_number = int(input("Nhập số thứ nhất: "))
second_number = int(input("Nhập số thứ hai: "))

total = first_number + second_number
print(f"Tổng hai số là: {total}")

# Bài 3
length = int(input("Nhập chiều dài: "))
width = int(input("Nhập chiều rộng: "))

area = length * width
print(f"Diện tích: {area}")