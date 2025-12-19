# we r given a list or array of numbers which can be both positive and negative
# and we have to find second largest element in that list.
# there are three methods to do that

# 3) single loop method - we find largest annd s_largest, in a single loops (MOST OPTIMAL METHOD)

nums = [55, 32, -97, 99, 3, 67]

largest = float("-inf")
s_largest = float("-inf")       
n = len(nums)

for i in range(0,n):
  if nums[i] > largest:
    s_largest= largest
    largest = nums[i]
  elif nums[i] > s_largest and nums[i] != largest:
    s_largest = nums[i]

print(s_largest)

'''
Time Complexity (TC)

There is only one loop, and it runs n times.

So,
Time Complexity = O(n)
'''

'''
Space Complexity (SC)

Only a few variables are used:

largest

s_largest

No extra data structures.

So,
Space Complexity = O(1)
'''