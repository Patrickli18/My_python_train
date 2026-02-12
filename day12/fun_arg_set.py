#coding:utf-8

def power_seq(func,seq):
    return [func(i) for i in seq]
def pingfang(x):
    return x ** 2

########################################

def string_def(func,str):
    return [func(i) for i in str]

def str1(x):
    return(str(x))



if __name__ == "__main__":
    num_seq = [111,3.14,2.91]
    r = power_seq(pingfang,num_seq)
    print(num_seq)
    print(r)

    print("\n\n******************")

    mun1 = [11,22,33,"44c",232,543545,"fd4564"]

    s = string_def(str1,mun1)
    print(mun1)
    print(s)






