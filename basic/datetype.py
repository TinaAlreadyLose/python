#!/usr/local/bin/python3ls
# 六大标准数据类型
'''
可变数据
Number ---- 数字
String ---- 字符串
Tuple ----元祖
不可变数据
List ----列表
Set ----集合
Dictionary----字典
'''
a, b, c, d, e = 20, 5.5, True, 4+3j, 6
print(type(a), type(b), type(c), type(d))
print(isinstance(a, int))
list1 = ['abcd', 789, 4787, 2.25, 'dan', 3+1j]
print(list1)
print(list1[0])
print(list1[2:4])
print(list1[-2:])
print(list1*2)
print(list1+list1)
tup = ('abcd', 786, 2.23, 'runoob', 70.2)
print(tup)
print(tup[0])
print(tup[2:4])
print(tup[-2:])
print(tup*2)
print(tup+tup)
a = set('asaklvwegvjjwvfov')
b = set('hvwupbvhwubhsaa')
print(a - b)#差集
print(a | b)#并集
print(a & b)#交集
print(a ^ b)# a 和 b 中不同时存在的元素
dicts={}
dicts['one']='demo'
dicts[2]=2
print(dicts['one'])
print(dicts[2])
print(dicts.keys())
print(dicts.values())
s='dan'
print(repr(s))


