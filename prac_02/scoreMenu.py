"""
display menu
get choice
while choice != <quit option>
    if choice == <first option>
        <do first task>
    else if choice == <second option>
        <do second task>
    ...
    else if choice == <n-th option>
        <do n-th task>
    else
        display invalid input error message
    display menu
    get choice
<do final thing, if needed>
"""

MENU = """
G - Get a valid score
P - Print result
S - Show stars
Q - Quit
"""


# (G)et a valid score (must be 0-100 inclusive)
# (P)rint result (copy or import your function to determine the result from score.py)
# (S)how stars (this should print as many stars as the score)
# (Q)uit


def main():
    """Main Function"""
    user_input = input(f"{MENU}: ").upper()
    # score = graded_score

    while user_input != "Q":
        if user_input == "G":
            score = float(input("Enter Your Score: "))  # user input to get user score
            score_check(score)  # running the 'graded_score function while inputting  the 'score' value
            user_input = input(f"{MENU}: ").upper()
        elif user_input == "P":
            print(graded_score(score))
            user_input = input(f"{MENU}: ").upper()
        elif user_input == "S":
            show_stars(score)
            user_input = input(f"{MENU}: ").upper()
        else:
            print("Invalid option")
            user_input = input(f"{MENU}: ").upper()


print("Farewell")


def graded_score(score):
    """Determining the grade """
    if score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    elif score > 0:
        return "Bad"


def show_stars(score):
    """Score to stars"""
    stars = '*' * int(score)
    print(f"{stars}")


def score_check(score):
    """"Checking to see if the Score is valid"""
    if score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    elif score < 0:
        print("Invalid score")
        score = float(input("Enter score: "))


main()
