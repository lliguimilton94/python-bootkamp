counter = 0
while counter <= 0:
    print(counter)
    counter += 1

# range(start, stop, increment)
# range function does not include stop number
# increment by defualt is 1

print("using three input to range()")
for number in range(0,5,1):
    print(number)

print("using one input to range()")
for number in range(5):
    print(number)
