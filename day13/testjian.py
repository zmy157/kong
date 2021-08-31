from unittest import TestCase
from Calc import Calc
class TestCalc(TestCase):

    def testAdd1(self):
        # 1.
        a = 5
        b = 6
        c = -1

        # 2.调用方法，得到实际结果
        calc = Calc()
        jian = calc.subs(a,b)

        # 3.断言
        self.assertEqual(c,jian)

    def testAdd2(self):
        # 1.
        a = -5
        b = -6
        c = 1

        # 2.调用方法，得到实际结果
        calc = Calc()
        jian = calc.subs(a,b)

        # 3.断言
        self.assertEqual(c,jian)
    def testAdd3(self):
        # 1.
        a = -5
        b = 6
        c = -11

        # 2.调用方法，得到实际结果
        calc = Calc()
        jian = calc.subs(a,b)

        # 3.断言
        self.assertEqual(c,jian)

    def testAdd4(self):
        # 1.
        a = 5
        b = -6
        c = 11

        # 2.调用方法，得到实际结果
        calc = Calc()
        jian = calc.subs(a,b)

        # 3.断言
        self.assertEqual(c,jian)


    def testAdd5(self):
        # 1.
        a = 50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        b = 6
        c = 49999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999994

        # 2.调用方法，得到实际结果
        calc = Calc()
        jian = calc.subs(a,b)

        # 3.断言
        self.assertEqual(c,jian)