"""
Direction functions: Travel directions, Age conflicts
Các hàm xử lý hướng xuất hành và tuổi xung
"""

from typing import Dict, List

try:
    from .lunar_types import (
        ConflictingAgeInfo, DirectionInfo, GodDirectionInfo, HourInfo
    )
    from .constants import (
        CHI, CHI_ANIMALS, CAN, DIRECTION_MAP,
        WEALTH_GOD_DIR, JOY_GOD_DIR, FORTUNE_GOD_DIR
    )
    from .astrology import get_nayin_by_can_chi
    from .calendar import get_element_relation
except ImportError:
    from lunar_types import (
        ConflictingAgeInfo, DirectionInfo, GodDirectionInfo, HourInfo
    )
    from constants import (
        CHI, CHI_ANIMALS, CAN, DIRECTION_MAP,
        WEALTH_GOD_DIR, JOY_GOD_DIR, FORTUNE_GOD_DIR
    )
    from astrology import get_nayin_by_can_chi
    from calendar import get_element_relation


def get_conflicting_ages(jd: int, current_year: int) -> ConflictingAgeInfo:
    """
    Get age conflict information (Tuổi Xung ngày)
    Lấy thông tin tuổi xung

    Quy tắc (khớp các lịch vạn niên đối chiếu, mới khớp một phần - xem docs/tuoi-xung.md):
    (A) Tuổi xung chính (*): Chi lục xung với chi ngày VÀ Nạp Âm khắc / bị khắc Nạp Âm ngày.
    (B) Tuổi xung phụ: cùng chi ngày, Can bị Can ngày khắc (Can ngày + 4) VÀ Nạp Âm khắc / bị khắc.
    
    Args:
        jd: Julian Day Number
        current_year: Năm dùng để tính tuổi (nên truyền năm âm lịch)
        
    Returns:
        ConflictingAgeInfo dictionary
    """
    day_can = (jd + 9) % 10
    day_chi = (jd + 1) % 12
    conflict_chi_index = (day_chi + 6) % 12
    day_nayin = get_nayin_by_can_chi(day_can, day_chi)

    def is_khac(can_index: int, chi_index: int) -> bool:
        other = get_nayin_by_can_chi(can_index, chi_index)['element']
        rel = get_element_relation(day_nayin['element'], other).lower()
        return rel in ("khắc", "bị khắc")

    candidates = []
    # (A) Chi xung + Nạp Âm khắc
    for can in range(conflict_chi_index % 2, 10, 2):
        if is_khac(can, conflict_chi_index):
            candidates.append((can, conflict_chi_index, True, "Địa chi xung, Nạp Âm khắc"))
    # (B) Cùng chi, Can bị khắc + Nạp Âm khắc
    can_bi_khac = (day_can + 4) % 10
    if is_khac(can_bi_khac, day_chi):
        candidates.append((can_bi_khac, day_chi, False, "Cùng chi, Thiên can khắc, Nạp Âm khắc"))

    conflicting_age_list = []
    for can, chi, primary, reason in candidates:
        year = current_year - 1
        while (year + 6) % 10 != can or (year + 8) % 12 != chi:
            year -= 1
        can_chi = f"{CAN[can]} {CHI[chi]}"
        conflicting_age_list.append({
            'year': year,
            'can_chi': can_chi + ("*" if primary else ""),
            'age': current_year - year,
            'chi': CHI[chi],
            'animal': CHI_ANIMALS[chi],
            'primary': primary,
            'reason': reason
        })

    names = ", ".join(a['can_chi'].replace("*", "") for a in conflicting_age_list)
    return {
        'day_chi': CHI[day_chi],
        'day_animal': CHI_ANIMALS[day_chi],
        'conflict_chi': CHI[conflict_chi_index],
        'conflict_animal': CHI_ANIMALS[conflict_chi_index],
        'description': f"Ngày {CAN[day_can]} {CHI[day_chi]} ({day_nayin['name']}) xung với tuổi: {names}",
        'conflicting_ages': conflicting_age_list,
        'note': f"Người tuổi {CHI_ANIMALS[conflict_chi_index]} nên cẩn thận trong ngày này"
    }


