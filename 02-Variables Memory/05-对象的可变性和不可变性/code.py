#更改对象内部的数据称为修改对象的内部状态

#内部状态可以改变的对象称为可变对象(mutable)

#1.immutable
# Numbers(int, float, booleans,etc)
# strings
# tuples
# frozenset
# 用户定义的类（你不允许任何方式修改对象的内部状态）


#2.mutable
# lists
# sets
# dictionaries
# 用户定义的类（允许修改对象的内部状态）


my_1 = [1, 2, 3]
my_2 = [1, 2, 3]

print(id(my_1))
print(id(my_2))


my_list_1 = [1, 2, 3]
print(id(my_1))
my_list_1.append(4)
print(id(my_1))


my_dict = dict(key1=1 , key2='a')
print(id(my_dict))
my_dict['key2'] = 3
print(id(my_dict))

print('_' * 20 )


# code 2
# 元组的元素是对象的引用，不是对象本身
# 元组本身用来存储：
#   长度信息
#   对象头信息（类型、引用计数）
#   对元素的引用（指针）
t = 1, 2, 3
print(id(t))
print(id(t[0]))   # t[0] 是对整数对象 1 的引用。


