from unittest import TestCase
from Calc import Calc
class TestCalc(TestCase):

    def testAdd1(self):
        # 1.
        a = 5
        b = 6
        c = 30

        # 2.调用方法，得到实际结果
        calc = Calc()
        chen = calc.multi(a,b)

        # 3.断言
        self.assertEqual(c,chen)

    def testAdd2(self):
        # 1.
        a = -5
        b = -6
        c = 30

        # 2.调用方法，得到实际结果
        calc = Calc()
        chen = calc.multi(a,b)

        # 3.断言
        self.assertEqual(c,chen)
    def testAdd3(self):
        # 1.
        a = -5
        b = 6
        c = -30

        # 2.调用方法，得到实际结果
        calc = Calc()
        chen = calc.multi(a,b)

        # 3.断言
        self.assertEqual(c,chen)

    def testAdd4(self):
        # 1.
        a = 5
        b = -6
        c = -30

        # 2.调用方法，得到实际结果
        calc = Calc()
        chen = calc.multi(a,b)

        # 3.断言
        self.assertEqual(c,chen)


    def testAdd5(self):
        # 1.
        a = 50000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        b = 6
        c = 300000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

        # 2.调用方法，得到实际结果
        calc = Calc()
        chen = calc.multi(a,b)

        # 3.断言
        self.assertEqual(c,chen)