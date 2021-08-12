


shop = [        ["lenovo PC",5000],
                ["Mac pc",12000],
                ["HUAWEI  WATCH PRO 20",2000],
                ["机械革命",15000],
                ["老干妈",7.5],
                ["卫龙辣条",3],
                ["西瓜",2]
                ]
shopping_cart = []


import random
youhuijuan = ['lenovo PC','lenovo PC','lenovo PC','lenovo PC','lenovo PC','lenovo PC','lenovo PC','lenovo PC','lenovo PC','lenovo PC',
              '老干妈优惠劵','老干妈优惠劵','老干妈优惠劵','老干妈优惠劵','老干妈优惠劵','老干妈优惠劵','老干妈优惠劵','老干妈优惠劵','老干妈优惠劵','老干妈优惠劵','老干妈优惠劵','老干妈优惠劵','老干妈优惠劵','老干妈优惠劵','老干妈优惠劵','老干妈优惠劵','老干妈优惠劵','老干妈优惠劵','老干妈优惠劵','老干妈优惠劵',
              'HUA WEI WATCH','HUA WEI WATCH','HUA WEI WATCH','HUA WEI WATCH','HUA WEI WATCH','HUA WEI WATCH','HUA WEI WATCH','HUA WEI WATCH','HUA WEI WATCH','HUA WEI WATCH','HUA WEI WATCH','HUA WEI WATCH','HUA WEI WATCH','HUA WEI WATCH','HUA WEI WATCH'
              ]
yhj = random.randint(0,44)
print("你获得的优惠券为：",youhuijuan[yhj])
if youhuijuan[yhj] == 'lenovo PC':
    a = 0.5
    s = 0
elif youhuijuan[yhj] == '老干妈优惠劵':
    a = 0.3
    s = 4
else:
    a = 0.8
    s = 3


salary = int(input('输入你的薪水:'))
m = salary
k = 0

while True:
    index = 0
    for goods in shop:
        print(index,goods)
        index += 1
    choice = input('>>>:').strip()
    if choice.isdigit():
        choice = int(choice)
        if choice >= 0 and choice < len(shop):
            goods = shop[choice]
            if goods[1] <= salary and choice == s:
                s = -99
                shopping_cart.append(goods)
                salary -= goods[1]*a
                print('添加商品 ' + str(goods[0]) + ' 进入购物车！您当前的余额:' + str(salary))
            elif goods[1] <= salary:
                shopping_cart.append(goods)
                salary -= goods[1]
                print('添加商品 '+str(goods[0])+' 进入购物车！您当前的余额:'+str(salary))

            else:
                print('钱不够！穷鬼！！！价格是:'+str(goods[1])+'! 需要更多:'+str(goods[1]-salary))
        else:
            print('没有，滚！！！！！！')
    elif choice == 'q':
        print('----------以下是您的购物小条，请拿好！！！！！----------')
        print('ID   商品   数量    单价   打折前总价')
        for i in range(len(shop)):
            j = shopping_cart.count(shop[i])
            if j > 0 :
                k += 1
                print(k,'\t',shop[i][0],'\t',j,'\t\t',shop[i][1],'\t',j * shop[i][1])
        print('打折后总价为：',m - salary)
        break
    else:
        print('对不起，您输入错误，别瞎弄！')