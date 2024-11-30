"""
CP1404/CP5632 Practical
Wikipedia Testing
Joe David Mathew
"""

import wikipedia

user_input = input("Enter a page title or a search phrase:")

while user_input != "":
    try:
        wiki_output = wikipedia.page(user_input)
        print(f"{wiki_output.title}\n{wiki_output.summary}\n{wiki_output.url}\n")
    except wikipedia.exceptions.DisambiguationError:
        print("Disambiguation Error, Please try again!")
    except wikipedia.exceptions.PageError:
        print("Page Error, Please try again!")
    except ValueError:
        print("Please try again!")




