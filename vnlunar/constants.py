"""
Constants for Vietnamese Lunar Calendar
Các hằng số cho Âm lịch Việt Nam

FILE ĐƯỢC SINH TỰ ĐỘNG từ vnlunar-ts (scripts/export-py-constants.js) - không sửa tay.
Xem docs/DECISIONS.md trong vnlunar-ts cho quy ước tính toán.
"""

import math

# *** Mathematical Constants ***
PI = math.pi

# Julian day offset
JULIAN_DAY_OFFSET = 2415021

# Timezone for Vietnam (UTC+7)
TIMEZONE = 7.0

# Phạm vi bảng TK19..TK22
FIRST_DAY = 2378521  # jdn(25, 1, 1800)
LAST_DAY = 2524593  # jdn(31, 12, 2199)

# Lunar calendar data 1800-1899 (Hồ Ngọc Đức)
TK19 = [
    0x30baa3, 0x56ab50, 0x422ba0, 0x2cab61, 0x52a370, 0x3c51e8, 0x60d160, 0x4ae4b0, 0x376926, 0x58daa0,
    0x445b50, 0x3116d2, 0x562ae0, 0x3ea2e0, 0x28e2d2, 0x4ec950, 0x38d556, 0x5cb520, 0x46b690, 0x325da4,
    0x5855d0, 0x4225d0, 0x2ca5b3, 0x52a2b0, 0x3da8b7, 0x60a950, 0x4ab4a0, 0x35b2a5, 0x5aad50, 0x4455b0,
    0x302b74, 0x562570, 0x4052f9, 0x6452b0, 0x4e6950, 0x386d56, 0x5e5aa0, 0x46ab50, 0x3256d4, 0x584ae0,
    0x42a570, 0x2d4553, 0x50d2a0, 0x3be8a7, 0x60d550, 0x4a5aa0, 0x34ada5, 0x5a95d0, 0x464ae0, 0x2eaab4,
    0x54a4d0, 0x3ed2b8, 0x64b290, 0x4cb550, 0x385757, 0x5e2da0, 0x4895d0, 0x324d75, 0x5849b0, 0x42a4b0,
    0x2da4b3, 0x506a90, 0x3aad98, 0x606b50, 0x4c2b60, 0x359365, 0x5a9370, 0x464970, 0x306964, 0x52e4a0,
    0x3cea6a, 0x62da90, 0x4e5ad0, 0x392ad6, 0x5e2ae0, 0x4892e0, 0x32cad5, 0x56c950, 0x40d4a0, 0x2bd4a3,
    0x50b690, 0x3a57a7, 0x6055b0, 0x4c25d0, 0x3695b5, 0x5a92b0, 0x44a950, 0x2ed954, 0x54b4a0, 0x3cb550,
    0x286b52, 0x4e55b0, 0x3a2776, 0x5e2570, 0x4852b0, 0x32aaa5, 0x56e950, 0x406aa0, 0x2abaa3, 0x50ab50
]

# Lunar calendar data 1900-1999
TK20 = [
    0x3c4bd8, 0x624ae0, 0x4ca570, 0x3854d5, 0x5cd260, 0x44d950, 0x315554, 0x5656a0, 0x409ad0, 0x2a55d2,
    0x504ae0, 0x3aa5b6, 0x60a4d0, 0x48d250, 0x33d255, 0x58b540, 0x42d6a0, 0x2cada2, 0x5295b0, 0x3f4977,
    0x644970, 0x4ca4b0, 0x36b4b5, 0x5c6a50, 0x466d50, 0x312b54, 0x562b60, 0x409570, 0x2c52f2, 0x504970,
    0x3a6566, 0x5ed4a0, 0x48ea50, 0x336a95, 0x585ad0, 0x442b60, 0x2f86e3, 0x5292e0, 0x3dc8d7, 0x62c950,
    0x4cd4a0, 0x35d8a6, 0x5ab550, 0x4656a0, 0x31a5b4, 0x5625d0, 0x4092d0, 0x2ad2b2, 0x50a950, 0x38b557,
    0x5e6ca0, 0x48b550, 0x355355, 0x584da0, 0x42a5b0, 0x2f4573, 0x5452b0, 0x3ca9a8, 0x60e950, 0x4c6aa0,
    0x36aea6, 0x5aab50, 0x464b60, 0x30aae4, 0x56a570, 0x405260, 0x28f263, 0x4ed940, 0x38db47, 0x5cd6a0,
    0x4896d0, 0x344dd5, 0x5a4ad0, 0x42a4d0, 0x2cd4b4, 0x52b250, 0x3cd558, 0x60b540, 0x4ab5a0, 0x3755a6,
    0x5c95b0, 0x4649b0, 0x30a974, 0x56a4b0, 0x40aa50, 0x29aa52, 0x4e6d20, 0x39ad47, 0x5eab60, 0x489370,
    0x344af5, 0x5a4970, 0x4464b0, 0x2c74a3, 0x50ea50, 0x3d6a58, 0x6256a0, 0x4aaad0, 0x3696d5, 0x5c92e0
]

