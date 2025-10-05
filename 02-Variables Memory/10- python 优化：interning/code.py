## 指向了同一个内存地址
a = 10 
b = 10 


## 指向了不同的内存地址
# 在启动cpython时候，预加载或者缓存一个范围为-5至256的整数的全局列表
# 小整数在我们的代码中频繁的出现
a = 500
b = 500


### String Interning(字符串驻留)
# 1.为什么优化
# 对于内容相同的字符串，只在内存中保存一份。之后所有用到这个字符串的地方，都指向这同一份内存地址。
# 在Python中，我们大量使用字符串，尤其是在字典（dictionary）中作为键（key）。比如，当你在代码里访问一个对象的属性 my_object.name 时，Python内部实际上是在一个类似字典的结构里查找一个叫 "name" 的字符串键。
# 每次查找，Python都需要确认你提供的键和字典里已有的键是否相等。

# 2.字符串驻留 (String Interning) 的魔法
# 现在我们知道了 is 比较很快，但问题是，通常情况下，即使两个字符串内容一样，它们也可能是两个不同的对象，存放在内存的不同位置。

# 假设没有字符串驻留
a = 'some_long_string'
b = 'some_long_string'

# a 和 b 的内容相同，但它们是两个独立的对象，内存地址不同
# a == b  会是 True
# a is b  会是 False 

# **字符串驻留（Interning）**就是为了解决这个问题。它的工作方式如下：

# Python内部维护一个“字符串池”（String Pool）。当你创建一个字符串时：

# Python会先检查这个“字符串池”里是否已经存在一个内容完全相同的字符串。
# 如果存在：Python不会创建新的字符串对象，而是直接把池中那个已存在的对象的内存地址，赋给你的新变量。
# 如果不存在：Python会创建一个新的字符串对象，把它放入“字符串池”中以备后用，然后把这个新对象的内存地址赋给你的变量。
# 经过这个“驻留”处理后，所有内容为 'some_long_string' 的字符串变量，实际上都指向了内存中的同一个对象。

# 3. 你可以使用 sys.intern() 函数来手动强制驻留一个字符串。

a = 'hello'
b = 'hello'

print(id(a), id(b))

c = 'hello world1'
d = 'hello world1'
print(id(c), id(d))

print(c is d)


import sys
import time

def compare_using_equals(n):
    a = 'a long string  that is not  interned' * 200
    b = 'a long string  that is not  interned' * 200
    
    for i in range(n):
        if a == b:
            pass
        
def compare_using_interning(n):
    a = sys.intern('a long string  that is not  interned' * 200)
    b = sys.intern('a long string  that is not  interned' * 200)
    
    for i in range(n):
        if a is b:
            pass
        

start = time.perf_counter()
compare_using_equals(100000)
end = time.perf_counter()
print(end - start)


start = time.perf_counter()
compare_using_interning(100000)
end = time.perf_counter()
print(end - start)