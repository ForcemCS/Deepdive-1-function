#py在某个内存地址上创建了一个整数类型的对象
# 我们可以跟踪这些在内存中创建的对象
my_var = 10

##如何发现引用计数
#sys.getrefcount(my_var) 当传递my_var来获取引用计算的时候，实际上是在内存中创建了对同一个对象的另一个引用
#ctypes.c_long.from_address(address).value   address 我们传递的是一个内存地址

import sys

a = [1, 2, 3]
print(id(a))
print(sys.getrefcount(a))       #2

import ctypes

def ref_count(address : int):
    print(ctypes.c_long.from_address(address).value)
    
ref_count(id(a))                #1 ,id(a) 已经释放了指针，所以是1

b = a
print(id(b))
ref_count(id(a))  # 2

b = None


a_id = id(a)

print(a_id)

ref_count(a_id)      # 1

#----------

a = None    #之前的内存地址释放了
ref_count(a_id)


