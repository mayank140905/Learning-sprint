# shift every element to right by 1 index, and last one comes in the front of array i.e 0th index
#TC = O(n)
#SC = O(n)

nums = [5,-2,3,9,0,6,10,7]
# we know arrays can be splitted into 2 different arrays, and joined two arrays to form a single one.

n = len(nums)

# nums = [nums[n-1]]+nums[0:n-1]        # will be saved in new address of nums
nums[:] = [nums[n-1]]+nums[0:n-1]     # will be saved in same address of nums

def printarr(nums):
  for i in range(0,n):
    print(nums[i],end=",")

printarr(nums)


#note - i did a mistake here, of adding list with int... list can be added with list only

'''
Time Complexity (TC)
1. Rotation line:

nums[:] = [nums[n-1]] + nums[0:n-1]
nums[n-1] → O(1)
nums[0:n-1] slicing → O(n)
creating new list with + → O(n)
assigning back to nums[:] → O(n)
so,
TC = O(n)

Space Complexity (SC)

Temporary list created during rotation:
[nums[n-1]] + nums[0:n-1] → size n → O(n) extra space
printarr() uses no extra memory → O(1)
Final SC = O(n)
'''