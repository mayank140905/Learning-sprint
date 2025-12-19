# we r given with an array and we have to check if it is already sorted or not.

arr =[12,14,16,18,20]
n = len(arr)

def check(arr):
  for i in range (0,n-1):
    if arr[i] > arr[i+1]:
      return False
  return True

print(check(arr))


'''
Time Complexity (TC)

The loop runs once for each adjacent pair in the array.

So,
Time Complexity = O(n)
'''

'''
Space Complexity (SC)

No extra data structures are used.
Only a few variables.

So,
Space Complexity = O(1)
'''