# Lunar calendar data 2000-2099
TK21 = [
    0x46c960, 0x2ed954, 0x54d4a0, 0x3eda50, 0x2a7552, 0x4e56a0, 0x38a7a7, 0x5ea5d0, 0x4a92b0, 0x32aab5,
    0x58a950, 0x42b4a0, 0x2cbaa4, 0x50ad50, 0x3c55d9, 0x624ba0, 0x4ca5b0, 0x375176, 0x5c5270, 0x466930,
    0x307934, 0x546aa0, 0x3ead50, 0x2a5b52, 0x504b60, 0x38a6e6, 0x5ea4e0, 0x48d260, 0x32ea65, 0x56d520,
    0x40daa0, 0x2d56a3, 0x5256d0, 0x3c4afb, 0x6249d0, 0x4ca4d0, 0x37d0b6, 0x5ab250, 0x44b520, 0x2edd25,
    0x54b5a0, 0x3e55d0, 0x2a55b2, 0x5049b0, 0x3aa577, 0x5ea4b0, 0x48aa50, 0x33b255, 0x586d20, 0x40ad60,
    0x2d4b63, 0x525370, 0x3e49e8, 0x60c970, 0x4c54b0, 0x3768a6, 0x5ada50, 0x445aa0, 0x2fa6a4, 0x54aad0,
    0x4052e0, 0x28d2e3, 0x4ec950, 0x38d557, 0x5ed4a0, 0x46d950, 0x325d55, 0x5856a0, 0x42a6d0, 0x2c55d4,
    0x5252b0, 0x3ca9b8, 0x62a930, 0x4ab490, 0x34b6a6, 0x5aad50, 0x4655a0, 0x2eab64, 0x54a570, 0x4052b0,
    0x2ab173, 0x4e6930, 0x386b37, 0x5e6aa0, 0x48ad50, 0x332ad5, 0x582b60, 0x42a570, 0x2e52e4, 0x50d160,
    0x3ae958, 0x60d520, 0x4ada90, 0x355aa6, 0x5a56d0, 0x462ae0, 0x30a9d4, 0x54a2d0, 0x3ed150, 0x28e952
]

