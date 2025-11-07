"""
Astrology functions: 12 Stars, 28 Mansions, Nayin, etc.
Các hàm xử lý chiêm tinh: 12 Sao, 28 Tú, Nạp Âm, v.v.
"""

from typing import Dict, List

try:
    from .lunar_types import (
        Star12Info, God12Info, Construction12Info, Mansion28Info,
        NayinInfo, DayTypeInfo, DaySelectionResult
    )
    from .constants import (
        STARS_12, GODS_12, CONSTRUCTIONS_12,
        MANSIONS_28, NAYIN_60, CAN, CHI
    )
    from .core import jdn2date, convert_solar_to_lunar, jdn
except ImportError:
    from lunar_types import (
        Star12Info, God12Info, Construction12Info, Mansion28Info,
        NayinInfo, DayTypeInfo, DaySelectionResult
    )
    from constants import (
        STARS_12, GODS_12, CONSTRUCTIONS_12,
        MANSIONS_28, NAYIN_60, CAN, CHI
    )
    from core import jdn2date, convert_solar_to_lunar, jdn


def get_12_stars(lunar_day: int, lunar_month: int) -> Star12Info:
    """
    Get 12 Day Officer (12 Sao Kiến Trừ)
    Lấy 12 Sao Kiến Trừ
    
    Args:
        lunar_day: Lunar day / Ngày âm lịch
        lunar_month: Lunar month / Tháng âm lịch
        
    Returns:
        Star information / Thông tin sao
    """
    star_index = (lunar_month + lunar_day - 2) % 12
    if star_index < 0:
        star_index += 12
    return STARS_12[star_index]


def get_12_gods(jd: int) -> God12Info:
    """
    Get 12 Gods (Hoàng Đạo/Hắc Đạo)
    Lấy 12 Thần (Hoàng Đạo/Hắc Đạo)
    
    Args:
        jd: Julian Day Number
        
    Returns:
        God information / Thông tin thần
    """
    day_chi = (jd + 1) % 12
    god_index = (day_chi + 8) % 12
    return GODS_12[god_index]


def get_12_constructions(lunar_day: int, lunar_month: int) -> Construction12Info:
    """
    Get 12 Day Construction (Thập Nhị Trực)
    Lấy Thập Nhị Trực
    
    Args:
        lunar_day: Lunar day / Ngày âm lịch
        lunar_month: Lunar month / Tháng âm lịch
        
    Returns:
        Construction information / Thông tin trực
    """
    index = (lunar_day + lunar_month + 2) % 12
    if index < 0:
        index += 12
    return CONSTRUCTIONS_12[index]


def get_28_mansions(jd: int) -> Mansion28Info:
    """
    Get 28 Lunar Mansion
    Lấy 28 Tú Sao
    
    Args:
        jd: Julian Day Number
        
    Returns:
        Mansion information / Thông tin tú sao
    """
    mansion_index = (jd + 11) % 28
    return MANSIONS_28[mansion_index]


def get_nayin(jd: int) -> NayinInfo:
    """
    Get Nayin (Nạp Âm) of the day
    Lấy Nạp Âm của ngày
    
    Args:
        jd: Julian Day Number
        
    Returns:
        Nayin information / Thông tin Nạp Âm
    """
    can_index = (jd + 9) % 10
    chi_index = (jd + 1) % 12
    
    # Find Can Chi 60 index
    can_chi_60_index = -1
    for i in range(60):
        if i % 10 == can_index and i % 12 == chi_index:
            can_chi_60_index = i
            break
    
    nayin_index = can_chi_60_index // 2
    nayin_name = NAYIN_60[nayin_index]
    
    # Determine element
    element = ""
    if "Kim" in nayin_name:
        element = "Kim"
    elif "Mộc" in nayin_name:
        element = "Mộc"
    elif "Thủy" in nayin_name:
        element = "Thủy"
    elif "Hỏa" in nayin_name or "Hoả" in nayin_name:
        element = "Hỏa"
    elif "Thổ" in nayin_name:
        element = "Thổ"
    
    return {
        'name': nayin_name,
        'element': element,
        'can': CAN[can_index],
        'chi': CHI[chi_index]
    }


