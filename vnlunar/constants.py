"""
Vietnamese Lunar Calendar Constants and Data
All constants and data arrays for Vietnamese lunar calendar calculations
"""

import math

# *** Mathematical Constants ***
PI = math.pi

# *** Lunar Calendar Conversion Constants ***

# Julian day offset
JULIAN_DAY_OFFSET = 2415021

# Timezone for Vietnam (UTC+7)
TIMEZONE = 7.0

# *** Lunar Calendar Data Arrays ***

# Lunar calendar data from 1800 to 1899
TK19 = [
    0x30baa3, 0x56ab50, 0x422ba0, 0x2cab61, 0x52a370, 0x3c51e8, 0x60d160, 0x4ae4b0, 0x376926, 0x58daa0,
    0x445b50, 0x3116d2, 0x562ae0, 0x3ea2e0, 0x28e2d2, 0x4ec950, 0x38d556, 0x5ed4a0, 0x46d950, 0x325d55,
    0x5856a0, 0x42a6d0, 0x2c55d4, 0x5252b0, 0x3ca9b8, 0x62a930, 0x4ab490, 0x34b6a6, 0x5aad50, 0x4655a0,
    0x2eab64, 0x54a570, 0x4052b0, 0x2ab173, 0x4e6930, 0x386b37, 0x5e6aa0, 0x48ad50, 0x332ad5, 0x582b60,
    0x42a570, 0x2e52e4, 0x50d160, 0x3ae958, 0x60d520, 0x4ada90, 0x355aa6, 0x5a56d0, 0x462ae0, 0x30a9d4,
    0x54a2d0, 0x3ed150, 0x28e952, 0x4eb520, 0x38d727, 0x5eada0, 0x4a55b0, 0x362db5, 0x5a45b0, 0x44a2b0,
    0x2eb2b4, 0x54a950, 0x3cb559, 0x626b20, 0x4cad50, 0x385766, 0x5c5370, 0x484570, 0x326574, 0x5852b0,
    0x406950, 0x2a7953, 0x505aa0, 0x3baaa7, 0x5ea6d0, 0x4a4ae0, 0x35a2e5, 0x5aa550, 0x42d2a0, 0x2de2a4,
    0x52d550, 0x3e5abb, 0x6256a0, 0x4c96d0, 0x3949b6, 0x5e4ab0, 0x46a8d0, 0x30d4b5, 0x56b290, 0x40b550,
    0x2a6d52, 0x504da0, 0x3b9567, 0x609570, 0x4a49b0, 0x34a975, 0x5a64b0, 0x446a90, 0x2cba94, 0x526b50
]

