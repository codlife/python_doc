# 默认 local 赋值 没有 改变外部变量的值，只是在内容新建一个同名变量
#使用 nonlocal 可以进行对象的重新绑定
#使用 global可以将 绑定上升到模块级别
spam=None
def scope_test():
    def do_local():
        spam="local spam"
    def do_nonlocal():
        nonlocal spam
        spam="nonlocal spam"
    def do_global():
        global spam
        spam="global spam"
    spam="test spam"
    do_local()
    print("After local assignment:",spam)
    do_nonlocal()
    print("After nonlocal assignment:",spam)
    do_global()
    print("After global assignment:",spam)
scope_test()
print("In global scope:",spam)
def f1(x,y):
    return min(x,y)
class C:
    f=None
    def __init__(self):
        self.f=f1(1,2)
        self.data=[]
    def g(self):
        return "hello world"
    h=g
    def add(self,x):
        self.data.append(x)
    def addtwice(self,x):
        self.add(x)
        self.add(x)


obj=C()
print(obj.g())
print(obj.h())
print('hello',obj.f)
print(obj.data)
obj.add(1)
print(obj.data)
obj.addtwice(2)
print(obj.data)

class Mapping:
    def __init__(self):
        pass
    def update(self):
        self.__updated()
    def __updated(self):
        print("this is a method in Mapping")
class MappingSubclass(Mapping):
    def update(self):
        print("this is a method in MappingSubclass")
map=Mapping()
map.update()
submap=MappingSubclass()
submap.update()

class Employee:
    pass
john=Employee()
john.name="john Doe"
john.dept="computer lab"
print(john.name)
class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass
for cls in [B,C,D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

s='abc'
it=iter(s)
print(it)
print(next(it))
print(next(it))

class Reverse:
    def __init__(self,data):
        self.data=data
        self.index=len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0 :
            raise StopIteration
        self.index=self.index-1
        return self.data[self.index]
    def reverse(self):
        for index in range(self.index-1, -1, -1):
            yield  self.data[index]

rev=Reverse('spam')
print(iter(rev))
for char in rev:
    print(char)
ite=rev.reverse()
print("this is the method reverse")
for char in ite:
    print(char)

print(sum(i*i for i in range(10)))

xvec=[10,20,30]
yvec=[7,4,3]
print(sum(x*y for x,y in zip(xvec,yvec)))
from math import pi, sin
print({x:sin(x*pi/180) for x in range(0,91)})