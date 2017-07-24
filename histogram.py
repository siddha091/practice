''''Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example,
        histogram([4, 9, 7]) should print the following
'''




def histogram(list1):
    for n in list1:
        print nestFun(n,'*')

def nestFun(n,str):
    result = " "
    for x in range(n):
        result += str
    return result

print histogram([1,2,3])