gl = 0


def factorial(n):
    if n == 1: return 1
    return n * factorial(n - 1)


def sum(n):
    """This function calculates the summation of 1 + 1/2 + 1/3 + ... 1/n"""
    if n == 1: return 1
    global gl
    gl += 1 / n
    sum(n - 1)

def sine_x(x,n):
    fnl = 0
    step = lambda a, b: ((-1 ^ b) * a ^ (2 * b + 1)) / (factorial(2 * b + 1))
    for i in range(n):
        fnl += step(x, i)
    fnl /=180 #to make it radian
    return fnl


a = factorial(5)
print(a)
print(sum.__doc__)
sum(5)
print(gl)

k = int(input("Enter x value: "))
l = int(input("Enter n value: "))
print(sine_x(k, l))

