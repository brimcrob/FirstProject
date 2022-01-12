# display person info
# Parameters : name, age
def display_person_info(name, age):
    print("You name is " + name + " you are " + str(age) + " years old.")
    print("Soon you will be " + str(age1 + 1) + " years old")






def ask_for_age(person_name):
    age_int = 0
    while age_int == 0:
        age_str = input(person_name + " How old are you? ")
        try:
            age_int = int(age_str)
        except:
            print("ERROR: Age must be a number ")
    return age_int


def ask_for_name():
    name_answer = ""
    while name_answer == "":
        name_answer = input("What is your name? ")
    return name_answer


# ask for the name
name1 = ask_for_name()
name2 = ask_for_name()
# ask for the age
age1 = ask_for_age(name1)
age2 = ask_for_age(name2)
# display the results
display_person_info(name1,age1)
display_person_info(name2,age2)
