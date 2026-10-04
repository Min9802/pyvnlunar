# Quy Tắc Tính Tuổi Xung Khắc Trong vnLunar v2.0

Tài liệu hướng dẫn về phương pháp xác định và tính toán Tuổi Xung Khắc (Xung ngày, Xung tuổi) trong thư viện `vnlunar`.

---

## 1. Bản Chất của Tuổi Xung Khắc trong Lịch Pháp

Trong thuật trạch nhật (chọn ngày lành tháng tốt) và phong thủy truyền thống Việt Nam / Á Đông, **Tuổi Xung** với ngày là các tuổi chịu ảnh hưởng tiêu cực nhất bởi trường khí của ngày đó. Khi tiến hành các công việc trọng đại (khởi công, xuất hành, cưới hỏi, an táng...), người chủ sự hoặc đương số có tuổi xung với ngày cần đặc biệt thận trọng hoặc tránh đứng tên chủ trì.

---

## 2. Các Cấp Độ Xung Khắc

Trong `vnlunar v2`, tuổi xung được phân tích và xếp loại dựa trên 3 tiêu chí chính xác:

### 2.1. Lục Xung Địa Chi (Trực Xung - Cốt lõi)
12 Địa Chi đối xứng tạo thành 6 cặp Lục Xung đối kháng trực diện theo phương vị không gian (trục đối xứng 180°):
- **Tý** (Bắc - Thủy) xung **Ngọ** (Nam - Hỏa)
- **Sửu** (Đông Bắc - Thổ) xung **Mùi** (Tây Nam - Thổ)
- **Dần** (Đông Bắc - Mộc) xung **Thân** (Tây Nam - Kim)
- **Mão** (Đông - Mộc) xung **Dậu** (Tây - Kim)
- **Thìn** (Đông Nam - Thổ) xung **Tuất** (Tây Bắc - Thổ)
- **Tỵ** (Đông Nam - Hỏa) xung **Hợi** (Tây Bắc - Thủy)

> **Lưu ý quan trọng**: Dân gian hay gọi "Tứ hành xung" (ví dụ: Dần - Thân - Tỵ - Hợi), nhưng trong thực tế học thuật chỉ có cặp **đối xứng trực tiếp** mới tạo thành xung sát nặng nề (Dần xung Thân, Tỵ xung Hợi; còn Dần với Tỵ hay Hợi thuộc quan hệ Hình/Hại/Hợp, không phải Lục Xung). Thư viện `vnlunar v2` không gộp bừa bãi 4 con giáp mà chỉ lấy cặp chính xung.

### 2.2. Thiên Khắc Địa Xung (Đại Kỵ - Tuổi Xung Chính)
Khi một tuổi vừa có:
1. **Địa Chi trực xung** với Chi ngày (Lục Xung).
2. **Thiên Can xung phá/khắc phạt** với Can ngày (ví dụ Giáp Canh, Ất Tân, Bính Nhâm, Đinh Quý).
3. **Nạp Âm ngũ hành tương khắc** với Nạp Âm của ngày.

Tuổi này được đánh dấu là **Tuổi Xung Chính** (`primary: true`, hiển thị kèm dấu `*` trong danh sách).

### 2.3. Nạp Âm Ngũ Hành Khắc
So sánh giữa mệnh Nạp Âm của ngày (trong 30 Nạp Âm Lục Thập Hoa Giáp) và mệnh Nạp Âm của năm sinh. Các tuổi có Chi trực xung và thêm mệnh khắc (ví dụ ngày Thiên Hà Thủy khắc Tích Lịch Hỏa) sẽ gia tăng tính sát khí.

---

## 3. Cách Sử Dụng Trong Code

### 3.1. TypeScript (`@min98/vnlunar`)

```typescript
import { get_conflicting_ages, check_age_conflict, getFullInfo } from '@min98/vnlunar';

// 1. Lấy danh sách tuổi xung cho một ngày
const info = getFullInfo(6, 11, 2025);
console.log('Ngày:', info.can_chi.day); // Kỷ Mão
console.log('Tuổi xung:', info.conflicting_ages.description);
// Output: Ngày Kỷ Mão xung với tuổi: Ất Dậu, Tân Dậu...

// 2. Chi tiết các tuổi xung
for (const age of info.conflicting_ages.conflicting_ages) {
  console.log(`- Năm ${age.year} (${age.can_chi}): ${age.primary ? 'Xung chính (*)' : 'Xung phụ'}`);
}

// 3. Kiểm tra độ tương thích giữa 2 tuổi (hoặc tuổi người với năm/ngày)
const check = check_age_conflict(1990, 1996); // Canh Ngọ vs Bính Tý
console.log(check.conflict ? 'Xung nhau' : 'Không xung');
```

### 3.2. Python (`vnlunar`)

```python
from vnlunar import get_conflicting_ages, check_age_conflict, get_full_info

# 1. Lấy danh sách tuổi xung
info = get_full_info(6, 11, 2025)
print(info['conflicting_ages']['description'])

# 2. Kiểm tra xung tuổi
result = check_age_conflict(1994, 2000) # Giáp Tuất vs Canh Thìn (Thìn - Tuất trực xung)
print(result['conflict'], result['description'])
```