def check_age_conflict(jd: int, birth_year: int) -> bool:
    """
    Check if birth year conflicts with day
    Kiểm tra tuổi có xung với ngày không
    
    Args:
        jd: Julian Day Number
        birth_year: Birth year / Năm sinh
        
    Returns:
        True if conflicts / True nếu xung
    """
    day_chi = (jd + 1) % 12
    birth_year_chi = (birth_year + 8) % 12
    
    # Check if they are opposite (6 positions away)
    return (day_chi + 6) % 12 == birth_year_chi


def get_direction_info(jd: int) -> DirectionInfo:
    """
    Get direction information according to Ngoc Hap Thong Thu
    Lấy thông tin hướng theo Ngọc Hạp Thông Thư

    THỰC NGHIỆM: bảng hướng theo chi ngày chưa có nguồn đối chiếu, không còn đưa vào get_full_info.
    
    Args:
        jd: Julian Day Number
        
    Returns:
        DirectionInfo dictionary
    """
    day_chi_index = (jd + 1) % 12
    day_chi = CHI[day_chi_index]
    
    directions = DIRECTION_MAP[day_chi]
    good_directions = directions['good']
    bad_directions = directions['bad']
    
    description = f"Ngày {day_chi}: Hướng tốt để xuất hành"
    good_text = ", ".join(good_directions)
    bad_text = ", ".join(bad_directions)
    
    return {
        'day_chi': day_chi,
        'chi': day_chi,  # Alias
        'good': good_directions,
        'bad': bad_directions,
        'description': description,
        'good_text': good_text,
        'bad_text': bad_text
    }


def get_god_directions(jd: int) -> GodDirectionInfo:
    """
    Get gods direction by day
    Lấy hướng thần theo ngày (Hỷ Thần, Tài Thần đã đối chiếu; Phúc Thần chưa đối chiếu)
    
    Args:
        jd: Julian Day Number
        
    Returns:
        GodDirectionInfo dictionary
    """
    day_can_index = (jd + 9) % 10
    day_can = CAN[day_can_index]
    
    joy_god = JOY_GOD_DIR[day_can_index]  # Joy God
    wealth_god = WEALTH_GOD_DIR[day_can_index]  # Wealth God
    fortune_god = FORTUNE_GOD_DIR[day_can_index]  # Fortune God
    
    description = f"Ngày {day_can}: Hướng các thần tài lộc"
    
    return {
        'day_can': day_can,
        'can': day_can,  # Alias
        'joy_god': joy_god,
        'wealth_god': wealth_god,
        'fortune_god': fortune_god,
        'description': description
    }