# Lunar calendar data from 1900 to 2199
TK20 = [
    0x3e2b60, 0x28ab61, 0x4c9570, 0x384ae6, 0x5cd160, 0x46e4a0, 0x2eed25, 0x54da90, 0x405b50, 0x2c36d3,
    0x502ae0, 0x3a93d7, 0x6092d0, 0x4ac950, 0x32d556, 0x58b4a0, 0x42b690, 0x2e5d94, 0x5255b0, 0x3e25fa,
    0x6425b0, 0x4e92b0, 0x36aab6, 0x5c6950, 0x4674a0, 0x31b2a5, 0x54ad50, 0x4055a0, 0x2aab73, 0x522570,
    0x3a5377, 0x6052b0, 0x4a6950, 0x346d56, 0x585aa0, 0x42ab50, 0x2e56d4, 0x544ae0, 0x3ca570, 0x2864d2,
    0x4cd260, 0x36eaa6, 0x5ad550, 0x465aa0, 0x30ada5, 0x5695d0, 0x404ad0, 0x2aa9b3, 0x50a4d0, 0x3ad2b7,
    0x5eb250, 0x48b540, 0x33d556, 0x58d4a0, 0x4215a5, 0x2896d0, 0x4c95b0, 0x3a4ab6, 0x5e4ad0, 0x48a570,
    0x3252d5, 0x58d160, 0x42e4a0, 0x2ceda4, 0x50d550, 0x3e5ad7, 0x6256a0, 0x4c96d0, 0x3a4afb, 0x5e4ad0,
    0x46aad0, 0x30d4b5, 0x56d2a0, 0x40d950, 0x2a5d54, 0x4e5aa0, 0x38a7a7, 0x5ea6d0, 0x48a2d0, 0x34d2b5,
    0x58b2a0, 0x42b550, 0x2ebd63, 0x52ada0, 0x3c95b7, 0x624970, 0x4c4ab0, 0x3695b5, 0x5c6a50, 0x466d50,
    0x2eaed4, 0x54daa0, 0x3eb5a6, 0x6295b0, 0x4c55b0, 0x38a6b4, 0x5e52b0, 0x46b2a0, 0x32abb3, 0x58a950,
    0x406d50, 0x2a5d55, 0x505aa0, 0x3abaa7, 0x60ad50, 0x4c55a0, 0x3695d5, 0x5c52b0, 0x46a930, 0x30b2a4,
    0x56ab50, 0x406570, 0x2c56d3, 0x524ae0, 0x3ca5d7, 0x62a2d0, 0x4ad150, 0x356d56, 0x5ab550, 0x4655a0,
    0x30ada5, 0x5695d0, 0x404ad0, 0x2aa9b3, 0x50a4d0, 0x3ad2b7, 0x5eb550, 0x48b540, 0x33d556, 0x58d4a0,
    0x4215a5, 0x2896d0, 0x4c95b0, 0x3a4ab6, 0x5e4ad0, 0x48a570, 0x3252d5, 0x58d160, 0x42e4a0, 0x2ceda4,
    0x50d550, 0x3e5ad7, 0x6256a0, 0x4c96d0, 0x3a4afb, 0x5e4ad0, 0x46aad0, 0x30d4b5, 0x56d2a0, 0x40d950,
    0x2a5d54, 0x4e5aa0, 0x38a7a7, 0x5ea6d0, 0x48a2d0, 0x34d2b5, 0x58b2a0, 0x42b550, 0x2ebd63, 0x52ada0,
    0x3c95b7, 0x624970, 0x4c4ab0, 0x3695b5, 0x5c6a50, 0x466d50, 0x2eaed4, 0x54daa0, 0x3eb5a6, 0x6295b0,
    0x4c55b0, 0x38a6b4, 0x5e52b0, 0x46b2a0, 0x32abb3, 0x58a950, 0x406d50, 0x2a5d55, 0x505aa0, 0x3abaa7,
    0x60ad50, 0x4c55a0, 0x3695d5, 0x5c52b0, 0x46a930, 0x30b2a4, 0x56ab50, 0x406570, 0x2c56d3, 0x524ae0,
    0x3ca5d7, 0x62a2d0, 0x4ad150, 0x356d56, 0x5ab550, 0x4655a0, 0x30ada5, 0x5695d0, 0x404ad0, 0x2aa9b3,
    0x50a4d0, 0x3ad2b7, 0x5eb550, 0x48b540, 0x33d556, 0x58d4a0, 0x4215a5, 0x2896d0, 0x4c95b0, 0x3a4ab6,
    0x5e4ad0, 0x48a570, 0x3252d5, 0x58d160, 0x42e4a0, 0x2ceda4, 0x50d550, 0x3e5ad7, 0x6256a0, 0x4c96d0,
    0x3a4afb, 0x5e4ad0, 0x46aad0, 0x30d4b5, 0x56d2a0, 0x40d950, 0x2a5d54, 0x4e5aa0, 0x38a7a7, 0x5ea6d0,
    0x48a2d0, 0x34d2b5, 0x58b2a0, 0x42b550, 0x2ebd63, 0x52ada0, 0x3c95b7, 0x624970, 0x4c4ab0, 0x3695b5,
    0x5c6a50, 0x466d50, 0x2eaed4, 0x54daa0, 0x3eb5a6, 0x6295b0, 0x4c55b0, 0x38a6b4, 0x5e52b0, 0x46b2a0,
    0x32abb3, 0x58a950, 0x406d50, 0x2a5d55, 0x505aa0, 0x3abaa7, 0x60ad50, 0x4c55a0, 0x3695d5, 0x5c52b0,
    0x46a930, 0x30b2a4, 0x56ab50, 0x406570, 0x2c56d3, 0x524ae0, 0x3ca5d7, 0x62a2d0, 0x4ad150, 0x356d56,
    0x5ab550, 0x4655a0, 0x30ada5, 0x5695d0, 0x404ad0, 0x2aa9b3, 0x50a4d0, 0x3ad2b7, 0x5eb550, 0x48b540,
    0x33d556, 0x58d4a0, 0x4215a5, 0x2896d0, 0x4c95b0, 0x3a4ab6, 0x5e4ad0, 0x48a570, 0x3252d5, 0x58d160,
    0x42e4a0, 0x2ceda4, 0x50d550, 0x3e5ad7, 0x6256a0, 0x4c96d0, 0x3a4afb, 0x5e4ad0, 0x46aad0, 0x30d4b5
]

