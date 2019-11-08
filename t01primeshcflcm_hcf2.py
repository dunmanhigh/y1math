# Find the Highest Common Factor (HCF) of a and b.

a = int(input("a: "))
b = int(input("b: "))

# Find the Highest Common Factor (HCF) of 18 and 30.

factorsofa=[]
factorsofb=[]
commonfactors=[]
for i in range(1,a+1):
    if a%i==0:
        factorsofa.append(i)

for i in range(1,b+1):
    if b%i==0:
        factorsofb.append(i)
print(factorsofa)
print(factorsofb)
for i in range(0,len(factorsofa)):
    for e in range(0,len(factorsofb)):
        if factorsofa[i] == factorsofb[e]:
            commonfactors.append(factorsofb[e])
print(commonfactors[-1])
