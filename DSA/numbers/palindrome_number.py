# palindrome - a number or string is said to be a palindrome, if it and it's reverse are same/equal.

def palindrome():
  n = int(input("enter your number : "))
  num = n
  result = 0

  while num>0:
    last_digit = num%10
    result = result*10 + last_digit
    num = num//10

  if n==result:
    print("yes, it's a palindrome.")
  else:
    print("no, it's not a palindrome.")

palindrome()




'''
Time Complexity (TC)

The while loop runs once for each digit of the number.
O(d)=O(logn)
where d = number of digits in n.
'''

'''
Space Complexity (SC)

Only constant extra variables are used (num, result, last_digit).
O(1)  
'''