# Lunar calendar data from 2200 to 2299
TK21 = [
    0x56b2a0, 0x40d950, 0x2a5d54, 0x4e5aa0, 0x38a7a7, 0x5ea6d0, 0x48a2d0, 0x34d2b5, 0x58b2a0, 0x42b550,
    0x2ebd63, 0x52ada0, 0x3c95b7, 0x624970, 0x4c4ab0, 0x3695b5, 0x5c6a50, 0x466d50, 0x2eaed4, 0x54daa0,
    0x3eb5a6, 0x6295b0, 0x4c55b0, 0x38a6b4, 0x5e52b0, 0x46b2a0, 0x32abb3, 0x58a950, 0x406d50, 0x2a5d55,
    0x505aa0, 0x3abaa7, 0x60ad50, 0x4c55a0, 0x3695d5, 0x5c52b0, 0x46a930, 0x30b2a4, 0x56ab50, 0x406570,
    0x2c56d3, 0x524ae0, 0x3ca5d7, 0x62a2d0, 0x4ad150, 0x356d56, 0x5ab550, 0x4655a0, 0x30ada5, 0x5695d0,
    0x404ad0, 0x2aa9b3, 0x50a4d0, 0x3ad2b7, 0x5eb550, 0x48b540, 0x33d556, 0x58d4a0, 0x4215a5, 0x2896d0,
    0x4c95b0, 0x3a4ab6, 0x5e4ad0, 0x48a570, 0x3252d5, 0x58d160, 0x42e4a0, 0x2ceda4, 0x50d550, 0x3e5ad7,
    0x6256a0, 0x4c96d0, 0x3a4afb, 0x5e4ad0, 0x46aad0, 0x30d4b5, 0x56d2a0, 0x40d950, 0x2a5d54, 0x4e5aa0,
    0x38a7a7, 0x5ea6d0, 0x48a2d0, 0x34d2b5, 0x58b2a0, 0x42b550, 0x2ebd63, 0x52ada0, 0x3c95b7, 0x624970,
    0x4c4ab0, 0x3695b5, 0x5c6a50, 0x466d50, 0x2eaed4, 0x54daa0, 0x3eb5a6, 0x6295b0, 0x4c55b0, 0x38a6b4
]

# Lunar calendar data from 2300 to 2399
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

# Solar terms (Tiết khí)
SOLAR_TERMS = [
    "Xuân phân", "Thanh minh", "Cốc vũ", "Lập hạ", "Tiểu mãn", "Mang chủng",
    "Hạ chí", "Tiểu thử", "Đại thử", "Lập thu", "Xử thử", "Bạch lộ",
    "Thu phân", "Hàn lộ", "Sương giáng", "Lập đông", "Tiểu tuyết", "Đại tuyết",
    "Đông chí", "Tiểu hàn", "Đại hàn", "Lập xuân", "Vũ Thủy", "Kinh trập"
]

# Five Elements (Ngũ Hành)
class ELEMENT:
    """Five Elements constants"""
    WATER = "Thủy"
    FIRE = "Hỏa"
    WOOD = "Mộc"
    METAL = "Kim"
    EARTH = "Thổ"

# Five Elements by Heavenly Stems
CAN_ELEMENTS = [
    ELEMENT.WOOD, ELEMENT.WOOD,    # Giáp, Ất = Mộc
    ELEMENT.FIRE, ELEMENT.FIRE,    # Bính, Đinh = Hỏa
    ELEMENT.EARTH, ELEMENT.EARTH,  # Mậu, Kỷ = Thổ
    ELEMENT.METAL, ELEMENT.METAL,  # Canh, Tân = Kim
    ELEMENT.WATER, ELEMENT.WATER   # Nhâm, Quý = Thủy
]

