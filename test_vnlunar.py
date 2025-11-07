#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test script for vnlunar
Quick test without needing package installation
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(__file__))

# Now we can import from local directory
from vnlunar import constants
from vnlunar import lunar_types
from vnlunar import core
from vnlunar import calendar
from vnlunar import astrology
from vnlunar import direction

# Main functions
get_lunar_date = core.get_lunar_date
jdn = core.jdn
get_can_chi = calendar.get_can_chi
get_year_ngu_hanh = calendar.get_year_ngu_hanh
get_12_sao = astrology.get_12_sao
get_12_than = astrology.get_12_than
get_hoang_hac_dao = astrology.get_hoang_hac_dao
get_thap_nhi_truc = astrology.get_thap_nhi_truc
get_28_tu_sao = astrology.get_28_tu_sao
get_nap_am = astrology.get_nap_am
get_gio_hoang_dao = calendar.get_gio_hoang_dao
get_day_of_week = calendar.get_day_of_week
xem_ngay = astrology.xem_ngay
tim_ngay_tot = astrology.tim_ngay_tot
get_tuoi_xung = direction.get_tuoi_xung
check_tuoi_xung = direction.check_tuoi_xung
get_ngoc_hap_thong_thu = direction.get_ngoc_hap_thong_thu
get_huong_than_theo_ngay = direction.get_huong_than_theo_ngay
get_huong_xuat_hanh_theo_tuoi = direction.get_huong_xuat_hanh_theo_tuoi
get_huong_xuat_hanh = direction.get_huong_xuat_hanh
kiem_tra_gio_xuat_hanh = direction.kiem_tra_gio_xuat_hanh

def get_full_info(day: int, month: int, year: int) -> dict:
    """Get complete information about a date"""
    lunar = get_lunar_date(day, month, year)
    jd_num = lunar['jd']
    
    result = {
        'solar': {
            'day': day,
            'month': month,
            'year': year,
            'day_of_week': get_day_of_week(jd_num)
        },
        'lunar': lunar,
        'can_chi': get_can_chi(lunar),
        'ngu_hanh_nam': get_year_ngu_hanh(lunar['year']),
        'sao_12_kien_tru': get_12_sao(lunar['day'], lunar['month']),
        'thap_nhi_truc': get_thap_nhi_truc(lunar['day'], lunar['month']),
        'sao_12_than': get_12_than(jd_num),
        'tu_sao_28': get_28_tu_sao(jd_num),
        'nap_am': get_nap_am(jd_num),
        'hoang_hac_dao': get_hoang_hac_dao(lunar['day'], lunar['month']),
        'tuoi_xung': get_tuoi_xung(jd_num, year),
        'ngoc_hap_thong_thu': get_ngoc_hap_thong_thu(jd_num),
        'huong_than': get_huong_than_theo_ngay(jd_num),
        'gio_hoang_dao': get_gio_hoang_dao(jd_num),
        'thu': get_day_of_week(jd_num),
        'jd': jd_num
    }
    
    return result

if __name__ == "__main__":
    print("=" * 60)
    print("TEST VNLUNAR")
    print("=" * 60)
    
    # Test basic conversion
    day, month, year = 7, 11, 2025
    lunar = get_lunar_date(day, month, year)
    
    print(f"\nDương lịch: {day}/{month}/{year}")
    print(f"Âm lịch: {lunar['day']}/{lunar['month']}/{lunar['year']}")
    print(f"Julian Day: {lunar['jd']}")
    
    # Test full info
    print("\nLấy thông tin đầy đủ...")
    info = get_full_info(day, month, year)
    print(f"Can Chi ngày: {info['can_chi']['ngay']}")
    print(f"12 Sao: {info['sao_12_kien_tru']['name']}")
    print(f"Hoàng/Hắc Đạo: {info['hoang_hac_dao']['type']}")
    
    print("\n✓ Test thành công!")
