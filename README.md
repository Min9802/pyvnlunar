# vnlunar - Vietnamese Lunar Calendar for Python

Thư viện Âm lịch Việt Nam cho Python - Vietnamese Lunar Calendar Library

## Giới thiệu / Introduction

vnlunar là thư viện Python để chuyển đổi và tính toán lịch âm Việt Nam, dựa trên thuật toán thiên văn chính xác. Thư viện hỗ trợ:

- Chuyển đổi dương lịch <-> âm lịch
- Tính Can Chi, Ngũ Hành
- Xem ngày tốt xấu (Hoàng Đạo / Hắc Đạo)
- 12 Sao Kiến Trừ, 28 Tú Sao
- Hướng xuất hành, Tuổi xung
- Giờ Hoàng Đạo
- Và nhiều tính năng khác...

## Cài đặt / Installation

```bash
pip install vnlunar
```

Hoặc cài đặt từ source:

```bash
git clone https://github.com/min9802/pyvnlunar.git
cd pyvnlunar
pip install -e .
```

## Sử dụng cơ bản / Basic Usage

### 1. Chuyển đổi dương lịch sang âm lịch

```python
import vnlunar

# Lấy thông tin âm lịch của ngày 7/11/2025
lunar = vnlunar.get_lunar_date(7, 11, 2025)

print(f"Ngày âm lịch: {lunar['day']}/{lunar['month']}/{lunar['year']}")
print(f"Tháng nhuận: {'Có' if lunar['leap'] == 1 else 'Không'}")
```

### 2. Lấy thông tin đầy đủ về một ngày

```python
import vnlunar

info = vnlunar.get_full_info(7, 11, 2025)

print(f"Dương lịch: {info['solar']['day']}/{info['solar']['month']}/{info['solar']['year']}")
print(f"Âm lịch: {info['lunar']['day']}/{info['lunar']['month']}/{info['lunar']['year']}")
print(f"Can Chi ngày: {info['can_chi']['day']}")
print(f"Can Chi tháng: {info['can_chi']['month']}")
print(f"Can Chi năm: {info['can_chi']['year']}")
print(f"Sao: {info['12_stars']['name']} - {info['12_stars']['description']}")
print(f"Hoàng/Hắc Đạo: {info['day_type']['type']}")
```

### 3. Xem ngày tốt xấu cho các việc

```python
import vnlunar

# Tính Julian Day Number
jd = vnlunar.jdn(7, 11, 2025)

# Xem ngày có tốt cho cưới hỏi không
ket_qua = vnlunar.check_good_day(jd, "wedding")
print(f"Ngày {ket_qua['star']['name']}: {ket_qua['description']}")

# Tìm các ngày tốt để khai trương trong tháng 11/2025
start_jd = vnlunar.jdn(1, 11, 2025)
end_jd = vnlunar.jdn(30, 11, 2025)
ngay_tot = vnlunar.find_good_days(start_jd, end_jd, "opening")

print(f"\nCác ngày tốt để khai trương trong tháng 11/2025:")
for ngay in ngay_tot:
    print(f"  {ngay['solar']['day']}/{ngay['solar']['month']}/{ngay['solar']['year']} - Sao {ngay['star']['name']}")
```

### 4. Kiểm tra tuổi xung

```python
import vnlunar

jd = vnlunar.jdn(7, 11, 2025)
nam_sinh = 1990

# Kiểm tra tuổi có xung không
xung = vnlunar.check_age_conflict(jd, nam_sinh)
print(f"Năm sinh {nam_sinh} xung với ngày này: {'Có' if xung else 'Không'}")

# Lấy thông tin chi tiết về tuổi xung
tuoi_xung_info = vnlunar.get_conflicting_ages(jd, 2025)
print(f"\n{tuoi_xung_info['description']}")
print(f"Các tuổi xung trong ngày này:")
for tuoi in tuoi_xung_info['ages'][:5]:
    print(f"  Tuổi {tuoi['age']}: {tuoi['can_chi']} ({tuoi['animal']})")
```

### 5. Xem hướng xuất hành

```python
import vnlunar

jd = vnlunar.jdn(7, 11, 2025)

# Hướng theo ngày
huong_ngay = vnlunar.get_direction_info(jd)
print(f"Hướng tốt: {', '.join(huong_ngay['good_directions'])}")
print(f"Hướng xấu: {', '.join(huong_ngay['bad_directions'])}")

# Hướng theo tuổi
huong_tuoi = vnlunar.get_age_direction(1990, 2025)
print(f"\nTuổi: {huong_tuoi['age']} ({huong_tuoi['zodiac']})")
print(f"Hướng tốt: {', '.join(huong_tuoi['good_directions'])}")

# Hướng kết hợp
huong_xuat_hanh = vnlunar.get_travel_direction(jd, 1990, 2025)
print(f"\n{huong_xuat_hanh['advice']}")
```

