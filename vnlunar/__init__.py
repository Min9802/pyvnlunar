"""
vnlunar - Vietnamese Lunar Calendar Library for Python
Thư viện Âm lịch Việt Nam cho Python

Dùng chung dữ liệu và quy ước với thư viện TypeScript @min98/vnlunar
(xem vnlunar-ts/docs/DECISIONS.md).

Author: Converted from TypeScript vnlunar
License: Free for personal and non-commercial use
"""

__version__ = "1.0.5"
__author__ = "vnlunar"

# Try relative imports first, fallback to absolute imports
try:
    from .core import (
        jdn,
        jdn2date,
        get_new_moon_day,
        get_sun_longitude_aa,
        get_lunar_month_11,
        get_leap_month_offset,
        convert_solar_to_lunar,
        convert_lunar_to_solar,
        get_lunar_date,
        get_lunar_date_from_table,
        get_solar_date,
        get_sun_longitude,
        get_year_info,
        get_year_month_lengths,
        get_month
    )
    from .calendar import (
        get_year_can_chi,
        get_hour_can,
        get_can_chi,
        get_can_element,
        get_chi_element,
        get_year_element,
        get_element_relation,
        get_auspicious_hours,
        get_day_of_week
    )
    from .almanac import (
        get_day_can_index,
        get_day_chi_index,
        get_solar_term,
        get_solar_term_index,
        solar_term_index_to_month_chi,
        get_month_chi,
        get_construction_index,
        get_god_index,
        get_12_stars,
        get_12_gods,
        get_12_constructions,
        get_day_type,
        get_hours_can_chi,
        get_four_pillars,
        DEFAULT_TRUC_BASIS,
        DEFAULT_GOD_BASIS,
        DEFAULT_TIME_ZONE
    )
    from .astrology import (
        get_28_mansions,
        get_nayin,
        get_nayin_by_can_chi,
        get_nayin_element,
        get_sexagenary_index,
        check_good_day,
        find_good_days,
        GOOD_CONSTRUCTIONS_FOR_ACTIVITY
    )
    from .direction import (
        get_conflicting_ages,
        check_age_conflict,
        get_direction_info,
        get_god_directions,
        get_age_direction,
        get_travel_direction,
        check_travel_hour
    )
    from .lunar_types import LunarDate
except ImportError:
    from core import (
        jdn,
        jdn2date,
        get_new_moon_day,
        get_sun_longitude_aa,
        get_lunar_month_11,
        get_leap_month_offset,
        convert_solar_to_lunar,
        convert_lunar_to_solar,
        get_lunar_date,
        get_lunar_date_from_table,
        get_solar_date,
        get_sun_longitude,
        get_year_info,
        get_year_month_lengths,
        get_month
    )
    from calendar import (
        get_year_can_chi,
        get_hour_can,
        get_can_chi,
        get_can_element,
        get_chi_element,
        get_year_element,
        get_element_relation,
        get_auspicious_hours,
        get_day_of_week
    )
    from almanac import (
        get_day_can_index,
        get_day_chi_index,
        get_solar_term,
        get_solar_term_index,
        solar_term_index_to_month_chi,
        get_month_chi,
        get_construction_index,
        get_god_index,
        get_12_stars,
        get_12_gods,
        get_12_constructions,
        get_day_type,
        get_hours_can_chi,
        get_four_pillars,
        DEFAULT_TRUC_BASIS,
        DEFAULT_GOD_BASIS,
        DEFAULT_TIME_ZONE
    )
    from astrology import (
        get_28_mansions,
        get_nayin,
        get_nayin_by_can_chi,
        get_nayin_element,
        get_sexagenary_index,
        check_good_day,
        find_good_days,
        GOOD_CONSTRUCTIONS_FOR_ACTIVITY
    )
    from direction import (
        get_conflicting_ages,
        check_age_conflict,
        get_direction_info,
        get_god_directions,
        get_age_direction,
        get_travel_direction,
        check_travel_hour
    )
    from lunar_types import LunarDate


