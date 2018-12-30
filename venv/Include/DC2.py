'''str = """Python是一种面向对象、解释型、动态
        类型计算机程序设计语言.
        解释型：程序无需编译成二进制代码，而是在执行时对语句一条一条编译
        动态类型：在程序执行过程中，可以改变变量的类型
        它常被昵称为
        胶水语言，能够把用其他语言制作的各种模块（尤其是C/C++）很轻松地联结在一起"""

 = isinstance("疯狂",str)

print(a)

x,y = 5,6
a = x if x > y else y
print(a)
value = "kwsj"
for i in value:
    print(i,len(i))
assert 6 < 8
print(str)'''

for i in range(10):
    if i%2 != 0:
        print(i)
        continue
    i +=2
    print(i)