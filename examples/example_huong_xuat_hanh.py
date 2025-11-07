"""
Ví dụ về xem hướng xuất hành và tuổi xung
Example of checking travel directions and age conflicts
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import vnlunar

def main():
    print("=" * 60)
    print("HƯỚNG XUẤT HÀNH VÀ TUỔI XUNG")
    print("=" * 60)
    
    # Thông tin
    day, month, year = 7, 11, 2025
    birth_year = 1990
    current_year = 2025
    
    jd = vnlunar.jdn(day, month, year)
    
    print(f"\nNgày: {day}/{month}/{year}")
    print(f"Năm sinh: {birth_year}")
    print(f"Tuổi: {current_year - birth_year}")
    
    # 1. Kiểm tra tuổi xung
    print("\n" + "=" * 60)
    print("1. KIỂM TRA TUỔI XUNG")
    print("-" * 60)
    
    xung = vnlunar.check_age_conflict(jd, birth_year)
    print(f"Tuổi {birth_year} có xung với ngày này: {'CÓ' if xung else 'KHÔNG'}")
    
    tuoi_xung_info = vnlunar.get_conflicting_ages(jd, current_year)
    print(f"\n{tuoi_xung_info['description']}")
    print(f"\nCác tuổi xung trong ngày này:")
    for tuoi in tuoi_xung_info['conflicting_ages'][:10]:
        print(f"  • Tuổi {tuoi['age']:2d}: {tuoi['can_chi']} ({tuoi['animal']})")
    
    # 2. Hướng theo Ngọc Hạp Thông Thư
    print("\n" + "=" * 60)
    print("2. HƯỚNG THEO NGỌC HẠP THÔNG THƯ")
    print("-" * 60)
    
    huong_ngay = vnlunar.get_direction_info(jd)
    print(f"Ngày: {huong_ngay['chi']}")
    print(f"Hướng tốt: {huong_ngay['good_text']}")
    print(f"Hướng xấu: {huong_ngay['bad_text']}")
    
    # 3. Hướng thần
    print("\n" + "=" * 60)
    print("3. HƯỚNG CÁC VỊ THẦN")
    print("-" * 60)
    
    huong_than = vnlunar.get_god_directions(jd)
    print(f"Can ngày: {huong_than['can']}")
    print(f"Hướng Thần Tài: {huong_than['wealth_god']}")
    print(f"Hướng Hỷ Thần: {huong_than['joy_god']}")
    print(f"Hướng Phúc Thần: {huong_than['fortune_god']}")
    
    # 4. Hướng theo tuổi
    print("\n" + "=" * 60)
    print("4. HƯỚNG THEO TUỔI (CON GIÁP)")
    print("-" * 60)
    
    huong_tuoi = vnlunar.get_age_direction(birth_year, current_year)
    print(f"Tuổi: {huong_tuoi['age']} ({huong_tuoi['chi']}) - {huong_tuoi['animal']}")
    print(f"Hướng tốt: {huong_tuoi['good_text']}")
    print(f"Hướng xấu: {huong_tuoi['bad_text']}")
    
    # 5. Hướng xuất hành tổng hợp
    print("\n" + "=" * 60)
    print("5. HƯỚNG XUẤT HÀNH TỔNG HỢP")
    print("-" * 60)
    
    huong_xuat_hanh = vnlunar.get_travel_direction(jd, birth_year, current_year)
    print(f"\n{huong_xuat_hanh['advice']}")
    
    if huong_xuat_hanh['common_good']:
        print(f"\nHướng tốt cho cả ngày và tuổi: {', '.join(huong_xuat_hanh['common_good'])}")
    else:
        print("\nKhông có hướng chung tốt cho cả ngày và tuổi.")
    
    # 6. Kiểm tra giờ xuất hành
    print("\n" + "=" * 60)
    print("6. GIỜ XUẤT HÀNH")
    print("-" * 60)
    
    cac_gio = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tị", 
               "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
    
    print("\nGiờ Hoàng Đạo trong ngày:")
    for gio in cac_gio:
        gio_info = vnlunar.check_travel_hour(jd, gio)
        if gio_info['good']:
            print(f"  • Giờ {gio_info['chi']:4s} ({gio_info['period']:13s}): ✓ TỐT")
    
    print("\nGiờ Hắc Đạo (không nên xuất hành):")
    for gio in cac_gio:
        gio_info = vnlunar.check_travel_hour(jd, gio)
        if not gio_info['good']:
            print(f"  • Giờ {gio_info['chi']:4s} ({gio_info['period']:13s}): ✗ XẤU")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
