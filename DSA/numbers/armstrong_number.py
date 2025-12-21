# armstrong number - sum of each digits raised to the power of number of digits in the given number.
'''
153 = 1^3 + 5^3 + 3^3 = 153
'''
#TC = O(log₁₀(n))
#SC = O(1)

def armstrong():
  n = int(input("enter number : "))
  num = n
  nod = len(str(n))    # number of digit
  sum = 0

  while num>0:
    ld = num%10
    sum = sum + (ld**nod)
    num = num//10

  if sum == n:
    print("its a armstrong num")
  else: 
    print("its not a armstrong num")

armstrong()
'''
Time Complexity (TC)

while num > 0 loop runs once per digit → O(d)
For an n-digit number, TC = O(log₁₀(n))
(Practically: O(d))


Space Complexity (SC)

Only a few variables (num, sum, ld, etc.) → O(1)
'''