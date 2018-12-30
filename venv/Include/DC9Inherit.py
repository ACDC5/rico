
# #继承
# #语法ClassName(父类),子类可继承父类所有属性和方法
# class Parent:
#     def hello(self):
#         print('正在调用父类的方法...')
#
# class Child(Parent):
#     pass
#
# c = Child()
# print(c.hello())#子类正在调用父类中的方法
#
# #如果子类中定义了和父类同名的方法或属性,则会自动覆盖父类对应的方法或属性(又和java一样..)
# class Child2(Parent):
#     def hello(self):
#         print('我是子类的hello方法(子类的方法将覆盖父类中同名的方法)')
#         pass
#
# c2 = Child2()
# print(c2.hello())
#
# p = Parent()#父类的实例对象
# print(p.hello())
#
# #多重继承:
#
#
# #组合,当某些事物不存在继承关系或直线关系时(如鱼和龟),可以使用继承将它们整合到一起
# class Turtle: #龟类
#     def __init__(self,x):
#         self.num = x
#
# class Fish: #鱼类
#     def __init__(self,x):
#         self.num = x
#
# class Pool:
#     def __init__(self,x,y):
#         self.turtle = Turtle(x)#所谓组合就是把其他类的实例放在另一个类中
#         self.fish = Fish(y)
#
#     def myPrint(self):
#         print('水池里共有乌龟%d只，鱼%d条~'%(self.turtle.num,self.fish.num))
#
#
# pool = Pool(1,10)
# print(pool.myPrint())

# #类、类对象和实例对象
# class Z: #类在定义完后就是一个对象,可以直接使用,比如用 类名.属性名调用类的方法或属性
#          #类的属性和类对象是相互绑定的,并不会依赖实例对象(所以当实例对象改变时并不会影响类对象的值,反过来亦然)
#     # 类中定义属性的都是静态的(相当于java中static)
#     count = 0
#
# a = Z()#创建一个Z类的实例对象引用为a
# b = Z()
# c = Z()
#
# print(a.count,b.count,c.count)
# c.count += 10#给c的实例对象赋值,实例对象的值将覆盖类对象的值(同时实例对象的值将不会影响类对象的值,因为这里的count是属于c的实例对象的(总结:实例对象只改变自身))
# print(c.count)
#
# Z.count += 101 #使用类对象
# print(Z.count)#使用类对象调用类的属性
#
# print(a.count,b.count,c.count) #因为实例对象的的值会覆盖类对象的值,所以c.count输出的是实例对象的值
#
# #类定义                Z #定义一个类Z
# #类对象                Z #当定义晚一个类Z后,Z即为类对象
# #实例对象             abc #当创建多个Z的实例对象时,每个实例对象的引用只对自己的世界负责

# #如果属性的名称和方法名称一样,属性将覆盖方法(教材Python3.4?)
# class Z1:
#     def xValue(self):
#         print('X-man')
#
# y = Z1()
# print(y.xValue)#等同于在y的实例中定义了一个xValue的属性.但虽然和方法同名,但并没有和教材中一样出现错误,可能版本不同
# print(y.xValue())#

# #绑定
# #python要求方法需要有实例才能被调用,这种限制其实就是python所谓的绑定概念
# class BB:
#     def printBB(): #这样写是错的(没有self),但为了演示...
#         print('no zuo no die')
#
# BB.printBB()#可以调用成功
#
# bb = BB()
# bb.printBB()#当用BB的实例对象去调用时将报错,此行代码正常时这样执行的:bb.printBB(bb),默认将引用bb传入.但因为printBB方法没有self参数,无法接收bb引用,所以报错

# class CC:
#     def setXY(self,x,y):
#         self.x = x
#         self.y = y
#
#     def printXY(self):
#         print(self.x,self.y)
#
# dd = CC()
# print(dd.__dict__)#以字典的形式返回实例对象所包含的属性
# print(CC.__dict__)#以字典的形式返类对象所包含的属性;字典只显示实例对象的属性,不显示类属性和特殊属性(魔法方法)键=属性名,值=属性对应的值
#
# dd.setXY(5,6)#执行过程dd.setXY(dd,5,6),即传入的是实例对象的空间/引用:将dd传给方法的self(这也是self的作用)，即为绑定
# print(dd.__dict__)
#
# del CC #删除类(类对象).实例对象dd还能否调用类中的方法?
# # nn = CC()#在类被删除的情况下,无法创建实例对象
#
## dd.printXY() #就算类被删除,实例对象仍可(从始至终都是)调用实例中的方法,因为类中定义的属性/方法是静态变量,就算类(类对象)被删除,但它的实例对象是仍旧存在于内存的(直至程序退出)
#              #在大多数情况下,应该使用实例对象(java称对象的引用),而不要使用类(对象)属性

