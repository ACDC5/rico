#
# #生成器:生成器是迭代器的一种实现,生成器其实是一个特殊的迭代器
# ##协同程序,就是可以运行的独立函数调用,函数可以暂停或者挂起,并在需要的时候从程序离开的地方继续或者重新开始
# #
# def myGen():
#     print('生成器被执行')
#     yield 1 #yield相当于return关键字,当代码执行到此时,会将1返回给调用者,并在此行停止执行代码.这有别于普通函数
#     yield 2 #当重新获得控制权时,代码在这里开始被执行
#
# myg = myGen()
# print(next(myg))
#
# print(next(myg))# 第二次调用时myGen函数将被继续执行
#
# # print(printnext(myg)) # 第三次调用将抛出stopIteration异常,不存在第三次执行的机会
#
# for i in myGen(): #使用for循环将自动隐式的执行next方法
#     print(i)
#
# #在一个列表里面写一个for循环称为列表推导式
# a = [i for i in range(100) if not(i % 2) and i % 3] #一个列表推导式,得到能被2整除不能被3整除的数
# print(a)
#
# #字典推导式
# b = {i:i % 2 == 0 for i in range(10)} #查看10内被2整除的的结果
# print(b)
#
# #集合推导式
# c = {i for i in [1,1,2,2,3,3,4,4,5,5,6,6,7,7]}#集合不能存在重复元素,重复将被去除
# print(c)
#
# #元组推导式（生成器推导式）
# d = (i for i in range(15)) #变量d既是生成器对象
# print(d) #输出生成器对象
# print(next(d)) #...开始打印生成器中的值
# for v in d:
#     print(v) #将自动调用next函数输出生成器d的所有值
#
# #当生成器作为函数的参数时
# mySum = sum(i for i in range(10) if i % 2) #sum需传入一个迭代器对象...得到的值将自动相加