# Lunar calendar data 2100-2199
TK22 = [
    0x4eb520, 0x38d727, 0x5eada0, 0x4a55b0, 0x362db5, 0x5a45b0, 0x44a2b0, 0x2eb2b4, 0x54a950, 0x3cb559,
    0x626b20, 0x4cad50, 0x385766, 0x5c5370, 0x484570, 0x326574, 0x5852b0, 0x406950, 0x2a7953, 0x505aa0,
    0x3baaa7, 0x5ea6d0, 0x4a4ae0, 0x35a2e5, 0x5aa550, 0x42d2a0, 0x2de2a4, 0x52d550, 0x3e5abb, 0x6256a0,
    0x4c96d0, 0x3949b6, 0x5e4ab0, 0x46a8d0, 0x30d4b5, 0x56b290, 0x40b550, 0x2a6d52, 0x504da0, 0x3b9567,
    0x609570, 0x4a49b0, 0x34a975, 0x5a64b0, 0x446a90, 0x2cba94, 0x526b50, 0x3e2b60, 0x28ab61, 0x4c9570,
    0x384ae6, 0x5cd160, 0x46e4a0, 0x2eed25, 0x54da90, 0x405b50, 0x2c36d3, 0x502ae0, 0x3a93d7, 0x6092d0,
    0x4ac950, 0x32d556, 0x58b4a0, 0x42b690, 0x2e5d94, 0x5255b0, 0x3e25fa, 0x6425b0, 0x4e92b0, 0x36aab6,
    0x5c6950, 0x4674a0, 0x31b2a5, 0x54ad50, 0x4055a0, 0x2aab73, 0x522570, 0x3a5377, 0x6052b0, 0x4a6950,
    0x346d56, 0x585aa0, 0x42ab50, 0x2e56d4, 0x544ae0, 0x3ca570, 0x2864d2, 0x4cd260, 0x36eaa6, 0x5ad550,
    0x465aa0, 0x30ada5, 0x5695d0, 0x404ad0, 0x2aa9b3, 0x50a4d0, 0x3ad2b7, 0x5eb250, 0x48b540, 0x33d556
]

# Heavenly Stems (Can - Thiên Can)
CAN = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]

# Earthly Branches (Chi - Địa Chi)
CHI = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]

# Chinese Zodiac Animals (Con Giáp)
CHI_ANIMALS = ["Chuột", "Trâu", "Hổ", "Mèo", "Rồng", "Rắn", "Ngựa", "Dê", "Khỉ", "Gà", "Chó", "Lợn"]

# Days of week
WEEKDAYS = ["Chủ nhật", "Thứ hai", "Thứ ba", "Thứ tư", "Thứ năm", "Thứ sáu", "Thứ bảy"]

# Solar terms (Tiết khí), 0 = Xuân phân
SOLAR_TERMS = ["Xuân phân", "Thanh minh", "Cốc vũ", "Lập hạ", "Tiểu mãn", "Mang chủng", "Hạ chí", "Tiểu thử", "Đại thử", "Lập thu", "Xử thử", "Bạch lộ", "Thu phân", "Hàn lộ", "Sương giáng", "Lập đông", "Tiểu tuyết", "Đại tuyết", "Đông chí", "Tiểu hàn", "Đại hàn", "Lập xuân", "Vũ Thủy", "Kinh trập"]


# Five Elements (Ngũ Hành)
class ELEMENT:
    """Five Elements constants"""
    WATER = "Thủy"
    FIRE = "Hỏa"
    WOOD = "Mộc"
    METAL = "Kim"
    EARTH = "Thổ"


# Five Elements by Heavenly Stems
CAN_ELEMENTS = ["Mộc", "Mộc", "Hỏa", "Hỏa", "Thổ", "Thổ", "Kim", "Kim", "Thủy", "Thủy"]

# Five Elements by Earthly Branches
CHI_ELEMENTS = ["Thủy", "Thổ", "Mộc", "Mộc", "Thổ", "Hỏa", "Hỏa", "Thổ", "Kim", "Kim", "Thổ", "Thủy"]

# Auspicious hours by day branch (Giờ Hoàng Đạo)
AUSPICIOUS_HOURS = ["110100101100", "001101001011", "110011010010", "101100110100", "001011001101", "010010110011", "110100101100", "001101001011", "110011010010", "101100110100", "001011001101", "010010110011"]

