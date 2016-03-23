a=[1,2,3,4]
print(a)
a[len(a):]=[4]
print(a)
a=[33,22,55,99]
print(a.count(33))
print(a.insert(2,-1))
print(a)
a.sort()
print(a)
a.sort(key=lambda x:-x)
print(a)
a.reverse()
print(a)
b=a.copy()
print(b)
c=a[:]
print("this is c",c)
c[0]=100
print("this is a",a)
print("this is c",c)

# 将列表 作为堆栈使用
stack=[3,4,5]
stack.append(6)
stack.pop()
print(stack)

from collections import deque
queue=deque(["eric",'john','michael'])
queue.append("terry")
queue.append("graham")
print(queue.popleft())
print(queue.pop())

#列表解析
squares=[]
for x in range(10):
    squares.append(x**2)
print(squares)

squares2=list(map(lambda x:x**2,range(10)))
print(squares2)

print([x**2 for x in range(10)])
print([lambda x: x**2 for x in range(10)])

questions=['name','quest','favorite color']
answers=['lancelot','the holy grail','blue']
for q,a in zip(questions,answers):
    print("What is your {0} It's {1}.".format(q,a))

#注意 python 中 不同类型的对象 比较是合法的，只要这些对象具有合适的
#比较方法
print(0==0.0)
import sys
print(sys.path)
print(dir(sys))
print(dir())
import builtins
print(dir(builtins))
