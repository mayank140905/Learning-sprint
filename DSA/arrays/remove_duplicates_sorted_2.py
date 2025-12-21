# we r given an array, and it contains duplicate elements... we need to remove duplicates, and also 
# return the number/count of unique elements (to be done in-place)

#TC = O(n)
#SC = O(1)

# method 2 -> 2 pointers method , no dictionary required
# here we use 2 pointers , i and j . 
# i starting from 0, j starting from i+1... j goes and check if j is not equal to i then i+1
# and swap i+1 with j and then j+1
# let's write in code to understand better

def remove_duplicates():
  nums = [1,1,1,2,3,4,4,7,9,9,9,10]     # given array
  n = len(nums)                         # to find length of array
  if n==1:
    return 1
  
  i = 0
  j = i+1
  while j < n:
    if nums[j] != nums[i]:
      i +=1
      nums[i],nums[j] = nums[j],nums[i]
    j+=1
  return i+1
  
print(remove_duplicates())