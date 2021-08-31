'''
    单元测试：
        unittest
    1.导入unittest  TestCase
    2.正常写测试方法
        必须test开头



'''
from unittest import TestCase
from Calc import Calc
class TestCalc(TestCase):

    def testAdd1(self):
        # 1.
        a = 5
        b = 6
        c = 11

        # 2.调用方法，得到实际结果
        calc = Calc()
        sum = calc.add(a,b)

        # 3.断言
        self.assertEqual(c,sum)

    def testAdd2(self):
        # 1.
        a = -5
        b = -6
        c = -11

        # 2.调用方法，得到实际结果
        calc = Calc()
        sum = calc.add(a,b)

        # 3.断言
        self.assertEqual(c,sum)
    def testAdd3(self):
        # 1.
        a = -5
        b = 6
        c = 1

        # 2.调用方法，得到实际结果
        calc = Calc()
        sum = calc.add(a,b)

        # 3.断言
        self.assertEqual(c,sum)

    def testAdd4(self):
        # 1.
        a = 5
        b = -6
        c = -1

        # 2.调用方法，得到实际结果
        calc = Calc()
        sum = calc.add(a,b)

        # 3.断言
        self.assertEqual(c,sum)


    def testAdd5(self):
        # 1.
        a = 50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        b = 6
        c = 50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000006

        # 2.调用方法，得到实际结果
        calc = Calc()
        sum = calc.add(a,b)

        # 3.断言
        self.assertEqual(c,sum)


























