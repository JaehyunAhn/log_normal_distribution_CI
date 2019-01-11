# coding: utf-8
from math import sqrt, exp

from ci import Z_VALUE, T_VALUE, SIGMAS, INDICES

class CredibilityInterval(object):
    def __init__(self, mean, variance, sample_size, stdev=None):
        self.mean = mean
        self.variance = variance
        if sample_size <= 0:
            raise ValueError
        self.sample_size = sample_size
        if stdev is None:
            self.stdev = sqrt(self.variance)
        else:
            self.stdev = stdev

    def __del__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def _normal_form(self, variate):
        """
        CI for normal distribution = mean +- z * sqrt(stdev/n)
        :param variate:
        :return:
        """
        norm = self.mean
        vari = variate * sqrt(self.variance / self.sample_size)
        return (norm - vari, norm + vari)

    def _cox_form(self, variate):
        """
        CI for log(theta) = mean + stdev/2 +- z * sqrt(stdev/n + stdev^2/2(n-1)
        :param variate:
        :return:
        """
        norm = self.mean + self.variance / 2
        vari = variate * sqrt(self.variance / self.sample_size + (self.variance)**2 / (2 * (self.sample_size - 1)))
        return (norm - vari, norm + vari)

    def get_variate(self, interval, z_value=False):
        """
        interval is string
        :type interval: str
        :param interval: 1-sigma, 1/2/3-sigma, 50 ~ 95% CI
        :type return: float
        :return: variance number
        """
        if SIGMAS.get(interval) is not None:
            index = INDICES.get(SIGMAS.get(interval))
        elif INDICES.get(interval):
            index = INDICES.get(interval)
        else:
            # exception, no interval found
            raise ValueError
        if z_value or self.sample_size > 31:
            return Z_VALUE[index]
        # 샘플 개수에 맞는 T-Value 리턴
        quotient = int((self.sample_size - 1) / 5)
        if quotient == 0:
            quotient = 1
        return T_VALUE[quotient * 5][index]

    def naive_method(self, interval=None):
        if interval is None:
            interval = '95%'
        variate = self.get_variate(interval)
        return self._normal_form(variate)

    def cox_method(self, interval=None):
        """
        Land (1971)
        :return:
        """
        if interval is None:
            interval = '1-sigma'
        variate = self.get_variate(interval, z_value=True)
        return self._cox_form(variate)

    def modified_cox_method(self, interval=None):
        """
        Zhou and Gao (1997)
        :return:
        """
        if interval is None:
            interval = '1-sigma'
        variate = self.get_variate(interval)
        return self._cox_form(variate)



class LogCredibilityInterval(CredibilityInterval):
    """
    신뢰구간을 리턴
    one-tail: lower limit
    two-tails: upper limit
    """
    def __init__(self, mean, variance, sample_size, stdev=None):
        super().__init__(mean=mean, variance=variance, sample_size=sample_size, stdev=stdev)

    def naive_method(self, interval=None):
        return self._get_exp(super(LogCredibilityInterval, self).naive_method(interval))

    def cox_method(self, interval=None):
        return self._get_exp(super(LogCredibilityInterval, self).cox_method(interval))

    def modified_cox_method(self, interval=None):
        return self._get_exp(super(LogCredibilityInterval, self).modified_cox_method(interval))

    def _get_exp(self, tp):
        return (exp(tp[0]), exp(tp[1]))


if __name__ == '__main__':
    a = LogCredibilityInterval(mean=5.127, variance=1.009, sample_size=40, stdev=1.004)
    print(a.naive_method('95%'))
    print(a.cox_method('95%'))
    print(a.modified_cox_method('95%'))
