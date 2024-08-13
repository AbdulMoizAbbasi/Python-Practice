#PLAYING WITH THE CASE OF WORDS
name = "ABdul moiz ABBASI       "
name = name.rstrip() #removes whitespace from right
print(f"Right Strip {name}")
name = "      ABdul moiz ABBASI"
name = name.lstrip() #removes whitespace from left
print(f"Left Strip {name}")
name = "      ABdul moiz ABBASI         "
name = name.strip()  #removes whitespace from both sides
print(f"Strip {name}")
name = name.title() #Capitalize first letter of each word and lowercase every other letter and returns the result
print(f"Title {name}")
name = name.capitalize() #Capitalize first letter of the string and every other letter small
print(f"Capitalize {name}")
name = name.lower() #all lower
print(f"Lower {name}")
name = name.upper() #all upper
print(f"Upper {name}")
upper = name.isupper() #check lower
lower = name.islower() #check upper

print(f"{upper}\n{lower}") #\n = New Line
print(f"{name}\t\t{upper}")  #\t = Tab Space

text = "moizabbasi"
print(text.removeprefix("moiz")) #removes the first letters if it exactly matches
print(text.removesuffix("abbasi")) #removes the last letters if it exactly matches
