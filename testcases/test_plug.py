#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import pytest
import random
class TestPlug:

    @pytest.mark.parametrize("x,y", [
            (3 + 5, 9),
            (2 + 4, 6),
            (6 * 9, 42),
            ("testerhome", "testerhome"),
        ])
    def test_add(self, x, y):
        assert x == y

    def add(self, x, y):
        return x + y


    @pytest.mark.flaky(reruns=5)
    # 重新运行失败的测试用例；
    def test_add2(self):
        random_value = random.randint(2, 6)
        print("random_value:" + str(random_value))
        assert self.add(1, 3) == random_value

    @pytest.mark.run(order=2)
    def test_one(self):
        print("第二个执行")
        assert True

    @pytest.mark.run(order=1)
    def test_two(self):
        print("\n第一个执行")
        assert True



