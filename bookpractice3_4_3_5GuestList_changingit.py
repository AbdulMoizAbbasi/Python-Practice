guests = ["ali", "ahmed", "umer"]

for i in guests:
    print(f"Hey! {i}\nYou are invited for the dinner.")

index = guests.index("ahmed")
guests[index] = "usman"


for i in guests:
    print(f"Hey! {i}\nYou are invited for the dinner.")
