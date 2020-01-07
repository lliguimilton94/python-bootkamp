# define f(x) = x + 1

def f(x):
    ans = x + 1
    return ans


my_solution = f(1)  # Defining the value of x
#print(my_solution)

# New function
# try for yourself:
# define a function of x, Where
# g(x) = X^4 + X^2 + 1

def g(x):
    return (x**4 + x**2 + 1)

#print(g(1),g(2),g(3))

# function with multiple returns

def get_first_two_even():
    return 2, 4

even1, even2, = get_first_two_even()
#print(even1)
#print(even2)

# function with no returns

def print_even(N): # where N is the upper limit
    for num in range(1, N+1): # N+1 means inclusive
        if num % 2 == 0:
            print(num)

#print_even(10) # 2,4,6,8,10 #important


# TODO: Write a function that takes N as an input and print
# all common multiples of 3 and 7, between 0 and N (inclusive)

#N = int(input("Enter an upper limit: "))

def print_common_multiples(N):
    for num in range(0, N+1): # can also add user input but print_common_multiples() *nothing in parenthesis*
        if (num % 3 == 0) and (num % 7 == 0):
            print(num)

#print_common_multiples(100)




# define a function that takes 3 inputs: x,y,N
# The function will find all the common multiples of x and y
# between 0 and N

def find_common_multiples():
    N = int(input("Enter an upper limit: "))
    x = int(input("Enter your first integer: "))
    y = int(input("Enter your second integer: "))
    for num in range(0, N):
        if (num % x == 0) and (num % y == 0):
            print(num)

find_common_multiples()
find_common_multiples()
