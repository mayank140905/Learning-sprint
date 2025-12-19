# we r given a list or array of numbers which can be both positive and negative
# and we have to find largest element in that list.

nums = [55,32,-97,99,3,67]

largest = nums[0]    # we will consider largest = nums[0], u can also take float("-inf")
n = len(nums)

for i in range(0,n):
  largest = max(largest,nums[i])

print(largest)


'''
Time Complexity (TC)

The loop runs once for each element in the array.

Time complexity = O(n)
'''

'''
Space Complexity (SC)

Only one extra variable (largest) is used.

Space complexity = O(1)
'''