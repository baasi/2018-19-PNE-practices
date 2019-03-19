import json
import termcolor

f = open("person.json", "r")

person = json.load(f)

print()


termcolor.cprint("Name: ", "red", end="")
print(person["Firstname"], person["Lastname"])
termcolor.cprint("Age: ", "yellow", end="")
print(person["age"])

for i, num in enumerate(person["phoneNumber"]):
    termcolor.cprint("Phone {}:".format(i), end="")

    termcolor.cprint("    Type: ", "red", end="")
    print(num["type"])
    termcolor.cprint("      Number:", "red", end="")
    print(num["number"])
