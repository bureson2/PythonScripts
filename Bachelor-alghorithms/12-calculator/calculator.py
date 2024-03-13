def addition(x, y):
    return float(x) + float(y)


def subtraction(x, y):
    return float(x) - float(y)


def multiplication(x, y):
    return float(x) * float(y)


def division(x, y):
    try:
        return float(x) / float(y)   
    except:
        raise ValueError('This operation is not supported for given input parameters')


def modulo(x, y):
    if x >= y and y > 0:
        return float(x) % float(y)
    else: 
        raise ValueError('This operation is not supported for given input parameters')

def secondPower(x):
    return float(x) ** 2


def power(x, y):
    if y >= 0:
        return float(x) ** float(y)
    else:
        raise ValueError('This operation is not supported for given input parameters')


def secondRadix(x):
    if x > 0:
        return float(x) ** 0.5
    else:
        raise ValueError('This operation is not supported for given input parameters')

def magic(x, y, z, k):
    try:
        return ((float(x)+float(k))/(float(y)+float(z)))+1
    except:
        raise ValueError('This operation is not supported for given input parameters')

def control(a, x, y, z, k):   
    if a == 1 or a == "ADDITION":
        return addition(x,y)
    elif a == 2 or a == "SUBTRACTION":
        return subtraction(x, y)
    elif a == 3 or a == "MULTIPLICATION":
        return multiplication(x, y)
    elif a == 4 or a == "DIVISION":
        return division(x, y)
    elif a == 5 or a == "MOD":
        return modulo(x,y)
    elif a == 6:
        return secondPower(x)
    elif a == 7 or a == "POWER":
        return power(x,y)
    elif a == 8 or a == "SECONDRADIX":
        return secondRadix(x)
    elif a == 9 or a == "MAGIC":
        return magic(x,y,z,k)
    else:
        raise ValueError('This operation is not supported for given input parameters')
        
print(control(5,1,1,1,1))

