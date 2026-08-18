list=[1,2,3,"a","b","c","d","e"]
print(list)

(list.append(10))
print(list)

(list.insert(3,10))
print (list)

list[2]=10
print(list)

list.extend([1,2,3])
print(list)

print(list[2])

list.remove("c")
print(list)

list.pop(1)
print(list)

list .pop()
print(list)

del list[1]
print(list)

print(len(list))

if 3 in list:
    print("element is present")
else:
    print("element is absent")    

for i in list:
    print(i)

print(list.count(1))

print(list.index(1))


list2=[1,2,3,4,5,6,7,8,9]
list2.sort()
print(list2)

list2.sort(reverse=True)
print(list2)


list.clear()
print(list)

newlist=list2.copy()
print(newlist)


    