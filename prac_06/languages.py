from programming_language import programmingLanguage


def main():
    python = programmingLanguage("Python", "Dynamic", True, 1991)
    ruby = programmingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = programmingLanguage("Visual Basic", "Static", False, 1991)

    print("The dynamically typed languages are: ")

    languages = [python, ruby, visual_basic]

    for language in languages:
        if language.typed == "Dynamic":  # Assuming 'typing' is an attribute for type system
            print(language.name)  # Assuming 'name' is the attribute for the language's name



main()






    # print(python)
