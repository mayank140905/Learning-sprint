# we r given an sorted array, and numbers r even repeated...
# we have to tell first and last occurence of that number, basically index.
# this is another variant of binary search question, or you can say linear search

nums = [1,2,3,3,3,3,3,5,6,8,9,9,10]

target = int(input("enter target value: "))

# we will use two more variables, first and last both equal to -1 , and will update both when the target value is matched
# but then stop updating the first one, only last will get updated later

def occurence(nums,target):
  first = last = -1
  n = len(nums)
  for i in range(0,n):
    if nums[i] == target:
      if first == -1:
        first = i
      last = i
  return [first,last]
  
result = occurence(nums,target)

if result[0] != -1:                          
  print(f"Target found at indices {result}")
else:
  print("Target not found")



'''
Time Complexity (TC)

This is Linear Search, array is scanned once.

Best Case: O(n)
(Even if found early, you still scan to get the last occurrence)

Worst Case: O(n)
(Target appears at the end or multiple times)

Average Case: O(n)

Overall Time Complexity: O(n)
------------------------------------------------------------------
Space Complexity (SC)

Only a few variables (first, last, i)

No extra data structures

Space Complexity: O(1)'''