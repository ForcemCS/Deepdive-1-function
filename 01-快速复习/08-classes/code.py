# code1
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
r1 = Rectangle(10, 20)
print(r1.width)

r1.width = 100
print(r1.width)


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    # some 这个参数就是用来接收那个新创建的、空的“空壳子”实例的。
    def perimeter(some):
        return 2 * (some.width + some.height)

# Python 在背后会做两件主要的事情：
# 创建实例 (Creation): Python 首先在内存中创建一个空的 Rectangle 类的实例。可以想象成一个没有任何属性的“空壳子”。
# 初始化实例 (Initialization): Python 接着自动调用 __init__ 方法，并且将刚刚创建的那个“空壳子”实例作为第一个参数传递进去。你提供的其他参数（10 和 5）会作为后续的参数（width 和 height）传递。

# 所以，r1 = Rectangle(10, 20) 这行代码，实际上触发了类似下面的调用：

# # 1. 创建一个空实例，我们暂时叫它 new_instance
# new_instance = object.__new__(Rectangle) 

# # 2. 自动调用 __init__，把这个新实例作为第一个参数传入
# Rectangle.__init__(new_instance, 10, 20) 

# # 3. 最后，将这个初始化好的实例赋值给 r
# r1 = new_instance
    
r1 = Rectangle(10, 20)

print(r1.area(), r1.perimeter())


print(str(r1))
print(hex(id(r1)))


# code2 

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def to_string(self):
        return 'Rectangle : width={0}, heigth={1}'.format(self.width, self.height)
    
print(Rectangle(10, 20).to_string())


## code3 

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return 'Rectangle : width={0}, heigth={1}'.format(self.width, self.height)
r1 = Rectangle(10, 20)    
print(str(r1))                #Rectangle : width=10, heigth=20

#字符串表示
l = [1, 2, 3]
print(str(l))


# code4 


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return 'Rectangle : width={0}, heigth={1}'.format(self.width, self.height)
    
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self.width, self.height)  == (other.width, other.height)
        else:
            return False
r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)
print(r1 == r2)

print(r1 == 100)


# code 5 

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    def get_width(self):
        return self._width
    
    def set_width(self, width):
        if width <= 0 :
            raise ValueError('width must be positive')
        else:
            self._width = width
            

    def get_height(self):
        return self._height
    
    def set_height(self, height):
        if height <= 0 :
            raise ValueError('height must be positive')
        else:
            self._height = height
    
    def __str__(self):
        return 'Rectangle : width={0}, heigth={1}'.format(self._width, self._height)
    
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self._width, self._height)
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self._width, self._height)  == (other._width, other._height)
        else:
            return False
        



# code 6

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        if width <= 0 :
            raise ValueError('width must be positive')
        else:
            self._width = width
    
    def __str__(self):
        return 'Rectangle : width={0}, heigth={1}'.format(self.width, self.height)
    
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self.width, self.height)  == (other.width, other.height)
        else:
            return False
        
        
r1 = Rectangle(20, 20)
print(r1.width)

r1.width = 200
print(r1.width)

r1.width = -200
print(r1.width)