# Thập Nhị Trực (tóm tắt): "Kiến Mãn Bình Thu hắc, Trừ Nguy Định Chấp hoàng,
# Thành Khai giai khả dụng, Bế Phá bất tương đương"
STARS_12 = [
    {"name": "Kiến", "status": "neutral", "color": "orange", "description": "Tốt cho xuất hành, nhậm chức, cầu tài; kỵ động thổ, đào giếng, an táng"},
    {"name": "Trừ", "status": "good", "color": "green", "description": "Tốt cho trừ bệnh, giải hạn, dọn dẹp, phá bỏ cái cũ; kỵ cưới hỏi, khai trương"},
    {"name": "Mãn", "status": "neutral", "color": "orange", "description": "Tốt cho cầu tài, cầu phúc, khai trương, nhập kho; kỵ nhậm chức, kiện tụng"},
    {"name": "Bình", "status": "neutral", "color": "orange", "description": "Tốt cho sửa sang nhà cửa, làm đường; việc lớn nên cân nhắc"},
    {"name": "Định", "status": "good", "color": "green", "description": "Tốt cho động thổ, nhập học, cầu thân, ký kết; kỵ kiện tụng, xuất hành xa"},
    {"name": "Chấp", "status": "good", "color": "green", "description": "Tốt cho xây dựng, sửa chữa, trồng trọt, tuyển người; kỵ xuất hành, chuyển nhà"},
    {"name": "Phá", "status": "bad", "color": "red", "description": "Chỉ tốt cho phá dỡ, chữa bệnh; kỵ mọi việc lớn"},
    {"name": "Nguy", "status": "good", "color": "green", "description": "Tốt cho cúng lễ, cầu an; kỵ leo cao, đi sông nước, việc mạo hiểm"},
    {"name": "Thành", "status": "good", "color": "green", "description": "Tốt cho cưới hỏi, khai trương, ký kết, nhập trạch, nhập học; kỵ kiện tụng"},
    {"name": "Thu", "status": "neutral", "color": "orange", "description": "Tốt cho thu nợ, thu hoạch, nhập kho; kỵ khai trương, an táng, xuất hành"},
    {"name": "Khai", "status": "good", "color": "green", "description": "Tốt cho khai trương, xuất hành, nhập học, cưới hỏi, làm nhà; kỵ an táng"},
    {"name": "Bế", "status": "bad", "color": "red", "description": "Chỉ tốt cho đắp đê, lấp hố, an táng; kỵ khai trương, xuất hành, cưới hỏi"}
]

# 12 Thần trực nhật (Hoàng Đạo / Hắc Đạo)
GODS_12 = [
    {"name": "Thanh Long", "type": "auspicious", "status": "good", "description": "Hoàng Đạo - Tốt cho mọi việc"},
    {"name": "Minh Đường", "type": "auspicious", "status": "good", "description": "Hoàng Đạo - Tốt cho gặp gỡ, văn thư"},
    {"name": "Thiên Hình", "type": "inauspicious", "status": "bad", "description": "Hắc Đạo - Xấu, tránh kiện tụng"},
    {"name": "Chu Tước", "type": "inauspicious", "status": "bad", "description": "Hắc Đạo - Xấu, tránh tranh cãi"},
    {"name": "Kim Quỹ", "type": "auspicious", "status": "good", "description": "Hoàng Đạo - Tốt cho cầu tài, xuất hành"},
    {"name": "Thiên Đức", "alias": "Bảo Quang", "type": "auspicious", "status": "good", "description": "Hoàng Đạo (còn gọi Bảo Quang) - Rất tốt, quý nhân giúp đỡ"},
    {"name": "Bạch Hổ", "type": "inauspicious", "status": "bad", "description": "Hắc Đạo - Rất xấu, tránh mọi việc"},
    {"name": "Ngọc Đường", "type": "auspicious", "status": "good", "description": "Hoàng Đạo - Tốt cho cưới hỏi, gia đạo"},
    {"name": "Thiên Lao", "type": "inauspicious", "status": "bad", "description": "Hắc Đạo - Xấu, tránh kiện tụng"},
    {"name": "Huyền Vũ", "type": "inauspicious", "status": "bad", "description": "Hắc Đạo - Xấu, cẩn thận trộm cắp"},
    {"name": "Tư Mệnh", "type": "auspicious", "status": "good", "description": "Hoàng Đạo - Tốt cho quan chức, công việc"},
    {"name": "Câu Trần", "type": "inauspicious", "status": "bad", "description": "Hắc Đạo - Xấu, tránh xuất hành"}
]

