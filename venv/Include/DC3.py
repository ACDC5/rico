
#列表
'''ksj = ["你","我","他"]
print(ksj)'''

'''number = [1,3,5,7,9]
print(number)'''

#混合列表
'''rico = ["hello",9,7,"hi"]
print(rico)
print(len(rico))'''

#添加元素
'''he = []
he.append('women')#向列表末尾添加元素,只能添加单个元素
he.extend(["王炸","不要",'关键字','woqu','nani'])#向列表末尾添加一个列表,即添加多个元素
print(he,len(he))
he.insert(0,'三带一')#将元素添加到指定位置
print(he,'长度:',len(he))
print(he[0])
he.remove('women')#移除元素,直接输入元素名
print(he)
del he[2]#使用del关键字删除指定元素,关键字后面是列表变量名时,列表会被删除
print(he)
a = he.pop()#以栈的方式实现,无参时移除列表中的最后一个元素,同时将该元素返回
print(a)
print(he)
print(he[1:3])#复制位置1到3-1间的元素
print(he[1:])'''

#列表操作符
'''
a = ['nimen,',789,456]
b = ['women',[123,'zeng'],8,9]
e = [2,3,5,1,45,68,2,1.1]
print(a < b)

print(a > b) #当有多个元素时,只比较第一个元素的大小

c = [123,456]
print(a < b and a==c)

print(a+b)
print('wo' not in a)#判断元素是否在列表
print(123 in b[1]) #判断二维列表的值
print(b[1][0])#访问二维列表值

print(dir(list))#查看list内置函数

c *= 10
print(c)

print(c.count(123))#返回该元素在列表中存在的数量

print(c.index(456))#返回该元素的索引位置

print(c.index(123,5,9))#在列表索引5至9之间找到第一个元素为123的索引值并返回

b.reverse()#颠倒整个列表元素的顺序

e.sort()#对列表进行排序,默认从小到大
e.sort(reverse=True)#从 大到小排序
print(e)
print(b)'''

#元组
'''yuan = (1,2,3,4,5,6,7,8)
temp1 = 1,#一个元组类型
temp2 = 1 #一个int类型
print(type(temp2))

wsj = ('采纳','采购','白天','月亮')
wsj = wsj[:2] + ('艺术',) + wsj[2:] #以切片的方式更新元组,原变量将被更新后的元组变量覆
                                    #概,python的回收器会将其回收,因为原变量没有引用指向它
print(wsj)

bb = 'lkj',
print(type(bb))

print(type(str(86)))
'''

'''
def myfunction():
    '我写的函数文档'
    print('函数的定义');
    return '返回值'

print(myfunction())

def Second(name):
    'ad'
    print('有函数')

print(myfunction.__doc__)#输出函数文档
print(Second.__doc__)

print(Second('rico'))
'''

'''
def zzf(name='默认值1',name2='默认值2'): #指定默认参数
    print('定义关键字')
    print(name + name2)

print(zzf())#如果没有传入实际参数,将是使用默认参数

def rico(*value,cookie = 8):#关键字*表示:可指定任意个参数
    print('第一个参数时:',len(value))#返回实际输入的参数
    print('第二个参数是:',value[1])#返回下标为1的参数

print(rico(1,'大大大',3.14,47,'jjjc'))
'''

'''
def hello():
    print('hello word')
print(hello())#因为这个函数没有返回值,python默认返回None(没有)对象

#temp1 = hello()
'''
'''
def fun1():
        print('输出fun1函数的内容')
        def fun2():#内部函数即嵌套函数
            print('输出fun2函数的内容')
        print(fun2())#必须声明调用,否则不能说是用到fun2函数

def funX(x):
    def funY(y):
        return x * y #1、内部函数使用了外函数的参数
    return funY #2、外函数返回的是内函数的引用,满足1和2即可视为闭包

i = funX(7)(5) #同时给外部和内部函数传参
print(i)
print(type(i))

def fun3():
    x = 5
    def fun5():
        nonlocal x # nonlocal关键字,强制将该变量声明为非局部变量
        x *= x #这里将报出局部变量未赋值前不能引用的错误,在内部函数看来x是未赋值的,外部函数的
        return x      #局部变量x从内部函数的角度可以理解为全局变量(可以参见356行内容,也适用于这里)
    return fun5()

print(fun3())
aa = fun3()
print(type(aa))

'''

