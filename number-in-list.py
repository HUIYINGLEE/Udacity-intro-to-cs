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
    
    while i<=len(string)-1:
        if num_list[i]<num_list[n]:
          while num_list[i]<num_list[n]:
              outer.append(num_list[i])
              i=i+1
              n=n+1
              if n>=len(string):
                  break
          if len(outer)==len(string)-1:
             outer.append(num_list[n-1])
        if n>=len(string):break
        
        if num_list[i]>=num_list[n]:
          while num_list[i]>=num_list[n]:
              if i==n-1:
                  outer.append(num_list[i])
              inner.append(num_list[n])
              n=n+1
              if n>=len(string):break
          outer.append(inner)
          i=n
          n=i+1
          if n>=len(string):break
          inner=[]
    return outer
#testcases
string = '543987'
print numbers_in_lists(string)
#result = [5,[4,3],9,[8,7]]
#print repr(string), numbers_in_lists(string) == result
string= '987654321'
print numbers_in_lists(string)
#result = [9,[8,7,6,5,4,3,2,1]]
#print repr(string), numbers_in_lists(string) == result
string = '455532123266'
print numbers_in_lists(string)
#result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
#print repr(string), numbers_in_lists(string) == result
string = '123456789'
print numbers_in_lists(string)
#result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#print repr(string), numbers_in_lists(string) == result
