"""
Core functions for Vietnamese Lunar Calendar
Astronomical algorithms for lunar calendar conversion
Thuật toán thiên văn cho chuyển đổi lịch âm Việt Nam
"""

import math
from typing import Tuple, List

try:
    from .constants import TK19, TK20, TK21, TK22, PI
    from .lunar_types import LunarDate
except ImportError:
    from constants import TK19, TK20, TK21, TK22, PI
    from lunar_types import LunarDate


def INT(d: float) -> int:
    """Integer part of a number / Phần nguyên của số"""
    return math.floor(d)


def jdn(dd: int, mm: int, yy: int) -> int:
    """
    Convert solar date to Julian Day Number
    Chuyển đổi ngày dương lịch sang Julian Day Number
    
    Args:
        dd: Day / Ngày
        mm: Month / Tháng
        yy: Year / Năm
        
    Returns:
        Julian Day Number
    """
    a = INT((14 - mm) / 12)
    y = yy + 4800 - a
    m = mm + 12 * a - 3
    jd = dd + INT((153 * m + 2) / 5) + 365 * y + INT(y / 4) - INT(y / 100) + INT(y / 400) - 32045
    return jd


def jdn2date(jd: int) -> Tuple[int, int, int]:
    """
    Convert Julian Day Number to solar date
    Chuyển đổi Julian Day Number sang ngày dương lịch
    
    Args:
        jd: Julian Day Number
        
    Returns:
        Tuple of (day, month, year)
    """
    Z = jd
    if Z < 2299161:
        A = Z
    else:
        alpha = INT((Z - 1867216.25) / 36524.25)
        A = Z + 1 + alpha - INT(alpha / 4)
    
    B = A + 1524
    C = INT((B - 122.1) / 365.25)
    D = INT(365.25 * C)
    E = INT((B - D) / 30.6001)
    dd = INT(B - D - INT(30.6001 * E))
    
    if E < 14:
        mm = E - 1
    else:
        mm = E - 13
    
    if mm < 3:
        yyyy = C - 4715
    else:
        yyyy = C - 4716
    
    return (dd, mm, yyyy)


def get_new_moon_day(k: float, time_zone: float) -> int:
    """
    Calculate new moon day (Sóc)
    Using astronomical algorithm
    Tính ngày sóc (trăng non) bằng thuật toán thiên văn
    
    Args:
        k: Moon phase number (k=0 at 1/1/1900)
        time_zone: Time zone (Vietnam = 7.0)
        
    Returns:
        Julian Day Number of new moon
    """
    T = k / 1236.85
    T2 = T * T
    T3 = T2 * T
    dr = PI / 180
    
    Jd1 = 2415020.75933 + 29.53058868 * k + 0.0001178 * T2 - 0.000000155 * T3
    Jd1 = Jd1 + 0.00033 * math.sin((166.56 + 132.87 * T - 0.009173 * T2) * dr)
    
    M = 359.2242 + 29.10535608 * k - 0.0000333 * T2 - 0.00000347 * T3
    Mpr = 306.0253 + 385.81691806 * k + 0.0107306 * T2 + 0.00001236 * T3
    F = 21.2964 + 390.67050646 * k - 0.0016528 * T2 - 0.00000239 * T3
    
    C1 = (0.1734 - 0.000393 * T) * math.sin(M * dr) + 0.0021 * math.sin(2 * dr * M)
    C1 = C1 - 0.4068 * math.sin(Mpr * dr) + 0.0161 * math.sin(dr * 2 * Mpr)
    C1 = C1 - 0.0004 * math.sin(dr * 3 * Mpr)
    C1 = C1 + 0.0104 * math.sin(dr * 2 * F) - 0.0051 * math.sin(dr * (M + Mpr))
    C1 = C1 - 0.0074 * math.sin(dr * (M - Mpr)) + 0.0004 * math.sin(dr * (2 * F + M))
    C1 = C1 - 0.0004 * math.sin(dr * (2 * F - M)) - 0.0006 * math.sin(dr * (2 * F + Mpr))
    C1 = C1 + 0.0010 * math.sin(dr * (2 * F - Mpr)) + 0.0005 * math.sin(dr * (2 * Mpr + M))
    
    if T < -11:
        deltat = 0.001 + 0.000839 * T + 0.0002261 * T2 - 0.00000845 * T3 - 0.000000081 * T * T3
    else:
        deltat = -0.000278 + 0.000265 * T + 0.000262 * T2
    
    JdNew = Jd1 + C1 - deltat
    return INT(JdNew + 0.5 + time_zone / 24)