def get_full_info(day: int, month: int, year: int,
                  truc_basis: str = DEFAULT_TRUC_BASIS,
                  god_basis: str = DEFAULT_GOD_BASIS,
                  time_zone: float = DEFAULT_TIME_ZONE) -> dict:
    """
    Get complete information about a date (English keys)
    Lấy toàn bộ thông tin của một ngày dương lịch

    Args:
        day: Solar day
        month: Solar month
        year: Solar year
        truc_basis: Cách tính tháng cho Thập Nhị Trực ("solar_term" mặc định | "lunar")
        god_basis: Cách tính tháng cho 12 Thần ("lunar" mặc định | "solar_term")
        time_zone: Múi giờ cho tiết khí (mặc định 7)

    Returns:
        Dictionary containing all date information with English keys
    """
    lunar = get_lunar_date(day, month, year)
    jd_num = lunar['jd']

    can_day = (jd_num + 9) % 10
    chi_day = (jd_num + 1) % 12
    term = get_solar_term(jd_num, time_zone)

    return {
        'solar': {
            'day': day,
            'month': month,
            'year': year,
            'day_of_week': get_day_of_week(jd_num)
        },
        'lunar': {
            'day': lunar['day'],
            'month': lunar['month'],
            'year': lunar['year'],
            'leap': lunar['leap'],
            'month_name': f"Tháng {lunar['month']} nhuận" if lunar['leap'] == 1 else f"Tháng {lunar['month']}"
        },
        'can_chi': get_can_chi(lunar),
        'year_element': get_year_element(lunar['year']),
        'elements': {
            'day': {
                'can': get_can_element(can_day),
                'chi': get_chi_element(chi_day)
            },
            'year': get_year_element(lunar['year'])
        },
        '12_stars': get_12_stars(jd_num, truc_basis, time_zone),
        '12_constructions': get_12_constructions(jd_num, truc_basis, time_zone),
        '12_gods': get_12_gods(jd_num, god_basis, time_zone),
        '28_mansions': get_28_mansions(jd_num),
        'nayin': get_nayin(jd_num),
        'day_type': get_day_type(jd_num, god_basis, time_zone),
        'conflicting_ages': get_conflicting_ages(jd_num, lunar['year']),
        'god_directions': get_god_directions(jd_num),
        'directions': get_direction_info(jd_num),
        'solar_term': term['name'],
        'solar_term_info': term,
        'auspicious_hours': get_auspicious_hours(jd_num),
        'day_of_week': get_day_of_week(jd_num),
        'options': {
            'truc_basis': truc_basis,
            'god_basis': god_basis,
            'time_zone': time_zone
        },
        'jd': jd_num
    }


__all__ = [
    # Version
    '__version__',
    '__author__',

    # Core functions
    'jdn',
    'jdn2date',
    'get_new_moon_day',
    'get_sun_longitude_aa',
    'get_lunar_month_11',
    'get_leap_month_offset',
    'convert_solar_to_lunar',
    'convert_lunar_to_solar',
    'get_lunar_date',
    'get_lunar_date_from_table',
    'get_solar_date',
    'get_sun_longitude',
    'get_year_info',
    'get_year_month_lengths',
    'get_month',

    # Calendar functions
    'get_year_can_chi',
    'get_hour_can',
    'get_can_chi',
    'get_can_element',
    'get_chi_element',
    'get_year_element',
    'get_element_relation',
    'get_auspicious_hours',
    'get_day_of_week',

    # Almanac functions
    'get_day_can_index',
    'get_day_chi_index',
    'get_solar_term',
    'get_solar_term_index',
    'solar_term_index_to_month_chi',
    'get_month_chi',
    'get_construction_index',
    'get_god_index',
    'get_12_stars',
    'get_12_gods',
    'get_12_constructions',
    'get_day_type',
    'get_hours_can_chi',
    'get_four_pillars',
    'DEFAULT_TRUC_BASIS',
    'DEFAULT_GOD_BASIS',
    'DEFAULT_TIME_ZONE',

    # Astrology functions
    'get_28_mansions',
    'get_nayin',
    'get_nayin_by_can_chi',
    'get_nayin_element',
    'get_sexagenary_index',
    'check_good_day',
    'find_good_days',
    'GOOD_CONSTRUCTIONS_FOR_ACTIVITY',

    # Direction functions
    'get_conflicting_ages',
    'check_age_conflict',
    'get_direction_info',
    'get_god_directions',
    'get_age_direction',
    'get_travel_direction',
    'check_travel_hour',

    # Types
    'LunarDate',

    # Full info
    'get_full_info'
]
