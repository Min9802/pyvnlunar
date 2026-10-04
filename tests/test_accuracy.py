"""
Accuracy tests - so khớp với golden fixtures dùng chung với vnlunar-ts.
Chạy: python -m pytest tests -q
"""

import json
import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

import vnlunar as L  # noqa: E402
from vnlunar import constants as C  # noqa: E402

FIX = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures')


def load(name):
    with open(os.path.join(FIX, name), encoding='utf-8') as f:
        return json.load(f)


CONVERSION = load('conversion.json')
NAYIN = load('nayin.json')
ANCHORS = load('anchors.json')
SOLAR_TERMS = load('solar_terms.json')


def test_range_constants():
    assert C.FIRST_DAY == L.jdn(25, 1, 1800)
    assert C.LAST_DAY == L.jdn(31, 12, 2199)
    assert C.LAST_DAY == CONVERSION['range']['last_jd']


def test_solar_to_lunar_matches_hnd_tables_every_day():
    months = CONVERSION['months']
    checked = 0
    for i in range(len(months) - 1):
        y, m, leap, start = months[i]
        end = months[i + 1][3]
        for jd in range(start, min(end, C.LAST_DAY + 1)):
            dd, mm, yy = L.jdn2date(jd)
            r = L.get_lunar_date(dd, mm, yy)
            expected = (jd - start + 1, m, y, leap, jd)
            got = (r['day'], r['month'], r['year'], r['leap'], r['jd'])
            assert got == expected, f"{dd}/{mm}/{yy}: got {got}, expected {expected}"
            checked += 1
    assert checked > 140000


def test_lunar_to_solar_round_trip():
    months = CONVERSION['months']
    for i in range(len(months) - 1):
        y, m, leap, start = months[i]
        length = months[i + 1][3] - start
        for d in (1, length):
            s = L.convert_lunar_to_solar(d, m, y, leap)
            assert s is not None, (d, m, y, leap)
            assert L.jdn(*s) == start + d - 1, (d, m, y, leap)
        if length == 29:
            assert L.convert_lunar_to_solar(30, m, y, leap) is None


def test_lunar_to_solar_invalid():
    assert L.convert_lunar_to_solar(1, 5, 2025, 1) is None
    assert L.convert_lunar_to_solar(1, 1, 2026, 1) is None
    assert L.convert_lunar_to_solar(0, 1, 2026) is None
    assert L.convert_lunar_to_solar(1, 13, 2026) is None
    assert L.get_solar_date(1, 6, 2025, 1) == {'day': 25, 'month': 7, 'year': 2025, 'jd': L.jdn(25, 7, 2025)}


def test_astronomical_day_in_range_and_matches_1968_2053():
    months = CONVERSION['months']
    for i in range(len(months) - 1):
        y, m, leap, start = months[i]
        end = months[i + 1][3]
        # Lấy mẫu mỗi 3 ngày để test chạy nhanh; ngày đầu tháng luôn được kiểm
        for jd in list(range(start, end, 3)) + [end - 1]:
            dd, mm, yy = L.jdn2date(jd)
            r = L.convert_solar_to_lunar(dd, mm, yy, 7.0)
            assert 1 <= r['day'] <= 30, (dd, mm, yy, r)
            if 1968 <= yy <= 2053:
                assert (r['day'], r['month'], r['year'], r['leap']) == (jd - start + 1, m, y, leap), (dd, mm, yy)


def test_out_of_table_range_uses_astronomical():
    r = L.get_lunar_date(1, 1, 2300)
    assert 1 <= r['day'] <= 30
    assert L.convert_lunar_to_solar(r['day'], r['month'], r['year'], r['leap']) == (1, 1, 2300)


def test_nayin_all_60():
    assert len(C.NAYIN_60) == 60
    assert len(C.NAYIN_30) == 30
    for item in NAYIN['items']:
        can, chi = item['index'] % 10, item['index'] % 12
        assert L.get_sexagenary_index(can, chi) == item['index']
        n = L.get_nayin_by_can_chi(can, chi)
        assert n['name'] == item['name'], item['can_chi']
        assert n['element'] == item['element'], item['can_chi']


