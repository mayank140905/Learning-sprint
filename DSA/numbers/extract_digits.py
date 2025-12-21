# we r given a number, and asked to extract its digits one by one.

# on floor division by 10 and remainder operator
# we get the last digit and also reduce the number by 1 digit.

#TC = O(logn)
#SC = O(1)

n = int(input("enter your number : "))
num = n
digits = []

while num > 0:
    digits.append(num % 10)
    num //= 10

print(digits)

''' Time complexity 
as loop depends on number of digits,
if:
digits in n = d

Loop:
with every iteration, removing 1 digit
Total iterations = d
so time complexity = O(d) 
d = log10​(n) 
so, So you can also say: TC = O(logn)
 
'''

''' Space complexity 
The space complexity is also O(d) due to storing digits in a list.
'''

'''
Can we reduce space complexity?
Yes, by printing digits directly instead of storing them
That would make SC = O(1)
'''
