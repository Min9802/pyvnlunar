"""
Astrology functions: 28 Mansions, Nayin, good-day selection.
Các hàm chiêm tinh: 28 Tú, Nạp Âm, xem ngày tốt.

Trực / 12 Thần / Hoàng-Hắc Đạo nằm trong almanac.py và được re-export ở đây để tương thích.
"""

from typing import Dict, List

try:
    from .lunar_types import Mansion28Info, NayinInfo, DaySelectionResult
    from .constants import MANSIONS_28, NAYIN_60, CAN, CHI, STARS_12, GODS_12
    from .core import jdn2date, get_lunar_date
    from .almanac import (
        get_12_stars, get_12_gods, get_12_constructions, get_day_type,
        get_construction_index, get_god_index, HOANG_DAO_GOD_INDEXES,
        DEFAULT_TRUC_BASIS, DEFAULT_GOD_BASIS, DEFAULT_TIME_ZONE
    )
except ImportError:
    from lunar_types import Mansion28Info, NayinInfo, DaySelectionResult
    from constants import MANSIONS_28, NAYIN_60, CAN, CHI, STARS_12, GODS_12
    from core import jdn2date, get_lunar_date
    from almanac import (
        get_12_stars, get_12_gods, get_12_constructions, get_day_type,
        get_construction_index, get_god_index, HOANG_DAO_GOD_INDEXES,
        DEFAULT_TRUC_BASIS, DEFAULT_GOD_BASIS, DEFAULT_TIME_ZONE
    )

__all__ = [
    'get_12_stars', 'get_12_gods', 'get_12_constructions', 'get_day_type',
    'get_28_mansions', 'get_sexagenary_index', 'get_nayin_element',
    'get_nayin_by_can_chi', 'get_nayin', 'check_good_day', 'find_good_days',
    'GOOD_CONSTRUCTIONS_FOR_ACTIVITY'
]


def get_28_mansions(jd: int) -> Mansion28Info:
    """
    Get 28 Lunar Mansion (Nhị Thập Bát Tú)

    Args:
        jd: Julian Day Number

    Returns:
        Mansion information / Thông tin tú sao
    """
    return MANSIONS_28[(jd + 11) % 28]


def get_sexagenary_index(can_index: int, chi_index: int) -> int:
    """Chỉ số Lục Thập Hoa Giáp (0 = Giáp Tý ... 59 = Quý Hợi) từ chỉ số Can và Chi"""
    return (6 * can_index - 5 * chi_index) % 60


def get_nayin_element(nayin_name: str) -> str:
    """Lấy hành từ tên Nạp Âm"""
    for element in ("Kim", "Mộc", "Thủy", "Hỏa", "Thổ"):
        if element in nayin_name:
            return element
    if "Hoả" in nayin_name:
        return "Hỏa"
    return ""


def get_nayin_by_can_chi(can_index: int, chi_index: int) -> NayinInfo:
    """Nạp Âm theo chỉ số Can, Chi"""
    name = NAYIN_60[get_sexagenary_index(can_index, chi_index)]
    return {
        'name': name,
        'element': get_nayin_element(name),
        'can': CAN[can_index],
        'chi': CHI[chi_index]
    }


def get_nayin(jd: int) -> NayinInfo:
    """
    Get Nayin (Nạp Âm) of the day
    Lấy Nạp Âm của ngày

    Args:
        jd: Julian Day Number

    Returns:
        Nayin information / Thông tin Nạp Âm
    """
    return get_nayin_by_can_chi((jd + 9) % 10, (jd + 1) % 12)


# Trực phù hợp cho từng loại việc
GOOD_CONSTRUCTIONS_FOR_ACTIVITY = {
    "wedding": ["Định", "Thành", "Khai"],
    "construction": ["Định", "Thành", "Khai"],
    "travel": ["Kiến", "Mãn", "Thành", "Khai"],
    "opening": ["Mãn", "Định", "Thành", "Khai"],
    "moving": ["Định", "Thành", "Khai"],
    "investment": ["Mãn", "Thành", "Thu", "Khai"],
}

_ACTIVITY_NAMES = {
    "wedding": "cưới hỏi",
    "construction": "xây nhà",
    "travel": "xuất hành",
    "opening": "khai trương",
    "moving": "chuyển nhà",
    "investment": "đầu tư",
}


def check_good_day(jd: int, activity: str, truc_basis: str = DEFAULT_TRUC_BASIS,
                   god_basis: str = DEFAULT_GOD_BASIS,
                   time_zone: float = DEFAULT_TIME_ZONE) -> DaySelectionResult:
    """
    Check if day is good for specific activity
    Kiểm tra ngày tốt cho việc cụ thể.

    Ngày tốt = ngày Hoàng Đạo (12 Thần) VÀ Trực nằm trong danh sách hợp với việc.

    Args:
        jd: Julian Day Number
        activity: "wedding", "construction", "travel", "opening", "moving", "investment"
        truc_basis: Cách tính tháng cho Trực ("solar_term" mặc định | "lunar")
        god_basis: Cách tính tháng cho 12 Thần ("lunar" mặc định | "solar_term")

    Returns:
        Day selection result / Kết quả xem ngày
    """
    star = STARS_12[get_construction_index(jd, truc_basis, time_zone)]
    god_index = get_god_index(jd, god_basis, time_zone)
    god = GODS_12[god_index]
    is_hoang_dao = god_index in HOANG_DAO_GOD_INDEXES

    good_list = GOOD_CONSTRUCTIONS_FOR_ACTIVITY.get(activity, [])
    is_good = is_hoang_dao and star['name'] in good_list
    activity_name = _ACTIVITY_NAMES.get(activity, activity)
    day_label = f"Ngày Trực {star['name']}, {god['name']} ({'Hoàng Đạo' if is_hoang_dao else 'Hắc Đạo'})"

    return {
        'star': star,
        'god': god,
        'activity': activity_name,
        'good': is_good,
        'description': (f"{day_label} - TỐT cho {activity_name}" if is_good
                        else f"{day_label} - KHÔNG TỐT cho {activity_name}")
    }


def find_good_days(start_jd: int, end_jd: int, activity: str,
                   truc_basis: str = DEFAULT_TRUC_BASIS,
                   god_basis: str = DEFAULT_GOD_BASIS,
                   time_zone: float = DEFAULT_TIME_ZONE) -> List[Dict]:
    """
    Find good days for specific activity in date range
    Tìm các ngày tốt cho việc cụ thể trong khoảng thời gian

    Args:
        start_jd: Start Julian Day Number / JDN bắt đầu
        end_jd: End Julian Day Number (bao gồm) / JDN kết thúc
        activity: Activity type / Loại việc

    Returns:
        List of good days / Danh sách các ngày tốt
    """
    good_days = []
    for jd_num in range(start_jd, end_jd + 1):
        result = check_good_day(jd_num, activity, truc_basis, god_basis, time_zone)
        if result['good']:
            solar_date = jdn2date(jd_num)
            lunar = get_lunar_date(solar_date[0], solar_date[1], solar_date[2])
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
                    'year': lunar['year'],
                    'leap': lunar['leap']
                },
                'star': result['star'],
                'god': result['god'],
                'description': result['description']
            })
    return good_days
