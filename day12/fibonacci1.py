# coding = utf-8
""" 
the better Fibonacci
"""
m = {0:0, 1:1}
def fib1(n):
    if not n in m:
        m[n] = fib1(n-1) + fib1(n-2)
    return m[n]

if __name__ == "__main__":
    f =fib1(10)
    print(f)
