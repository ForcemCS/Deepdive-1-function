a = 0 
b = 2

while a < 4:
    print('-----------')
    
    a += 1
    b -= 1 
    try:
        a /b
    except ZeroDivisionError:
        print("{0}, {1} - division by 0".format(a, b))
        continue                              # 下边的内容不会执行，但是finally会执行
    finally:
        print("{0}, {1} - always executes".format(a, b))
    
    print("{0}, {1} - main loop".format(a, b))
    
a = 0 
b = 10



while a < 4:
    print('-----------')
    
    a += 1
    b -= 1 
    try:
        a /b
    except ZeroDivisionError:
        print("{0}, {1} - division by 0".format(a, b))
        break                              # 捕获了异常之后，else的内容就不会执行了
    finally:
        print("{0}, {1} - always executes".format(a, b))
    
    print("{0}, {1} - main loop".format(a, b))

else:
    print('Code executed without a zero division error')