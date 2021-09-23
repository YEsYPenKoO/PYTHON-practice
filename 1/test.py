dogage = 0
reage = 0
agefull = float(input("Enter your age: "))
if agefull < 0:
    print("Error:\nAge < 0")
else:
    if agefull - 2 <= 0:
        dogage = agefull * 10,5
        print(dogage)
    elif agefull - 2 > 0:
        reage = agefull - 2
        dogage =  21 + reage * 4
        print(dogage) 
