'''
The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two
        and three numbers, respectively. But suppose we have a much larger number of numbers, or suppose we cannot tell
        in advance how many they are? Write a function max_in_list() that takes a list of numbers and returns the largest one

'''

def max_in_list(list1):
    sortedList = sorted(list1)

    # to return the largest one
    return sortedList[-1]


List = [1, 0, 3, 6, 12, 2342, 2345, 10037266, 2, 4, 8]

print("The list is: " + str(List))

print("The max in the list is: " + str(max_in_list(List)))