def get_age_direction(birth_year: int, current_year: int) -> Dict:
    """
    Get travel direction by age
    Lấy hướng xuất hành theo tuổi (THỰC NGHIỆM - chưa có nguồn đối chiếu)
    
    Args:
        birth_year: Birth year / Năm sinh
        current_year: Current year / Năm hiện tại
        
    Returns:
        Direction information dictionary
    """
    age = current_year - birth_year + 1
    age_chi_index = (birth_year + 8) % 12
    age_chi = CHI[age_chi_index]
    
    # Simplified direction calculation based on zodiac
    # Directions that are good: same direction + compatible directions
    # Directions to avoid: opposite direction + conflicting directions
    
    all_directions = ["Bắc", "Đông Bắc", "Đông", "Đông Nam", "Nam", "Tây Nam", "Tây", "Tây Bắc"]
    
    # Zodiac direction mapping (simplified)
    chi_directions = {
        "Tý": {"good": ["Bắc", "Đông", "Đông Nam"], "bad": ["Nam", "Tây Nam"]},
        "Sửu": {"good": ["Đông Bắc", "Đông", "Bắc"], "bad": ["Tây Nam", "Nam"]},
        "Dần": {"good": ["Đông", "Đông Bắc", "Nam"], "bad": ["Tây", "Tây Nam"]},
        "Mão": {"good": ["Đông", "Đông Nam", "Bắc"], "bad": ["Tây", "Tây Bắc"]},
        "Thìn": {"good": ["Đông Nam", "Đông", "Nam"], "bad": ["Tây Bắc", "Tây"]},
        "Tỵ": {"good": ["Nam", "Đông Nam", "Đông"], "bad": ["Bắc", "Tây Bắc"]},
        "Ngọ": {"good": ["Nam", "Đông", "Tây"], "bad": ["Bắc", "Đông Bắc"]},
        "Mùi": {"good": ["Tây Nam", "Nam", "Đông"], "bad": ["Đông Bắc", "Bắc"]},
        "Thân": {"good": ["Tây", "Tây Nam", "Bắc"], "bad": ["Đông", "Đông Nam"]},
        "Dậu": {"good": ["Tây", "Tây Bắc", "Nam"], "bad": ["Đông", "Đông Bắc"]},
        "Tuất": {"good": ["Tây Bắc", "Tây", "Bắc"], "bad": ["Đông Nam", "Đông"]},
        "Hợi": {"good": ["Bắc", "Tây Bắc", "Đông"], "bad": ["Nam", "Đông Nam"]}
    }
    
    directions = chi_directions.get(age_chi, {"good": [], "bad": []})
    
    return {
        'age': f"{age} tuổi",
        'chi': age_chi,
        'animal': CHI_ANIMALS[age_chi_index],
        'birth_year': birth_year,
        'good': directions['good'],
        'bad': directions['bad'],
        'good_text': ", ".join(directions['good']),
        'bad_text': ", ".join(directions['bad'])
    }


def get_travel_direction(jd: int, birth_year: int, current_year: int) -> Dict:
    """
    Get combined travel direction information
    Lấy thông tin hướng xuất hành tổng hợp
    
    Args:
        jd: Julian Day Number
        birth_year: Birth year / Năm sinh
        current_year: Current year / Năm hiện tại
        
    Returns:
        Combined direction information
    """
    by_day = get_direction_info(jd)
    by_age = get_age_direction(birth_year, current_year)
    
    # Find common good directions
    common_good = list(set(by_day['good']) & set(by_age['good']))
    
    # Find directions to avoid (in either bad list)
    should_avoid = list(set(by_day['bad']) | set(by_age['bad']))
    
    advice = ""
    if common_good:
        advice = f"Nên đi hướng: {', '.join(common_good)}"
    else:
        advice = "Hãy cân nhắc kỹ trước khi xuất hành"
    
    return {
        'by_day': by_day,
        'by_age': by_age,
        'common_good': common_good,
        'should_avoid': should_avoid,
        'common_good_text': ", ".join(common_good) if common_good else "Không có",
        'should_avoid_text': ", ".join(should_avoid),
        'advice': advice
    }


def check_travel_hour(jd: int, hour_chi: str) -> HourInfo:
    """
    Check if hour is auspicious for travel
    Kiểm tra giờ có tốt cho xuất hành không
    
    Args:
        jd: Julian Day Number
        hour_chi: Hour chi name / Tên chi của giờ
        
    Returns:
        HourInfo dictionary
    """
    # Get hour index
    chi_index = -1
    for i, chi in enumerate(CHI):
        if chi == hour_chi:
            chi_index = i
            break
    
    if chi_index == -1:
        return {
            'chi': hour_chi,
            'index': -1,
            'period': "Không xác định",
            'good': False
        }
    
    # Calculate time range
    start_hour = (chi_index * 2 + 23) % 24
    end_hour = (chi_index * 2 + 1) % 24
    period = f"{start_hour:02d}:00 - {end_hour:02d}:00"
    
    # Check from calendar
    from .calendar import get_auspicious_hours
    auspicious_hours_str = get_auspicious_hours(jd)
    
    is_good = hour_chi in auspicious_hours_str
    
    return {
        'chi': hour_chi,
        'index': chi_index,
        'period': period,
        'good': is_good
    }
