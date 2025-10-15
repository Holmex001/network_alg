class Num:
    def __init__(self, digit:int, coefficient:list):
        if digit is None:
            self.digit = 0
        if coefficient is None:
            self.coefficient = []

        self.digit = digit
        self.coefficient = coefficient

    def __str__(self):
        out = ""
        for i in range(self.digit, -1, -1):
            out = out + str(self.coefficient[i])
        return out

def mult_one(x1:Num, x2, digit):
    coefficient = []
    for i in range(0,x1.digit + digit + 1 + 1):
        coefficient.append(0)
    out = Num(0,coefficient)
    flag = 0

    for i in range(0, x1.digit+1):
        out.coefficient[i+digit] = x2 * x1.coefficient[i]
        if flag == 1:
            out.coefficient[i + digit] += 1
            flag = 0
        if out.coefficient[i+digit] >=10:
            out.coefficient[i+digit] = out.coefficient[i+digit] % 10
            flag = 1
    out.digit = x1.digit + digit
    if flag == 1:
        out.coefficient[x1.digit + digit + 1] = 1
        out.digit = x1.digit + digit + 1
    return out


def alg_1(x1:Num, x2:Num):
    out = []
    out_x = Num(0,[])
    for i in range(0, x2.digit + 1) :
        out_temp = mult_one(x1,x2.coefficient[i],i)
        out.append(out_temp)
    flag = 0
    temp = 0
    for i in range(0, x1.digit + x2.digit + 1):
        if flag != 0:
            temp += flag
        for out_temp in out:
            if out_temp.digit >= i:
                temp += out_temp.coefficient[i]
        flag = int(temp / 10)
        out_x.coefficient.append(temp % 10)
        temp = 0
    if flag != 0:
        out_x.coefficient.append(flag)
    out_x.digit = len(out_x.coefficient) - 1

    return out_x





x1 = Num(3,[3,4,1,1])
x2 = Num(3,[3,4,1,1])
out = alg_1(x1,x2)

print(out)



