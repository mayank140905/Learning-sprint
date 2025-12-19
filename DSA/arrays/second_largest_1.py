# we r given a list or array of numbers which can be both positive and negative
# and we have to find second largest element in that list.
# there are three methods to do that

# 1) sort method - use .sort and print last 2nd element.

nums = [55, 32, -97, 99, 3, 67]
nums.sort()
print(nums[-2])

'''
Time Complexity (TC)

The main operation here is nums.sort().

Python sorting takes O(n log n) time, where n is the number of elements in the list.

So,
Time Complexity = O(n log n)
'''

'''
Space Complexity (SC)

list.sort() sorts the list in-place and does not create a new list.

Extra space used is constant.

So,
Space Complexity = O(1)
'''