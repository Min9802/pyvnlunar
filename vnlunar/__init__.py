"""
vnlunar - Vietnamese Lunar Calendar Library for Python
Thư viện Âm lịch Việt Nam cho Python

Based on the TypeScript implementation with astronomical algorithms
for accurate lunar calendar conversion according to Vietnamese tradition.

Author: Converted from TypeScript vnlunar
License: Free for personal and non-commercial use
"""

__version__ = "1.0.2"
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
        get_lunar_date,
        get_sun_longitude
    )
except ImportError:
    from core import (
        jdn,
        jdn2date,
        get_new_moon_day,
        get_sun_longitude_aa,
        get_lunar_month_11,
        get_leap_month_offset,
        convert_solar_to_lunar,
        get_lunar_date,
        get_sun_longitude
    )

try:
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
except ImportError:
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

try:
    from .astrology import (
        get_12_stars,
        get_12_gods,
        get_12_constructions,
        get_28_mansions,
        get_nayin,
        get_day_type,
        check_good_day,
        find_good_days
    )
except ImportError:
    from astrology import (
        get_12_stars,
        get_12_gods,
        get_12_constructions,
        get_28_mansions,
        get_nayin,
        get_day_type,
        check_good_day,
        find_good_days
    )

try:
    from .direction import (
        get_conflicting_ages,
        check_age_conflict,
        get_direction_info,
        get_god_directions,
        get_age_direction,
        get_travel_direction,
        check_travel_hour
    )
except ImportError:
    from direction import (
        get_conflicting_ages,
        check_age_conflict,
        get_direction_info,
        get_god_directions,
        get_age_direction,
        get_travel_direction,
        check_travel_hour
    )

try:
    from .lunar_types import LunarDate
except ImportError:
    from lunar_types import LunarDate

def get_full_info(day: int, month: int, year: int) -> dict:
    """
    Get complete information about a date (English keys)
    
    Args:
        day: Solar day
        month: Solar month
        year: Solar year
        
    Returns:
        Dictionary containing all date information with English keys
    """
    lunar = get_lunar_date(day, month, year)
    jd_num = lunar['jd']
    
    can_day = (jd_num + 9) % 10
    chi_day = (jd_num + 1) % 12
    can_month = (lunar['year'] * 12 + lunar['month'] + 3) % 10
    chi_month = (lunar['month'] + 1) % 12
    
    result = {
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
        '12_stars': get_12_stars(lunar['day'], lunar['month']),
        '12_constructions': get_12_constructions(lunar['day'], lunar['month']),
        '12_gods': get_12_gods(jd_num),
        '28_mansions': get_28_mansions(jd_num),
        'nayin': get_nayin(jd_num),
        'day_type': get_day_type(lunar['day'], lunar['month']),
        'conflicting_ages': get_conflicting_ages(jd_num, year),
        'directions': get_direction_info(jd_num),
        'god_directions': get_god_directions(jd_num),
        'auspicious_hours': get_auspicious_hours(jd_num),
        'day_of_week': get_day_of_week(jd_num),
        'jd': jd_num
    }
    
    return result

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
    'get_lunar_date',
    'get_sun_longitude',
    
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
    
    # Astrology functions
    'get_12_stars',
    'get_12_gods',
    'get_12_constructions',
    'get_28_mansions',
    'get_nayin',
    'get_day_type',
    'check_good_day',
    'find_good_days',
    
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
