firstList = list(range(5))

print(firstList)

firstList.append(6)

print(firstList)

print("======================BREAK1=====================")
firstList.append([7,8,9])

print(firstList)

print("======================BREAK2=====================")

secondList = list(range(5))

print(secondList)

secondList.append(6)

print(secondList)

secondList.extend([7,8,9])

print(secondList)

print("======================BREAK3=====================")


secondList.insert(0,100)

print(secondList)

secondList.insert(5,[2,3,4])

print(secondList)

print("======================BREAK4=====================")

del secondList[5]

print(secondList)

secondList.pop()  #removes last element and return also.

print(secondList)

print("======================BREAK5=====================")

thirdList = ["kumar", "varun", "kumar", "malar", "kumar","malar", "kumar"]

print(thirdList)

thirdList.remove("kumar")

print(thirdList)

thirdList.pop()
thirdList.pop(1)   #removes last element and return also. Try in console

print("======================BREAK6=====================")

#try in console

fourthList = ["kumar", "varun", "kumar", "malar", "kumar","malar", "kumar"]

"varun" in fourthList

"kala" in fourthList










