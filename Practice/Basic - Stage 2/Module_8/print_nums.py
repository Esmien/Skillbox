def foo(a, b):
    if a == b:
        print(a)
        return
    else:
        foo(a+1, b)
        print(a)
foo(1, 5)