# nums = [3,9,5,6,7,2]    right rotate by  k=3
# [2,3,9,5,6,7]   when done k=1
# [7,2,3,9,5,6]   when done k=2
# [6,7,2,3,9,5]   when done k=3

# basically we keep doing one-place rotation k times.

#TC = O(k · n)
#SC = O(1)

#code:- 
nums = [3,9,5,6,7,2]
k = int(input("enter k- for k times rotation : "))

for _ in range(0,k):
  e = nums.pop()
  nums.insert(0,e)


  '''
Time Complexity (TC)
pop() → O(1)
insert(0, e) → O(n) (saare elements shift hote hain)
loop k times
Overall TC = O(k · n)

Space Complexity (SC)
sirf ek variable e use ho raha hai
SC = O(1)'''