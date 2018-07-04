
def mul(*args):
    result = 1
    for n in args:
        result *= n
    print(result)

mul(1,2,3,4,5)