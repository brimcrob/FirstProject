
name = ""
while name == "":
    name = input("What is your name? ")

age = 0
while age == 0:
    age_str = input("How old are you? ")
    try:
        age = int(age_str)
    except:
        print("ERROR: Age must be a number ")

print("You name is " + name + " you are " + str(age) + " years old.")
print("Soon you will be " + str(age + 1) + " years old")




"""
while name ==""
    print pleas enter a name 
"""


"""
while age is not valid
    ask for age

print age
"""