# Thập Nhị Trực (chi tiết)
CONSTRUCTIONS_12 = [
    {"name": "Trực Kiến", "short_name": "Kiến", "status": "neutral", "good_for": ["Xuất hành", "Nhậm chức", "Cầu tài", "Gặp gỡ đối tác"], "bad_for": ["Động thổ", "Đào giếng", "An táng", "Mở kho"]},
    {"name": "Trực Trừ", "short_name": "Trừ", "status": "good", "good_for": ["Chữa bệnh", "Giải hạn, cúng giải trừ", "Tắm gội, dọn dẹp", "Phá dỡ nhà cũ"], "bad_for": ["Cưới hỏi", "Khai trương", "Xuất hành xa", "Ký kết, giao dịch lớn"]},
    {"name": "Trực Mãn", "short_name": "Mãn", "status": "neutral", "good_for": ["Cầu tài, cầu phúc", "Khai trương", "Nhập kho, nhập hàng", "Tế tự"], "bad_for": ["Nhậm chức", "Kiện tụng", "Chữa bệnh", "An táng"]},
    {"name": "Trực Bình", "short_name": "Bình", "status": "neutral", "good_for": ["Sửa sang nhà cửa", "Làm đường, san nền", "Việc nhỏ thường ngày"], "bad_for": ["Cưới hỏi", "Khai trương", "Xuất hành xa", "Đào mương, khơi rãnh"]},
    {"name": "Trực Định", "short_name": "Định", "status": "good", "good_for": ["Động thổ, san nền", "Nhập học", "Cầu thân, đính hôn", "Ký kết, giao dịch", "Mua bán gia súc"], "bad_for": ["Kiện tụng", "Xuất hành xa", "Chữa bệnh"]},
    {"name": "Trực Chấp", "short_name": "Chấp", "status": "good", "good_for": ["Xây dựng, sửa chữa", "Trồng trọt", "Tuyển người, thuê người làm", "Bắt kẻ gian"], "bad_for": ["Xuất hành", "Mở kho, xuất tiền", "Chuyển nhà", "Khai trương"]},
    {"name": "Trực Phá", "short_name": "Phá", "status": "bad", "good_for": ["Phá dỡ nhà cũ", "Chữa bệnh", "Dọn dẹp, tiêu hủy đồ cũ"], "bad_for": ["Cưới hỏi", "Khai trương", "Ký kết", "Xuất hành", "Động thổ"]},
    {"name": "Trực Nguy", "short_name": "Nguy", "status": "good", "good_for": ["Cúng lễ, cầu an", "An giường", "Việc nhỏ cần thận trọng"], "bad_for": ["Leo cao, đi sông nước", "Xuất hành xa", "Khai trương", "Đầu tư mạo hiểm"]},
    {"name": "Trực Thành", "short_name": "Thành", "status": "good", "good_for": ["Cưới hỏi", "Khai trương", "Ký kết, giao dịch", "Nhập trạch, chuyển nhà", "Nhập học", "Xuất hành"], "bad_for": ["Kiện tụng, tranh chấp"]},
    {"name": "Trực Thu", "short_name": "Thu", "status": "neutral", "good_for": ["Thu nợ, thu hoạch", "Nhập kho, mua hàng", "Cầu tài"], "bad_for": ["Khai trương", "An táng", "Xuất hành", "Chữa bệnh"]},
    {"name": "Trực Khai", "short_name": "Khai", "status": "good", "good_for": ["Khai trương", "Xuất hành", "Nhập học", "Cưới hỏi", "Động thổ, làm nhà", "Nhậm chức"], "bad_for": ["An táng", "Động mồ mả", "Chặt cây"]},
    {"name": "Trực Bế", "short_name": "Bế", "status": "bad", "good_for": ["Đắp đê, lấp hố, sửa tường", "An táng", "Cất giữ, đóng kho"], "bad_for": ["Khai trương", "Xuất hành", "Cưới hỏi", "Chữa bệnh", "Nhậm chức"]}
]

