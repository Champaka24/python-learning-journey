#List: collection of items. It uses [].

items=["bru","sugar","Milk","Bru"]

items[0]
print(items)
print(items[0])
print(items[-1])

# l=[1,"bru",True,[1,2,3]]

items.pop() #removes last element
print(items)

items.append("biscuit") #adding items into the list
print(items)

items.pop(2) #removing items from certain position
print(items)

items.remove("sugar") #to remove certain element which is present in the list
print(items)