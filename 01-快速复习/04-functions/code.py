import math
print(math.exp(1))   #e

def func_1(a: int, b: int):         #int只是一个提示的作用,多态性
    return a * b 

print(func_1('a', 3))

print(func_1([1, 2], 3))            #[1, 2, 1, 2, 1, 2]

def func_2():
    print('running func_2')
    
print(type(func_2))


#----------
#def _tmp(x):
#    return x + 5
fn1 = lambda x : x ** 3              #将匿名函数赋值给变量fn1

print(fn1(2))

