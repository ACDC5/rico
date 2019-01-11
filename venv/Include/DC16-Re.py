import  re

#理解正则表达式的要点,是人为创建一个匹配字符的规则,而不是使用死板的方法去匹配字符
#search()方法用于在字符串中搜索正则表达式模式第一次出现的位置
sou = re.search(r'.','I love Wikipedia.org!') #点号可匹配除反斜杠外的 任意字符,结果为I
sre = re.search(r'Wiki.','I love Wikipedia.org!') #,匹配结果Wikip
ma = re.search(r'\.','I love Wikipedia.org!' ) #符号 \反斜杠可以剥夺元字符本身的含义

print(sou ,sre)
print('ma:',ma)

num = re.search(r'\d','I love 523Wikipedia.org!')#匹配一个数字
print('mun:',num)

num = re.search(r'\d\d\d\d','I love 5236Wikipedia.org!')#匹配4个数字
print(num)
print('-----------------------------------------------------------------')

#模拟匹配一个IP地址 问题IP地址并非每一个都是三个数一组，如：192.168.1.1；代码不美观
ip = re.search(r'\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d','192.168.111.123')
print('ip:',ip)

#中括号[]在正则表达式表示两个元字符,里面的内容称为字符类(字符集合),字符类中的任意一个字符匹配成功都算匹配成功
aei = re.search(r'[aeiou]','I love Wikipedia.org') #使用中括号创建一个字符类,匹配里面的任何一个字符都算匹配
print('aei:',aei) #输出字母o,字母I之所以没有匹配是因为正则表达式默认是开启大小写敏感的

#将大小写都输入到字符类中可解决大小写敏感的问题，或者关闭大小写敏感
aei2 = re.search(r'[aeiouAEIOU]','I love Wikipedia.org')
print('aei2:',aei2)

# - 用于表示一个区间范围
scope = re.search(r'[a-z]','I love Wikipedia.org')
print('scope:',scope) #输出小写字母l

scope2 = re.search(r'[0-9]','I love Wiki987pedia.org') #匹配0至9的数字
print('scope2:',scope2)

scope3 = re.search(r'[2-9]','I love Wiki12987pedia.org')
print('scope3:',scope3)
print('----------------------------------------------------------')

# {} 用于限定重复的次数
span = re.search(r'ab{3}','abbb') #匹配字符以ab开头同时b出现3次的内容
print('span:',span)

span1 = re.search(r'ab{3,10}','abbbbbbb') #匹配字符以ab开头同时b出现3至10次的内容
print('span1:',span1)

print('理解错误的 示范---------------------------------------------------')
#匹配一个255范围内的数字，如188
error = re.search(r'[0-255]','188') #预期匹配数字188
print('错误示范1:',error) #在字符类[0-255]中0-2表示0 1 2,两个5是重复的将被视为一个5,所以匹配的是0125的数字,结果为1
#正则表达式匹配的是字符串对任何字符串来说任何数字都是0到9组成的,不存在个十百千的概念，如188对正则表达式来说是由三个字符组成的

error2 = re.search(r'[0-2][0-5][0-5]','188')#无法匹配88这两个数字,因为指定的最大数只能到5
print('错误示范2:',error2)

print('-------------------------------------------------------------------------')
#匹配一个255范围内的数字
# | 即为逻辑或，[01]\d\d 表示当百位为1时,十位个位可以是任意数字
            #  2[0-4]\d 表示当百万为2时,十为必须在0至4之间,个位可以是任意数字
            #  25[0-5]  表示当百位和十位为2和5时,个位不能超过5
true = re.search(r'[01]\d\d|2[0-4]\d|25[0-5]','200') #可匹配255以内的数字
print(true)


ipAddress = re.search('r(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])','192.168.1.1')
print('ipAddress:',ipAddress)

# 元字符  .  ^   $   *   +   ?   {   }   [   ]   \   |   (   )
