import sys

print(list(range(3, 6)))
args = [3, 6]
print(list(range(*args)))


def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(42)
print(f(0))
print(f(1))
pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
print(pairs.sort(key=lambda pair: pair[1]))
print(pairs)

# 编写 文档
def my_function():
    """Do nothing, but document it.
        NO, really, it doesn't do anything.
    """
    pass
#print(my_function.__doc__)
