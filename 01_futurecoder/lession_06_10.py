'''
# ----- Ngày 6: List -----
number = [3, 5, 7, 9]
names = ["Quan", "An", "Binh"]
mixed = ["Quan", 22, True]

fruits = ["Tao", "Cam", "Xoai"]
print(fruits)

# ----- Ngày 7: Truy cập phần tử trong List -----

chatbot = ["ChatGPT", "Claude", "Gemini"]
print(chatbot[0])
print(chatbot[1])
print(chatbot[2])
print(chatbot[-1])
print(len(chatbot))

# ----- Ngày 8: Duyệt List bằng For -----

apps = ["Tiktok", "Facebook", "Instagram"]
for app in apps:
    print(app)
'''
# ----- Ngày 9: Tính tổng, đếm, tìm kiếm trong List -----
# 1. Tính tổng các số trong List 
'''numbers = [3, 5, 7, 9]
total = 0

for number in numbers:
    total += number
print(total)
'''
# 2. Đếm sô chẵn trong list
'''
numbers = [3, 4, 7, 10, 12]
count = 0
for number in numbers:
    if number % 2 == 0:
        count += 1
print(count)

# 3. Tìm sô lớn nhất trong list
numbers = [3, 9, 2, 12, 7]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest += number
print(largest)
'''

# ----- Bài thực hành ------
'''
# Bài 1: 

numbers = [1, 2, 3, 4, 5]
print(numbers)

# Bài 2: 

names = ["Quân", "An", "Bình", "Huy"]
print(names[0])
print(names[-1])
print(f"Danh sách có {len(names)} phần tử" )

# Bài 3: 

fruits = ["Táo", "Cam", "Xoài", "Chuối"]

for fruit in fruits:
    print(fruit)


# Bài 4:

numbers = [4, 7, 2, 9, 10]
total = 0
for number in numbers:
    total += number
print(total)


# Bài 5:

numbers = [3, 8, 12, 5, 7, 10, 15]
count = 0
for number in numbers:
    if number % 2 == 0:
        count += 1
print(f"Có {count} số chẵn")


# Bài 6: 

numbers = [5, 9, 2, 15, 7]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print(largest)
'''

# Bài tổng hợp: 

scores = [8.5, 6, 9, 4.5, 7, 3.5, 10]
totalScore = 0
count = 0 

for score in scores:
    if score >= 5:
        count +=1
    totalScore += score
print(f"Tổng điểm: {totalScore}")
print(f"Số bài đạt: {count}")

averageGrade = totalScore / 7
print(f"Điểm trung bình: {averageGrade}")

largest = scores[0]
for score in scores:
    if score > largest:
        largest = score
print(f"Điểm sô cao nhất: {largest}")

        




