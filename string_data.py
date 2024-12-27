#100 days of code comment 
#escape sequences \n
print("I am good girl \n and adding for escape sequences")

#type casting
a="1" #string
print(int(a)) #conversion of string to int

# a=input()
# print(a)

# a=int(input("enter ur inpur"))
print(a)

ans="priyanka!!!!!!!!!!!"
print(ans.lower())
print(ans.upper())
print(ans.capitalize())
print(ans.replace("a", "aa"))
print(ans[0])
print(ans[1])
print(ans[-1])
print(ans[::-1])

for character in ans:
    print(character)


#slicing
print(ans[0:5])

print(len(ans))

#rstrip remove trailing characters
print(ans.rstrip("!"))

name="priyanka anuradha"
print(name.split(" "))
print(ans.count("priyanka"))

print(ans.endswith("ri", 2, 4)) #checking

print(name.find("a"))

print(name.index("an"))

print(name.isalnum())

print(name.isalpha())

print(name.islower())

print(name.isupper())

print(name.isascii())

print(name.isprintable())

print(name.isspace())

print(name.istitle())

print(name.startswith("I"))

print(name.swapcase())