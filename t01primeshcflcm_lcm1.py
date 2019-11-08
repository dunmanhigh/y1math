# Find the Lowest Common Multiple (LCM) of 18 and 30.
def lcm(30, 18):  
   if 30 > 18:  
       greater = 30  
   else:  
       greater = 18  
  while(True):  
       if((greater % 30 == 0) and (greater % 18 == 0)):  
           lcm = greater  
           break  
       greater += 1  
   return lcm  
