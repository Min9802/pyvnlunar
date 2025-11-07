"""
Ví dụ cơ bản về sử dụng vnlunar
Basic usage example for vnlunar
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Import vnlunar
import vnlunar

def main():
    print("=" * 60)
    print("VÍ DỤ CƠ BẢN - VNLUNAR")
    print("=" * 60)
    
    # Ngày hôm nay (ví dụ)
    day, month, year = 7, 11, 2025
    
    print(f"\n1. CHUYỂN ĐỔI DƯƠNG LỊCH -> ÂM LỊCH")
    print("-" * 60)
    lunar = vnlunar.get_lunar_date(day, month, year)
    print(f"Dương lịch: {day}/{month}/{year}")
    print(f"Âm lịch: {lunar['day']}/{lunar['month']}/{lunar['year']}")
    print(f"Tháng nhuận: {'Có' if lunar['leap'] == 1 else 'Không'}")
    print(f"Julian Day: {lunar['jd']}")
    
    print(f"\n2. THÔNG TIN ĐẦY ĐỦ")
    print("-" * 60)
    info = vnlunar.get_full_info(day, month, year)
    
    # Can Chi
    print(f"\nCan Chi:")
    print(f"  Năm: {info['can_chi']['year']}")
    print(f"  Tháng: {info['can_chi']['month']}")
    print(f"  Ngày: {info['can_chi']['day']}")
    print(f"  Giờ Tý: {info['can_chi']['hour']}")
    
    # Ngũ Hành
    print(f"\nNgũ Hành năm: {info['year_element']['name']}")
    print(f"  Can năm: {info['year_element']['can_element']}")
    print(f"  Chi năm: {info['year_element']['chi_element']}")
    
    # 12 Sao
    print(f"\n12 Sao Kiến Trừ: {info['12_stars']['name']}")
    print(f"  Mô tả: {info['12_stars']['description']}")
    print(f"  Trạng thái: {info['12_stars']['status']}")
    
    # 12 Thần
    print(f"\n12 Thần: {info['12_gods']['name']}")
    print(f"  Loại: {info['12_gods']['type']}")
    print(f"  Mô tả: {info['12_gods']['description']}")
    
    # Hoàng Đạo / Hắc Đạo
    print(f"\nHoàng/Hắc Đạo:")
    print(f"  Loại: {info['day_type']['type']}")
    print(f"  Sao: {info['day_type']['star']}")
    
    # Thập Nhị Trực
    print(f"\nThập Nhị Trực: {info['12_constructions']['name']}")
    print(f"  Nên làm: {info['12_constructions']['good_for']}")
    print(f"  Không nên: {info['12_constructions']['bad_for']}")
    
    # 28 Tú Sao
    print(f"\n28 Tú Sao: {info['28_mansions']['name']}")
    print(f"  Động vật: {info['28_mansions']['animal']}")
    print(f"  Ngũ hành: {info['28_mansions']['element']}")
    print(f"  Mô tả: {info['28_mansions']['description']}")
    
    # Nạp Âm
    print(f"\nNạp Âm: {info['nayin']['name']}")
    print(f"  Ngũ hành: {info['nayin']['element']}")
    print(f"  Can Chi: {info['nayin']['can']} {info['nayin']['chi']}")
    
    # Giờ Hoàng Đạo
    print(f"\nGiờ Hoàng Đạo: {info['auspicious_hours']}")
    
    # Thứ
    print(f"\nThứ trong tuần: {info['day_of_week']}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
