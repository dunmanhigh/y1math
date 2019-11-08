# Generate cubes number pattern from 1 to 10
# 1 8 27 64 ...

# declare lists
numbers = []
cubes = []

# start and end numbers
start = 1 
end = 10 

# run a loop from start to end+1 
for count in range (start, end+1) :
    numbers.append (count)
    cubes.append (count**3)

# print the lists
print "numbers: ",numbers
print "cubes  : ",cubes
