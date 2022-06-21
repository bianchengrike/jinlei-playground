# Functional Programming
def func():
    print("Hello World")

d = {"cat": 1, func: 2, 42: 3}

d

d[func]

f  = "ff"

d_f = {"cat": 1, f: 22, 42: 3}

d_f

d_f[f]
d_f["ff"]

id(f)
id("ff")