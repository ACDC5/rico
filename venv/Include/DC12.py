#
# #魔法方法-描述符. 描述符就是将某种特殊类型的类的实例指派给另一个类的属性
# class MyDecriptor:#当一个类存在以下任意一个魔法方法即为特殊类型的类(描述符类)
#     def __get__(self, instance, owner): #用于访问属性,它返回属性的值
#         print('get..',self,instance,owner)
#
#     def __set__(self,instance,value): #将在属性分配操作中调用,不返回任何内容
#         print('set..',self,instance,value)
#
#     def __delete__(self, instance):# 控制删除操作,不返回任何内容
#         print('delete...',self,instance)
#
# class Test:
#     x = MyDecriptor() #将此实例对象赋值给另一个类的属性,MyDecriptor()即为x属性的描述符
#
#
# t = Test()
# print(t.x) #调用属性时触发get魔法方法,打印的参数self为描述符类本身的实例对象,参数3为拥有描述符类的实例对象,参数4为Test类本身
#
# t.x = 'ddd' #为x属性赋值时将自动调用set魔法方法
#
# del t.x #删除时将自动触发delete魔法方法
#
# #--------------------------------------------------------------
#
# # 结合上面的内容定义property类(系统的property其实就是一个描述符类)
# class MyProperty:
#     def __init__(self,fget=None,fset=None,fdel=None):
#         self.get = fget
#         self.set = fset
#         self.dele = fdel
#
#     def __get__(self,instance,owner):
#         print('执行了get')
#         return self.get(instance)
#
#     def __set__(self, instance, value):
#         self.set(instance,value)
#         print('执行了set')
#
#     def __delete__(self,instance):
#         self.dele(instance)
#         print('执行了del')
#
#
# class M:
#     def __int__(self):
#         self.x = None
#
#     def getX(self):
#         return self.x
#
#     def setX(self,value):
#         self.x = value
#
#     def delX(self):
#         del self.x
#
#     _x = MyProperty(getX,setX,delX) #MyProperty类的实例即为属性_x的描述符
#
# m = M()
# m._x = 5 #设置属性值,自动触发描述符类的set魔法方法
# m._x # 访问属性,自动触发描述符类的get魔法方法
# del m._x #删除属性,自动触发描述符类的delete魔法方法

#----------------------------------------------------------------------
#需求:定义一个温度类,然后定义两个描述类用于描述摄氏度和华氏度两个属性.
#要求两个属性会自动进行转换,也就是说你可以给摄氏度这个属性赋值,然后打印的华氏度属性时自动转换后的结果
#转换公式 摄氏度*1.8+32=华氏度
class Celsius:
    def __int__(self,value = 20.6):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)

class Fahrenheit:
    def __get__(self, instance, owner):
        return instance.cel * 1.8 + 32

    def __set__(self, instance, value):
        instance.cel = (float(value) - 32) / 1.8

class Temperature:
    cel = Celsius() #步骤1 创建实例时构造函数默认对属性赋值为20.6
    fah = Fahrenheit()

t = Temperature()
# #print(t.cel) #步骤2 访问了描述符类Celsius对象,所以自动触发其get魔法方法.这里报错,value没有被定义,原因不明

t.cel = 30 # 为描述符类Celsius对象的value属性赋值,所以自动触发其set魔法方法
print(t.cel) #访问了描述符类Celsius对象,所以自动触发其get魔法方法,value被定了且有值,未报错

t.fah = 81




