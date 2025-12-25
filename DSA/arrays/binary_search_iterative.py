# we will be doing iterative binary search, array must be sorted
# we r gonna define a search space, from low to high
# then we find middle element, and keep minimising search space , if element found - return index , not found - return -1

# Time Complexity = O(log n)
# Space Complexity = O(1)

nums = [2,4,6,7,9,11,18,19]

target = int(input("enter target value: "))

def binary_search(nums, target):
  n = len(nums)
  low = 0
  high = n-1

  while low <= high:           # loop will run until low is less than or equal to high
    mid = (low+high)//2
    if nums[mid] == target:
      return mid
    elif nums[mid] <= target:
      low = mid+1
    else:
      high = mid-1

  return -1

result = binary_search(nums,target) 

if result != -1:
    print(f"Target found at index {result}")
else:
    print("Target not found")


'''Time Complexity (TC)
This is an iterative Binary Search.

Best Case: O(1)
→ When the target is found at the middle index in the first comparison.

Worst Case: O(log n)
→ The search space is halved at every step until the element is found or the range becomes empty.

Average Case: O(log n)

Overall Time Complexity: O(log n)

 
Space Complexity (SC)
The algorithm uses only a few variables (low, high, mid).
No extra data structures or recursive calls are used.

Space Complexity: O(1)
'''