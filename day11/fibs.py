# Fibs

def fibs(n):
    """
    fibs 的 Docstring
    
    :param n: 说明
    """
    result = [0,1]
    for i in range(n-2):
        result.append(result[-1] + result[-1])
    return result

if __name__ == "__main__":
   lst = fibs(10)
   print(lst)

print(fibs.__doc__)
print(help(fibs))