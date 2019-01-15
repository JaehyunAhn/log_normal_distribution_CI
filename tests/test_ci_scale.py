# coding: utf-8
from pytest import approx
from CredibilityInterval import CredibilityInterval, LogCredibilityInterval

def test_ci_interval():
    a = CredibilityInterval(mean=1, variance=4, sample_size=4)
    assert a.naive_method('70%') == approx((-0.036, 2.036), abs=0.001)
    assert a.naive_method('95%') == approx((-0.959, 2.959), abs=0.001)
    assert a.naive_method('99%') == approx((-1.575, 3.575), abs=0.001)
    assert a.naive_method('1-sigma') == approx((0.0, 1.999), abs=0.001)
    assert a.naive_method('2-sigma') == approx((-0.999, 2.999), abs=0.001)
    assert a.naive_method('3-sigma') == approx((-1.999, 3.999), abs=0.001)

def test_log_ci_interval():
    a = LogCredibilityInterval(log_mean=5.127, log_variance=1.009, stdev=1.004, sample_size=40)
    assert a.naive_method(interval='95%') == approx((123.434, 230.048), abs=0.001)
    assert a.cox_method(interval='70%') == approx((227.858, 341.816), abs=0.001)
    assert a.cox_method(interval='95%') == approx((190.193, 409.509), abs=0.001)
    assert a.modified_cox_method(interval='95%') == approx((187.873, 414.565), abs=0.001)
    assert a.cox_method(interval='99%') == approx((168.603, 461.947), abs=0.001)