# Nhị Thập Bát Tú (14 cát tú)
MANSIONS_28 = [
    {"name": "Giác", "full_name": "Giác Mộc Giao", "animal": "Giao (thuồng luồng)", "element": "Mộc", "good": True, "description": "Cát tú - Tốt cho cưới hỏi, xây dựng, thi cử; kỵ an táng"},
    {"name": "Cang", "full_name": "Cang Kim Long", "animal": "Rồng", "element": "Kim", "good": False, "description": "Hung tú - Kỵ cưới hỏi, xây dựng, an táng"},
    {"name": "Đê", "full_name": "Đê Thổ Lạc", "animal": "Lạc (lửng)", "element": "Thổ", "good": False, "description": "Hung tú - Kỵ khởi công, cưới hỏi, đi đường thủy"},
    {"name": "Phòng", "full_name": "Phòng Nhật Thố", "animal": "Thỏ", "element": "Nhật", "good": True, "description": "Cát tú - Tốt cho cưới hỏi, xây dựng, khai trương"},
    {"name": "Tâm", "full_name": "Tâm Nguyệt Hồ", "animal": "Cáo", "element": "Nguyệt", "good": False, "description": "Hung tú - Kỵ khởi công, cưới hỏi, kiện tụng"},
    {"name": "Vĩ", "full_name": "Vĩ Hỏa Hổ", "animal": "Hổ", "element": "Hỏa", "good": True, "description": "Cát tú - Tốt cho cưới hỏi, xây dựng, khai trương"},
    {"name": "Cơ", "full_name": "Cơ Thủy Báo", "animal": "Báo", "element": "Thủy", "good": True, "description": "Cát tú - Tốt cho xây dựng, khai trương, an táng"},
    {"name": "Đẩu", "full_name": "Đẩu Mộc Giải", "animal": "Giải (cua)", "element": "Mộc", "good": True, "description": "Cát tú - Tốt cho xây dựng, may mặc, khai trương"},
    {"name": "Ngưu", "full_name": "Ngưu Kim Ngưu", "animal": "Trâu", "element": "Kim", "good": False, "description": "Hung tú - Kỵ cưới hỏi, xây dựng, khai trương"},
    {"name": "Nữ", "full_name": "Nữ Thổ Bức", "animal": "Dơi", "element": "Thổ", "good": False, "description": "Hung tú - Kỵ cưới hỏi, kiện tụng, an táng"},
    {"name": "Hư", "full_name": "Hư Nhật Thử", "animal": "Chuột", "element": "Nhật", "good": False, "description": "Hung tú - Kỵ cưới hỏi, xây dựng, khai trương"},
    {"name": "Nguy", "full_name": "Nguy Nguyệt Yến", "animal": "Chim én", "element": "Nguyệt", "good": False, "description": "Hung tú - Kỵ xây dựng, đi sông nước, cưới hỏi"},
    {"name": "Thất", "full_name": "Thất Hỏa Trư", "animal": "Lợn", "element": "Hỏa", "good": True, "description": "Cát tú - Tốt cho cưới hỏi, xây dựng, khai trương, an táng"},
    {"name": "Bích", "full_name": "Bích Thủy Du", "animal": "Du (rái cá)", "element": "Thủy", "good": True, "description": "Cát tú - Tốt cho cưới hỏi, xây dựng, khai trương"},
    {"name": "Khuê", "full_name": "Khuê Mộc Lang", "animal": "Sói", "element": "Mộc", "good": False, "description": "Hung tú - Kỵ khai trương, an táng; tốt cho nhập học"},
    {"name": "Lâu", "full_name": "Lâu Kim Cẩu", "animal": "Chó", "element": "Kim", "good": True, "description": "Cát tú - Tốt cho cưới hỏi, xây dựng, khai trương"},
    {"name": "Vị", "full_name": "Vị Thổ Trĩ", "animal": "Chim trĩ", "element": "Thổ", "good": True, "description": "Cát tú - Tốt cho cưới hỏi, xây dựng, kinh doanh"},
    {"name": "Mão", "full_name": "Mão Nhật Kê", "animal": "Gà", "element": "Nhật", "good": False, "description": "Hung tú - Kỵ cưới hỏi, xây cất, khai trương"},
    {"name": "Tất", "full_name": "Tất Nguyệt Ô", "animal": "Quạ", "element": "Nguyệt", "good": True, "description": "Cát tú - Tốt cho xây dựng, cưới hỏi, khai trương"},
    {"name": "Chủy", "full_name": "Chủy Hỏa Hầu", "animal": "Khỉ", "element": "Hỏa", "good": False, "description": "Hung tú - Kỵ xây dựng, an táng"},
    {"name": "Sâm", "full_name": "Sâm Thủy Viên", "animal": "Vượn", "element": "Thủy", "good": True, "description": "Cát tú - Tốt cho xây dựng, khai trương, nhập học; kỵ cưới hỏi"},
    {"name": "Tỉnh", "full_name": "Tỉnh Mộc Hãn", "animal": "Hãn (chó rừng)", "element": "Mộc", "good": True, "description": "Cát tú - Tốt cho xây dựng, nhập học, cầu tài; kỵ an táng"},
    {"name": "Quỷ", "full_name": "Quỷ Kim Dương", "animal": "Dê", "element": "Kim", "good": False, "description": "Hung tú - Kỵ hầu hết mọi việc, chỉ hợp an táng"},
    {"name": "Liễu", "full_name": "Liễu Thổ Chương", "animal": "Chương (hoẵng)", "element": "Thổ", "good": False, "description": "Hung tú - Kỵ xây dựng, cưới hỏi, an táng"},
    {"name": "Tinh", "full_name": "Tinh Nhật Mã", "animal": "Ngựa", "element": "Nhật", "good": False, "description": "Hung tú - Kỵ cưới hỏi, đào ao; tạm được cho xây dựng"},
    {"name": "Trương", "full_name": "Trương Nguyệt Lộc", "animal": "Nai", "element": "Nguyệt", "good": True, "description": "Cát tú - Tốt cho xây dựng, cưới hỏi, khai trương"},
    {"name": "Dực", "full_name": "Dực Hỏa Xà", "animal": "Rắn", "element": "Hỏa", "good": False, "description": "Hung tú - Kỵ xây dựng, cưới hỏi, an táng"},
    {"name": "Chẩn", "full_name": "Chẩn Thủy Dẫn", "animal": "Giun", "element": "Thủy", "good": True, "description": "Cát tú - Tốt cho cưới hỏi, xây dựng, khai trương, xuất hành"}
]