### 6. Giờ Hoàng Đạo

```python
import vnlunar

jd = vnlunar.jdn(7, 11, 2025)

# Lấy các giờ Hoàng Đạo trong ngày
gio_hoang_dao = vnlunar.get_auspicious_hours(jd)
print("Giờ Hoàng Đạo:")
for hour in gio_hoang_dao:
    print(f"  {hour['hour_name']}: {hour['time_range']}")

# Kiểm tra một giờ cụ thể
gio_info = vnlunar.check_travel_hour(jd, "Tý")
print(f"\nGiờ {gio_info['zodiac_hour']}: {'TỐT' if gio_info['is_good'] else 'XẤU'}")
```

## Các loại việc hỗ trợ xem ngày

- `"wedding"`: Cưới hỏi
- `"building"`: Xây nhà
- `"travel"`: Xuất hành
- `"opening"`: Khai trương
- `"moving"`: Chuyển nhà
- `"investing"`: Đầu tư

## API Reference

### Core Functions

- `jdn(day, month, year)`: Chuyển ngày dương lịch sang Julian Day Number
- `jdn2date(jd)`: Chuyển Julian Day Number sang ngày dương lịch
- `get_lunar_date(day, month, year)`: Lấy thông tin âm lịch
- `convert_solar_to_lunar(day, month, year, timezone)`: Chuyển đổi với múi giờ tùy chỉnh

### Calendar Functions

- `get_can_chi(lunar)`: Lấy Can Chi của ngày, tháng, năm
- `get_year_can_chi(year)`: Lấy Can Chi của năm
- `get_year_element(year)`: Lấy Ngũ Hành của năm
- `get_auspicious_hours(jd)`: Lấy giờ Hoàng Đạo
- `get_day_of_week(jd)`: Lấy thứ trong tuần

### Astrology Functions

- `get_12_stars(lunar_day, lunar_month)`: Lấy 12 Sao Kiến Trừ
- `get_12_gods(jd)`: Lấy 12 Thần Hoàng Đạo/Hắc Đạo
- `get_12_constructions(lunar_day, lunar_month)`: Lấy Thập Nhị Trực
- `get_28_mansions(jd)`: Lấy 28 Tú Sao
- `get_nayin(jd)`: Lấy Nạp Âm
- `get_day_type(lunar_day, lunar_month)`: Kiểm tra Hoàng Đạo/Hắc Đạo
- `check_good_day(jd, activity)`: Xem ngày tốt xấu cho việc
- `find_good_days(start_jd, end_jd, activity)`: Tìm các ngày tốt

### Direction Functions

- `get_conflicting_ages(jd, current_year)`: Lấy thông tin tuổi xung
- `check_age_conflict(jd, birth_year)`: Kiểm tra tuổi xung
- `get_direction_info(jd)`: Lấy hướng theo Ngọc Hạp Thông Thư
- `get_god_directions(jd)`: Lấy hướng thần (Thần Tài, Hỷ Thần, Phúc Thần)
- `get_age_direction(birth_year, current_year)`: Hướng theo tuổi
- `get_travel_direction(jd, birth_year, current_year)`: Hướng xuất hành tổng hợp
- `check_travel_hour(jd, zodiac_hour)`: Kiểm tra giờ xuất hành

### Main Function

- `get_full_info(day, month, year)`: Lấy tất cả thông tin của một ngày

## So sánh với cnlunar (Lịch Trung Quốc)

| Tính năng | vnlunar (VN) | cnlunar (CN) |
|-----------|----------------|--------------|
| Múi giờ mặc định | UTC+7 (VN) | UTC+8 (CN) |
| Thuật toán | Thiên văn VN | Thiên văn CN |
| Tên Can Chi | Tiếng Việt | Tiếng Trung |
| Con giáp | Mèo (năm Mão) | Thỏ (năm Mão) |
| Tiết khí | Tiếng Việt | Tiếng Trung |
| Hướng xuất hành | Theo truyền thống VN | Theo truyền thống CN |

## Đóng góp / Contributing

Mọi đóng góp đều được hoan nghênh! Vui lòng:

1. Fork repository
2. Tạo branch mới (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Mở Pull Request

## License

Free for personal and non-commercial use.

## Version

Current version: **1.0.3**

## Credits

- Dựa trên thuật toán thiên văn của Ho Ngoc Duc
- Tham khảo: "Lịch Việt Nam - Nguyên lý và các bảng tra cứu" - Hoàng Xuân Hãn

## Liên hệ / Contact

- **Website**: https://vnlunar.min-services.com
- GitHub Issues: [https://github.com/min9802/pyvnlunar/issues](https://github.com/min9802/pyvnlunar/issues)

---

Made with ❤️ for Vietnamese Lunar Calendar
