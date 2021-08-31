from unittest import TestCase
from Calc import Calc
class TestCalc(TestCase):

    def testAdd1(self):
        # 1.
        a = 6
        b = 6
        c = 1

        # 2.调用方法，得到实际结果
        calc = Calc()
        chu = calc.devision(a,b)

        # 3.断言
        self.assertEqual(c,chu)

    def testAdd2(self):
        # 1.
        a = -6
        b = -6
        c = 1

        # 2.调用方法，得到实际结果
        calc = Calc()
        chu = calc.devision(a,b)

        # 3.断言
        self.assertEqual(c,chu)
    def testAdd3(self):
        # 1.
        a = -6
        b = 6
        c = -1

        # 2.调用方法，得到实际结果
        calc = Calc()
        chu = calc.devision(a,b)

        # 3.断言
        self.assertEqual(c,chu)

    def testAdd4(self):
        # 1.
        a = 6
        b = -5
        c = -1.2

        # 2.调用方法，得到实际结果
        calc = Calc()
        chu = calc.devision(a,b)

        # 3.断言
        self.assertEqual(c,chu)


    def testAdd5(self):
        # 1.
        a = 3000
        b = 6
        c = 500

        # 2.调用方法，得到实际结果
        calc = Calc()
        chu = calc.devision(a,b)

        # 3.断言
        self.assertEqual(c,chu)