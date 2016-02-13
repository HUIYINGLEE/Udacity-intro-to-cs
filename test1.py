# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal 
# to the preceding number y, the number x should be inserted 
# into a sublist. Continue adding the following numbers to the 
# sublist until reaching a number z that
# is greater than the number y. 
# Then add this number z to the normal list and continue.

#Hint - "int()" turns a string's element into a number

def numbers_in_lists(string):
    num_list=[]
    i=0
    n=1
    inner=[]
    outer=[]
    for s in string:
        num_list.append(int(s))
    while i<=len(string)+1:
        while num_list[i]>=num_list[n]:
            if i==n-1:
                outer.append(num_list[i])
                print outer
            inner.append(num_list[n])
            print inner
            n=n+1
            if n==len(string):break
            print n
        print inner
        outer.append(inner)
        print outer
        i=i+n
        n=i+1
        if n==len(string)+1:break
        print i
        print n
        inner=[]
    return outer
#testcases
string = '543987'
numbers_in_lists(string)
#result = [5,[4,3],9,[8,7]]
#print repr(string), numbers_in_lists(string) == result
#string= '987654321'
#result = [9,[8,7,6,5,4,3,2,1]]
#print repr(string), numbers_in_lists(string) == result
#string = '455532123266'
#result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
#print repr(string), numbers_in_lists(string) == result
#string = '123456789'
#result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#print repr(string), numbers_in_lists(string) == result
