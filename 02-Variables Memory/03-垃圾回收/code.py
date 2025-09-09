
import ctypes
import gc    #垃圾收集模块

def ref_count(address: int):
    """通过内存地址获取对象的引用计数"""
    print(ctypes.c_long.from_address(address).value)

def object_by_id(object_id: int):
    """根据对象的ID（内存地址）查找对象是否存在"""
    for obj in gc.get_objects():
        if id(obj) == object_id:
            print("Object exists")
    print("Not Found")

class A:
    def __init__(self):
        # 注意这里的 print 语句修正了
        print('A 对象被创建, self 的地址是: {}'.format(hex(id(self))))
        self.b = B(self) # 创建一个B的实例，并把A的实例(self)传给B

class B:
    def __init__(self, a: A):
        # 注意这里的 print 语句也修正了
        print('B 对象被创建, self 的地址是: {}, 传入的 a 的地址是: {}'.format(hex(id(self)), hex(id(a))))
        self.a = a # B的实例保存了对A实例的引用

gc.disable()
my_var = A()

a_id = id(my_var)
b_id = id(my_var.b)

print(a_id, b_id)

my_var = None

ref_count(a_id),ref_count(b_id)


##手动启用垃圾回收
gc.collect()
object_by_id(a_id)