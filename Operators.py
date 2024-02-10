x = 5
y = 3

# +, *, -, /, %, ** (arithmetic operators)

z = x + y
print(z)
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)

# assignment operators

x = 10
x = x + 3
print(x)
x = +3
x = x - 4
x = -4

x = x*2
x*= 2
x=x/5
x/=5

# comparison operator
x=3
y=4

print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x<=y)
print(x>=y)

# logical operators (and, or & not)
x = 10
y = 20

print((x<y) and (y<x))
print((x>y) and (y>x))
print((x<y) and (x==y))
print((x<y) and (x<=y))

print((x<y) or (y>y))
print((x>y) or (y<x))
print((x<y) or (y<=x))
print((x>y) or (y==x))

print(not((x>y) and (x<y)))
print(not((x<y) and (x==y)))

# identity operators (is & is not)
x = 7
y = 6

print(x is y)
print(x is not y)