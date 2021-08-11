'''
    猜数字：
        需求：系统随机产生一个数字，让用户从键盘输入您要的数字。(0~10000)
            1.如果猜中，则恭喜
            2.如果猜的数字比系统的数字大，温馨提示：大了
            3.如果猜小了，温馨提示：小了。
            一直到用户猜中为止。
        技术选型：
            1.random
            2.input
            3.if....else
            4.while
    金币功能：
        0.先登录，若登陆成功！
        1.玩家初始化5000硬币，猜错扣500,金币不够，系统锁定。
        2.猜中，奖励10000硬币，是否进行第二轮游戏。
'''
u=1121
m=1121
import random
while True:
    name = int(input("请输入用户名："))
    password = int(input("请输入密码："))
    if name == u and password == m:
        print("登录成功")
        break
    else:
        print("登录失败")
import random
num = random.randint(0,5)
count = 0
qi = 5000
cuo = -500

while True:
    if qi > 0:
            count = count + 1
            chose = input("亲输入您要的猜的数字：")
            chose = int(chose)
            if chose > num:
                qi = qi + cuo
                print("大了！","剩余",qi,)
            elif chose < num:
                qi = qi + cuo
                print("小了！","剩余",qi,)
            else:
                num = random.randint(0, 5)
                qi = qi+10000
                print("恭喜，您猜中了，本次数字为：",num,"，您本次输入了",count,"次！","剩余",qi,)

    else:
        print("GG")
        break