# conding = utf-8 #lambda(匿名函数)表达式
# def ds(x): #普通函数
#     return 2 * x +1
# print(ds(6))
# #使用lambda(匿名函数)表达式,返回的是函数对象
# g = lambda x :2 * x + 1#冒号前面是参数,后面是返回值,将其赋给一个变量即可使用
# print(g(3))
#
# #多个参数
# gg = lambda x,y : x + y + 2
# print(gg(3,0))

#相关常用的牛逼的bif

#过滤函数
# ls = list(filter(None,[1,2,0,3,False,True])) #只返回True值.把过滤器返回的对象转为一个列表
# print(ls)
#
# def odd(x):
#     return x % 2 #去取余数
#
# temp1 = range(10)#获取从0到10的数字
# show = filter(odd,temp1)# 使用过滤函数,自定义的odd函数不用加括号
# show = list(show) #转成列表类型
# print(show)
#
# #map函数,参数1为函数,参数2为可迭代的序列/列表..
# # 函数的功能是将序列的每一元素当作第一个函数的参数进行运算加工,
# #直到序列的每个元素被迭代完成,返回由序列被处理后的新列表
# mapf = list(map(lambda x : x * 3,range(10)))#参数一运算参数二传过来的元素,返回一个新列表
# print(mapf)

# import sys
# sys.setrecursionlimit(1000) #设置递归深度,python3默认递归100层,python默认1000层
#
# #求某正整数的阶乘,使用一般函数实现
# def re(x):
#     result = x
#     for i in range(1,x):
#         result *= i
#     return result
# print(re(10))
#
# #递归
# def re2(x):
#     if x == 1 or x == 0:
#         return 1#当条件等于1,递归不再进行,此时会结束条件,一层层的返回递归所得到的结果
#                 #debug时的现象可以在此得到解释,为什么条件等于1时,x的值会逐渐变大,就是
#                 #递归运算后的值
#     else:
#         return x * re2(x - 1) #当条件为1,将递归每层运算后的值
# print(re2(15))

# #递归 - 斐波那契数列
# #迭代实现
# def f(n):
#     n1 = 1
#     n2 = 1
#     n3 = 1
#
#     if n < 1:
#         print('输入错误')
#         return -1
#     while (n-2) > 0:
#         n3 = n2 + n1
#         n1 = n2
#         n2 = n3
#         n -= 1
#     return n3
#
# summery = f(20)
# if summery != -1:
#     print('共有%d对小兔子诞生！'% summery)
#
# #递归实现
# def d(n):
#     if n < 1:
#         print('输入有误')
#         return -1
#
#     if n == 1 or n == 2:
#         return 1
#     else:
#         n1 = n
#         return d(n-1)+d(n-2)
#
# val = d(3)
# if val != -1:
#     print('小兔子共诞生了%d对' % val)

#递归 - 汉诺塔
# def hanoi(n,x,y,z):#xyz代表三根柱子
#     if n == 1:
#         print(x,'-->',z)
#     else:
#         hanoi(n-1,x,z,y) #将前n-1个盘中从x移动到y上
#         print(x,'-->',z) #将最底下的最后一个盘子从x移动到z上
#         hanoi(n-1,y,x,z) #将y上的n-1个盘子移动到z上
#
# n = int(input('请输入汉诺塔的层数:'))
# hanoi(n,'X','Y','Z')

# #字典
# #用列表的方式获取建队值
# list2 = ['1','2','3','4','5','6']
# list3 = ['11','22','33','44','55','66']
# print('自定义的键:',list2[list3.index('33')])

# #创建字典:
# #每一对键值组合称为项
# dictl = {'1':'11','2':'22','3':'33','简体':'繁体',100:50}
# #访问字典:
# print(dictl['简体'])

# #创建空字典
# dict2 = {}
# print(dict2)

