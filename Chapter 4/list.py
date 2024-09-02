#List are mutable

group = ["Ram","Syam","grape", 90 ,False , 3.6]
print(group[3])
group[3] = 30

print(group[3])
print(group[1:4])
group.append("Sushree")
print(group)

#list methods

l1 = [2,56,3,11,93,67]
l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.insert(2,62) #insert 3 such that its index in the list is 3
print(l1)

print(l1.pop(3))
print(l1)

l1.remove(11)
print(l1)
