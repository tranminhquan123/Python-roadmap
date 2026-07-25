# ----- Chuỗi ------

# --- Bài 1 ---
text = "Python is easy"
print(len(text))

# --- Bài 2 ---
name = "Quan"
print(name[0])
print(name[-1])

# --- Bài 3 ---
word = "Python"
for character in word:
    print(character)

# --- Bài 4 ---
fruit = "banana"
count = 0
for character in fruit:
    if character == "a":
        count += 1
print(f"Có {count} chữ a")

# --- Bài 5 --- 
message = "hello python"
vowel_count = 0
for character in message:
    if character in "ueoai":
        vowel_count += 1
print(f"Có {vowel_count} nguyên âm")

# --- Bài 6 ---
password = input("Nhập mật khẩu: ")
if len(password) >= 8:
    print("Mật khẩu hợp lệ.")
else:
    print("Mật khẩu quá ngắn")

# --- Bài tổng hợp --- 
sentence = input("Nhập một câu bất kỳ: ")
count = 0
vowel_count = 0

print(len(sentence))
print(sentence.lower())
print(sentence.upper())

for character in sentence:
    if character == "a":
        count += 1
    if character in "ueoai":
        vowel_count += 1
print(f"Có {count} chữ a")
print(f"Có {vowel_count} nguyên âm")
