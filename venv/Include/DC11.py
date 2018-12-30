##
# #属性访问
# class C:
#     #使用这几个魔法方法需要注意
#     def __getattribute__(self, name):#触发条件,定义当该类的属性被访问时的行为
#         print('getattribute')
#         return super().__getattribute__(name) #返回当前对象的父类的魔法的值C类默认继承了Object
#
#     def __getattr__(self, name): #触发条件,定义当用户试图获取一个不存在的属性时的行为
#         print('getattr')
#
#     def __setattr__(self, name, value):#触发条件,定义当一个属性被设置时的行为
#         print('setattr')
#         super().__setattr__(name,value)
#
#     def __delattr__(self, name):#触发条件,定义当一个属性被删除时的行为
#         print('delattr')
#         super().__delattr__(name)
#
# c = C()
# c.y #访问一个不存在的属性
# c.x = 6 #设置一个属性
# c.x
# del c.x #删除属性x
#
# #使用以上几个魔法方法需要注意,尤其时setattr和getattribute容易导致死循环
# class Rectangle:
#     def __init__(self,width=0,height=0):
#         self.x = width
#         self.y = height
#
#     def __setattr__(self, key, value):#当类被实例化后调用构造器时对属性x进行了第一次赋值,对属性的赋值将自动触发setattr魔法方法.key对应对象属性的名称即x,value即属性值
#         if key == 'square': #条件不成立
#             self.x = value
#             self.y = value
#         else:
#             # self.key = value #value的值的来自x属性的值6,所以这个和上面的if条件构成了无限循环
#             # super().__setattr__(key,value) #解决方法1,调用父类的魔法方法
#             self.__dict__[key] = value #解决方法2
#
#     def getArea(self):
#         return self.x * self.y
#
# r = Rectangle(6,5)
# # r.square = 100 #定义一个新属性并赋值
# # r.x
# # r.y
# print(r.getArea())
#
# print(r.__dict__)#以字典的形式获取当实例对象的属性
