guests = ["ali", "ahmed", "umer"]
guests.insert(0, "sdf")
guests.insert(2, "john")
guests.append("john")

for i in guests:
    print(f"Hey! {i}\nYou are invited for the dinner.")

index = guests.index("ahmed")
guests[index] = "usman"


for i in guests:
    print(f"Hey! {i}\nYou are invited for the dinner.")
print(len(guests))

while len(guests) == 2:
    x = guests.pop()
    print(f"Hey! {x} I'm sorry I can’t invite you to dinner.")