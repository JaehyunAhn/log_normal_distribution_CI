# coding: utf-8
from math import log, exp
from statistics import mean, variance, stdev

class LogNormDistrib(object):
    """
    데이터 리스트를 받아 log normal distribution 형태로 정제하고
    각종 기초 통계를 반환하는 함수
    """
    def __init__(self, data):
        """
        :param data: 일반 관측치
        :type data: list
        """
        self.data = data
        self.ln_data = [log(x) for x in self.data]

    def __del__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def get_ln_list(self):
        return self.ln_data

    def get_mean(self):
        return mean(self.ln_data)

    def get_variance(self):
        return variance(self.ln_data)

    def get_stdev(self):
        return stdev(self.ln_data)

    def get_sample_size(self):
        return len(self.ln_data)


if __name__ == '__main__':
    # local test
    a = LogNormDistrib(data=[1,2,3,4])
    print(a.get_ln_list())
    print([exp(x) for x in a.get_ln_list()])
    print(a.get_mean())
    print(a.get_variance())
    print(a.get_stdev())
    print(a.get_sample_size())