##dict()的用法
# dict3 = dict((('f',70),('s',115),('h',104),('c',67)))#传入一个maping类型的参数,以构造一个字典
# print(dict3)
#
# dict4 = dict(企鹅='北极',rico='fenkuang企鹅',小猪='佩奇')#以key+value的形式建立字典,输出的内容会自动会排序
# print(dict4)
#
# #直接给key赋值.如果这个key是在字典中存在的,则更新对应的值,如果不存在就创建这个键值
# dict4['rico'] = '特斯拉'#key如果存在则更新
# print(dict4)
# dict4['马达'] = '风驰电掣'#key不存在则新建这个键值对
# print(dict4)

# #fromkeys(s,v)返回一个新的字典,第一参数为新字典键的值,第二参数可选,为字典的值,不填为none
# nullV = {}
# print(nullV.fromkeys((1,2,3)))#输出的字典值是None
#
# print(nullV.fromkeys((1,2,3),'value'))#每个键所对应的字典值都是相同的
#
# print(nullV.fromkeys((1,2,3),('11','22','33')))#第二参数将复制三次给三个序列作值

# #keys()返回字典键的引用
# nullv2 = {}
# print(nullv2.fromkeys(range(1,11),'a'))
# for eachKey in nullv2.keys():
#     print(eachKey)
#
# #velues()返回字典值的引用,即返回字典的值
# print(nullv2.fromkeys(range(1, 11), 'b'))
# for eachValue in nullv2.values():
#     print(eachValue)
#
# #items()返回字典项的引用即key：value
# print(nullv2.fromkeys(range(1, 11), 'c'))
# for eachItem in nullv2.items():
#     print(eachItem)

#######################################################################################
#访问键获取对应的值
# nullv3 = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'e',}
# print(nullv3[4])#获取对应键的值
# #print(nullv3[7])#当键不存在时,将报错
#
# var = nullv3.get(7)#当获取字典中没有的键时,返回None对象
# print(var)
# print(nullv3.get(5,'指定返回的提示'))#当获取字典中没有的键时,返回第二参数
#
# #使用成员操作符判断字典是否存在指定的键
# print(3 in nullv3)
# print(2 not in nullv3)

# # setdefault()和get()类似,setdefault()在找不对应的键时,它会自动进行添加
# var1 = {1:'a',2:'b',3:'c',4:'d',5:'e'}
# var1.setdefault(6)#当键不存在时自动添加该键,默认值None
# print(var1)
# var1.setdefault(7,'自定义的值')#当键不存在时自动添加该键,可自定义值
# print(var1)

#
# #清空字典
# print(nullv3.clear())
# print(nullv3)

# #不建议使用nullv3 = {} 清空字典,因为引用该字典的变量不会被清空
#
# #字典的copy函数
# var01 = {1:'a',2:'b',3:'c'}
# b = var01.copy()#强/前？拷贝
# c = var01 #赋值
# print(c,b,var01)#看起来时相同的,但它们的地址不一样
# print(id(var01))#使用id函数查看变量地址
# print(id(b))#强拷贝后的内存地址实际是一个新建的内存地址,所以原值的改变不会影响它
# print(id(c))#被赋值的变量他的内存地址是和原值一样的,代表了它们指向相同的引用,原值的改变能影响它
#
# #pop()给定键弹出对应的值
# var3 = {1:'a',2:'b',3:'c',4:'d',5:'e'}
# print(var3.pop(2))#弹出2对应的值
# print(var3)#被弹出的键值对将在字典中消失
#
# #popitem()给定键弹出对应的项(key:value)
# print(var3.popitem())# 弹出字典中的第一项
# print(var3)#被弹出的项将在字典中消失

# #update()利用一个字典或映射关系去更新另一个字典
# var4 = {3:'大白'}
# var5 = {1:'a',2:'b'}
# var5.update(var4)#用4来更新var5，如果键相同只更新对应键的值,否则新建该k:v
# print(var4)
# var4.update(var5)#用5来更新var4，4只有一对k:v时将被5更新所有
# print(var4)

