
def search(x, list):

    for index in range(0, len(list)):
        if list[index] == x:

            return index

my_list = [8, 3, 2, 44, 52, 90]
ans = search(44, my_list)
print(ans)
