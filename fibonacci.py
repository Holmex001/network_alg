import numpy as np


# 递归算法
def fib_1 (n) :
    if n <= 1:
        return  n
    else :
        return  fib_1(n - 1) + fib_1(n -2)

# for
def fib_2 (n) :
    if n <= 1:
        return n
    a = 0
    b = 1
    for i in range(1,n):
        temp = a + b
        a = b
        b = temp

    return temp

# fast matrix powering
def fib_3 (n) :
    if n <= 1:
        return n
    else :
        a = np.matrix('1,1;1,0')
        b = np.matrix('1;0')
        a_n =  np.matrix('1,0;0,1')
        for i in range(0,n):
            a_n = np.matmul(a,a_n)

        c = np.matmul(a_n, b)
        c_value = c[1, 0]

        return c_value
