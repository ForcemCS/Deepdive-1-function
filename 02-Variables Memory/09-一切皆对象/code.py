#py中一切皆对象（也就是说都是类的实例）

#任何对象都可以传递给函数，传递给函数的参数

a = 10 
print(type(a))  #<class 'int'>   a是int类的一个实例

b = int(10)

#help(int)

c = int('101', base=3)
print(c)               #10


# code 2 
def square(a):
    return a ** 2

print(type(square))


f  = square

print(id(f), id(square))

## code 3 

def cube(a):
    return a ** 3

def select_func(fn_id):
    if fn_id  == 1 : 
        return square
    else:
        return cube

f = select_func(1)

print(f is square)          #True


f = select_func(2)

print(f is cube)           #True


