# fun arg

def func(x, *arg):
    print(x)
    result = x
    print(arg)
    for i in arg:
        result += i
    return result


print(func(1,2,3,4,5,6,7,8,9))



def fib(n):
    """
    This is Fibonacci by Recursion.
    
    :param n: 说明
    """
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fib(n-1) + fib (n-2)
    
f = fib(10)
print(f)