# 30 Nạp Âm (mỗi Nạp Âm ứng với 2 Can Chi liên tiếp)
NAYIN_30 = ["Hải Trung Kim", "Lư Trung Hỏa", "Đại Lâm Mộc", "Lộ Bàng Thổ", "Kiếm Phong Kim", "Sơn Đầu Hỏa", "Giản Hạ Thủy", "Thành Đầu Thổ", "Bạch Lạp Kim", "Dương Liễu Mộc", "Tuyền Trung Thủy", "Ốc Thượng Thổ", "Tích Lịch Hỏa", "Tòng Bách Mộc", "Trường Lưu Thủy", "Sa Trung Kim", "Sơn Hạ Hỏa", "Bình Địa Mộc", "Bích Thượng Thổ", "Kim Bạc Kim", "Phúc Đăng Hỏa", "Thiên Hà Thủy", "Đại Trạch Thổ", "Thoa Xuyến Kim", "Tang Đố Mộc", "Đại Khê Thủy", "Sa Trung Thổ", "Thiên Thượng Hỏa", "Thạch Lựu Mộc", "Đại Hải Thủy"]

# 60 Nạp Âm theo chỉ số Lục Thập Hoa Giáp (0 = Giáp Tý ... 59 = Quý Hợi)
NAYIN_60 = [name for name in NAYIN_30 for _ in range(2)]

# Direction names (8 hướng)
DIRECTIONS = ["Bắc", "Đông Bắc", "Đông", "Đông Nam", "Nam", "Tây Nam", "Tây", "Tây Bắc"]

