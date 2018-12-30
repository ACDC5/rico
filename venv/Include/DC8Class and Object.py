#类的定义
class MyClass:
			#属性
			color = 'green'
			legs = 4
			mouth = '大醉'

			#方法
			def climb(self):
				print("我是方法中的代码")


#self相当于java的this
class Ball:

    #def __init__(self):  #每个类都有默认的构造函数
    #默认无参数,self(this)不是参数.(也和java一样,用于给对象初始化.默认不显示)

    def setName(self,name):
        self.jj = name#将setName函数的中的name参数传给self

    def kick(self):#传入了谁的参数,就代表了执行了哪个实例对象
        print('我叫%s,是谁踢我。。。'%self.jj)


a = Ball()#创建实例A
a.setName('球A')

b = Ball()#创建实例B
b.setName('球B')

c = Ball()#创建实例C
c.setName('球C')

a.kick()#将参数隐式传入给函数


#构造函数:
class Ballv2:
    def __init__(self,name): #重写构造函数,
        self.name = name

    def kick(self):
        print(print('我叫%s,是谁踢我。。。'%self.name))

aa = Ballv2('小猪佩奇')#在创建对象的后,调用重写的构造函数给对象赋值
aa.kick()


#共有和私有的数据(相当java的public、private关键词的概念)
#当方法名和变量名前存在双下划线时,即为私有的成员变量
##写法__name称为name mangling(名字改编或名字重置)
class Person:
    name = '廖企'#公有的变量
    __myName = '纵贯线' #私有的数据,理论上只能从类的内部访问

    def getDate(self):
        return self.__myName
p = Person()
print(p.name)
# print(p.__myName)#无法访问
print(p.getDate())#如果相从外部访问私有的数据,须在类的内部定义一个调用该私有属性的方法
# print(p._Person.__myName)#python3.5这样写不成功,教材上的3.3好像可以