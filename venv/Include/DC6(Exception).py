
#异常
# AssertionError断言语句assert失败(即返回结果为fales)
# AttributeError访问未知(不存在)的对象属性

# #检测和处理异常(和Java很像啊...):
# #1 try-except语句.对可能出现的错误进行捕捉/检测,并对错误进行处理
# #在try...except中的代码如果没有检测到错误或异常,将不会执行except中的代码
# try:
#     #需要检测(捕获)的代码
#     f = open('我是一个文本.txt')
#     print(f.read())
#     f.close()
# except OSError:
#     #处理错误的代码
#     print('文件不存在')
#
# #2捕获多种可能的错误,并对可能捕获到的错误类型进行对应的处理
# try:
#     #需要检测的代码
#     number = 1 + '1'#首先捕获该错误(如果有对应的处理(捕获)代码,)
#     f = open('我是一个文本.txt')
#     print(f.read())
#     f.close()
# except OSError as xyh1:#用一个变量记录具体的错误,后续可以打印此变量以查看错误信息
#     #处理错误同时输出错误信息
#     print('文件不存在\n错误原因:' + str(xyh1))
# except TypeError as xyh2:#当检测到代码存在的错误时,系统会自动调用对应错误类型的处理代码
#     print('运算错误\n错误原因:' + str(xyh2))
#
#
# #3处理多种错误的的另一种写法:
# try:
#     number = 1 + '1'
#     f = open('我是一个文本.txt')
#     print(f.read())
#     f.close()
# except (OSError,TypeError):#当捕获到的错误类型在该元组中存在时,执行except中的处理代码
#     print('出错了')
#
#
# #4可以这么写,但不建议,这种写法会隐藏开发者没有注意到或需要处理的错误
# try:
#     a = int('abc')#当错误在这一行发生时,后续的代码将停止执行
#     print(a)
# except:#不声明任何类型的错误,只要检测到异常,则进入错误处理区
#     print('出错了')

# #try-finally语句：
# try:
#     f = open('C:\\Users\\Ryen\\Desktop\\gitDemo\\my_pickle_file.pkl','rb')#写入模式
#     print(f.read())
#     number = 1 + '1'#类型错误异常,导致后面的代码没有执行
#     f.close()#上面代码报错,导致写入的数据仍在缓存区,没有写入磁盘
# except TypeError as error:#当检测到可能的错误,执行错误处理代码再执行finally
#     print('出错了\n问题原因：' + str(error))
# finally:#无论是否发生错误,
#     #无论错误是否出现,finally中的代码都将被执行
#     f.close()
#     print('文件已关闭')
#
#
## #raise语句:
# #自己引发一个异常
# raise ZeroDivisionError('手动触发的异常')

# #else语句
# try:
#     ks = int('8')
# except ValueError as info:
#     print('类型错误')
# else:#如果没有报错,执行else中的语句
#     print('没有报错')

#with语句
try:
    with open('无.txt','w') as f:#with关键字将关注打开的文件,当文件没被使用时,会调用f.close方法,无需再写关闭代码
        for each_line in f:
            print(each_line)
except OSError as reason:
    print('出错了' + str(reason))
