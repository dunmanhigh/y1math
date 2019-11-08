# Find the Highest Common Factor (HCF) of 18 and 30.
num1=18
num2=30
factorsofnum1=[]
factorsofnum2=[]
commonfactors=[]
for i in range(1,num1+1):
    if num1%i==0:
        factorsofnum1.append(i)

for i in range(1,num2+1):
    if num2%i==0:
        factorsofnum2.append(i)
print(factorsofnum1)
print(factorsofnum2)
for i in range(0,len(factorsofnum1)):
    for e in range(0,len(factorsofnum2)):
        if factorsofnum1[i] == factorsofnum2[e]:
            commonfactors.append(factorsofnum2[e])
print(commonfactors[-1])
