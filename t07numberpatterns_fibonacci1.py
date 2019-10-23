# Generate the first k Fibonacci numbers

k = 10

fprev = 1
fnext = 1
print(fprev, end=' ')
print(fnext, end=' ')
for i in range(k-2): # first 2 terms already printed before loop
  fib = fprev + fnext 
  print(fib, end=' ')
  fprev = fnext
  fnext = fib  
Telephone Box Attack
