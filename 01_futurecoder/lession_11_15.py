# -------- Bài 1 --------
text = "Python is easy"

print(f"Chuỗi có {len(text)} ký tự")


# -------- Bài 2 --------
name = "Quan"

print(f"Ký tự đầu tiên là: {name[0]}")
print(f"Ký tự cuối cùng là: {name[-1]}")


# -------- Bài 3 --------
word = "Python"

for character in word:
    print(character)


# -------- Bài 4 --------
text = "banana"
count = 0

for character in text:
    if character == "a":
        count += 1

print(f"Có {count} chữ a")


# -------- Bài 5 --------
text = "hello python"
vowel_count = 0

for character in text:
    if character in "aeiou":
        vowel_count += 1

print(f"Có {vowel_count} nguyên âm")


# -------- Bài 6 --------
password = input("Nhập mật khẩu: ")

if len(password) >= 8:
    print("Mật khẩu hợp lệ")
else:
    print("Mật khẩu quá ngắn")


# -------- Bài tổng hợp --------
sentence = input("Nhập một câu: ")

lower_sentence = sentence.lower()
upper_sentence = sentence.upper()

a_count = 0
vowel_count = 0

for character in lower_sentence:
    if character == "a":
        a_count += 1

    if character in "aeiou":
        vowel_count += 1

print(f"Độ dài câu: {len(sentence)}")
print(f"Viết thường: {lower_sentence}")
print(f"Viết hoa: {upper_sentence}")
print(f"Số chữ a: {a_count}")
print(f"Số nguyên âm: {vowel_count}")