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
'''
# 3. Tìm sô lớn nhất trong list
numbers = [3, 9, 2, 12, 7]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest += number
print(largest)