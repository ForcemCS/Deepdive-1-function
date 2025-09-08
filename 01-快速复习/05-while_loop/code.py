i = 0 
while i < 5:
    print(i)
    
    i += 1
    
#至少运行一次
i = 6

while True:
    print(i)
        
    if  i >=6:
        break             #跳出整个while
    print('something')


## cod2 ,参数位置索引
print("坐标: x={0}, y={1}".format(10, 20))


## code3

min_length = 2
name = input("Please enter your name: ")  #并把输入的字符串保存到 name 变量。

#name.isprintable()         # 输入的字符都是可打印字符（没有换行符、控制字符等）
# 输入的字符全是字母（不能有数字或符号）
while not(len(name) >= min_length and name.isprintable() and name.isalpha()):
    name = input("Please enter your name: ")

print("Hello, {0}".format(name))

##等效代码如下
min_length = 2

while True:
    name = input("请输入你的名字: ")
    if len(name) >= min_length and name.isprintable() and name.isalpha():
        break

print("欢迎, {0}".format(name))


## code4 
a = 0 
while a < 10:
    a += 1 
    if a % 2 == 0:
        continue     #满足条件，不走下边的内容
    print(a) 
    
## code5 

l = [1, 2, 3]
val = 10 

found  = False
idx = 0 

while idx <len(l):
    
    if l[idx] == 10:
        found = True
        break
    idx += 1 

if not found:
    l.append(10)
print(l)

## code6 
l = [1, 2, 3]
val = 10

idx = 0 

while idx < len(l):
    if l[idx] == val:
        break
    idx += 1
else:
    l.append(10)
print(l)

 