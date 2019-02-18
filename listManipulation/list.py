def displayList(list):
  for item in list:
    print(item)

miscList = ["halacska", True, "apple", 3, False]
displayList(miscList)
print(miscList)

miscList.append(False)             #Add to end os list
print(miscList)

del miscList[len(miscList) - 1]    #Delete from list at index
print(miscList)

miscList.insert(0, False)          #Insert to list atindex
print(miscList)

print(miscList.count(False))       #Count occurances

miscList.remove(False)             #Removes first macthing from list
print(miscList)

miscList.pop()                     #Delete from end in list
print(miscList)

miscList.pop(1)                    #Delete from list at index. Yes, again.
print(miscList)

miscList.reverse()                 #Reverse list
print(miscList)

miscList.pop(0)

miscList.sort()                   #Sort list items. All numbers or strings. There is sorted(List) also.
print(miscList)
displayList(miscList)