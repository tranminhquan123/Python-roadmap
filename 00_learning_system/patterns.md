# Python Problem Solving Patterns

Mục đích của file này: lưu lại các **mẫu tư duy giải bài** thường gặp trong Python.

Không học thuộc từng bài riêng lẻ. Hãy học theo pattern:

```text
Đề bài có dấu hiệu gì?
→ Cần dùng công cụ nào?
→ Khung suy nghĩ là gì?
→ Code mẫu tối giản là gì?
```

---

# Cách ghi một pattern mới

```md
## Pattern: Tên pattern

### Khi nào dùng?
Dùng khi đề yêu cầu...

### Dấu hiệu trong đề bài
- ...
- ...

### Ý tưởng bằng tiếng Việt
1. ...
2. ...
3. ...

### Code mẫu
```python
# code mẫu
```

### Ví dụ bài tập
...

### Lỗi dễ gặp
- ...
```

---

# Pattern 1: Total

## Khi nào dùng?

Dùng khi đề yêu cầu tính tổng.

## Dấu hiệu trong đề bài

- tính tổng
- tổng điểm
- tổng tiền
- tổng số lượng
- cộng tất cả

## Ý tưởng bằng tiếng Việt

1. Tạo biến `total = 0`.
2. Duyệt từng phần tử.
3. Cộng giá trị hiện tại vào `total`.
4. Sau vòng lặp, `total` là kết quả.

## Code mẫu

```python
total = 0

for number in numbers:
    total += number
```

## Ví dụ

```python
numbers = [2, 4, 6]
total = 0

for number in numbers:
    total += number

print(total)  # 12
```

## Lỗi dễ gặp

- Quên tạo `total = 0` trước vòng lặp.
- Đặt `total = 0` bên trong vòng lặp làm tổng bị reset.
- Cộng nhầm biến.

---

# Pattern 2: Count

## Khi nào dùng?

Dùng khi đề yêu cầu đếm số lượng phần tử thỏa điều kiện.

## Dấu hiệu trong đề bài

- đếm
- có bao nhiêu
- số lượng
- bao nhiêu số chẵn
- bao nhiêu học sinh đạt

## Ý tưởng bằng tiếng Việt

1. Tạo biến `count = 0`.
2. Duyệt từng phần tử.
3. Nếu phần tử thỏa điều kiện thì `count += 1`.
4. Sau vòng lặp, `count` là số lượng cần tìm.

## Code mẫu

```python
count = 0

for item in items:
    if condition:
        count += 1
```

## Ví dụ

```python
numbers = [1, 2, 3, 4, 5, 6]
count = 0

for number in numbers:
    if number % 2 == 0:
        count += 1

print(count)  # 3
```

## Lỗi dễ gặp

- Dùng `count += number` thay vì `count += 1`.
- Quên điều kiện `if`.
- Đặt `count = 0` bên trong vòng lặp.

---

# Pattern 3: Max / Min

## Khi nào dùng?

Dùng khi đề yêu cầu tìm giá trị lớn nhất hoặc nhỏ nhất.

## Dấu hiệu trong đề bài

- lớn nhất
- cao nhất
- nhỏ nhất
- thấp nhất
- điểm cao nhất
- giá thấp nhất

## Ý tưởng bằng tiếng Việt

1. Giả sử phần tử đầu tiên là lớn nhất hoặc nhỏ nhất.
2. Duyệt từng phần tử.
3. Nếu gặp phần tử tốt hơn thì cập nhật lại biến đang lưu.
4. Sau vòng lặp, biến đó là kết quả.

## Code mẫu tìm lớn nhất

```python
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
```

## Code mẫu tìm nhỏ nhất

```python
smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number
```

## Ví dụ với dictionary

```python
students = [
    {"name": "Quan", "score": 8.5},
    {"name": "An", "score": 6},
    {"name": "Binh", "score": 9}
]

highest_student = students[0]

for student in students:
    if student["score"] > highest_student["score"]:
        highest_student = student

print(highest_student)
```

## Lỗi dễ gặp

- Khởi tạo `largest = 0` trong khi list có thể chứa số âm.
- Quên dùng `[0]` để lấy phần tử đầu tiên.
- Với dictionary, so sánh cả dictionary thay vì so sánh `student["score"]`.

---

# Pattern 4: Search

## Khi nào dùng?

Dùng khi đề yêu cầu tìm một phần tử, kiểm tra tồn tại, hoặc tra cứu dữ liệu.

## Dấu hiệu trong đề bài

- tìm
- tra cứu
- kiểm tra có tồn tại không
- tìm học sinh theo tên
- tìm sản phẩm theo mã

## Ý tưởng bằng tiếng Việt

1. Nhập hoặc có sẵn giá trị cần tìm.
2. Duyệt từng phần tử trong danh sách.
3. Nếu phần tử khớp điều kiện thì báo tìm thấy.
4. Nếu duyệt hết mà không thấy thì báo không tìm thấy.

## Code mẫu với `found`

