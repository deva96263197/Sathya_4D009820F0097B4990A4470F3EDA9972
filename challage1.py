def recur_fact(n):
  if n == 0 or n == 1:
     return n
  else:
    return n * recur_fact(n - 1)
num = int(input("enter the n value: "))
res = recur_fact(num)
print("The factorial of {} is {} ".format(num, res))
 