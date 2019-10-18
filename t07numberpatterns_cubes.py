# Generate cubes number pattern from 1 to 10
# 1 8 27 64 ...
for number in range(1, 10):
    base = number * (number -1) + 1

    output = str.format("{}^3 = {}", number, base)
    base += 2
    
    for i in range(0, number - 1):
        output += str.format(" + {}", base)
        base += 2
        
    print(output)
