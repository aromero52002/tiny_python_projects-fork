myList = [0, 5, 6]
print("og list ", myList)
myList.append(10)
print("append 10", myList)
myList.extend([11, 12, 13])
print("extend 11 12 13", myList)
myList.sort()
print("my sorted", myList)
myList = sorted(myList)
print("my sorted", myList)
myList.reverse()
print("reverse", myList)
myList = list(reversed(myList))
print("reversed", list(reversed(myList)))
myList.insert(69, 69)
print("insert", myList)
del myList[0]
print("del ", myList)
myList.index(69)
print("index", myList)


myJoinList = ' '.join(['what', 'are', 'you', 'doing'])
print(myJoinList)

newList = list("Andrew")
print(newList)
if 1 in newList:
    print("1 in list")
else:
    print("1 not in list")

newList.remove("A")
print(newList)

newList.pop(0)
print(newList)

print("This is a slice: ", newList[0:1])
print("This is the length of the list: ", len(newList))
