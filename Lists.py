bicycles = ['trek', 'cannondale', 'redline', 'specialized']
bicycles[0] = bicycles[0].title()
print(bicycles[-3])
print(bicycles[-1:-4])
print(bicycles[0:3])
print(bicycles) #??
print(type(bicycles))

message = f"I have a {bicycles[0]} that looks exactly same as {bicycles[-2]}"
print(message)
print(type(message))

bicycles.insert(3,"sdfa")
print(bicycles)

bicycles.append("Honda")
print(bicycles)

del bicycles[1]
print(f"{bicycles} Delete function")

del bicycles[2]
print(f"del {bicycles}")

x = bicycles.pop(2) #returns the value just popped
print(bicycles)
print(f"x = {x}")

y = bicycles.remove("Trek") #doesn't return anything
print(bicycles)
print(f"y = {y}")

bicycles.reverse()
print(bicycles)

bicycles.clear()
print(bicycles)

#Organizing a List

car= ["Audi", "Toyota", "Honda"] #Give preference to the capital Letter, and only compares first letter
car.sort()  #.sort() returns none
print(f"Sorted Car {car}")
car.sort(reverse = True)
print(f"Reverse Car {car}")
num = [1, 2.5, -4, 5, 1, 7, 2, 9, 15, 11, 4]
num.sort()
print(num)

car= ["Audi", "Toyota", "Honda"]
print(f"Sorted {sorted(car)}") #doesn't change the original list but returns a sorted list
print(f"Original {car}")
print(f"Reverse Sorted {sorted(car, reverse = True)}")
