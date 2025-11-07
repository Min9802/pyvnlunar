"""
Ví dụ về xem ngày tốt xấu
Example of checking auspicious/inauspicious days
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import vnlunar

def main():
    print("=" * 60)
    print("XEM NGÀY TỐT XẤU")
    print("=" * 60)
    
    # Ngày cần kiểm tra
    day, month, year = 15, 11, 2025
    jd = vnlunar.jdn(day, month, year)
    
    print(f"\nNgày kiểm tra: {day}/{month}/{year}")
    
    # Danh sách các việc cần xem
    cac_viec = [
        ("wedding", "Cưới hỏi"),
        ("construction", "Xây nhà"),
        ("travel", "Xuất hành"),
        ("opening", "Khai trương"),
        ("moving", "Chuyển nhà"),
        ("investment", "Đầu tư"),
    ]
    
    print("\n" + "-" * 60)
    print("KẾT QUẢ XEM NGÀY:")
    print("-" * 60)
    
    for viec_key, viec_name in cac_viec:
        ket_qua = vnlunar.check_good_day(jd, viec_key)
        print(f"\n{viec_name.upper()}:")
        print(f"  Sao: {ket_qua['star']['name']}")
        print(f"  {ket_qua['description']}")
    
    # Tìm các ngày tốt để cưới hỏi trong tháng
    print("\n" + "=" * 60)
    print("TÌM NGÀY TỐT ĐỂ CƯỚI HỎI TRONG THÁNG 11/2025")
    print("=" * 60)
    
    start_jd = vnlunar.jdn(1, 11, 2025)
    end_jd = vnlunar.jdn(30, 11, 2025)
    
    ngay_tot = vnlunar.find_good_days(start_jd, end_jd, "cuoi")
    
    if ngay_tot:
        print(f"\nTìm thấy {len(ngay_tot)} ngày tốt:")
        for i, ngay in enumerate(ngay_tot[:10], 1):  # Hiển thị tối đa 10 ngày
            lunar = vnlunar.convert_solar_to_lunar(
                ngay['solar']['day'], 
                ngay['solar']['month'], 
                ngay['solar']['year'], 
                7.0
            )
            print(f"\n{i}. Dương lịch: {ngay['solar']['day']}/{ngay['solar']['month']}/{ngay['solar']['year']}")
            print(f"   Âm lịch: {lunar['day']}/{lunar['month']}/{lunar['year']}")
            print(f"   Sao: {ngay['star']['name']} - {ngay['star']['description']}")
            print(f"   {ngay['description']}")
        
        if len(ngay_tot) > 10:
            print(f"\n... và {len(ngay_tot) - 10} ngày tốt khác")
    else:
        print("\nKhông tìm thấy ngày tốt trong khoảng thời gian này.")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
