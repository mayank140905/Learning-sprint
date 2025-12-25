# we r given an array, it maybe sorted or unsorted... doesn't matter
# user will enter a target value , and then output should be the index of that target value in the array, return -1 if not found.

# Time Complexity (TC) :  O(n) (considering worst case)
# Space Complexity = O(1)

nums = [5, 3, 9, 8, 1, 6, 4, -10, -100]

target = int(input("Enter target number: "))

def linear_search(nums, target):
    for i in range(0,len(nums)):
        if nums[i] == target:
            return i
    return -1

result = linear_search(nums, target)

if result != -1:
    print(f"Target found at index {result}")
else:
    print("Target not found")


'''
Time Complexity (TC)
Linear Search checks elements one by one from the beginning.

Best Case: O(1)
→ When the target is found at the first index.

Worst Case: O(n)
→ When the target is at the last index or not present in the array.

Average Case: O(n)

Time Complexity: O(n)

----------------------------------------------------------------------
Space Complexity (SC)

Only a constant number of variables are used.

No extra data structures are required.

Space Complexity: O(1)
'''