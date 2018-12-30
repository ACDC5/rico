
# #魔法方法-定义序列
# # 协议与其他编程语言中接口很相似,它规定你哪些方法必须要定义.然而,在
# # python中的协议就显得那么不正式.事实上,在python协议更像是一种指南/建议
# # 容器类型的协议:
# # 	1 当希望定义的容器是不可变的化,只需要定义__len__()和__getitem__()方法
# #   2 当希望定制的容器是可变的话,除了__len__()和__getitem__()方法,还需定义__setitem__()和__delitem__()两个方法
#
# #需求,编写一个不可改变的自定义列表,要求记录列表中每个元素被访问的次数
# class MyList:
#     def __init__(self,*args):
#         self.values = [x for x in args] #每循环一次args得到的值赋值给x,x会赋值给values
#         self.count = {}.fromkeys(range(len(self.values)),0) # fromkeys() 函数用于创建一个新字典，以参数1中元素做字典的键，参数2(可选)为字典所有键对应的初始值
#
#     def __len__(self):
#         return len(self.values)
#
#     def __getitem__(self, item): #每访问一次元素,将该元素的key+1以累加访问该元素的数量.可以理解为对对象的的循环
#         self.count[item] += 1
#         return self.values[item]
#
# c1 = MyList(2,4,6,8,10)
# c2 = MyList(1,3,5,7,9)
# print(c1[0]) #访问下标所在的元素
# print(c1[0])
# print(c1.count) #查看各元素被访问的次数
#
# print(c2[3],c2[3])
# print(c2.count)

#-----------------------------------------------------------------------
# #迭代器,每一次重复的过程即迭代,每一次迭代得到结果将为下一次迭代的初始值
# class Fibs:
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.a,self.b = self.b,self.a + self.b #赋值规则,在等于号两边,逗号左边的赋值给左边的值,依次类推
#         return self.a
#
# fi = Fibs()
# for each in fi:
#     if each <= 20: #只打印20以内的斐波那契数列,以避免死循环
#         print(each)
#     else:
#         break
#
# #避免死循环的方式2
# class FibsV2:
#     def __init__(self,n=20):#设置默认的循环得到的数值不超过20
#         self.a = 0
#         self.b = 1
#         self.m = n
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.a,self.b = self.b,self.a + self.b #赋值规则    ,在等于号两边,逗号左边的赋值给左边的值,依次类推
#         if self.a > self.m:
#             raise StopIteration #当超过指定数值时产生一个异常
#         return self.a
#
## fi2 = FibsV2(100)
# for each in fi2:
#     print(each)