def test_28_mansions_good_and_weekday():
    good = [m['name'] for m in C.MANSIONS_28 if m['good']]
    assert good == ['Giác', 'Phòng', 'Vĩ', 'Cơ', 'Đẩu', 'Thất', 'Bích', 'Lâu', 'Vị', 'Tất', 'Sâm', 'Tỉnh', 'Trương', 'Chẩn']
    weekday_element = {'Thứ năm': 'Mộc', 'Thứ sáu': 'Kim', 'Thứ bảy': 'Thổ', 'Chủ nhật': 'Nhật',
                       'Thứ hai': 'Nguyệt', 'Thứ ba': 'Hỏa', 'Thứ tư': 'Thủy'}
    for jd in range(L.jdn(1, 1, 2025), L.jdn(1, 1, 2026)):
        assert L.get_28_mansions(jd)['element'] == weekday_element[L.get_day_of_week(jd)]


@pytest.mark.parametrize('a', ANCHORS['anchors'], ids=lambda a: '{}-{}-{}'.format(*a['solar']))
def test_anchor(a):
    d, m, y = a['solar']
    info = L.get_full_info(d, m, y)
    if 'lunar' in a:
        lu = info['lunar']
        assert [lu['day'], lu['month'], lu['year'], lu['leap']] == a['lunar']
    if 'day_can_chi' in a:
        assert info['can_chi']['day'] == a['day_can_chi']
    if 'month_can_chi' in a:
        assert info['can_chi']['month'] == a['month_can_chi']
    if 'year_can_chi' in a:
        assert info['can_chi']['year'] == a['year_can_chi']
    if 'weekday' in a:
        assert info['solar']['day_of_week'].lower() == a['weekday'].lower()
    if 'truc' in a:
        assert info['12_stars']['name'] == a['truc']
        assert info['12_constructions']['short_name'] == a['truc']
    if 'god' in a:
        assert info['12_gods']['name'] == a['god']
    if 'day_type' in a:
        assert info['day_type']['type'] == a['day_type']
    if 'mansion' in a:
        assert info['28_mansions']['name'] == a['mansion']
    if 'nayin' in a:
        assert info['nayin']['name'] == a['nayin']
    if 'joy_god' in a:
        assert info['god_directions']['joy_god'] == a['joy_god']
    if 'wealth_god' in a:
        assert info['god_directions']['wealth_god'] == a['wealth_god']
    ages = [x['can_chi'].replace('*', '') for x in info['conflicting_ages']['conflicting_ages']]
    if 'conflicting_ages' in a:
        assert ages == a['conflicting_ages']
    for c in a.get('conflicting_ages_include', []):
        assert c in ages


def test_month_basis_options():
    jd = L.jdn(15, 1, 2026)
    assert L.get_12_stars(jd)['name'] == 'Kiến'
    assert L.get_12_stars(jd, truc_basis='lunar')['name'] == 'Trừ'
    assert L.get_12_gods(jd)['name'] == 'Thiên Đức'
    assert L.get_12_gods(jd, god_basis='solar_term')['name'] == 'Chu Tước'
    with pytest.raises(ValueError):
        L.get_12_stars(jd, truc_basis='abc')


def test_old_signature_raises():
    with pytest.raises(TypeError):
        L.get_12_stars(19, 9)


@pytest.mark.parametrize('t', SOLAR_TERMS['terms'], ids=lambda t: t['name'])
def test_solar_term_start(t):
    jd = L.jdn(*t['solar'])
    assert L.get_solar_term(jd)['name'] == t['name']
    assert L.get_solar_term(jd - 1)['name'] != t['name']


def test_four_pillars():
    p = L.get_four_pillars(8, 11, 2025, 10)
    assert [p[k]['can_chi'] for k in ('year', 'month', 'day', 'hour')] == ['Ất Tỵ', 'Đinh Hợi', 'Tân Tỵ', 'Quý Tỵ']
    p = L.get_four_pillars(2, 2, 2025, 12)
    assert (p['year']['can_chi'], p['month']['can_chi']) == ('Giáp Thìn', 'Đinh Sửu')
    p = L.get_four_pillars(4, 2, 2025, 12)
    assert (p['year']['can_chi'], p['month']['can_chi']) == ('Ất Tỵ', 'Mậu Dần')
    p = L.get_four_pillars(1, 2, 2025, 23, 30)
    assert p['day_jd'] == L.jdn(2, 2, 2025) and p['hour']['chi'] == 'Tý'


def test_check_good_day_requires_hoang_dao_and_truc():
    for jd in range(L.jdn(1, 1, 2025), L.jdn(1, 1, 2026)):
        r = L.check_good_day(jd, 'wedding')
        if r['good']:
            assert r['god']['status'] == 'good'
            assert r['star']['name'] in ('Định', 'Thành', 'Khai')
    days = L.find_good_days(L.jdn(1, 11, 2025), L.jdn(30, 11, 2025), 'opening')
    assert isinstance(days, list)