# Ngọc Hạp Thông Thư (hướng theo chi ngày) - THỰC NGHIỆM, chưa có nguồn đối chiếu
DIRECTION_MAP = {"Tý": {"good": ["Đông", "Tây", "Nam"], "bad": ["Bắc", "Đông Bắc", "Tây Bắc", "Đông Nam", "Tây Nam"]}, "Sửu": {"good": ["Đông", "Nam", "Tây"], "bad": ["Bắc", "Đông Bắc", "Tây Bắc", "Đông Nam", "Tây Nam"]}, "Dần": {"good": ["Đông", "Nam", "Bắc"], "bad": ["Tây", "Đông Bắc", "Tây Bắc", "Đông Nam", "Tây Nam"]}, "Mão": {"good": ["Bắc", "Nam", "Tây"], "bad": ["Đông", "Đông Bắc", "Tây Bắc", "Đông Nam", "Tây Nam"]}, "Thìn": {"good": ["Bắc", "Đông", "Tây"], "bad": ["Nam", "Đông Bắc", "Tây Bắc", "Đông Nam", "Tây Nam"]}, "Tỵ": {"good": ["Bắc", "Đông", "Nam"], "bad": ["Tây", "Đông Bắc", "Tây Bắc", "Đông Nam", "Tây Nam"]}, "Ngọ": {"good": ["Đông", "Tây", "Bắc"], "bad": ["Nam", "Đông Bắc", "Tây Bắc", "Đông Nam", "Tây Nam"]}, "Mùi": {"good": ["Đông", "Bắc", "Tây"], "bad": ["Nam", "Đông Bắc", "Tây Bắc", "Đông Nam", "Tây Nam"]}, "Thân": {"good": ["Bắc", "Nam", "Đông"], "bad": ["Tây", "Đông Bắc", "Tây Bắc", "Đông Nam", "Tây Nam"]}, "Dậu": {"good": ["Bắc", "Nam", "Tây"], "bad": ["Đông", "Đông Bắc", "Tây Bắc", "Đông Nam", "Tây Nam"]}, "Tuất": {"good": ["Đông", "Tây", "Nam"], "bad": ["Bắc", "Đông Bắc", "Tây Bắc", "Đông Nam", "Tây Nam"]}, "Hợi": {"good": ["Đông", "Nam", "Bắc"], "bad": ["Tây", "Đông Bắc", "Tây Bắc", "Đông Nam", "Tây Nam"]}}

# Hướng Hỷ Thần, Tài Thần theo Can ngày (Giáp → Quý)
JOY_GOD_DIR = ["Đông Bắc", "Tây Bắc", "Tây Nam", "Nam", "Đông Nam", "Đông Bắc", "Tây Bắc", "Tây Nam", "Nam", "Đông Nam"]
WEALTH_GOD_DIR = ["Đông Nam", "Đông Nam", "Đông", "Đông", "Bắc", "Nam", "Tây Nam", "Tây Nam", "Tây", "Tây Bắc"]
# Hướng Phúc Thần - CHƯA được đối chiếu nguồn
FORTUNE_GOD_DIR = ["Bắc", "Tây Nam", "Đông Nam", "Đông", "Đông Bắc", "Nam", "Tây", "Tây Bắc", "Tây Nam", "Đông Nam"]

# Giờ xuất hành theo Lý Thuần Phong (theo chi ngày)
TRAVEL_HOURS_LY = {0: [0, 2, 3, 6, 7, 9], 1: [1, 2, 5, 6, 8, 11], 2: [0, 1, 4, 5, 9, 10], 3: [0, 3, 4, 7, 8, 11], 4: [1, 3, 5, 7, 9, 11], 5: [0, 2, 4, 6, 8, 10], 6: [0, 2, 3, 6, 7, 9], 7: [1, 2, 5, 6, 8, 11], 8: [0, 1, 4, 5, 9, 10], 9: [0, 3, 4, 7, 8, 11], 10: [1, 3, 5, 7, 9, 11], 11: [0, 2, 4, 6, 8, 10]}
