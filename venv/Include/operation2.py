print("********************作业******************")

#
print("********请你猜数字**********")

value = input("请你输入要猜的数字:")

number = int(value)

if number >= 1 and number <= 100:
    print("你猜对了")
else:
    print("你猜错了")

print('over')