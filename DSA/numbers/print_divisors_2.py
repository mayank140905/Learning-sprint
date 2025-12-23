# better solution - we know after half of number, only that number is divisible.
# so we go until half, and stop.

# TC - O(N/2) ≃ O(N)
# SC - O(k)

num = int(input("enter the number: "))
result = []

for i in range(1,num//2):
  if num%i == 0:
    result.append(i)
result.append(num)
print(result)



'''
Time Complexity - cuz loop will till number's half

Space Complexity - k would be total number of factors.
'''