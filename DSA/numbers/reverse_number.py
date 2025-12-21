# we r given a number, and we have to reverse it 

#TC=O(logn)
#SC=O(1)

n = 12345
num = n
result = 0

while num>0:
  last_digit = num%10
  result = (result*10) + last_digit 
  num = num//10

print("reverse of the given number is : ",result)

'''
Time Complexity (TC)

Loop runs once for each digit of the number.
O(d)=O(logn)
where d = number of digits in n.'''
'''

Space Complexity (SC)

Only constant extra variables are used (num, result, last_digit).
O(1)
'''

