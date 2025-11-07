"""
Ví dụ về Ngũ Hành và quan hệ tương sinh, tương khắc
Example of Five Elements and their relationships
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import vnlunar
from vnlunar.calendar import get_element_relation

def main():
    print("=" * 60)
    print("NGŨ HÀNH VÀ QUAN HỆ TƯƠNG SINH, TƯƠNG KHẮC")
    print("=" * 60)
    
    # Thông tin một số năm
    cac_nam = [1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025]
    
    print("\n1. NGŨ HÀNH CỦA CÁC NĂM")
    print("-" * 60)
    
    for nam in cac_nam:
        info_nam = vnlunar.get_year_element(nam)
        print(f"\nNăm {nam}: {info_nam['can_chi']}")
        print(f"  Ngũ hành năm: {info_nam['name']}")
        print(f"  Can: {info_nam['can']} → {info_nam['can_element']}")
        print(f"  Chi: {info_nam['chi']} → {info_nam['chi_element']}")
    
    # Quan hệ giữa các ngũ hành
    print("\n\n2. QUAN HỆ GIỮA CÁC NGŨ HÀNH")
    print("-" * 60)
    
    ngu_hanh_list = ["Kim", "Mộc", "Thủy", "Hỏa", "Thổ"]
    
    print("\nBẢNG TƯƠNG QUAN NGŨ HÀNH:")
    print("\n(Hành 1 → Hành 2)")
    print("-" * 40)
    
    for hanh1 in ngu_hanh_list:
        print(f"\n{hanh1}:")
        for hanh2 in ngu_hanh_list:
            if hanh1 == hanh2:
                continue
            relation = get_element_relation(hanh1, hanh2)
            print(f"  → {hanh2:5s}: {relation}")
    
    # Ví dụ cụ thể về quan hệ
    print("\n\n3. VÍ DỤ CỤ THỂ")
    print("-" * 60)
    
    nam_1990 = vnlunar.get_year_element(1990)
    nam_2025 = vnlunar.get_year_element(2025)
    
    print(f"\nSo sánh năm 1990 và năm 2025:")
    print(f"  Năm 1990: {nam_1990['can_chi']} - {nam_1990['name']}")
    print(f"  Năm 2025: {nam_2025['can_chi']} - {nam_2025['name']}")
    
    relation = get_element_relation(nam_1990['name'], nam_2025['name'])
    print(f"\n  Quan hệ: {nam_1990['name']} → {nam_2025['name']}: {relation}")
    
    # Chu kỳ tương sinh
    print("\n\n4. CHU KỲ TƯƠNG SINH")
    print("-" * 60)
    print("\nThủy → Mộc → Hỏa → Thổ → Kim → Thủy")
    print("(Nước sinh Cây, Cây sinh Lửa, Lửa sinh Đất, Đất sinh Kim, Kim sinh Nước)")
    
    sinh_cycle = [("Thủy", "Mộc"), ("Mộc", "Hỏa"), ("Hỏa", "Thổ"), 
                  ("Thổ", "Kim"), ("Kim", "Thủy")]
    
    for h1, h2 in sinh_cycle:
        relation = get_element_relation(h1, h2)
        print(f"  {h1:5s} → {h2:5s}: {relation}")
    
    # Chu kỳ tương khắc
    print("\n\n5. CHU KỲ TƯƠNG KHẮC")
    print("-" * 60)
    print("\nThủy → Hỏa → Kim → Mộc → Thổ → Thủy")
    print("(Nước khắc Lửa, Lửa khắc Kim, Kim khắc Cây, Cây khắc Đất, Đất khắc Nước)")
    
    khac_cycle = [("Thủy", "Hỏa"), ("Hỏa", "Kim"), ("Kim", "Mộc"), 
                  ("Mộc", "Thổ"), ("Thổ", "Thủy")]
    
    for h1, h2 in khac_cycle:
        relation = get_element_relation(h1, h2)
        print(f"  {h1:5s} → {h2:5s}: {relation}")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