#40集,一些和类、对象相关的BIF
#issubclass(Class,Classinfo) 判断参一数是参数二的子类 成立为true,这是宽松的检查,传入类本身也返回true,


#魔法方法(构造和析构): 魔法方法总是被双下划线包围,如构造函数__int__
#魔法方法是面向对象的python的一切
# #__init__
# class Rectangle:
#     #不要给init作任何返回
#     def __init__(self,x,y): #在创建实例对象时给实例对象赋值
#         self.g = x #self代表的是类实例化后的引用,self.g的g是属于实例对象中的局部变量,
#                    #由于重写了构造函数,在创建实例对象时必需传入相应的参数,参数将赋值给self.g(即实例对象中的局部变量)
#         self.y = y
#
#     def getPeri(self):
#         return (self.g + self.y) * 2 #这里的self.g和self.y在实例对象创建后即被构造函数赋值了
#     def getArea(self):
#         return self.g * self.y
#
# rect = Rectangle(2,4) #给实例对象(java称为引用)赋值
# print(rect.getArea())
#
# #__new__ 在python实例对象最先被调用的方法是__new__(cls,par),其后才是构造函数
# #该魔法方法一般很少去重写,但当继承一个不可编辑的类,有需要修改的时候,需要重写该方法
# class CapStr(str): #继承一个不可改变的类型 - 字符
#
#     def __new__(cls,string):#cls指当前class,第二参数会原封不动的传给构造函数,此方法会返回一个实例对象(通常是参数一的实例对象,其他类实例对象也可以)
#         string = string.upper()
#         return  str.__new__(cls,string)# 调用父类的new方法,将大写后的string参数给父类去处理
#
# vk = CapStr('hello word')
# print(vk)
#
# #__del__(self)析构器, 当对象将被销毁时,会自动调用此方法
# class T:
#     def __init__(self):
#         print('我是init')
#
#     def __del__(self):
#         print('我是del')
#
# t = T()
#
# t1 = t #t1是对实例对象t的引用,当所有指向实例对象的引用都被删除后,才会触发垃圾回收机制,垃圾回收机制会自动触发对象的del方法
# t2 = t1
#
# del t2 #t1和t2只是对对象的引用,它们指向了同一个实例对象(引用),所以删除t1和t2不会触发析构器del,只有当所有引用被删除是才会调用del
# del t1
# del t

# #工厂函数-算术运算符的魔法方法
# class Zzf(int):
#     #重写魔法方法:没有重写的情况下add会返回两个对象相加的值(数字类型),sub返回两个对象相减的值
#     def __add__(self, other): #相加的魔法方法
#         return int.__sub__(self,other) #但返回是相减后的结果,因为调用了相减的魔法方法
#
#     def __sub__(self, other): #相减的魔法方法
#         return int.__add__(self,other) #但返回是相加后的结果,因为调用了相加的魔法方法
#
#     #...还有其他的一些跟算术有关的魔法方法
#
# z = Zzf(5)
# f = Zzf(3)
#
# print(z + f) #当两个对象进行算术运行时,会自动调用相关的魔法方法.正常情况下这里应是5+3=8,但因重写了add方法,改变了运算的逻辑,所以加减的效果是相反的

# #魔法方法-反运算(和算术运算符的相同,当左(对象的)魔法方法没有实现或不支持操作时,调用左边变量的魔法方方法
# class Nint(int):
#     def __rsub__(self, other):
#         return  int.__sub__(self,other) #返回相减后的值
#
#
#
# yh = Nint(6)
# yy = Nint(5)
#
# print(yh + yy) #调用了yh的add魔法方法,所以用不上重写后的radd魔法方法
#
# print(1 - yy) #1没有add魔法方法,所以调用了重写后的radd方法.
# # 需要注意,反运算时是调用右边的操作数,以当前的例子来讲,self参数代表了yy5,other参数代表了1,
# # 即实际执行self-other=4,所以结果并不是意料中的-4,将rsub魔法方法中返回的sub方法的参数相互调换即可得到正确的值
# #对运算时注重顺序的代码来说都应该注意这种情况(减法,除法,移位...)
#
#
# #魔法方法-增量运算赋值.在特定情况下触发+=运算符的魔法方法











