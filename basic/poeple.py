class people:
    #定义基本属性
    name='dan'
    age=10
    #定义私有属性
    _height=30
    #定义构造方法
    def __init__(self,name,age,_height):
        self.name=name
        self.age=age
        self._height=_height
    def speak(self):
        print("%s 说： 我 %d 岁。"%(self.name,self.age))
p=people('dan',10,20)
p.speak()