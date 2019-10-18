# Generate oscillating pattern 1, -1, 1, -1, 1, -1, ... k times

# Generate oscillating pattern 1, -1, 1, -1, 1, -1, ... k times

k = int(input()) #read input for k
even = (k%2 == 0) #check if k is even
pattern = []

if even:
    times = int(k/2)
    for i in range(times):
        pattern.append(1)
        pattern.append(-1)
    print(pattern)

else:
    times = int((k-1)/2)
    for i in range(times):
        pattern.append(1)
        pattern.append(-1)
    pattern.append(1)
    print(pattern)
