userName = input("Enter your name: ")
Menu = """(H) Hello    
(G) Goodbye
(Q) Quit"""
print(Menu)
choice = input("Enter your choice: ").upper()

while choice != 'Q':
    if choice == 'H':
        print(f"Hello, {userName}!")
        print(Menu)
        break

    elif choice == 'G':
        print(f"Goodbye, {userName}!")
        print(Menu)
        break

    else:
        print("Invalid choice. Please try again.")
        print(Menu)
        break

print("Finished")
