# brute force - check in a loop upto that no from 1, whatever leaves remainder 0, on dividing. Then that  no is a factor.

# TC - O(N) 
# SC - O(k)

num = int(input("enter the number: "))
result = []

for i in range(1,num+1):
  if num%i == 0:
    result.append(i)
print(result)





'''
Time Complexity - cuz loop will till number

Space Complexity - k would be total number of factors.
'''