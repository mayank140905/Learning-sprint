# we r given a list or array of numbers which can be both positive and negative
# and we have to find second largest element in that list.
# there are three methods to do that

#Time Complexity = O(n + n) = O(n)
#Space Complexity = O(1)

# 2) double loop method - we find largest annd s_largest, in different loops

nums = [55, 32, -97, 99, 3, 67]

largest = float("-inf")
s_largest = float("-inf")       
n = len(nums)

for i in range(0,n):
  largest = max(largest, nums[i])

for i in range(0,n):
  if nums[i] > s_largest and nums[i] != largest:
    s_largest = nums[i]
print(s_largest)


'''
Time Complexity (TC)

There are two loops, and each loop runs n times.

So,
Time Complexity = O(n + n) = O(n)
'''

'''
Space Complexity (SC)

Only constant extra variables are used:

largest,s_largest
No extra data structures.

So,
Space Complexity = O(1)
'''