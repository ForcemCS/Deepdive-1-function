#常量表达式或计算结果为常量的表达式会被预先计算和存储
# short squences 长度小于20 也会被存储

# “窥孔优化”（Peephole Optimization）
# 你可以把编译器想象成一个工匠，他正在检查一行行刚刚写好的代码。所谓“窥孔”，就是指他只通过一个小孔（a small peephole）去看一小段（通常是几条）相邻的指令。当他发现这段指令可以用更少、更快的指令来替代时，他就会直接进行替换。
# 这种优化是局部的、简单的、但非常有效的。


# 自动优化：编译器自动将可变（mutable）的常量数据结构替换为不可变（immutable）的。
# 建议优化：建议程序员手动选择速度更快的数据结构（set）来进行成员测试。
for i in range(1000):
    if i in [1, 2, 3]:  # 这里会创建1000次新的列表 [1, 2, 3]，实际上是用的同一个元组对象 (1, 2, 3)
        ...
        
# lists -> tuples （列表常量被优化成元组）
# sets -> frozensets （集合常量 {1, 2, 3} 被优化成不可变集合 frozenset({1, 2, 3})）

def  my_func(e):
    if e in [1, 2, 3]:
        pass
print(my_func.__code__.co_consts)         #(None, (1, 2, 3))



def  my_func(e):
    if e in {1, 2, 3}:
        pass
print(my_func.__code__.co_consts)         #(None, frozenset({1, 2, 3}))


## code2 
import  string
import time

char_list = list(string.ascii_letters)
print(char_list)
char_tuple = tuple(string.ascii_letters)    #list tuple都是有序序列

char_set = set(string.ascii_letters)

def membership_test(n, container):
    for i in range(n):
        if 'z' in container:
            pass
        
start = time.perf_counter()
membership_test(100_000_000, char_set)
end = time.perf_counter()
print('set: ', end - start)