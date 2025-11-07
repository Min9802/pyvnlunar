# vnlunar - Hướng dẫn Sử dụng Nhanh


### Cấu trúc thư viện

```
vnlunar/
├── vnlunar/                 # Source code chính
│   ├── __init__.py          # Module entry point
│   ├── lunar_types.py       # Type definitions
│   ├── constants.py         # Vietnamese constants & data
│   ├── core.py              # Astronomical algorithms
│   ├── calendar.py          # Can Chi & Five Elements
│   ├── astrology.py         # 12 Stars, 28 Mansions, etc.
│   └── direction.py         # Travel directions, age conflicts
├── examples/                # Ví dụ sử dụng
│   ├── example_basic.py
│   ├── example_xem_ngay.py
│   ├── example_huong_xuat_hanh.py
│   ├── example_ngu_hanh.py
│   └── README.md
├── test_vnlunar.py          # Test script đơn giản
├── setup.py                 # Package setup
├── requirements.txt         # Dependencies (empty - no external deps)
├── README.md                # Documentation
└── LICENSE                  # MIT License
```

## Cách sử dụng

### 1. Test nhanh (không cần cài đặt)

```bash
cd h:\Project\python\vnlunar\pyvnlunar
python test_vnlunar.py
```

### 2. Cài đặt package

```bash
cd h:\Project\python\vnlunar\pyvnlunar
pip install -e .
```

Sau khi cài đặt, bạn có thể import trực tiếp:

```python
import vnlunar

# Sử dụng các functions
lunar = vnlunar.get_lunar_date(7, 11, 2025)
info = vnlunar.get_full_info(7, 11, 2025)
```

### 3. Chạy ví dụ

```bash
cd h:\Project\python\vnlunar\pyvnlunar
python test_vnlunar.py  # Test cơ bản
```

## Tính năng chính

### ✅ Core Functions (core.py)
- `jdn(day, month, year)` - Chuyển ngày thành Julian Day Number
- `jdn2date(jd)` - Chuyển JDN về ngày
- `get_lunar_date(day, month, year)` - Lấy thông tin âm lịch
- `convert_solar_to_lunar()` - Chuyển đổi với múi giờ tùy chỉnh

### ✅ Calendar Functions (calendar.py)
- `get_can_chi(lunar)` - Lấy Can Chi ngày/tháng/năm
- `get_year_element(year)` - Lấy Ngũ Hành của năm
- `get_auspicious_hours(jd)` - Lấy giờ Hoàng Đạo
- `get_day_of_week(jd)` - Lấy thứ trong tuần

### ✅ Astrology Functions (astrology.py)
- `get_12_stars()` - 12 Sao Kiến Trừ
- `get_12_gods()` - 12 Thần Hoàng Đạo/Hắc Đạo
- `get_12_constructions()` - Thập Nhị Trực
- `get_28_mansions()` - 28 Tú Sao
- `get_nayin()` - Nạp Âm 60
- `check_good_day(jd, activity)` - Xem ngày tốt xấu cho việc
- `find_good_days()` - Tìm các ngày tốt

### ✅ Direction Functions (direction.py)
- `get_conflicting_ages()` - Lấy thông tin tuổi xung
- `check_age_conflict()` - Kiểm tra tuổi xung
- `get_direction_info()` - Hướng theo cổ thư
- `get_god_directions()` - Hướng các vị thần
- `get_age_direction()` - Hướng theo tuổi
- `get_travel_direction()` - Hướng xuất hành tổng hợp
- `check_travel_hour()` - Kiểm tra giờ xuất hành

## Ví dụ sử dụng cơ bản

```python
import vnlunar

# Chuyển đổi ngày
lunar = vnlunar.get_lunar_date(7, 11, 2025)
print(f"Âm lịch: {lunar['day']}/{lunar['month']}/{lunar['year']}")

# Lấy thông tin đầy đủ
info = vnlunar.get_full_info(7, 11, 2025)
print(f"Can Chi: {info['can_chi']['day']}")
print(f"12 Sao: {info['12_stars']['name']}")

# Xem ngày
jd = vnlunar.jdn(15, 12, 2025)
ket_qua = vnlunar.check_good_day(jd, "wedding")
print(f"Cưới hỏi: {ket_qua['description']}")
```

## Điểm khác biệt với cnlunar (Lịch Trung Quốc)

- **Múi giờ**: UTC+7 (Việt Nam) thay vì UTC+8 (Trung Quốc)
- **Tên Can Chi**: Tiếng Việt thuần túy
- **Con giáp**: Mèo (Mão) thay vì Thỏ
- **Thuật toán**: Theo truyền thống Việt Nam
- **Hướng xuất hành**: Theo phong tục Việt Nam

## Các tính năng đã implement

✅ Chuyển đổi dương lịch <-> âm lịch  
✅ Can Chi (Thiên Can Địa Chi)  
✅ Ngũ Hành (Five Elements) và quan hệ Sinh/Khắc  
✅ 12 Sao Kiến Trừ  
✅ 12 Thần Hoàng Đạo/Hắc Đạo  
✅ Thập Nhị Trực  
✅ 28 Tú Sao  
✅ Nạp Âm 60  
✅ Giờ Hoàng Đạo  
✅ Xem ngày tốt xấu cho các việc (cưới hỏi, xây nhà, xuất hành, v.v.)  
✅ Tìm ngày tốt trong khoảng thời gian  
✅ Tuổi xung (Age conflicts)  
✅ Hướng xuất hành theo ngày và tuổi  
✅ Hướng các vị thần (Thần Tài, Hỷ Thần, Phúc Thần)  

## Hướng phát triển tiếp theo

Nếu muốn package hoạt động như một module chuẩn, cần:

1. **Tổ chức lại cấu trúc thư mục** để hỗ trợ `import pyvnlunar` trực tiếp
2. **Viết tests** với pytest
3. **Thêm CI/CD** với GitHub Actions
4. **Publish lên PyPI** để `pip install pyvnlunar`
5. **Documentation** với Sphinx hoặc MkDocs
6. **Type hints đầy đủ** và mypy checking

## Credits

- Based on Ho Ngoc Duc's astronomical algorithms
- Vietnamese lunar calendar traditions

## License

MIT License - Free for personal and non-commercial use

---

**Status**: ✅ Core implementation complete and tested
**Version**: 1.0.2  
**Date**: November 2025