# #集合(set)
# num1 = {}
# print(type(num1))
# num1 ={1,2,3,4,5}#创建集合
# print(type(num1))
# num1 = {5,4,3,2,1,2,3,4,5,6}#集合具有唯一性,即集合中的元素不可重复,重复将被去掉
# print(num1)
# #print(num1[2])#集合不支持索引,不能根据索引得到值
#
# #使用set()工厂函数创建集合,由此得到集合是无序的
# set1 = set([1,2,3,4,5,5,6,7,8,9])#传入一个列表\元组和字符串均可创建一个集合
# print(set1)
#
# #获取列表中的元素:
# #可以使用for读取集合中的每个元素,也可用in和not in判断元素是否存在于集合
# num2 = {11,22,33,44,55,66}
# print(num2)
# for aa in num2:#使用for循环得到集合中每个值
#     print(aa)
#
# print(10 in num2)#判断指定值是否存在于集合
# print(97 not in num2)
#
# #add()向集合添加元素
# num2.add(88)
# print(num2)
#
# #remove移除集合中的元素
# num2.remove(44)#输入需要移除的元素值
# print(num2)
#
# #不可变集合(frozen冻结的）
# num3 = frozenset([111,222,333,444,555])
# print(num3)
# num3.add(666)
# num3.remove(444)#任何增删的尝试对不可变集合都将是无效的

# #文件(即java中的IO)
# #open()将返回一个文件对象,第一个必填参数为文件路径,第二参数非必需,默认为只读模式r,即以只读模式打开文件
# #open('path','w')打开模式'w'以写入的方式打开文件,会覆盖已存在的文件
#                 #打开模式'x'如果文件已经存在,使用此模式打开将引发异常
#                 #打开模式'a'以写入模式打开,如果文件存在,则在尾末追加写入
#                 #打开模式'b'以二进制模式打开文件
#                 #打开模式't'以文本模式打开(默认)
#                 #打开模式'+'可读写模式(可添加到其他模式中使用)
#                 #打开模式'U'通用换行符模式（已弃用）
#
# #encoding是用于解码或编码的编码的名称文件。这应该只在文本模式下使用。默认编码是平台依赖，但Python支持的任何编码都可以通过。
# #使用右斜杠需要用到转义符
# f = open('C:\\Users\\Ryen\\PycharmProjects\\rico\\venv\\Include\\DC3.py',encoding='utf_8')#不使用encoding参数读取文件时因字符集为gbk报错
# print(f)#返回文件对象
# #read()按字符读取文件.指针概念可以理解为书签,读到某页书签即在某页
# #一个中文字符占两个字节,英文字符占一个字节
#
# print(f.read(10))#按指定字符量读取,读取文件中的1至5的字符
#
# #tell()返回指针在当前在文件中的位置
# print(f.tell())
#
# print(f.read())#不指定参数将读取整个文件,指针将移到文件的末尾
# print(f.read())#再读取时,将返回空,因为指针会从上次读取过的位置接着读取,而上一次已经读取到了末尾
# print(f.tell())
#
# #seek(offset,from)改变指针的位置,从from(0代表文件起始位置,1代表指针当前位置,2代表文件末尾)偏移offset个字节
# print(f.seek(45,0))#返回指针位置,从文件开始的位置到第45个字节
# print(f.readline())#从第45个字节开始读取并返回一行数据
#
# print(list(f))#以一行为一个元素返回一个列表
#
# #分别输出打印每一行
# for each_line in f:
#     print(each_line)
# print(f.close())#关闭文件
#
# #文件写入(如果要向文件写入,要确保打开open()模式中带了'w'或'a')
# #write()
# #使用左斜杠不需要用到转义符
# f2 = open('C:\\Users\\Ryen\\Desktop\\gitDemo\gittest3.txt','w',encoding='utf_8')
# print(f2.write('我写入的ff'))#如果文件不存在将被创建,如果文件存在,则写入的内容将覆盖文件原内容,同时返回写入的字符数量
# #f.writelines(seq)#向文件写入字符串序列seq(即依次写入该字符串),seq应该是一个返回字符串的可迭代对象
# f2.close()


