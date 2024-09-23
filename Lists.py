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


