def recur_fibo(n) :
  if n <= 1:
    return n
  else :
    return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 20
# note: change nterms to whatever you want

#check if number is valid
if nterms <= 0 :
  print("Please enter a positive integar")
else :
  print("Fibo sequence: ")
  for i in range(nterms) :
    print(recur_fibo(i))  
