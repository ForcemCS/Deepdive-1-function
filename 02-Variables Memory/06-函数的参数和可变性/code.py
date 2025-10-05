def process(s):
    s = s + ' world'
    return s

my_var = 'hello'

#my_var的引用传递给了process , 走到s = s + ' world'时候，s的引用发生了改变
#在模块作用域中my_var的引用没有改变
process(my_var)   


def process_1(lst):
    lst.append(100)
    
my_list = [1, 2, 3]

# module scope 和函数scope指向了同一个内存地址，调用函数之后，原来的my_list已经被修改，这就是所谓的副作用
process_1(my_list)


