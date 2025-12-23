# shift every element to right by 1 index, and last one comes in the front of array i.e 0th index

#Time Complexity (TC) - O(n)
#Space Complexity (SC)- O(1)

# method-2) loop method, we will be using loop to access elements of array.... we have used reverse loop.

nums = [5, -2, 3, 9, 0, 6, 10, 7]
n = len(nums)

# store last element
temp = nums[n-1]

# shift elements right
for i in range(n-2, -1, -1):
    nums[i+1] = nums[i]

# insert last element at start
nums[0] = temp

# print array
for i in range(n):
    print(nums[i], end=",")



'''
Time Complexity (TC)

O(n)
→ ek loop chal raha hai poore array par (shifting)

💾 Space Complexity (SC)

O(1)
→ sirf ek variable temp use hua, no extra array'''