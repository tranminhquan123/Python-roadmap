# Error Log

Mục đích: ghi lại lỗi sai để biến lỗi thành bài học, không chỉ sửa cho code chạy được.

---

## Quy tắc ghi lỗi

Mỗi lỗi nên có đủ 5 phần:

1. Lỗi là gì?
2. Lỗi nằm ở đâu?
3. Vì sao sai?
4. Cách sửa là gì?
5. Pattern cần nhớ là gì?

---

## Mẫu ghi lỗi

```md
## Lỗi 001: Tên lỗi

### Ngày gặp lỗi
YYYY-MM-DD

### Bài / file liên quan
Ví dụ: lesson_16_20.py, final_project_26_30.py

### Code bị lỗi
```python
# Dán đoạn code lỗi ở đây
```

### Thông báo lỗi nếu có
```text
# Dán lỗi terminal ở đây
```

### Lỗi nằm ở đâu?
Mô tả dòng hoặc đoạn bị sai.

### Vì sao sai?
Giải thích nguyên nhân bằng tiếng Việt.

### Cách sửa
```python
# Code đã sửa
```

### Pattern cần nhớ
- ...

### Tôi sẽ tránh lỗi này bằng cách nào?
- ...
```

---

## Nhóm lỗi thường gặp

### 1. Lỗi cú pháp

Ví dụ:

- Thiếu dấu `:` sau `if`, `for`, `while`, `def`.
- Sai thụt dòng.
- Thiếu dấu ngoặc.
- Nhầm dấu `=` và `==`.

### 2. Lỗi biến

Ví dụ:

- Dùng biến chưa tạo.
- Sai tên biến do Python phân biệt hoa/thường.
- Đặt tên biến không rõ nghĩa.

Ví dụ:

```python
total_score = 0
# nhưng bên dưới lại dùng totalScore
```

### 3. Lỗi vòng lặp

Ví dụ:

- Đặt `total = 0` bên trong vòng lặp.
- Quên `count += 1`.
- Dùng `count += number` khi đang cần đếm.
- In kết quả quá sớm bên trong vòng lặp.

### 4. Lỗi if/else

Ví dụ:

- Điều kiện sai thứ tự.
- Thiếu trường hợp `else`.
- Dùng `>` thay vì `>=`.
- Nhầm `and` và `or`.

### 5. Lỗi function

Ví dụ:

- Quên gọi hàm.
- Quên `return`.
- Dùng `print` trong hàm tính toán thay vì `return`.
- Truyền sai tham số.

### 6. Lỗi list / dictionary

Ví dụ:

- Truy cập index không tồn tại.
- Nhầm list và dictionary.
- Truy cập sai key.
- So sánh cả dictionary thay vì so sánh giá trị bên trong.

### 7. Lỗi while / menu

Ví dụ:

- Quên `break`.
- So sánh `choice == 1` thay vì `choice == "1"`.
- Không xử lý lựa chọn không hợp lệ.

---

## Entry mẫu 1: Quên return trong function

### Ngày gặp lỗi
2026-07-26

### Bài / file liên quan
lesson_16_20.py

### Code bị lỗi

```python
def calculate_total(numbers):
    total = 0

    for number in numbers:
        total += number

    print(total)

result = calculate_total([2, 4, 6])
print(result)
```

### Lỗi nằm ở đâu?

Trong hàm `calculate_total`, dùng `print(total)` thay vì `return total`.

### Vì sao sai?

`print()` chỉ in ra màn hình. Nó không trả kết quả ra ngoài hàm để gán vào biến `result`.

### Cách sửa

```python
def calculate_total(numbers):
    total = 0

    for number in numbers:
        total += number

    return total
```

### Pattern cần nhớ

- Hàm tính toán thường nên `return` kết quả.
- `print` dùng để hiển thị.
- `return` dùng để trả dữ liệu ra ngoài.

---

## Entry mẫu 2: Đặt biến tích lũy bên trong vòng lặp

### Code bị lỗi

```python
for number in numbers:
    total = 0
    total += number
```

### Vì sao sai?

Mỗi vòng lặp `total` bị reset về 0, nên không thể cộng dồn.

### Cách sửa

```python
total = 0

for number in numbers:
    total += number
```

### Pattern cần nhớ

Biến tích lũy như `total`, `count`, `largest` thường được tạo trước vòng lặp.
