'''
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？'''
def demo1():

    arr = []
    for i in range(1,5):
        for k in range(1,5):
            for j in range(1,5):
                if i != j and j != k and i != k:  # 确保三个数字互不相同
                    num = 100*i + 10*k+j
                    arr.append(num)
        print(len(arr),arr)
# 2
def demo2():
    profit = int(input("净利润: "))
    bound = [100000,200000,400000,600000,1000000]
    ratio = [0.1, 0.075,0.05, 0.03, 0.015, 0.01]
    bonus = 0  # 初始化奖金

    for i in range(len(bound)):
        if profit <= bound[i]:
            bonus += profit * ratio[i]
            break
        else:
            bonus += bound[i] * ratio[i]
            if i == len(bound) -1:
                bonus += (profit - bound[i]) * ratio[i+1]
    print(f"应发放奖金总数为：{bonus}元")

def demo3():
    import time
    data = input("请输入时间：例如2023-09-14 ：")
    str = time.strptime(data,'%Y-%m-%d')
    num = str.tm_yday
    print(num)
def demo4():
    arr = []
    input_str = input("请输入三个整数，以空格分隔：")
    for num in  input_str.split():
        arr.append(int(num))
    arr.sort()
    print(arr)
def demo5():
    a = [1,2,3]
    b= [4,5,6]
    b += a
    print(b)

def demo6():
    for i in range(1,10):
        for j in range(1,i+1) :
            print(f"{i} x {j} = {i *j}",end="\t")
        print()

def demo7():
    '''
    其实这道题就是斐波那契数列的由来。
    【个人备注】：理清思路是关键，理解成满两个月后，每月都能生兔子，就好办了。
    '''
    # 初始月份
    months = 12

    # 初始化第1个月和第2个月的兔子数量
    first_month = 1
    second_month = 1

    # 输出前两个月的兔子数量
    print("第1个月的兔子总数：", first_month)
    print("第2个月的兔子总数：", second_month)

    # 计算从第3个月到第12个月的兔子数量
    for i in range(3, months + 1):
        # 计算当前月份的兔子数量
        current_month = first_month + second_month

        # 输出当前月份的兔子数量
        print(f"第{i}个月的兔子总数：", current_month)

        # 更新前两个月的兔子数量
        first_month = second_month
        second_month = current_month

def demo8():
    def is_prime(number):
        if number <= 1:
            return False
        if number == 2 :
            return True
        if number % 2 == 0:
            return False
        for i in range(3, int(number * 0.5)+1,2):
            if number % i == 0:
                return False
        return True

    prime_numbers = []
    for num in range(101, 201):
        if is_prime(num):
            prime_numbers.append(num)

    # 输出素数的数量和所有素数
    print(f"101-200之间的素数数量为：{len(prime_numbers)}")
    print("这些素数为：", prime_numbers)
def demo9():
    for i in range(100,1000):
        b = i // 100
        s = (i // 10) % 10
        g = i % 10
        sum_of_cubes = b ** 3 + s ** 3 + g ** 3

        # 如果立方和等于原数字，则为水仙花数，输出
        if sum_of_cubes == i:
            print(i)
def demo10():
    total = 0
    m = 100  # 第一次落地，经过了一百米
    total += m
    for i in range(10 - 1):  # 之后9次弹起到落地
        m = m / 2  # 弹起的高度
        total += 2 * m  # 弹起然后重新落地，一共经过的距离
    print(total)
    print(m / 2)
def demo11():
    s,t=0,1
    for n in range(1,21):
        t*=n
        s+=t
    print(s)

def demo12():
    arr = [2]
    for i in range(3,100):
        for j in arr:
            if i%j == 0:
                break
        else:
            arr.append(i)
    print(arr)

def demo13():
    aaa = [1,5,8,14,28,39,60,89,134,324,612,900]
    b = [55,555]
    # 将 b 按数字顺序插入到 aaa 中
    for item in b:
        for i, num in enumerate(aaa):
            if item < num:
                aaa.insert(i, item)
                break
        else:
            aaa.append(item)

    # 输出合并后的列表 aaa
    print(aaa)


