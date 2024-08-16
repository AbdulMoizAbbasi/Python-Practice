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