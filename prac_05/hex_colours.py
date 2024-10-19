

#creating a dictionery

hex_colours = {
    "Cardinal" : "#c41e3a",
    "Crystal" : "#a7d8de",
    "MediumOrchid" : "#ba55d3",
    "Middle Green" : "#4d8c57",
    "beige": "#f5f5dc",
    "black": "#000000",


}


def main():
    user_colour = input("Enter a colour name: ")

    if hex_colours.get(user_colour):
        print(f"The hex code is {hex_colours} for {user_colour}")
    else:
        print(f"Please re-enter another colour name!")



main()