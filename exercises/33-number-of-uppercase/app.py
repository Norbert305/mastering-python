phrase = input("Type in: ")
phrase = list(phrase)

u, l = 0, 0
for i in phrase:
    if i.isupper():
        u = u + 1
    if i.islower():
        l = l + 1
    else:
        pass

print("UPPER:", u)
print("lower:", l)

#input: Hello world!
#output: UPPER CASE 1 LOWER CASE 9