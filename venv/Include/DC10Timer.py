import time as t

# couuerTime = t.localtime()# 以元组的形式返回当前时间
# print(couuerTime)
#  #实现一个计时器v1
# class MyTimer():
#     #计时开始
#     def start(self):
#         self.activate = t.localtime() #以元组的形式返回当前时间的年月日...等格式
#         print('计时开始...')
#
#     #计时结束
#     def end(self):
#         self.stop = t.localtime()
#         self._calc() #计时结束时调用内部方法计算运行的持续时间
#         print('计时结束...')
#
#     #内部方法,计算运行时间
#     def _calc(self):# self代表传入的实例对象
#         self.lasted = [] #定义列表存放运行持续时间000000分别代表了年月日时分秒
#         self.prompt = '总共运行了' #存储累加的时间
#         for index in range(6): #下标从0开始,所以迭代只到5.因为函数localtime返回的是年月日时分秒毫秒等...但案例只需要运算到秒的的数据,所以只循环6次,即取包含秒之前的时间单位数据来运算
#             self.lasted.append(self.stop[index] - self.activate[index]) #第一次循环时用结束时间的第0下标(即年份)和开始时间的第0下标(年份)时间相减,一直循环到秒的下标位置为止
#             self.prompt += str(self.lasted[index]) #将每次相减的时间累加到一起
#
#         print(self.prompt) #输出持续时间
#
# t1 = MyTimer()
#
# t1.start()
# t1.end()

# #v2优化
# class MyTimerV2():
#     def __str__(self): #该魔法方法一般使类的实例以字符打印(当前案例是返回实例的一个属性)，或者自己定义输出。
#         return self.prompt
#
#     __repr__ = __str__
#     #计时开始
#     def start(self):
#         self.activate = t.localtime() #以元组的形式返回当前时间的年月日...等格式
#         print('计时开始...')
#
#     #计时结束
#     def end(self):
#         self.stop = t.localtime()
#         self._calc() #计时结束时调用内部方法计算运行的持续时间
#         print('计时结束...')
#
#     #内部方法,计算运行时间
#     def _calc(self):# self代表传入的实例对象
#         self.lasted = [] #定义列表存放运行持续时间000000分别代表了年月日时分秒
#         self.prompt = '总共运行了' #存储累加的时间
#         for index in range(6): #下标从0开始,所以迭代只到5.因为函数localtime返回的是年月日时分秒毫秒等...但案例只需要运算到秒的的数据,所以只循环6次,即取包含秒之前的时间单位数据来运算
#             self.lasted.append(self.stop[index] - self.activate[index]) #第一次循环时用结束时间的第0下标(即年份)和开始时间的第0下标(年份)时间相减,一直循环到秒的下标位置为止
#             self.prompt += str(self.lasted[index]) #将每次相减的时间累加到一起
#
# t2 = MyTimerV2()
# t2.start()
# t2.end()
# print(t2) #当end方法没有被调用时将错误,prompt属性还未被定义,在执行了end方法后才会被定义.解决方法,所有属于实例对象的属性都可以定义在__init__方法中 参照v3


##v3优化
# class MyTimerV3():
#
#     #所以属于实例对象的属性都可以定义在__init__方法中
#     def __init__(self):
#         self.prompt = '未开始计时'
#         self.lasted = []
#         self.activate = 0
#         # self.stop = 0 #此属性名和stop方法重名了,同名函数将无法调用
#         self.end = 0 #新定义end属性以代替stop属性,同时需要将代码中用到stop属性的地方换成end属性
#
#     def __str__(self): #该魔法方法一般使类的实例以字符打印(当前案例是返回实例的一个属性)，或者自己定义输出。
#         return self.prompt
#
#     __repr__ = __str__
#     #计时开始
#     def start(self):
#         self.activate = t.localtime() #以元组的形式返回当前时间的年月日...等格式
#         print('计时开始...')
#
#     #计时结束
#     def stop(self):
#         self.end = t.localtime()
#         self._calc() #计时结束时调用内部方法计算运行的持续时间
#         print('计时结束...')
#
#     #内部方法,计算运行时间
#     def _calc(self):# self代表传入的实例对象
#         self.lasted = [] #定义列表存放运行持续时间000000分别代表了年月日时分秒
#         self.prompt = '总共运行了' #存储累加的时间
#         for index in range(6): #下标从0开始,所以迭代只到5.因为函数localtime返回的是年月日时分秒毫秒等...但案例只需要运算到秒的的数据,所以只循环6次,即取包含秒之前的时间单位数据来运算
#             self.lasted.append(self.end[index] - self.activate[index]) #第一次循环时用结束时间的第0下标(即年份)和开始时间的第0下标(年份)时间相减,一直循环到秒的下标位置为止
#             self.prompt += str(self.lasted[index]) #将每次相减的时间累加到一起
#
# t3 = MyTimerV3()
# print(t3)
# t3.start()
# t3.stop()#报int对象不能被调用错误.当被调用的函数名和属性名相同时,属性会覆盖方法
# print(t3)

