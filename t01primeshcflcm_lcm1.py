# Find the Lowest Common Multiple (LCM) of 18 and 30.
def final_lcm(thelist):
   previous_thelist = thelist
   prime_thelist = list(set(thelist) - set(returns_new_thelist(previous_thelist))
   factors = 1
   for i in prime_thelist:
       factors = factors*i
   new_thelist = returns_new_thelist(previous_thelist)
   for i in range(1, 10000000000):
       s_empty = []
       for j in new_thelist:
           if i % j  == 0:
               s_empty.append(True)
       if len(new_thelist) == len(s_empty):
           initial_lcm = i
           break
   final_lcm = factor*initial_lcm
   return final_lcm

