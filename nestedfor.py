
"""Define a function overlapping() that takes two lists and returns True if they have at least one member in common,
        False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise,
        you should (also) write it using two nested for-loops
"""

def overlapping(list1, list2):
    for elem1 in list1:
        for elem2 in list2:
            if elem1 == elem2:
                return True
    return False


print overlapping([1, 2], [3, 4])
print overlapping([1, 2], [2, 3])
print overlapping([5, 6,7], [7, 8])