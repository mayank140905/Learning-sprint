# we will reverse an array using two pointers
#TC = O(n)
#SC = O(1)

nums = [1,2,3,4,5,6,7,8,9,10]

def reverse(nums,left,right):
  while left < right:
    nums[left],nums[right] = nums[right],nums[left]
    left += 1
    right -= 1

n = len(nums)
reverse(nums,0,n-1)

def printarr(nums):
  for i in range(0,n):
    print(nums[i],",",end="")

printarr(nums)


'''
Time Complexity (TC)
1. reverse(nums, 0, n-1)
The while-loop runs until left < right → roughly n/2 swaps →
TC = O(n)

2. Printing loop
Runs n times → O(n)
Final TC = O(n)


Space Complexity (SC)
we're swapping in-place, no extra array:
Only temporary variables for swap → O(1)'''