# Five Elements by Earthly Branches
CHI_ELEMENTS = [
    ELEMENT.WATER, ELEMENT.EARTH,  # Tý = Thủy, Sửu = Thổ
    ELEMENT.WOOD, ELEMENT.WOOD,    # Dần, Mão = Mộc
    ELEMENT.EARTH, ELEMENT.FIRE,   # Thìn = Thổ, Tỵ = Hỏa
    ELEMENT.FIRE, ELEMENT.EARTH,   # Ngọ = Hỏa, Mùi = Thổ
    ELEMENT.METAL, ELEMENT.METAL,  # Thân, Dậu = Kim
    ELEMENT.EARTH, ELEMENT.WATER   # Tuất = Thổ, Hợi = Thủy
]

# Auspicious hours by day branch
AUSPICIOUS_HOURS = [
    "110100101100",  # Tý
    "001101001011",  # Sửu
    "110011010010",  # Dần
    "101100110100",  # Mão
    "001011001101",  # Thìn
    "010010110011",  # Tỵ
    "110100101100",  # Ngọ
    "001101001011",  # Mùi
    "110011010010",  # Thân
    "101100110100",  # Dậu
    "001011001101",  # Tuất
    "010010110011"   # Hợi
]

# 12 Day Officers (12 Sao Kiến Trừ)
STARS_12 = [
    {"name": "Kiến", "status": "good", "color": "green", "description": "Khai trương, cưới hỏi, xuất hành, xây dựng"},
    {"name": "Trừ", "status": "bad", "color": "red", "description": "Xấu, chỉ tốt cho trừ bệnh, dọn dẹp, phá cũ"},
    {"name": "Mãn", "status": "good", "color": "green", "description": "Tốt cho hội họp, cưới hỏi, khánh thành, cầu tài"},
    {"name": "Bình", "status": "neutral", "color": "orange", "description": "Trung bình, an táng, tu bổ"},
    {"name": "Định", "status": "good", "color": "green", "description": "Tốt cho ký kết, cưới hỏi, xây dựng, khai trương"},
    {"name": "Chấp", "status": "neutral", "color": "orange", "description": "Tốt cho xây dựng, an táng, không tốt cho xuất hành"},
    {"name": "Phá", "status": "bad", "color": "red", "description": "Rất xấu, tránh mọi việc quan trọng"},
    {"name": "Nguy", "status": "bad", "color": "red", "description": "Nguy hiểm, tránh xuất hành, động thổ, cưới hỏi"},
    {"name": "Thành", "status": "good", "color": "green", "description": "Rất tốt, mọi việc đều thuận lợi"},
    {"name": "Thu", "status": "good", "color": "green", "description": "Tốt cho thu hoạch, kết quả, cầu tài"},
    {"name": "Khai", "status": "good", "color": "green", "description": "Khai trương, xuất hành, khai công, mọi việc đều tốt"},
    {"name": "Bế", "status": "bad", "color": "red", "description": "Đóng cửa, tránh mọi việc quan trọng, chỉ tốt cho tu tâm"}
]

# 12 Gods (12 Thần - Hoàng Đạo/Hắc Đạo)
GODS_12 = [
    {"name": "Thanh Long", "type": "auspicious", "status": "good", "description": "Sao tốt - Hoàng Đạo"},
    {"name": "Minh Đường", "type": "auspicious", "status": "good", "description": "Sao tốt - Hoàng Đạo"},
    {"name": "Thiên Hình", "type": "inauspicious", "status": "bad", "description": "Sao xấu - Hắc Đạo"},
    {"name": "Chu Tước", "type": "inauspicious", "status": "bad", "description": "Sao xấu - Hắc Đạo"},
    {"name": "Kim Quỹ", "type": "auspicious", "status": "good", "description": "Sao tốt - Hoàng Đạo"},
    {"name": "Thiên Đức", "type": "auspicious", "status": "good", "description": "Sao tốt - Hoàng Đạo"},
    {"name": "Bạch Hổ", "type": "inauspicious", "status": "bad", "description": "Sao xấu - Hắc Đạo"},
    {"name": "Ngọc Đường", "type": "auspicious", "status": "good", "description": "Sao tốt - Hoàng Đạo"},
    {"name": "Thiên Lao", "type": "inauspicious", "status": "bad", "description": "Sao xấu - Hắc Đạo"},
    {"name": "Huyền Vũ", "type": "inauspicious", "status": "bad", "description": "Sao xấu - Hắc Đạo"},
    {"name": "Tư Mệnh", "type": "auspicious", "status": "good", "description": "Sao tốt - Hoàng Đạo"},
    {"name": "Câu Trần", "type": "inauspicious", "status": "bad", "description": "Sao xấu - Hắc Đạo"}
]

