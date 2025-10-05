# a = 10 
# b= a  #将b的内存引用设置为和a的内存引用一致

a = 'hello'
b = 'hello'

print(hex(id(a)),hex(id(b)))