# to count digits in a number, there r 2 ways
# 2nd method - log method, find log10(N) of that number and then add 1.

from math import *
def countDigits(num):
  print(int(log10(num)+1))

countDigits(182)

'''
Time Complexity (TC)

This is a constant-time math operation.

Time complexity = O(1)
'''

'''
Space Complexity (SC)

No extra space is used.

Space complexity = O(1)
'''