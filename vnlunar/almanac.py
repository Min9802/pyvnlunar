"""
Almanac functions (Lịch vạn niên): Tiết khí, Thập Nhị Trực, 12 Thần Hoàng/Hắc Đạo, Tứ Trụ.

Quy ước (xem vnlunar-ts/docs/DECISIONS.md):
- Chi tháng theo âm lịch: (tháng âm + 1) % 12 (tháng Giêng = Dần).
- Chi tháng theo tiết khí: tháng Dần bắt đầu từ Lập Xuân, mỗi Tiết lệnh đổi một tháng.
- Trực = (chi ngày - chi tháng) mod 12, 0 = Kiến.
- 12 Thần: Thanh Long khởi tại Tý ở tháng Dần/Thân, Dần ở tháng Mão/Dậu, ... (bước 2 chi).
- Mặc định truc_basis = "solar_term", god_basis = "lunar".
"""

from typing import Dict, List, Optional

try:
    from .constants import CAN, CHI, SOLAR_TERMS, STARS_12, CONSTRUCTIONS_12, GODS_12
    from .core import jdn, jdn2date, get_lunar_date, get_sun_longitude
except ImportError:
    from constants import CAN, CHI, SOLAR_TERMS, STARS_12, CONSTRUCTIONS_12, GODS_12
    from core import jdn, jdn2date, get_lunar_date, get_sun_longitude

LUNAR = "lunar"
SOLAR_TERM = "solar_term"

DEFAULT_TRUC_BASIS = SOLAR_TERM
DEFAULT_GOD_BASIS = LUNAR
DEFAULT_TIME_ZONE = 7.0

# Chỉ số (trong GODS_12) của 6 Thần Hoàng Đạo
HOANG_DAO_GOD_INDEXES = (0, 1, 4, 5, 7, 10)


def _check_basis(basis: str) -> str:
    if basis not in (LUNAR, SOLAR_TERM):
        raise ValueError(f"basis phải là 'lunar' hoặc 'solar_term', nhận {basis!r}")
    return basis


def _assert_jd(jd: int, fn: str) -> None:
    if not isinstance(jd, int) or jd < 100000:
        raise TypeError(
            f"{fn}(jd, ...) nhận Julian Day Number (vd. jdn(8, 11, 2025)). "
            f"Chữ ký cũ {fn}(lunar_day, lunar_month) của v1.x đã bị bỏ vì cho kết quả sai."
        )


def get_day_chi_index(jd: int) -> int:
    """Chi ngày (0 = Tý)"""
    return (jd + 1) % 12


def get_day_can_index(jd: int) -> int:
    """Can ngày (0 = Giáp)"""
    return (jd + 9) % 10


def get_solar_term_index(jd: int, time_zone: float = DEFAULT_TIME_ZONE) -> int:
    """Chỉ số tiết khí tại cuối ngày (0 = Xuân phân ... 23 = Kinh trập)"""
    return get_sun_longitude(jd + 1, time_zone)


