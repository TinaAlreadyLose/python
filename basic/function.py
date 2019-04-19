#匿名函数
sum=lambda arg1,arg2:arg1+arg2
print(sum(1,2))
#不定长参数
def function1(arg1,*abc):
    print(arg1)
    for i in abc:
        print(i)

print(function1(1,2,3))
print('------------------')
print()
print()
print()
num=1
def fun1():
    global num
    num=10
    print(num)
fun1()
print(num)
print('------------------')
print()
print()
print()
def function2():
    dd=1
    def function3():
        nonlocal dd
        dd=10
        print(dd)
    function3()
    print(dd)
function2()