"""
Calendar functions for Can Chi (Heavenly Stems & Earthly Branches), Five Elements
Các hàm xử lý Can Chi và Ngũ Hành
"""

from typing import Dict

try:
    from .lunar_types import LunarDate, CanChiInfo, ElementInfo, YearElementInfo
    from .constants import (
        CAN, CHI, CHI_ANIMALS, 
        CAN_ELEMENTS, CHI_ELEMENTS, ELEMENT, 
        AUSPICIOUS_HOURS, WEEKDAYS
    )
except ImportError:
    from lunar_types import LunarDate, CanChiInfo, ElementInfo, YearElementInfo
    from constants import (
        CAN, CHI, CHI_ANIMALS, 
        CAN_ELEMENTS, CHI_ELEMENTS, ELEMENT, 
        AUSPICIOUS_HOURS, WEEKDAYS
    )


def get_year_can_chi(year: int) -> str:
    """
    Get year Can Chi (Heavenly Stem & Earthly Branch)
    Lấy Can Chi của năm
    
    Args:
        year: Year / Năm
        
    Returns:
        Can Chi string
    """
    return CAN[(year + 6) % 10] + " " + CHI[(year + 8) % 12]


def get_hour_can(jdn: int) -> str:
    """
    Get Can (Heavenly Stem) of hour Tý (00:00) of the day
    Lấy Can của giờ Tý (00:00) trong ngày
    
    Args:
        jdn: Julian Day Number
        
    Returns:
        Can string
    """
    return CAN[(jdn - 1) * 2 % 10]


def get_can_chi(lunar: LunarDate) -> CanChiInfo:
    """
    Get full Can Chi of day, month, year, hour
    Lấy Can Chi đầy đủ của ngày, tháng, năm, giờ
    
    Args:
        lunar: LunarDate dictionary
        
    Returns:
        CanChiInfo dictionary with 'day', 'month', 'year', 'hour' keys
    """
    day_canchi = CAN[(lunar['jd'] + 9) % 10] + " " + CHI[(lunar['jd'] + 1) % 12]
    month_canchi = CAN[(lunar['year'] * 12 + lunar['month'] + 3) % 10] + " " + CHI[(lunar['month'] + 1) % 12]
    
    if lunar['leap'] == 1:
        month_canchi += " (nhuận)"
    
    year_canchi = get_year_can_chi(lunar['year'])
    hour_0_can = get_hour_can(lunar['jd'])
    
    return {
        'day': day_canchi,
        'month': month_canchi,
        'year': year_canchi,
        'hour': hour_0_can + " " + CHI[0]  # Giờ Tý (hour 0)
    }


def get_can_element(can_index: int) -> str:
    """
    Get Five Element of Can (Heavenly Stem)
    Lấy Ngũ Hành của Can
    
    Args:
        can_index: Can index (0-9)
        
    Returns:
        Five Element name
    """
    return CAN_ELEMENTS[can_index % 10]


def get_chi_element(chi_index: int) -> str:
    """
    Get Five Element of Chi (Earthly Branch)
    Lấy Ngũ Hành của Chi
    
    Args:
        chi_index: Chi index (0-11)
        
    Returns:
        Five Element name
    """
    return CHI_ELEMENTS[chi_index % 12]


def get_year_element(year: int) -> YearElementInfo:
    """
    Get Five Element information of year
    Lấy thông tin Ngũ Hành của năm
    
    Args:
        year: Year / Năm
        
    Returns:
        YearElementInfo dictionary
    """
    can_index = (year + 6) % 10
    chi_index = (year + 8) % 12
    
    can_chi_text = CAN[can_index] + " " + CHI[chi_index]
    element_name = CAN_ELEMENTS[can_index]
    
    return {
        'can': CAN[can_index],
        'chi': CHI[chi_index],
        'animal': CHI_ANIMALS[chi_index],
        'can_chi': can_chi_text,
        'name': element_name,
        'element': element_name,
        'can_element': CAN_ELEMENTS[can_index],
        'chi_element': CHI_ELEMENTS[chi_index]
    }


def get_element_relation(element1: str, element2: str) -> str:
    """
    Get relationship between two Five Elements
    Lấy quan hệ giữa hai Ngũ Hành
    
    Args:
        element1: First element
        element2: Second element
        
    Returns:
        Relationship description
    """
    if element1 == element2:
        return "Đồng"
    
    # Sinh cycle: Thủy → Mộc → Hỏa → Thổ → Kim → Thủy
    sinh_map = {
        "Thủy": "Mộc",
        "Mộc": "Hỏa",
        "Hỏa": "Thổ",
        "Thổ": "Kim",
        "Kim": "Thủy"
    }
    
    # Khắc cycle: Thủy → Hỏa → Kim → Mộc → Thổ → Thủy
    khac_map = {
        "Thủy": "Hỏa",
        "Hỏa": "Kim",
        "Kim": "Mộc",
        "Mộc": "Thổ",
        "Thổ": "Thủy"
    }
    
    if sinh_map.get(element1) == element2:
        return "Sinh"
    elif sinh_map.get(element2) == element1:
        return "Bị sinh"
    elif khac_map.get(element1) == element2:
        return "Khắc"
    elif khac_map.get(element2) == element1:
        return "Bị khắc"
    else:
        return "Không liên quan"


def get_auspicious_hours(jd: int) -> str:
    """
    Get auspicious hours (Giờ Hoàng Đạo) of the day
    Lấy các giờ Hoàng Đạo trong ngày
    
    Args:
        jd: Julian Day Number
        
    Returns:
        String of auspicious hours
    """
    chi_index = (jd + 1) % 12
    auspicious_str = AUSPICIOUS_HOURS[chi_index]
    
    result = []
    time_ranges = [
        "23-1h", "1-3h", "3-5h", "5-7h", "7-9h", "9-11h",
        "11-13h", "13-15h", "15-17h", "17-19h", "19-21h", "21-23h"
    ]
    
    for i, chi in enumerate(CHI):
        if auspicious_str[i] == '1':
            result.append(f"{chi} ({time_ranges[i]})")
    
    return ", ".join(result)


def get_day_of_week(jd: int) -> str:
    """
    Get day of week in Vietnamese
    Lấy thứ trong tuần
    
    Args:
        jd: Julian Day Number
        
    Returns:
        Day of week string
    """
    return WEEKDAYS[(jd + 1) % 7]
