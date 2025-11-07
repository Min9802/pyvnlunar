# vnlunar Examples

Các file ví dụ minh họa cách sử dụng thư viện vnlunar.

## Danh sách ví dụ

### 1. example_basic.py
Ví dụ cơ bản về chuyển đổi lịch và lấy thông tin đầy đủ.

```bash
python example_basic.py
```

Nội dung:
- Chuyển đổi dương lịch sang âm lịch
- Lấy thông tin Can Chi
- Xem 12 Sao, 12 Thần
- Kiểm tra Hoàng Đạo / Hắc Đạo
- 28 Tú Sao, Nạp Âm
- Giờ Hoàng Đạo

### 2. example_xem_ngay.py
Ví dụ về xem ngày tốt xấu cho các việc.

```bash
python example_xem_ngay.py
```

Nội dung:
- Xem ngày cho cưới hỏi, xây nhà, xuất hành
- Xem ngày cho khai trương, chuyển nhà, đầu tư
- Tìm các ngày tốt trong một khoảng thời gian

### 3. example_huong_xuat_hanh.py
Ví dụ về xem hướng xuất hành và tuổi xung.

```bash
python example_huong_xuat_hanh.py
```

Nội dung:
- Kiểm tra tuổi xung
- Hướng theo Ngọc Hạp Thông Thư
- Hướng các vị thần (Thần Tài, Hỷ Thần, Phúc Thần)
- Hướng theo tuổi (con giáp)
- Hướng xuất hành tổng hợp
- Giờ Hoàng Đạo để xuất hành

### 4. example_ngu_hanh.py
Ví dụ về Ngũ Hành và quan hệ tương sinh, tương khắc.

```bash
python example_ngu_hanh.py
```

Nội dung:
- Ngũ Hành của các năm
- Quan hệ giữa các Ngũ Hành
- Chu kỳ tương sinh
- Chu kỳ tương khắc
- Ví dụ cụ thể về so sánh Ngũ Hành giữa các năm

## Chạy tất cả ví dụ

Để chạy tất cả các ví dụ:

```bash
python example_basic.py
python example_xem_ngay.py
python example_huong_xuat_hanh.py
python example_ngu_hanh.py
```

## Tùy chỉnh

Bạn có thể sửa đổi các ngày trong file ví dụ để kiểm tra các ngày khác nhau:

```python
# Thay đổi ngày cần kiểm tra
day, month, year = 15, 12, 2025  # 15/12/2025
```

## Yêu cầu

- Python >= 3.7
- vnlunar đã được cài đặt hoặc thư mục cha có thể import được

## Lưu ý

Các ví dụ này được thiết kế để chạy từ thư mục examples. Nếu chạy từ thư mục khác, bạn có thể cần điều chỉnh đường dẫn import trong đầu file.