# 12 Day Construction (Thập Nhị Trực)
CONSTRUCTIONS_12 = [
    {
        "name": "Trực kiến",
        "good_for": ["Động thổ", "san nền đắp nền", "lên quan nhậm chức", "xuất hành", "khai trương tàu thuyền", "khởi công làm lò"],
        "bad_for": ["Khai trương", "khởi công xây cất và chôn cất"]
    },
    {
        "name": "Trực trừ",
        "good_for": ["Giải trừ", "tắm gội", "chỉnh dung", "cạo đầu", "chỉnh tay chân móng", "cầu y trị bệnh", "quét dọn nhà cửa"],
        "bad_for": ["Mọi việc khác"]
    },
    {
        "name": "Trực mãn",
        "good_for": ["Tiến người", "may cắt", "dựng cột lên đòn dông", "kinh vệ", "khai trương", "lập khoán giao dịch", "nạp tài", "mở kho", "đắp lỗ lỗ rác", "sửa tường"],
        "bad_for": ["Tế tự", "cầu phúc", "cầu tự", "lên sách chương biểu", "ban chiếu", "ban ơn", "chiêu hiền cử nhân"]
    },
    {
        "name": "Trực bình",
        "good_for": ["Tu sửa tường tường", "bình trị đạo đồ"],
        "bad_for": ["Cầu phúc cầu tự", "lên sách lên chương biểu"]
    },
    {
        "name": "Trực định",
        "good_for": ["Quan đái"],
        "bad_for": ["Mọi việc khác"]
    },
    {
        "name": "Trực chấp",
        "good_for": ["Bắt bớ"],
        "bad_for": ["Mọi việc khác"]
    },
    {
        "name": "Trực phá",
        "good_for": ["Cầu y trị bệnh"],
        "bad_for": ["Mọi việc khác"]
    },
    {
        "name": "Trực nguy",
        "good_for": ["An phủ biên cảnh", "tuyển tướng", "an sàng"],
        "bad_for": ["Mọi việc khác"]
    },
    {
        "name": "Trực thành",
        "good_for": ["Nhập học", "an phủ biên cảnh", "di chuyển", "trúc đê phòng", "khai trương"],
        "bad_for": ["Mọi việc khác"]
    },
    {
        "name": "Trực thu",
        "good_for": ["Tiến người", "nạp tài", "bắt bớ", "thu tất"],
        "bad_for": ["Cầu phúc cầu tự", "lên sách lên chương biểu"]
    },
    {
        "name": "Trực khai",
        "good_for": ["Tế tự", "cầu phúc", "cầu tự", "lên sách lên chương biểu", "xuất hành", "lên quan lâm chính", "di chuyển"],
        "bad_for": ["Mọi việc khác"]
    },
    {
        "name": "Trực bế",
        "good_for": ["Trúc đê phòng", "đắp lỗ", "sửa tường"],
        "bad_for": ["Lên sách lên chương biểu", "xuất hành", "khai trương"]
    }
]

