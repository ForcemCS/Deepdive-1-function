# 类似C语言的for循环
i = 0 
while i < 5:
    print(i)
    i += 1

i = None

#可迭代的对象
for i  in range(5):
    print(i)
    
for c in 'hello':
    print(c)

print('-' * 20 )
    
for  a in [(1, 2), (3, 4), (5, 6)]:
    print(a)
print('-' * 20 )

for  a, b  in [(1, 2), (3, 4), (5, 6)]:
    print(a, b )
    
print('-' * 20 )

for i  in  range(5):
    
    if i == 3:
        continue
    print(i)
print('-' * 20 )

for i in  range(1, 5):
    
    if i % 7 == 0 :
        print('multiple of 7 found ')
        break

else:
    print('no multiples of 7 in range')
    
print('=' * 20 )

    
for i in range(5):
    print('-' * 20 )
    
    try:
        10 / (i - 3)
    except ZeroDivisionError:
        print('dividided by 0 ')
        continue
    finally:
        print('always run')
    
    print(i)
    
print('=' * 20 )

## code2

s = 'hello'
print(s[0])

for i  in range(len(s)):
    print(i, s[i])

print('-' * 20 )  
    
for i, c in enumerate(s):
    print(i, c)