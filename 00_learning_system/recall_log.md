# Recall Log

Mục đích của file này: ghi lại những gì mình **tự nhớ lại được** sau mỗi buổi học, không mở tài liệu ngay từ đầu.

Nguyên tắc:

- Trước khi học bài mới, dành 10–15 phút để tự nhớ lại bài cũ.
- Không mở ChatGPT, không mở code cũ, không mở ghi chú trong 5–10 phút đầu.
- Ghi rõ phần nhớ được, phần quên, phần cần ôn lại.
- Không cần viết hoàn hảo. File này dùng để phát hiện lỗ hổng trí nhớ.

---

## Mẫu ghi mỗi ngày

```md
## Ngày: YYYY-MM-DD

### 1. Chủ đề ôn lại
Ví dụ: for loop, if/else, list, function, dictionary...

### 2. Tôi tự nhớ lại được
- ...
- ...
- ...

### 3. Tôi bị quên hoặc còn mơ hồ
- ...
- ...

### 4. Tôi tự viết lại được đoạn code nào?
```python
# Viết lại code từ trí nhớ ở đây
```

### 5. Tôi bị kẹt ở đâu khi tự viết lại?
- ...

### 6. Việc cần ôn lại
- [ ] ...
- [ ] ...
```

---

## Bộ câu hỏi recall nhanh trước mỗi buổi học

### Python nền tảng

1. Biến dùng để làm gì?
2. `input()` trả về kiểu dữ liệu gì?
3. Khi nào cần dùng `int()` hoặc `float()`?
4. `print()` khác `return` như thế nào?

### if / elif / else

1. `if` dùng khi nào?
2. `elif` khác `else` như thế nào?
3. Điều kiện trong `if` trả về kiểu dữ liệu gì?
4. Khi nào cần dùng `and`, `or`, `not`?

### for loop

1. `for` thường dùng khi nào?
2. Khi nào dùng pattern `total`?
3. Khi nào dùng pattern `count`?
4. Khi nào dùng pattern `max/min`?

### list / string

1. List dùng để lưu kiểu dữ liệu gì?
2. Index bắt đầu từ số mấy?
3. `len()` dùng để làm gì?
4. String có thể duyệt bằng `for` không?

### dictionary

1. Dictionary lưu dữ liệu theo dạng gì?
2. Key là gì? Value là gì?
3. Truy cập giá trị trong dictionary như thế nào?
4. Khi nào nên dùng list chứa dictionary?

### function

1. Function dùng để làm gì?
2. Tham số là gì?
3. Khi nào nên dùng `return`?
4. Hàm tính toán nên `print` hay `return`?

### while / menu

1. `while` khác `for` như thế nào?
2. `while True` dùng khi nào?
3. `break` dùng để làm gì?
4. Vì sao menu chương trình thường dùng `while True`?

---

## Entry mẫu

```md
## Ngày: 2026-07-26

### 1. Chủ đề ôn lại
Function + list

### 2. Tôi tự nhớ lại được
- Function dùng để gom logic thành một khối có tên.
- Tham số là dữ liệu truyền vào hàm.
- `return` trả kết quả ra ngoài để dùng tiếp.
- Có thể truyền list vào function.

### 3. Tôi bị quên hoặc còn mơ hồ
- Khi nào nên dùng `print`, khi nào nên dùng `return`.
- Cách đặt tên hàm cho rõ nghĩa.

### 4. Tôi tự viết lại được đoạn code nào?
```python
def calculate_total(numbers):
    total = 0

    for number in numbers:
        total += number

    return total
```

### 5. Tôi bị kẹt ở đâu khi tự viết lại?
- Ban đầu tôi định dùng `print(total)` trong hàm, nhưng sau đó nhớ ra hàm tính toán nên `return total`.

### 6. Việc cần ôn lại
- [ ] print vs return
- [ ] function + dictionary
```
