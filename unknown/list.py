"""Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where
each command will be of the  types listed above. Iterate through each command in
order and perform the corresponding operation on your list.
"""

n = input("enter a number:")

arr = []

for x in range(n):
    s = raw_input("Enter numbers").split()
    cmd = s[0]
    args = s[1:]
    if cmd != "print":
        cmd += "("+",".join(args) + ")"
        eval("arr."+cmd)
    else:
        print arr
    
    
