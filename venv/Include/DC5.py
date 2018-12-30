import pickle

##pickle模块,可将所有python对象转换成二进制字节流.过程:
#存放:pickling
#将二进制数据转为python对象时称为-读取:unpickling

#以二进制的形式写入数据
my_list = [12,34,0.618,'你好',['二维','数据']]
pickle_file = open('C:\\Users\\Ryen\\Desktop\\gitDemo\\my_pickle_file.pkl','wb')#参数wb意味着以二进制的形式写入数据到该文件
pickle.dump(my_list,pickle_file)#将指定数据写入到指定的文件中
pickle_file.close()#

#以二进制的形式读取数据
pickle_file = open('C:\\Users\\Ryen\\Desktop\\gitDemo\\my_pickle_file.pkl','rb')#参数rb,代表以二进制的形式读取指定文件的数据
my_list2 = pickle.load(pickle_file)#将读取到的二进制数据还原
print(my_list2)
pickle_file.close()