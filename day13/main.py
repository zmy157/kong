import unittest
from HTMLTestRunner import HTMLTestRunner

# 1.加载所有用例

tests = unittest.defaultTestLoader.discover(r"C:\Users\W540\PycharmProjects\pythonProject\day13",pattern="test*.py")


# 2.创建运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title="这是计算器的测试报告",
    description="这是计算器的算法测试报告",
    verbosity=1,#  写死
    stream = open(file="计算器的报告.html",mode="w+",encoding="utf-8")
)


# 3.让运行器运行测试用例
runner.run(tests)


# 任务1：
# 任务2：减法、乘法、除法
# 4.邮件发送附件代码：将报告统一使用代码发送给我   2431320433@qq.com

# 温馨提示：密码【授权码】








