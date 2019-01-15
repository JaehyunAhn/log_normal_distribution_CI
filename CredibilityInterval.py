# coding: utf-8
from math import sqrt, exp
from scipy.stats import t, norm
from ci import CONFIDENCE

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

    def _p2f(self, x):
        """
        Convert sting to float, example: x='95%', returns float 0.95.
        :type x: str
        :return:
        """
        return float(x.strip('%')) / 100

    def _normal_form(self, variate):
        """
        CI for normal distribution = mean +- z * sqrt(stdev/n)
        :param variate:
        :return:
        """
        norm = self.mean
        vari = variate * sqrt(self.variance / self.sample_size)
        return (norm - vari, norm + vari)

    def get_variate(self, interval, sample_size=None):
        """
        interval is string
        :param interval: 1-sigma, 1/2/3-sigma, 50 ~ 95% CI
        :type sample_size: int
        :type interval: str
        :type return: float
        :return: variance number
        """
        # get confidence
        confidence = CONFIDENCE.get(interval)
        if confidence is None:
            confidence = self._p2f(x=interval)

        # if No sample size then z-score, else t-score
        if sample_size is None:
            variate = norm.ppf((1 + confidence) / 2)
        else:
            variate = t.ppf((1 + confidence) / 2, sample_size - 1)

        return variate

    def naive_method(self, interval=None):
        if interval is None:
            interval = '95%'
        variate = self.get_variate(interval)
        return self._normal_form(variate)



class LogCredibilityInterval(CredibilityInterval):
    """
    신뢰구간을 리턴
    one-tail: lower limit
    two-tails: upper limit
    """
    def __init__(self, log_mean, log_variance, sample_size, stdev=None):
        super().__init__(mean=log_mean, variance=log_variance, sample_size=sample_size, stdev=stdev)

    def _cox_form(self, variate):
        """
        CI for log(theta) = mean + stdev/2 +- z * sqrt(stdev/n + stdev^2/2(n-1)
        :param variate:
        :return:
        """
        norm = self.mean + self.variance / 2
        vari = variate * sqrt(self.variance / self.sample_size + (self.variance)**2 / (2 * (self.sample_size - 1)))
        return (norm - vari, norm + vari)

    def _get_exp(self, tp):
        return (exp(tp[0]), exp(tp[1]))

    def naive_method(self, interval=None):
        return self._get_exp(super(LogCredibilityInterval, self).naive_method(interval))

    def cox_method(self, interval=None):
        """
        Land (1971)
        :return:
        """
        if interval is None:
            interval = '1-sigma'
        variate = self.get_variate(interval)
        return self._get_exp(self._cox_form(variate))

    def modified_cox_method(self, interval=None):
        """
        Zhou and Gao (1997)
        :return:
        """
        if interval is None:
            interval = '1-sigma'
        variate = self.get_variate(interval, sample_size=self.sample_size)
        return self._get_exp(self._cox_form(variate))


if __name__ == '__main__':
    a = LogCredibilityInterval(log_mean=5.127, log_variance=1.009, sample_size=40, stdev=1.004)
    print(a.naive_method('95%'))
    print(a.cox_method('95%'))
    print(a.modified_cox_method('95%'))
