print("Good morning")

print("Good afternoon")

print("Good evening")

numi = 1
numf = 1.23

print(numi)
print(numf)

print(type(numi))
print(type(numf))

bool = (numi<numf)

print(bool)
print(type(bool))

list = ["sato","susuki","tanaka"]
print(list)
list[2] = "tanakamaro"
print(list)

list1 = [[1,2,3,4,5],[2,3,4,5,6]]
print(list1[0])
print(list1[1])

print(1!=2)
print(1>=2)

print(1!=2 and 1 > 2)
print(1!=2 or 1 > 2)

age = 42
if age >= 20 :
    print("adult")
elif age == 0 :
    print("baby")
else :
    print("child")

for i in range (5) :
    if i==2:
        continue
    if i==4:
        break
    print(i)

for i in range(5):
    for j in range(2):
        print(i,j,sep="-")
    
sum = 0
for i in list:
    print(i)
    sum += 1
print(sum)
# command+k -> command+c
# でコメントアウトすることができる