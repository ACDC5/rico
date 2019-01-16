import  re

# 元字符  .  ^   $   *   +   ?   {   }   [   ]   \   |   (   )

rr = re.search(r'Wiki(a|P)','WikiP')  #匹配Wikia或WikiP 括号里面的内容为子组
print(rr)

wk = re.search(r'^Zeng','Zengzhifa') # ^脱字符匹配输入字符串的开始位置,即参数二的第一个字母要和参数一的第一个字母相同
print(wk)

wk1 = re.search(r'FishC$','LoveFishC') # $匹配输入字符串的结束位置,即参数二的最后一个字母要和参数一的最后一个字母相同
print(wk1)

wk2 = re.search(r'(WikiP)\1','WikiPWikiP') # 括号里面的内容为子组 理解r'(WikiP)\1'==r'WikiPWikiP'
print(wk2)

wk3 = re.search(r'(FishC)\060','FishCFishC0') # 涉及8进制和16进制...需研究
print(wk3)

wk4 = re.search(r'(FishC)\141','FishCFishCa') #(97对应的asll码是a,a对应的8进制是141,所以能匹配到末尾为a的字符)这里的0开头或三位数的数字都表示8进制
print(wk4)

wk5 = re.search(r'[.]','FishC.com') # [] 字符类(字符的集合),即将里面的内容当普通的内容来看待
print('wk5: ',wk5)

wk6 = re.findall(r'[a-z]','FishC.com') # -代表字母或数字指定一个匹配区间，将匹配到的字符以列表的形式保存
print('wk6: ',wk6) #正则表达式默认不匹配大写字母

wk7 = re.findall(r'[\n]','FishC.com\n') # \反斜杠,\n代表回车,将匹配目标中的反斜杠,并以列表的形式返回
print('wk7: ',wk7)

wk8 = re.findall(r'[^a-h]','FishC.com\n') # ^脱字符,代表取反,即除了字符类里面指定的内容,其他都匹配
print('wk8: ',wk8) #脱字符必需放在字符类前面才能达到取反的匹配效果,若放在字符类后面则匹配指定的字符类

# {M,N} M和N均为非负整数,其中M <= N,表示前边的RE匹配M~N次。
# {M,}表示至少匹配M次
# {,N}等价于{0,N}
# {N}表示至少匹配N次
wk9 = re.search(r'FishC{3}','FishCCCC') # 匹配C三次
print('wk9: ',wk9)

wk10 = re.search(r'(FishC){3}','FishCFishCFishC') # ()括号中内容为子组(可以理解为一个整体),即匹配FishC3次
print('wk10: ',wk10)

wk11 = re.search(r'(FishC){1,5}','FishCFishCFishC') # 匹配1至5次(即最少一次,最多匹配五次,此行代码实际匹配3次即可)
print('wk11: ',wk11)

# *星号表示匹配前面的子表达式0次或多次,等价于{0,}
# +加号 匹配前面子表达式一次或多次,等价于{1,}
# ? 匹配前面子表达式0次或一次.   推荐使用这个三个符号代替{},因为比较高效

#贪婪模式,正则表达式默认式开启贪婪模式的，贪婪模式:即在符合的情况下正则表达式会尽可能多的匹配字符
h = '<html><title>I love Wiki.com</title></html>'
wk12 = re.search(r'<.+>',h) # 匹配到<符号后,再根据.匹配<符号后的任意一个字符,然后+号根据.再次匹配一次或多次,由于开启了贪婪模式,所以+会匹配>前的所有字符
print('wk12: ',wk12)

h = '<html><title>I love Wiki.com</title></html>'
wk13 = re.search(r'<.+?>',h) # 匹配到<符号后,再根据.匹配<符号后的任意一个字符,+号根据.再次匹配一次或多次,由于?号最多只匹配前面子表达式(+)1次,所以贪婪模式由此被禁止了
print('wk13: ',wk13)










