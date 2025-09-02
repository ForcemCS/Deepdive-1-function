a = [1, 2, 3]

a = [ 1, 2, 
     3, 4, 5 ]

a = [1 # item 1 
     , 2]

a = (1  ##comment
    ,2 ##comment
    ,3)


a = {'key1': 1 # value for key1
    ,'key2': 2 # value for key2
    }
     
     
def my_func(a,  # this is used for indicate....
            b,  # comment
            c):
    print(a, b, c)

my_func(10, 20, 30)


a = 10 
b = 20
c = 30

if a > 5 and b > 10 and c > 20:
    print('yes')


if a > 5 \
    and b > 10 \
        and c > 20:
    print('yes')
    
a = '''This is 
is a string'''

print(a)

a = '''
    * 
   * * 
  * * * 
'''
print(a)