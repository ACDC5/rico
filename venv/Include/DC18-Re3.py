import re
import urllib.request as req

# ri = re.search(r' (\w+) (\w+)','I love Wiki') # 从第一个空格开始匹配...(括号中的为子组)  \w代表任何字符
# print(ri)# 返回的是匹配对象
#
# string = ri.group() #从匹配对象中获取字符串。
# print(string) #得到字符串
#
# str1 = ri.group(1)#获取第一个子组中的内容。如果正则表达式中存在子组,子组会将匹配的内容捕获，通过在group方法中设置序号可以获取对应的内容
# print(str1)
#
# str2 = ri.group(2)
# print(str2)
#
# startlocaltion = ri.start() #返回开始匹配的位置
# print('start： ',startlocaltion)
#
# endlocaltion = ri.end() #返回结束匹配的位置
# print('end： ',endlocaltion)
#
# scope = ri.span() # 返回正则表达式匹配的范围
# print(scope)


#---------------------------------------------------------------------


# 正则 模拟爬虫获取贴吧里的图片
def open_url(url):
    url_r = req.Request(url)
    #通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。现使用win10发起模拟请求
    url_r.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')
    page = req.urlopen(url_r)
    html = page.read().decode('utf-8')
    # print(html)
    return html


def get_img(html):
    p = r'<img class="BDE_Image" src="([^"]+\.jpg)"' #匹配<img class="BDE_Image" src=开头的字符至.jpg"结束(匹配了多条,加入子组()将直接获得图片的下载地址,因为子组)
    imglist = re.findall(p,html) #在没有子组的情况下findall()方法会查找到匹配的内容以列表的形式返回
                                 #如果正则表达式存在子组(这个例子中([^"]+\.jpg)就是一个子组),将会把子组单独返回;如果有多个子组会将匹配的内容以元组的形式返回

                                 #当在某些场景存在多个子组匹配的内容，而又不需要以元组的方式返回时,可以使用非捕获组:语法(?:xxx) 即该子组匹配的字符串无法从后后边获取

    #开始下载
    for each in imglist:
        filename = each.split("/")[-1] #取当前图片url中最后一个/斜杠后的字符作为文件的名称
        print(each)
        localtion = "C:\\Users\\Ryen\\Desktop\\" + filename
        req.urlretrieve(each,localtion,None)

if __name__ =='__main__':
    print(__name__)
    url = 'https://tieba.baidu.com/p/5094576274'
    get_img(open_url(url))
