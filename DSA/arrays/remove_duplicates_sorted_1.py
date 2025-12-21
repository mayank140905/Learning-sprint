# we r given an array, and it contains duplicate elements... we need to remove duplicates, and also 
# return the number/count of unique elements (to be done in-place)

# TC -> O(N+N) 
# SC -> O(N)   

# the primary concept that we will use is dictionary, as it stores unique keys only(no duplicacy)
# and order is also maintained

# method 1 -> 2 loops method, dictionary required

nums = [1,1,1,2,3,4,4,7,9,9,9,10]     # given array
n = len(nums)                         # to find length of array
my_dict = {}                          # created an empty dictionary

for i in range(0,n):
  my_dict[nums[i]] = 0                # assigning 0 values to keys, u can assign anything...

j = 0 
for k in my_dict:
  nums[j] = k                         # putting back every key from 0th index in list
  j+=1
print(j)                              # to find number of unique of elements i.e j



'''
worst case- when all elements are unique
TC -> O(N+N) as 2 loops will run till n
SC -> O(N)   as N variables will be stored
''' 