def get_day_type(lunar_day: int, lunar_month: int) -> DayTypeInfo:
    """
    Check if day is Auspicious (Hoàng Đạo) or Inauspicious (Hắc Đạo)
    Kiểm tra ngày là Hoàng Đạo hay Hắc Đạo
    
    Args:
        lunar_day: Lunar day / Ngày âm lịch
        lunar_month: Lunar month / Tháng âm lịch
        
    Returns:
        Auspicious/Inauspicious information
    """
    star = get_12_stars(lunar_day, lunar_month)
    auspicious = ["Kiến", "Mãn", "Định", "Thành", "Thu", "Khai"]
    inauspicious = ["Trừ", "Bình", "Chấp", "Phá", "Nguy", "Bế"]
    
    is_auspicious = star['name'] in auspicious
    is_inauspicious = star['name'] in inauspicious
    
    return {
        'type': "Hoàng Đạo" if is_auspicious else "Hắc Đạo",
        'star': star['name'],
        'good': is_auspicious,
        'bad': is_inauspicious,
        'desc': "Ngày Hoàng Đạo - Tốt, thuận lợi" if is_auspicious else "Ngày Hắc Đạo - Xấu, nên tránh"
    }


def check_good_day(jd: int, activity: str) -> DaySelectionResult:
    """
    Check if day is good for specific activity
    Kiểm tra ngày tốt cho việc cụ thể
    
    Args:
        jd: Julian Day Number
        activity: Activity type: "wedding", "construction", "travel", "opening", "moving", "investment"
        
    Returns:
        Day selection result / Kết quả xem ngày
    """
    solar_date = jdn2date(jd)
    lunar = convert_solar_to_lunar(solar_date[0], solar_date[1], solar_date[2], 7.0)
    star = get_12_stars(lunar['day'], lunar['month'])
    
    # Define good stars for each activity
    good_for_activity = {
        "wedding": ["Kiến", "Mãn", "Định", "Thành", "Khai"],
        "construction": ["Kiến", "Định", "Thành", "Khai"],
        "travel": ["Kiến", "Mãn", "Thành", "Khai"],
        "opening": ["Kiến", "Thành", "Khai", "Thu"],
        "moving": ["Kiến", "Mãn", "Thành"],
        "investment": ["Định", "Thành", "Thu", "Khai"]
    }
    
    good_list = good_for_activity.get(activity, [])
    is_good = star['name'] in good_list
    
    activity_names = {
        "wedding": "cưới hỏi",
        "construction": "xây nhà",
        "travel": "xuất hành",
        "opening": "khai trương",
        "moving": "chuyển nhà",
        "investment": "đầu tư"
    }
    
    activity_name = activity_names.get(activity, activity)
    
    if is_good:
        description = f"Ngày {star['name']} - TỐT cho {activity_name}"
    else:
        description = f"Ngày {star['name']} - KHÔNG TỐT cho {activity_name}"
    
    return {
        'star': star,
        'activity': activity_name,
        'good': is_good,
        'description': description
    }


def find_good_days(start_jd: int, end_jd: int, activity: str) -> List[Dict]:
    """
    Find good days for specific activity in date range
    Tìm các ngày tốt cho việc cụ thể trong khoảng thời gian
    
    Args:
        start_jd: Start Julian Day Number / JDN bắt đầu
        end_jd: End Julian Day Number / JDN kết thúc
        activity: Activity type / Loại việc
        
    Returns:
        List of good days / Danh sách các ngày tốt
    """
    good_days = []
    
    for jd_num in range(start_jd, end_jd + 1):
        result = check_good_day(jd_num, activity)
        if result['good']:
            solar_date = jdn2date(jd_num)
            lunar = convert_solar_to_lunar(solar_date[0], solar_date[1], solar_date[2], 7.0)
            
            good_days.append({
                'jd': jd_num,
                'solar': {
                    'day': solar_date[0],
                    'month': solar_date[1],
                    'year': solar_date[2]
                },
                'lunar': {
                    'day': lunar['day'],
                    'month': lunar['month'],
                    'year': lunar['year']
                },
                'star': result['star'],
                'description': result['description']
            })
    
    return good_days
