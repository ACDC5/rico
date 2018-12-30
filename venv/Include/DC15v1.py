def c2f(cel):
    fah = cel * 1.8 + 32
    return fah

def f2c(fah):
    cel = (fah - 32) / 1.8
    return cel

def test(): # 测试
    print('测试，0摄氏度 = %.2f华氏度' % c2f(0))
    print('测试，0华氏度 = %.2f摄氏度' % f2c(0))

if __name__ == '__main__': #当模块以程序运行时 __name__属性的值将等于__main__,以模块运行时__name__属性的值是当前模块的名称.
    test()

print(__name__,'根据被调用对象打印不同的值...请查看DC15v1.py')