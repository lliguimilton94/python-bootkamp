#TODO: Write a function that takes integer and a list as the input.
# The function should return the index of where the integer was found
# On the list

def search(x, list):
    """
    this function returns the index of where the element x was found
    on the list.

    \tparam : x - the element you're searching for
    \tparam : lst - the list you're searching through
    \treturns : the index of where the element was found  (if applicable)
    """
    for index in range(0,len(list)):
        if list[index] == x:

            return index

my_list = [10, 8, 7, 19, 42, 2]
ans = search(10, my_list)
print(ans)


def find_max(list):
    """
    this function returns the maximum element in the List

    \tparam : lst - a list of numerical elements
    \treturns : the maximum value in the List
    """
    max = list[0]

    for i in range(0,len(list)):
        if list[i] >= max:
            max = list[i]
    return max

my_list = [10, 8, 19, 42, 17, 20]
print(find_max(my_list))



# max = list[0]

#    for element in list:
     #if element >= max:
        #    max = element
#    return max

# my_list = [10, 8, 19, 42, 17, 20]
# print(find_max(my_list))
