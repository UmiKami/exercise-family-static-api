def foo1(a):
    # function block
    a += 1
    print('id of a:', id(a))  # id of y and a are same
    print(a)
    return a

# main or caller block
x = 10
y = foo1(x)

# value of x is unchanged
print('x:', x)

# value of y is the return value of the function foo1
# after adding 1 to argument 'a' which is actual variable 'x'
print('y:', y)

print('id of x:', id(x))    # id of x
print('id of y:', id(y))    # id of y, different from x