# the goal of this script is to print all the odd numbers between
# 0 and N inclusively, where N is the user input
N = int(input("Enter an Uper Limit: "))

# use a for loop first
print("Using a for loop: ")
for number in range(0, N+1):
    if(number % 2 == 1):
        print(number)


# Use a while loop:
print("Using a while loop: ")
number = 1
while number <= N:
    if(number % 2 == 1):
        print(number)
        
number += 1