# 28 Lunar Mansions (28 Tú Sao)
MANSIONS_28 = [
    {"name": "Giác", "animal": "Giao", "element": "Mộc", "good": True, "description": "Tốt"},
    {"name": "Cang", "animal": "Rồng", "element": "Kim", "good": False, "description": "Xấu"},
    {"name": "Đê", "animal": "Lễ", "element": "Thổ", "good": False, "description": "Xấu"},
    {"name": "Phòng", "animal": "Thỏ", "element": "Nhật", "good": True, "description": "Tốt"},
    {"name": "Tâm", "animal": "Cáo", "element": "Nguyệt", "good": False, "description": "Xấu"},
    {"name": "Vĩ", "animal": "Hổ", "element": "Hỏa", "good": True, "description": "Tốt"},
    {"name": "Cơ", "animal": "Báo", "element": "Thủy", "good": True, "description": "Tốt"},
    {"name": "Đẩu", "animal": "Hề", "element": "Thủy", "good": True, "description": "Tốt"},
    {"name": "Ngưu", "animal": "Trâu", "element": "Kim", "good": False, "description": "Xấu"},
    {"name": "Nữ", "animal": "Dơi", "element": "Thổ", "good": False, "description": "Xấu"},
    {"name": "Hư", "animal": "Chuột", "element": "Nhật", "good": False, "description": "Xấu"},
    {"name": "Nguy", "animal": "Nhén", "element": "Nguyệt", "good": False, "description": "Xấu"},
    {"name": "Thất", "animal": "Heo", "element": "Hỏa", "good": True, "description": "Tốt"},
    {"name": "Bích", "animal": "Chốc", "element": "Thủy", "good": True, "description": "Tốt"},
    {"name": "Khuê", "animal": "Sói", "element": "Mộc", "good": False, "description": "Xấu"},
    {"name": "Lâu", "animal": "Chó", "element": "Kim", "good": False, "description": "Xấu"},
    {"name": "Vị", "animal": "Trĩ", "element": "Thổ", "good": True, "description": "Tốt"},
    {"name": "Mão", "animal": "Gà", "element": "Nhật", "good": True, "description": "Tốt"},
    {"name": "Tất", "animal": "Quạ", "element": "Nguyệt", "good": True, "description": "Tốt"},
    {"name": "Chủy", "animal": "Khỉ", "element": "Hỏa", "good": False, "description": "Xấu"},
    {"name": "Thâm", "animal": "Vượn", "element": "Thủy", "good": True, "description": "Tốt"},
    {"name": "Tỉnh", "animal": "Dẫn", "element": "Mộc", "good": True, "description": "Tốt"},
    {"name": "Quỷ", "animal": "Dương", "element": "Kim", "good": False, "description": "Xấu"},
    {"name": "Liễu", "animal": "Nai", "element": "Thổ", "good": False, "description": "Xấu"},
    {"name": "Tinh", "animal": "Ngựa", "element": "Nhật", "good": False, "description": "Xấu"},
    {"name": "Trương", "animal": "Lộc", "element": "Nguyệt", "good": True, "description": "Tốt"},
    {"name": "Dực", "animal": "Rắn", "element": "Hỏa", "good": False, "description": "Xấu"},
    {"name": "Chẩn", "animal": "Giun", "element": "Thủy", "good": True, "description": "Tốt"}
]

# Nayin 60 (Nạp Âm 60)
NAYIN_60 = [
    "Hải Trung Kim", "Hải Trung Kim", "Lư Trung Hỏa", "Lư Trung Hỏa", "Đại Lâm Mộc", "Đại Lâm Mộc",
    "Lộ Bàng Thổ", "Lộ Bàng Thổ", "Kiếm Phong Kim", "Kiếm Phong Kim", "Sơn Đầu Hỏa", "Sơn Đầu Hỏa",
    "Giản Hạ Thủy", "Giản Hạ Thủy", "Thành Đầu Thổ", "Thành Đầu Thổ", "Bạch Lạp Kim", "Bạch Lạp Kim",
    "Dương Liễu Mộc", "Dương Liễu Mộc", "Tuyền Trung Thủy", "Tuyền Trung Thủy", "Ốc Thượng Thổ", "Ốc Thượng Thổ",
    "Tích Lịch Hỏa", "Tích Lịch Hỏa", "Tòng Bách Mộc", "Tòng Bách Mộc", "Trường Lưu Thủy", "Trường Lưu Thủy",
    "Sa Trung Kim", "Sa Trung Kim", "Sơn Hạ Hỏa", "Sơn Hạ Hỏa", "Bình Địa Mộc", "Bình Địa Mộc",
    "Bích Thượng Thổ", "Bích Thượng Thổ", "Kim Bạc Kim", "Kim Bạc Kim", "Phúc Đăng Hỏa", "Phúc Đăng Hỏa",
    "Thiên Hà Thủy", "Thiên Hà Thủy", "Đại Dịch Thổ", "Đại Dịch Thổ", "Thoa Xuyến Kim", "Thoa Xuyến Kim",
    "Tang Đố Mộc", "Tang Đố Mộc", "Đại Khê Thủy", "Đại Khê Thủy", "Sa Trung Thổ", "Sa Trung Thổ",
    "Thiên Thượng Hỏa", "Thiên Thượng Hỏa", "Thạch Lựu Mộc", "Thạch Lựu Mộc", "Đại Hải Thủy", "Đại Hải Thủy"
]

