#List with the function to infinitely add more items into the list
what = ["1"]

print(what)

loopie = True
while loopie == True:
    burn = input("what're ya adding matey: ").lower()
    what.append(burn)
    print(what)
    sern = input("continue? (Y/N)")
        
    if sern.lower() == "n":
        break
    elif sern.lower() == "y":
        continue
    else:
        print("INVALID INPUT")
        continue