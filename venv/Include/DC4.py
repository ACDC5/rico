import os

# #文件系统模块(python模块可以理解成java类)
# print(os.getcwd())#返回当前工作目录
# # print(os.chdir('d:\\'))#改变工作目录
# print(os.getcwd())
#
# print(os.listdir('d:/'))#获取该路径下的所有文件和文件夹
# print(os.mkdir('D:/A plan'))#在指定目录下创建一个文件夹
# print(os.mkdir('D:/B plan/C plan'))#如果创建的子目录时父目录不存在,将报错
#
# print(os.makedirs('路径参数'))#递归创建多层目录,如果目录已存在将抛出异常,注意:'E:\\a\\b'和'E:\\a\\c'并不会冲突
#
# print(os.remove('D:/A plan/dddddd.txt'))#删除文件,不能删除文件夹
# print(os.rmdir('文件夹路径'))#删除文件夹,当文件夹中存在文件时,将抛出错误
#
# print(os.removedirs('X:\\A\\B\\C'))#递归删除目录,从子到父目录逐层尝试删除,目录非空时抛异常
#
# os.rename('old','new')#将文件old重命名为new
#
# print(os.system('CMD'))#运行系统的shell命令,打开cmd
# print(os.system('calc'))#打开计算机中计算器
#
# os.curdir#一个常量,指代当前目录,即'.'（点）
# os.pardir#一个常量,指代上一级目录,即'..'(点点)
#
# os.sep#输出操作系统特定的路径分隔符,win下为'\\',linux下为'/'
# os.linesep#当前平台使用的行终止符.win下为'\r和\n'表示换行,linux下为'\n'换行
# os.name#指代当前使用的操作系统,包括posix,nt,mac,os2,ce,java

##os.path模块的常用函数
# print(os.path.basename('C:\\Users\\Ryen\\Desktop\\gitDemo\\gitTest.txt'))#去掉目录路径,单独返回文件名,如果末尾为非文件,则返回最后一级路径
# print(os.path.dirname('C:\\Users\\Ryen\\Desktop\\gitDemo\\gitTest.txt'))#去掉文件名,只返回目录路径
#
# os.path.join('path1','path2')#将1和2的路径组合成一个新的路径
# os.path.split('path')#分割文件名和目录路径,返回(f_path,f_name)元组,如果完全使用目录,它也会将最后一个目录作为文件名分离,且不会判断文件或目录是否存在
#
# os.path.splitext('path')#分离文件名与扩展名,返回(f_name,f_path)元组
# os.path.getsize('file')#返回指定文件的大小,单位字节
# os.path.getatime('file')#返回指定文件最近的访问时间,(浮点型秒数,可用time模块的gmtime()或localtime()函数换算)

