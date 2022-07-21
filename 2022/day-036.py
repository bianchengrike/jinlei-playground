# Argument Tuple packing
arg_1 = [1,2,3]

def a(*arg):
    for i in arg:
        print(i)

a(arg_1)

# Argument Tuple Unpacking
 arg_2 = [1,2,3]

 def b(a,b,c):
    print(a)
    print(b)
    print(c)


b(*arg_2)