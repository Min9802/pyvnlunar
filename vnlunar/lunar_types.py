"""
Type definitions for vnlunar library
Các định nghĩa kiểu dữ liệu cho thư viện vnlunar
"""

from typing import TypedDict, Literal, List

# Type aliases
Element = Literal["Thủy", "Hỏa", "Mộc", "Kim", "Thổ"]  # Water, Fire, Wood, Metal, Earth
StarStatus = Literal["good", "bad", "neutral"]  # good, bad, neutral
GodType = Literal["auspicious", "inauspicious"]  # auspicious, inauspicious


class LunarDate(TypedDict):
    """Lunar date information / Thông tin ngày âm lịch"""
    day: int
    month: int
    year: int
    leap: int  # 0 = normal month, 1 = leap month
    jd: int  # Julian Day Number


class SolarDate(TypedDict):
    """Solar date information / Thông tin ngày dương lịch"""
    day: int
    month: int
    year: int
    day_of_week: str


class CanChiInfo(TypedDict):
    """Can Chi (Heavenly Stems & Earthly Branches) information"""
    day: str  # Day Can Chi
    month: str  # Month Can Chi
    year: str  # Year Can Chi
    hour: str  # Hour Can Chi (hour 0 - Tý)


class ElementInfo(TypedDict):
    """Five Elements information for a date"""
    can: Element  # Heavenly Stem element
    chi: Element  # Earthly Branch element


class YearElementInfo(TypedDict):
    """Year Five Elements information"""
    can: str  # Heavenly Stem
    chi: str  # Earthly Branch
    animal: str  # Zodiac animal
    can_chi: str  # Combined Can Chi
    name: Element  # Main element
    element: Element  # Main element (alias)
    can_element: Element  # Can element
    chi_element: Element  # Chi element


class Star12Info(TypedDict):
    """12 Day Officers information (12 Sao Kiến Trừ)"""
    name: str
    status: StarStatus
    color: str
    desc: str


class God12Info(TypedDict):
    """12 Gods information (Hoàng Đạo / Hắc Đạo)"""
    name: str
    type: GodType
    status: StarStatus
    desc: str


class Construction12Info(TypedDict):
    """12 Day Constructions information (Thập Nhị Trực)"""
    name: str
    should_do: List[str]  # Things should do
    should_not_do: List[str]  # Things should not do


class Mansion28Info(TypedDict):
    """28 Lunar Mansions information (28 Tú Sao)"""
    name: str
    animal: str  # Associated animal
    element: str  # Associated element
    good: bool  # Is it auspicious?
    desc: str


class NayinInfo(TypedDict):
    """Nayin 60 information (Nạp Âm)"""
    name: str
    element: str
    can: str
    chi: str


class DayTypeInfo(TypedDict):
    """Auspicious/Inauspicious day type information"""
    type: Literal["Hoàng Đạo", "Hắc Đạo"]  # Auspicious Day / Inauspicious Day
    star: str
    good: bool
    bad: bool
    desc: str


class ConflictingAgeInfo(TypedDict):
    """Age conflict information (Tuổi Xung)"""
    day_chi: str
    day_animal: str
    conflict_chi: str
    conflict_animal: str
    description: str
    conflicting_ages: List[dict]
    note: str


class DirectionInfo(TypedDict):
    """Travel direction information (Ngọc Hạp Thông Thư)"""
    day_chi: str
    good: List[str]
    bad: List[str]
    description: str
    good_text: str
    bad_text: str


class GodDirectionInfo(TypedDict):
    """Gods direction information"""
    day_can: str
    joy_god: str  # Hỷ Thần direction
    wealth_god: str  # Thần Tài direction
    fortune_god: str  # Phúc Thần direction
    description: str


class HourInfo(TypedDict):
    """Hour information"""
    chi: str
    index: int
    period: str
    good: bool


class DaySelectionResult(TypedDict):
    """Day selection result for activities"""
    star: Star12Info
    activity: str
    good: bool
    description: str
