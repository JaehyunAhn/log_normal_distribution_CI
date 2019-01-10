# coding: utf-8

class Observations(object):
    """
        로그 데이터가 들어왔을 때 정제하는 클래스
    """
    def __init__(self, log):
        self.log = log

    def __del__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def get_intervals(self):
        """
        log data 로부터 interval 리스트를 반환
        :type return: list
        :return: 데이터 인터벌
        """
        return_list = list()
        return return_list


if __name__ == '__main__':
    pass
