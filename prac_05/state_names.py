"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland",
                "NSW": "New South Wales",
                "NT": "Northern Territory",
                "WA": "Western Australia",
                "ACT": "Australian Capital Territory",
                "VIC": "Victoria",
                "TAS": "Tasmania",
                "SA": "South Australia"}

print(CODE_TO_NAME)
for state, name in CODE_TO_NAME.items(): #the .items command returns the whole dict. Created 'state' and 'name' to specifically call the individual states and full names
    print(f"{state} is {name}")

state_code = input("Enter short state: ").upper()
print(state_code)


while state_code != "":




    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")
