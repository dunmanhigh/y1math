# Generate oscillating pattern 1, -1, 1, -1, 1, -1, ... k times

print('What is k?')
k = int(input())
print('How many times do you want to repeat the loop?')
counter = int(input())
x=1
while counter > 0:
    if x ==1:
        k = k + 1
        x = x + 1
        counter = int(counter - 1)
        print(k)
    if x == 2:
        k = k - 1
        x = x - 1
        counter = int(counter - 1)
        print(k)
