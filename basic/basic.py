#!/usr/local/bin/python3
import keyword
s=[55,56,54,79,115,69,114,116,107,49,50]
for i in s:
	print(chr(i),end='')
print('你好 世界')
print(keyword.kwlist) # 查看python保留字
# ``根式锁紧``
if True:
    print("true")
else:
    print("false")
#多行语句
item_one='a'
item_two='b'
item_three='c'
total=item_one+\
    item_two+\
        item_three
print(total)
#基本数据类型
'''
int(整型)： 只有一种整数类型，取消了python2的长整型
bool(布尔类型)： true与false 两个值
float(浮点数)： 1.235，3E+2
complex(负数)：1+2j
'''
#字符串
str="dan J"
print(str) # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字
print(str[0]) # 输出字符串第一个字符
print(str[2:])# 输出从第三个开始到最后一个字符
print(str[2:5])# 输出从第三个开始到第五个的字符
print(str*2) # 输出字符串两次
print('hello'+str) # 连接字符串
print('hello\nword') # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nword')# 在字符串前面添加一个 r，表示原始字符串，不会发生转义
#为了更好的区分代码块，一般用空行分割代码块，这是一中良好的编程风格
input("\n\n 按下enter键退出")
# 在同一行显示多条语句，用；号隔开
import sys; x='dan_j';sys.stdout.write(x+'\n');
# 是否换行输出
print(x)#换行
print(x)
print(x,end=' ')#不换行
print(x,end=' ')
#import and from... import
#import 倒入整个模块
#from import 倒入模块的一个方法