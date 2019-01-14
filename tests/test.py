# coding: utf-8
import os
import time
from math import log, exp
from statistics import mean, variance

from CredibilityInterval import LogCredibilityInterval

if __name__ == '__main__':
    stop = 0.01
    interval = '1-sigma'
    current_path = os.path.dirname(os.path.realpath(__file__))
    data_file = os.path.join(current_path, '../external_files/dummy.txt')

    # functional test
    with open(data_file, 'r') as file:
        data = [int(line.rstrip()) for line in file]
        u_outlier = 0
        o_outlier = 0
        for i in range(1, len(data)):
            cur_data = [log(x) for x in data[:i]]
            m = mean(cur_data)
            # variance requires at least two data points
            if len(cur_data) >= 2:
                var = variance(cur_data)
                lci = LogCredibilityInterval(log_mean=m, log_variance=var, sample_size=len(cur_data))
                (one_tail, two_tails) = lci.modified_cox_method(interval=interval)

                current = cur_data[-1]
                int_current = round(exp(current))
                result = 'Current:\t{}\t\t({:.2f} < x < {:.2f})\t'.format(int_current, one_tail, two_tails)
                if one_tail > int_current:
                    result += 'under outlier!'
                    u_outlier += 1
                elif two_tails < int_current:
                    result += 'over outlier!'
                    o_outlier += 1
                print('{}'.format(result))
            time.sleep(stop)
        print('{}/{} (outliers: {}, {})'.format(u_outlier + o_outlier, len(data), u_outlier, o_outlier))