def solar_term_index_to_month_chi(term_index: int) -> int:
    """Chi của tháng tiết khí (2 = Dần, bắt đầu từ Lập Xuân)"""
    return (((term_index - 21 + 24) % 24) // 2 + 2) % 12


def get_solar_term(jd: int, time_zone: float = DEFAULT_TIME_ZONE) -> Dict:
    """
    Tiết khí của ngày

    Returns:
        {'index', 'name', 'month_chi'}
    """
    index = get_solar_term_index(jd, time_zone)
    return {
        'index': index,
        'name': SOLAR_TERMS[index],
        'month_chi': solar_term_index_to_month_chi(index)
    }


def get_month_chi(jd: int, basis: str = LUNAR, time_zone: float = DEFAULT_TIME_ZONE) -> int:
    """
    Chi tháng của ngày theo cách tính đã chọn

    Args:
        jd: Julian Day Number
        basis: "lunar" | "solar_term"
        time_zone: Múi giờ cho tiết khí
    """
    if _check_basis(basis) == SOLAR_TERM:
        return solar_term_index_to_month_chi(get_solar_term_index(jd, time_zone))
    dd, mm, yy = jdn2date(jd)
    lunar = get_lunar_date(dd, mm, yy)
    return (lunar['month'] + 1) % 12


def get_construction_index(jd: int, truc_basis: str = DEFAULT_TRUC_BASIS,
                           time_zone: float = DEFAULT_TIME_ZONE) -> int:
    """Chỉ số Trực (0 = Kiến ... 11 = Bế)"""
    month_chi = get_month_chi(jd, truc_basis, time_zone)
    return (get_day_chi_index(jd) - month_chi + 12) % 12


def get_12_constructions(jd: int, truc_basis: str = DEFAULT_TRUC_BASIS,
                         time_zone: float = DEFAULT_TIME_ZONE) -> Dict:
    """Thập Nhị Trực của ngày (chi tiết việc nên/không nên)"""
    _assert_jd(jd, 'get_12_constructions')
    return CONSTRUCTIONS_12[get_construction_index(jd, truc_basis, time_zone)]


def get_12_stars(jd: int, truc_basis: str = DEFAULT_TRUC_BASIS,
                 time_zone: float = DEFAULT_TIME_ZONE) -> Dict:
    """Thập Nhị Trực của ngày (tóm tắt, có trạng thái tốt/xấu)"""
    _assert_jd(jd, 'get_12_stars')
    return STARS_12[get_construction_index(jd, truc_basis, time_zone)]


def get_god_index(jd: int, god_basis: str = DEFAULT_GOD_BASIS,
                  time_zone: float = DEFAULT_TIME_ZONE) -> int:
    """Chỉ số Thần trực nhật (0 = Thanh Long ... 11 = Câu Trần)"""
    month_chi = get_month_chi(jd, god_basis, time_zone)
    start = ((month_chi - 2 + 12) % 6) * 2  # chi nơi Thanh Long khởi
    return (get_day_chi_index(jd) - start + 12) % 12


def get_12_gods(jd: int, god_basis: str = DEFAULT_GOD_BASIS,
                time_zone: float = DEFAULT_TIME_ZONE) -> Dict:
    """12 Thần trực nhật (Hoàng Đạo / Hắc Đạo)"""
    _assert_jd(jd, 'get_12_gods')
    return GODS_12[get_god_index(jd, god_basis, time_zone)]


def get_day_type(jd: int, god_basis: str = DEFAULT_GOD_BASIS,
                 time_zone: float = DEFAULT_TIME_ZONE) -> Dict:
    """Ngày Hoàng Đạo / Hắc Đạo (theo 12 Thần trực nhật)"""
    _assert_jd(jd, 'get_day_type')
    index = get_god_index(jd, god_basis, time_zone)
    god = GODS_12[index]
    is_hoang_dao = index in HOANG_DAO_GOD_INDEXES
    label = f"{god['name']} ({god['alias']})" if god.get('alias') else god['name']
    return {
        'type': "Hoàng Đạo" if is_hoang_dao else "Hắc Đạo",
        'star': god['name'],
        'good': is_hoang_dao,
        'bad': not is_hoang_dao,
        'desc': (f"Ngày Hoàng Đạo ({label}) - Tốt, thuận lợi" if is_hoang_dao
                 else f"Ngày Hắc Đạo ({label}) - Xấu, nên tránh việc lớn")
    }


def _pillar(can_index: int, chi_index: int) -> Dict:
    return {
        'can': CAN[can_index],
        'chi': CHI[chi_index],
        'can_index': can_index,
        'chi_index': chi_index,
        'can_chi': f"{CAN[can_index]} {CHI[chi_index]}"
    }


def get_hours_can_chi(jd: int) -> List[Dict]:
    """Can Chi của 12 giờ trong ngày"""
    day_can = get_day_can_index(jd)
    result = []
    for chi in range(12):
        can = (day_can * 2 + chi) % 10
        start = (chi * 2 + 23) % 24
        end = (chi * 2 + 1) % 24
        item = _pillar(can, chi)
        item['period'] = f"{start}h-{end}h"
        result.append(item)
    return result


def get_four_pillars(dd: int, mm: int, yyyy: int, hour: int = 0, minute: int = 0,
                     time_zone: float = DEFAULT_TIME_ZONE) -> Dict:
    """
    Tứ Trụ (Bát Tự) theo dương lịch.

    - Năm đổi tại Lập Xuân (không phải Tết âm lịch).
    - Tháng theo tiết khí, Can tháng theo Ngũ Hổ Độn.
    - Giờ >= 23 được tính sang ngày hôm sau (giờ Tý đầu ngày mới).
    Độ phân giải theo ngày: ngày giao tiết được tính theo tiết khí tại cuối ngày.
    """
    del minute  # độ phân giải theo giờ
    base_jd = jdn(dd, mm, yyyy)
    day_jd = base_jd + 1 if hour >= 23 else base_jd
    _, s_month, s_year = jdn2date(day_jd)

    term = get_solar_term(day_jd, time_zone)
    month_chi = term['month_chi']

    pillar_year = s_year
    if s_month <= 2 and month_chi in (0, 1):
        pillar_year = s_year - 1
    year_can = (pillar_year + 6) % 10
    year_chi = (pillar_year + 8) % 12

    can_dan = ((year_can % 5) * 2 + 2) % 10
    month_can = (can_dan + (month_chi - 2 + 12) % 12) % 10

    day_can = get_day_can_index(day_jd)
    day_chi = get_day_chi_index(day_jd)

    hour_chi = ((hour + 1) // 2) % 12
    hour_can = (day_can * 2 + hour_chi) % 10

    return {
        'year': _pillar(year_can, year_chi),
        'month': _pillar(month_can, month_chi),
        'day': _pillar(day_can, day_chi),
        'hour': _pillar(hour_can, hour_chi),
        'day_jd': day_jd,
        'solar_term': term['name']
    }
