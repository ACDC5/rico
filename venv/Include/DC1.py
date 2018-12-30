import random

secret = random.randint(1,10)
print("-----------------第一个游戏实例------------------")
temp = input("请猜测一个数字:")#input接收外界输入的数据
guess = int(temp)
while guess != secret:
    if guess == secret:
        print("你猜中了")
        print("猜中了也没有奖励")
    else:
        if guess > secret:
            print("猜的数太大")
            temp = input("猜错了，请重新输入:")
            guess = int(temp)
        else:
            print("猜的数太小了")
            temp = input("猜错了，请重新输入:")
            guess = int(temp)

print("运气真鸡儿好,第一次就猜中了.so 游戏结束")

'''a = rico

b = rico

if a == b:
    print("不限制大小写")
else:
    print("区分大小写")
'''