import math

def f(x):
    return math.cos(x)

def find_root(a,b):
    c = (a + b)/2 # initial c
    ans = f(c)   # f(c)

    num_iterations = 0
    tolerance = 0.00001
    while ans != 0 and num_iterations < 1000 and ans > tolerance:
        num_iterations += 1
        #print(num_iterations)
        c = (a + b)/2
        ans = f(c)

        if (ans > 0):
            b = c
        elif (ans <0):
            a = c

        print(ans)

    if (num_iterations >= 1000 and f(c) != 0 and ans > tolerance):
        print("There are no zeros in this region with that tolerance")
        return none
    else:
        return c

lower = math.pi
upper = 2*math.pi

print(find_root(lower, upper))
print((3*math.pi)/2)
