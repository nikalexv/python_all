def m(f, v):
    print('m=',f(f(v)))
    return f(f(v))

def func(n):
    print('n*n=', n*n)
    return n*n


print(m(func, 2))
