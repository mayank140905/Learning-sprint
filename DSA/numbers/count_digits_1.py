# to count digits in a number, there r 2 ways
# 1st method - loop, keep doing floor division until it becomes zero.

def count_digits():
  n = int(input("enter your number: "))
  num = n
  count = 0    # we will be adding 1 here on every division

  while num>0:
    num = num//10
    count += 1
  
  print(count)

count_digits()


'''
Time Complexity (TC)

The loop runs once for each digit in the number.

So, the time complexity is O(d), where d is the number of digits in the number.
In terms of the value of the number, this is O(log n).
'''

'''
Space Complexity (SC)

The code uses only a few variables (num and count).
No extra data structures are used.
So, the space complexity is O(1).
'''