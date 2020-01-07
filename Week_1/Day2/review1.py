# TODO: write a script that prints out the multiples of 3
# between 0 and N, where N is the user input

N = int(input("Enter an upper limit: ")) # Making string into an integer

for num in range(0,N+1):
    if num % 3 == 0:
       print(num)

# Using a While loop
counter = 0
while counter <= N:
    if (counter % 3 == 0):
        print(counter)

    counter += 1
