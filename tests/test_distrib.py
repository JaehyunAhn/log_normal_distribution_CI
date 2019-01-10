# coding: utf-8
from pytest import approx

from Distrib import LogNormDistrib, NormalDistrib

def test_normaldist():
    a = NormalDistrib(data=[1, 2, 3, 4])
    assert a.get_sample_size() == 4
    assert a.get_mean() == 2.5
    assert a.get_variance() == approx(1.67, abs=0.01)
    assert a.get_stdev() == approx(1.29, abs=0.01)

def test_lognormaldist():
    a = LogNormDistrib(data=[1, 2, 3, 4])
    assert a.get_sample_size() == 4
    assert a.get_mean() == approx(0.794, abs=0.001)
    assert a.get_variance() == approx(0.361, abs=0.001)
    assert a.get_stdev() == approx(0.601, abs=0.001)
