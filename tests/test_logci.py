# coding: utf-8
from pytest import approx, mark

from CredibilityInterval import LogCredibilityInterval

@mark.xfail(raises=ValueError)
def test_ci_error():
    LogCredibilityInterval(log_mean=1, log_variance=4, sample_size=-4)
    LogCredibilityInterval(log_mean=1, log_variance=4, sample_size=0)


def test_stat_value():
    a = LogCredibilityInterval(log_mean=1, log_variance=4, sample_size=4)
    assert a.mean == 1
    assert a.variance == 4.0
    assert a.stdev == 2.0
    assert a.sample_size == 4


def test_ci_string():
    a = LogCredibilityInterval(log_mean=1, log_variance=4, sample_size=1)
    assert a.get_variate('1-sigma') == approx(0.999, abs=0.001)
    assert a.get_variate('2-sigma') == approx(1.999, abs=0.001)
    assert a.get_variate('3-sigma') == approx(2.999, abs=0.001)
