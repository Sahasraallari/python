n = int(input("Enter the rows"))
for  i in range (1,n):
  for j in range (i):
     print("*", end="")
  print()

n = int(input("Enter the rows"))7
for i in range (n,1,-1):
   for j in range (i,1,-1):
      print("*", end="")
   print()


def no_notes(a):
   Q =  [500, 200, 100, 50, 20, 10]
x = 0
for i in range(7):
    q = Q[i]
    x = a//q
    print("Notes of {} = {}".format(q, x))
a = a%q
amount = int(input("Enter Total Amount"))
no_notes(amount)
 