#v4优化 优化点,只显示值不为0的时间和时间单位和增加温馨提示、让两个计时器的对象相加,返回相加值
class MyTimerV4():

    #所有属于实例对象的属性都可以定义在__init__方法中
    def __init__(self):
        self.unit = ['年','月','天','时','分','秒']
        self.prompt = '未开始计时'
        self.lasted = []
        self.activate = 0
        # self.stop = 0 #此属性名和stop方法重名了,同名函数将无法调用
        self.end = 0 #新定义end属性以代替stop属性,同时需要将代码中用到stop属性的地方换成end属性

    def __str__(self): #该魔法方法一般使类的实例以字符打印(当前案例是返回实例的一个属性)，或者自己定义输出。
        return self.prompt

    __repr__ = __str__

    def __add__(self,other):#当两个对象相加时会自动调用此魔法方法
        prompt = '两计时器值相加总共运行了' #这里的prompt时局部变量,不是来自实例对象的变量
        result = []
        for idx in range(6):
            result.append(self.lasted[idx] + other.lasted[idx]) #左边对象的值加右边对象的值
            if result[idx]: #等于True,即不为0时
                prompt += (str(result[idx] + self.unit[idx]))
        return prompt

    #计时开始
    def start(self):
        self.activate = t.localtime() #以元组的形式返回当前时间的年月日...等格式
        self.prompt = '提示,请先调用stop() 停止计时' #当在没有调用stop函数时试图打印实例对象时 给出此提示
        print('计时开始...')

    #计时结束
    def stop(self):
        if not self.activate:
            print('提示,请先调用start()方法以启动计时')
        else:
            self.end = t.localtime()
            self._calc() #计时结束时调用内部方法计算运行的持续时间
            print('计时结束...')

    #内部方法,计算运行时间
    def _calc(self):# self代表传入的实例对象
        self.lasted = [] #定义列表存放运行持续时间000000分别代表了年月日时分秒
        self.prompt = '总共运行了' #存储累加的时间
        for index in range(6): #下标从0开始,所以迭代只到5.因为函数localtime返回的是年月日时分秒毫秒等...但案例只需要运算到秒的的数据,所以只循环6次,即取包含秒之前的时间单位数据来运算
            self.lasted.append(self.end[index] - self.activate[index]) #第一次循环时用结束时间的第0下标(即年份)和开始时间的第0下标(年份)时间相减,一直循环到秒的下标位置为止
            if self.lasted[index] != 0:
                 self.prompt += str(self.lasted[index]) + self.unit[index]#将每次相减的时间累加到一起,同时加上对应的单位
            #为下一轮计时初始化变量
        self.activate = 0
        self.end = 0

t4 = MyTimerV4()
t4.start()
t4.stop()
print(t4) #有时候会出现总共1分-30秒这种情况-30的出现是因为:例如,开始时间时2010-11-16 10:09:50,结束时间2015-10-01 12:11:30即结束时间减开始时间=3年-1月-15日 -2小时...

##是对象相加,算出总时间数
t4v1 = MyTimerV4()
t4v1.start()
t4v1.stop()
t4 + t4v1


