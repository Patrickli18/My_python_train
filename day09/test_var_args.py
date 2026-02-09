# Test var args

def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:",arg)
    
test_var_args("yasoob","python","egg","test")


print("#"*10)

def get_me(**kwargs):
    for key,value in kwargs.items():
        print("{0} == {1}".format(key,value))

get_me(name = "yasoob")

print("#"*10)


def test_args_kwargs(arg1,arg2,arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


arg = ("two", 3 ,5)

test_args_kwargs(*arg)