# Direction names (8 hướng)
DIRECTIONS = ["Bắc", "Đông Bắc", "Đông", "Đông Nam", "Nam", "Tây Nam", "Tây", "Tây Bắc"]

# Ngọc Hạp Thông Thư (Direction by day Chi)
DIRECTION_MAP = {
    "Tý": {"good": ["Đông", "Tây", "Nam"], "bad": ["Bắc", "Đông Bắc", "Tây Bắc", "Đông Nam", "Tây Nam"]},
    "Sửu": {"good": ["Đông", "Nam", "Tây"], "bad": ["Bắc", "Đông Bắc", "Tây Bắc", "Đông Nam", "Tây Nam"]},
    "Dần": {"good": ["Đông", "Nam", "Bắc"], "bad": ["Tây", "Đông Bắc", "Tây Bắc", "Đông Nam", "Tây Nam"]},
    "Mão": {"good": ["Bắc", "Nam", "Tây"], "bad": ["Đông", "Đông Bắc", "Tây Bắc", "Đông Nam", "Tây Nam"]},
    "Thìn": {"good": ["Bắc", "Đông", "Tây"], "bad": ["Nam", "Đông Bắc", "Tây Bắc", "Đông Nam", "Tây Nam"]},
    "Tỵ": {"good": ["Bắc", "Đông", "Nam"], "bad": ["Tây", "Đông Bắc", "Tây Bắc", "Đông Nam", "Tây Nam"]},
    "Ngọ": {"good": ["Đông", "Tây", "Bắc"], "bad": ["Nam", "Đông Bắc", "Tây Bắc", "Đông Nam", "Tây Nam"]},
    "Mùi": {"good": ["Đông", "Bắc", "Tây"], "bad": ["Nam", "Đông Bắc", "Tây Bắc", "Đông Nam", "Tây Nam"]},
    "Thân": {"good": ["Bắc", "Nam", "Đông"], "bad": ["Tây", "Đông Bắc", "Tây Bắc", "Đông Nam", "Tây Nam"]},
    "Dậu": {"good": ["Bắc", "Nam", "Tây"], "bad": ["Đông", "Đông Bắc", "Tây Bắc", "Đông Nam", "Tây Nam"]},
    "Tuất": {"good": ["Đông", "Tây", "Nam"], "bad": ["Bắc", "Đông Bắc", "Tây Bắc", "Đông Nam", "Tây Nam"]},
    "Hợi": {"good": ["Đông", "Nam", "Bắc"], "bad": ["Tây", "Đông Bắc", "Tây Bắc", "Đông Nam", "Tây Nam"]}
}

# Hướng Thần Tài, Hỷ Thần, Phúc Thần theo Can Ngày
WEALTH_GOD_DIR = ["Đông Bắc", "Đông", "Đông Nam", "Nam", "Nam", "Tây Nam", "Tây", "Tây Bắc", "Bắc", "Bắc"]
JOY_GOD_DIR = ["Đông Nam", "Đông Nam", "Nam", "Nam", "Đông Bắc", "Đông", "Tây Bắc", "Tây", "Tây Nam", "Tây"]
FORTUNE_GOD_DIR = ["Bắc", "Tây Nam", "Đông Nam", "Đông", "Đông Bắc", "Nam", "Tây", "Tây Bắc", "Tây Nam", "Đông Nam"]
