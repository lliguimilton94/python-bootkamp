# finding the roots of a function between a specific region

def f(x):
    return x**2 - 16

def find_root(a,b):
    c = (a + b)/2 # initial c
    ans = f(c)   # f(c)

    num_iterations = 0
    while ans != 0 and num_iterations < 1000:
        num_iterations += 1
        #print(num_iterations)
        c = (a + b)/2
        ans = f(c)

        if (ans > 0):
            b = c
        elif (ans <0):
            a = c
    if (num_iterations == 1000 and f(c) != 0):
        print("There are no zeros in this region")
    else:
        return c

lower = -2
upper = 2

print(find_root(lower, upper))
