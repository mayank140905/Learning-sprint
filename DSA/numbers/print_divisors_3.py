# optimal solution

# 6*2 and 2*6 means same , thus we go till sqrt of num

# TC - O(sqrt(N)) + O(NlogN)
# SC - O(k)

from math import sqrt

num = int(input("enter the number: "))

if num <= 0:
    print("enter a positive number greater than 0")
else:
    result = []
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            result.append(i)
            if num // i != i:             # we dont wanna append 6*6 (6 two times)
                result.append(num // i)

    result.sort()     #if u want sorted array     # TC - O(NlogN)
    print(result)


'''
Time Complexity - cuz loop will till number's square-root  + sort TC (NlogN)

Space Complexity - k would be total number of factors.
'''