def get_sun_longitude_aa(jdn: int, time_zone: float) -> int:
    """
    Calculate sun longitude for solar terms
    Tính kinh độ mặt trời cho tiết khí
    
    Args:
        jdn: Julian Day Number
        time_zone: Time zone (Vietnam = 7.0)
        
    Returns:
        Sector number (0-11) for 12 major solar terms
    """
    T = (jdn - 2451545.5 - time_zone / 24) / 36525
    T2 = T * T
    dr = PI / 180
    
    M = 357.52910 + 35999.05030 * T - 0.0001559 * T2 - 0.00000048 * T * T2
    L0 = 280.46645 + 36000.76983 * T + 0.0003032 * T2
    
    DL = (1.914600 - 0.004817 * T - 0.000014 * T2) * math.sin(dr * M)
    DL = DL + (0.019993 - 0.000101 * T) * math.sin(dr * 2 * M) + 0.000290 * math.sin(dr * 3 * M)
    
    L = L0 + DL
    L = L * dr
    L = L - PI * 2 * INT(L / (PI * 2))
    
    return INT(L / PI * 6)


def get_lunar_month_11(yy: int, time_zone: float) -> int:
    """
    Find lunar month 11 (containing Winter Solstice)
    Tìm tháng 11 âm lịch (có Đông chí)
    
    Args:
        yy: Solar year
        time_zone: Time zone (Vietnam = 7.0)
        
    Returns:
        Julian Day Number of first day of lunar month 11
    """
    off = jdn(31, 12, yy) - 2415021
    k = INT(off / 29.530588853)
    nm = get_new_moon_day(k, time_zone)
    sun_long = get_sun_longitude_aa(nm, time_zone)
    
    if sun_long >= 9:
        nm = get_new_moon_day(k - 1, time_zone)
    
    return nm


def get_leap_month_offset(a11: int, time_zone: float) -> int:
    """
    Determine leap month position after lunar month 11
    Xác định vị trí tháng nhuận sau tháng 11 âm lịch
    
    Args:
        a11: JDN of lunar month 11
        time_zone: Time zone (Vietnam = 7.0)
        
    Returns:
        Leap month position (1-12), 0 if no leap month
    """
    k = INT((a11 - 2415021.076998695) / 29.530588853 + 0.5)
    last = 0
    i = 1
    arc = get_sun_longitude_aa(get_new_moon_day(k + i, time_zone), time_zone)
    
    while arc != last and i < 14:
        last = arc
        i += 1
        arc = get_sun_longitude_aa(get_new_moon_day(k + i, time_zone), time_zone)
    
    return i - 1


def convert_solar_to_lunar(dd: int, mm: int, yy: int, time_zone: float) -> LunarDate:
    """
    Convert solar date to lunar date
    Using astronomical algorithm according to Vietnamese tradition
    Chuyển đổi ngày dương lịch sang âm lịch
    
    Args:
        dd: Day
        mm: Month
        yy: Year
        time_zone: Time zone (Vietnam = 7.0)
        
    Returns:
        LunarDate dictionary
    """
    day_number = jdn(dd, mm, yy)
    k = INT((day_number - 2415021.076998695) / 29.530588853)
    month_start = get_new_moon_day(k + 1, time_zone)
    
    if month_start > day_number:
        month_start = get_new_moon_day(k, time_zone)
    
    a11 = get_lunar_month_11(yy, time_zone)
    b11 = a11
    
    if a11 >= month_start:
        lunar_year = yy
        a11 = get_lunar_month_11(yy - 1, time_zone)
    else:
        lunar_year = yy + 1
        b11 = get_lunar_month_11(yy + 1, time_zone)
    
    lunar_day = day_number - month_start + 1
    diff = INT((month_start - a11) / 29)
    lunar_leap = 0
    lunar_month = diff + 11
    
    if b11 - a11 > 365:
        leap_month_diff = get_leap_month_offset(a11, time_zone)
        if diff >= leap_month_diff:
            lunar_month = diff + 10
            if diff == leap_month_diff:
                lunar_leap = 1
    
    if lunar_month > 12:
        lunar_month = lunar_month - 12
    
    if lunar_month >= 11 and diff < 4:
        lunar_year -= 1
    
    return {
        'day': lunar_day,
        'month': lunar_month,
        'year': lunar_year,
        'leap': lunar_leap,
        'jd': day_number
    }


def get_lunar_date(dd: int, mm: int, yyyy: int) -> LunarDate:
    """
    Get lunar date from solar date
    Main conversion function for Vietnam timezone
    Lấy ngày âm lịch từ ngày dương lịch (múi giờ Việt Nam)
    
    Args:
        dd: Day
        mm: Month
        yyyy: Year
        
    Returns:
        LunarDate dictionary
    """
    time_zone = 7.0  # Vietnam timezone
    return convert_solar_to_lunar(dd, mm, yyyy, time_zone)


