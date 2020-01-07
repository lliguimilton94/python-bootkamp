# the goal of this script is to sum up all the numbers between
# N and M (inclusively), where N and M are both user inputs.

N = int(input("Enter lower limit: "))
M = int(input("Enter upper limit: "))

# Use a for loop
sum = 0
for number in range(N,M+1):
    sum += number

print("The total sum is: ", sum)
#    print("The type is:", type(sum))

print("Using a While Loop: ")
sum = 0
number = N
while number <= M:
    sum += number
    number += 1

print("The total sum is: ", sum)
