# coding: utf-8
from pytest import approx
from CredibilityInterval import CredibilityInterval, LogCredibilityInterval

def test_ci_interval():
    a = CredibilityInterval(mean=1, variance=4, sample_size=4)
    assert a.naive_method('70%') == approx((-0.156, 2.156), abs=0.001)
    assert a.naive_method('95%') == approx((-1.571, 3.571), abs=0.001)
    assert a.naive_method('99%') == approx((-3.032, 5.032), abs=0.001)
    assert a.naive_method('1-sigma') == approx((-0.156, 2.156), abs=0.001)
    assert a.naive_method('2-sigma') == approx((-1.571, 3.571), abs=0.001)
    assert a.naive_method('3-sigma') == approx((-3.032, 5.032), abs=0.001)

def test_log_ci_interval():
    a = LogCredibilityInterval(mean=5.127, variance=1.009, stdev=1.004, sample_size=40)
    assert a.naive_method(interval='95%') == approx((123.433, 230.049), abs=0.001)
    assert a.cox_method(interval='70%') == approx((227.699, 342.055), abs=0.001)
    assert a.cox_method(interval='95%') == approx((190.191, 409.511), abs=0.001)
    assert a.modified_cox_method(interval='95%') == approx((190.191, 409.511), abs=0.001)
    assert a.cox_method(interval='99%') == approx((168.630, 461.872), abs=0.001)
