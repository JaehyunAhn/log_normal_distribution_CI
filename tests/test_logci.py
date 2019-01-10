# coding: utf-8
import pytest

from CredibilityInterval import LogCredibilityInterval

@pytest.mark.xfail(raises=ValueError)
def test_ci_error():
    LogCredibilityInterval(mean=1, variance=4, sample_size=-4)
    LogCredibilityInterval(mean=1, variance=4, sample_size=0)


def test_stat_value():
    a = LogCredibilityInterval(mean=1, variance=4, sample_size=4)
    assert a.mean == 1
    assert a.variance == 4.0
    assert a.stdev == 2.0
    assert a.sample_size == 4

def test_ci_value_bound():
    # 경계값 테스트
    a = LogCredibilityInterval(mean=1, variance=4, sample_size=1)
    assert a.get_variate('95%') == 2.571
    a = LogCredibilityInterval(mean=1, variance=4, sample_size=4)
    assert a.get_variate('95%') == 2.571
    a = LogCredibilityInterval(mean=1, variance=4, sample_size=5)
    assert a.get_variate('95%') == 2.571
    a = LogCredibilityInterval(mean=1, variance=4, sample_size=6)
    assert a.get_variate('95%') == 2.571
    a = LogCredibilityInterval(mean=1, variance=4, sample_size=11)
    assert a.get_variate('95%') == 2.228
    a = LogCredibilityInterval(mean=1, variance=4, sample_size=16)
    assert a.get_variate('95%') == 2.131
    a = LogCredibilityInterval(mean=1, variance=4, sample_size=21)
    assert a.get_variate('95%') == 2.086
    a = LogCredibilityInterval(mean=1, variance=4, sample_size=26)
    assert a.get_variate('95%') == 2.060
    a = LogCredibilityInterval(mean=1, variance=4, sample_size=31)
    assert a.get_variate('95%') == 2.042
    a = LogCredibilityInterval(mean=1, variance=4, sample_size=32)
    assert a.get_variate('95%') == 1.96


def test_ci_string():
    a = LogCredibilityInterval(mean=1, variance=4, sample_size=1)
    assert a.get_variate('1-sigma') == a.get_variate('70%')
    assert a.get_variate('2-sigma') == a.get_variate('95%')
    assert a.get_variate('3-sigma') == a.get_variate('99%')
    assert a.get_variate('1-sigma') == 1.156
    assert a.get_variate('2-sigma') == 2.571
    assert a.get_variate('3-sigma') == 4.032
