s='hello world!'
print(str(s))
print(repr(s))
x=10*3.25
y=200*200
s='the value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),end=' ')
    print(repr(x**3).rjust(4))
for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x,x**2,x**3))
print('-0.12'.zfill(6))

table={'sjorsded':4127, 'Jack':40298}
print(table)
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name,phone))