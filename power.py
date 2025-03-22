def power(a, b):
    result = 1
    base = a  
    exponent = b  

    while exponent > 0:
        result *= base
        exponent -= 1

    return result


a = 3
b = 4
print(power(a, b))