def sun_longitude(jdn: int) -> float:
    """
    Calculate sun longitude for solar terms (alternative method)
    Tính kinh độ mặt trời (phương pháp thay thế)
    
    Args:
        jdn: Julian Day Number
        
    Returns:
        Sun longitude in radians
    """
    T = (jdn - 2451545.0) / 36525
    T2 = T * T
    dr = PI / 180
    
    M = 357.52910 + 35999.05030 * T - 0.0001559 * T2 - 0.00000048 * T * T2
    L0 = 280.46645 + 36000.76983 * T + 0.0003032 * T2
    
    DL = (1.914600 - 0.004817 * T - 0.000014 * T2) * math.sin(dr * M)
    DL = DL + (0.019993 - 0.000101 * T) * math.sin(dr * 2 * M) + 0.000290 * math.sin(dr * 3 * M)
    
    L = L0 + DL
    L = L * dr
    L = L - PI * 2 * INT(L / (PI * 2))
    
    return L


def get_sun_longitude(day_number: int, time_zone: float) -> int:
    """
    Get sun longitude sector
    Lấy sector kinh độ mặt trời
    
    Args:
        day_number: Julian Day Number
        time_zone: Time zone
        
    Returns:
        Sector number (0-23) for 24 solar terms
    """
    return INT(sun_longitude(day_number - 0.5 - time_zone / 24.0) / PI * 12)


def decode_lunar_year(yy: int, k: int) -> List[LunarDate]:
    """
    Decode lunar year data (fallback method)
    Giải mã dữ liệu năm âm lịch (phương pháp dự phòng)
    
    Args:
        yy: Year
        k: Year code
        
    Returns:
        List of LunarDate for first day of each month
    """
    month_lengths = [29, 30]
    regular_months = []
    offset_of_tet = k >> 17
    leap_month = k & 0xf
    leap_month_length = month_lengths[k >> 16 & 0x1]
    solar_ny = jdn(1, 1, yy)
    current_jd = solar_ny + offset_of_tet
    j = k >> 4
    
    for i in range(12):
        regular_months.insert(0, month_lengths[j & 0x1])
        j >>= 1
    
    ly = []
    if leap_month == 0:
        for mm in range(1, 13):
            ly.append({
                'day': 1,
                'month': mm,
                'year': yy,
                'leap': 0,
                'jd': current_jd
            })
            current_jd += regular_months[mm - 1]
    else:
        for mm in range(1, leap_month + 1):
            ly.append({
                'day': 1,
                'month': mm,
                'year': yy,
                'leap': 0,
                'jd': current_jd
            })
            current_jd += regular_months[mm - 1]
        
        ly.append({
            'day': 1,
            'month': leap_month,
            'year': yy,
            'leap': 1,
            'jd': current_jd
        })
        current_jd += leap_month_length
        
        for mm in range(leap_month + 1, 13):
            ly.append({
                'day': 1,
                'month': mm,
                'year': yy,
                'leap': 0,
                'jd': current_jd
            })
            current_jd += regular_months[mm - 1]
    
    return ly


def get_year_info(yyyy: int) -> List[LunarDate]:
    """
    Get year information (fallback method)
    Lấy thông tin năm (phương pháp dự phòng)
    
    Args:
        yyyy: Year
        
    Returns:
        List of LunarDate
    """
    if yyyy < 1900:
        year_code = TK19[yyyy - 1800]
    elif yyyy < 2000:
        year_code = TK20[yyyy - 1900]
    elif yyyy < 2100:
        year_code = TK21[yyyy - 2000]
    else:
        year_code = TK22[yyyy - 2100]
    
    return decode_lunar_year(yyyy, year_code)


def get_month(mm: int, yy: int) -> List[LunarDate]:
    """
    Get lunar month information
    Lấy thông tin tháng âm lịch
    
    Args:
        mm: Solar month
        yy: Solar year
        
    Returns:
        List of LunarDate for all days in the month
    """
    mm1 = mm + 1 if mm < 12 else 1
    yy1 = yy if mm < 12 else yy + 1
    jd1 = jdn(1, mm, yy)
    jd2 = jdn(1, mm1, yy1)
    result = []
    
    for i in range(jd1, jd2):
        solar_date = jdn2date(i)
        lunar = get_lunar_date(solar_date[0], solar_date[1], solar_date[2])
        result.append(lunar)
    
    return result