```python
found = False

for item in items:
    if item == target:
        found = True
        break

if found:
    print("Tìm thấy")
else:
    print("Không tìm thấy")
```

## Code mẫu tìm gần đúng với string

```python
keyword = input("Nhập tên cần tìm: ").lower()

for student in students:
    if keyword in student["name"].lower():
        print(student)
```

## Lỗi dễ gặp

- Quên `.lower()` nên tìm kiếm bị phân biệt hoa/thường.
- In “không tìm thấy” bên trong vòng lặp làm in sai nhiều lần.
- Quên `break` khi chỉ cần tìm kết quả đầu tiên.

---

# Pattern 5: Filter

## Khi nào dùng?

Dùng khi cần tạo danh sách mới chỉ gồm các phần tử thỏa điều kiện.

## Dấu hiệu trong đề bài

- lọc
- lấy ra danh sách
- danh sách học sinh đạt
- danh sách số chẵn

## Ý tưởng bằng tiếng Việt

1. Tạo list rỗng để chứa kết quả.
2. Duyệt từng phần tử.
3. Nếu phần tử thỏa điều kiện thì thêm vào list kết quả.
4. Trả về hoặc in list kết quả.

## Code mẫu

```python
result = []

for item in items:
    if condition:
        result.append(item)
```

## Ví dụ

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)  # [2, 4, 6]
```

---

# Pattern 6: Transform

## Khi nào dùng?

Dùng khi cần biến đổi từng phần tử thành dạng mới.

## Dấu hiệu trong đề bài

- chuyển đổi
- biến mỗi phần tử thành
- tạo danh sách mới
- viết hoa toàn bộ tên
- nhân đôi từng số

## Ý tưởng bằng tiếng Việt

1. Tạo list rỗng.
2. Duyệt từng phần tử.
3. Biến đổi phần tử hiện tại.
4. Thêm kết quả đã biến đổi vào list mới.

## Code mẫu

```python
result = []

for item in items:
    new_item = transform(item)
    result.append(new_item)
```

## Ví dụ

```python
names = ["quan", "an", "binh"]
upper_names = []

for name in names:
    upper_names.append(name.upper())

print(upper_names)
```

---

# Pattern 7: Menu

## Khi nào dùng?

Dùng khi chương trình có nhiều chức năng và người dùng được chọn chức năng.

## Dấu hiệu trong đề bài

- menu
- chọn chức năng
- nhập lựa chọn
- thoát chương trình

## Ý tưởng bằng tiếng Việt

1. Dùng `while True` để menu chạy liên tục.
2. In danh sách chức năng.
3. Người dùng nhập lựa chọn.
4. Dùng `if / elif / else` để xử lý lựa chọn.
5. Nếu chọn thoát thì dùng `break`.

## Code mẫu

```python
while True:
    print("1. Xem danh sách")
    print("2. Thêm dữ liệu")
    print("0. Thoát")

    choice = input("Chọn chức năng: ")

    if choice == "1":
        print("Xem danh sách")
    elif choice == "2":
        print("Thêm dữ liệu")
    elif choice == "0":
        print("Tạm biệt")
        break
    else:
        print("Lựa chọn không hợp lệ")
```

## Lỗi dễ gặp

- Quên `break` nên không thoát được.
- So sánh `choice == 1` thay vì `choice == "1"`.
- Không xử lý trường hợp lựa chọn sai.

---

# Pattern 8: Function Decomposition

## Khi nào dùng?

Dùng khi bài toán có nhiều chức năng hoặc một đoạn logic cần tái sử dụng.

## Dấu hiệu trong đề bài

- viết hàm
- chương trình có nhiều chức năng
- tính toán lặp lại nhiều lần
- cần tách code cho dễ đọc

## Bộ câu hỏi trước khi viết function

1. Hàm tên gì?
2. Hàm nhận tham số gì?
3. Hàm cần trả về gì?
4. Bên trong hàm có cần biến tạm không?
5. Có cần `for` không?
6. Có cần `if` không?
7. Cuối cùng `return` cái gì?

## Code mẫu

```python
def function_name(parameter):
    # xử lý logic
    return result
```

## Ví dụ

```python
def count_passed_students(students):
    count = 0

    for student in students:
        if student["score"] >= 5:
            count += 1

    return count
```

---

# Pattern 9: Input → Process → Output

## Khi nào dùng?

Dùng để phân tích gần như mọi bài toán lập trình cơ bản.

## Ý tưởng

Mọi bài toán thường có 3 phần:

```text
Input  → dữ liệu đầu vào
Process → xử lý
Output → kết quả đầu ra
```

## Mẫu phân tích

```md
### Input
- ...

### Process
1. ...
2. ...
3. ...

### Output
- ...
```

## Ví dụ

Đề: Nhập điểm, nếu điểm >= 5 thì in Đạt, ngược lại in Rớt.

```md
### Input
- score

### Process
1. Nhập điểm
2. Chuyển điểm sang float
3. Nếu score >= 5 thì Đạt
4. Ngược lại Rớt

### Output
- Đạt hoặc Rớt
```
