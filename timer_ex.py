import time as t
import timeit
def a(x):
    return 10 * x

def time(f,x):
    start = t.clock()
    f(x)
    end= t.clock()
    return end - start

print(time(a,10))
print("----------")
print(timeit.timeit("a(10)", setup="from __main__ import a", number=1000))
