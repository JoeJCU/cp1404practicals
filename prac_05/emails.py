
email_dicts = {

}

def main():
    while True:
        user_email = input("Enter your email: ")  # input and splits all the words up in the user emails
        # print(f"Text: {user_email}")
        if user_email == "":
            continue # restarts the loop so that the user have to re enter/enter their email=

        user_name = user_email.split('@')
        print(user_name)

        user_confirm = input(f"Is your name {user_name}?(Y/n)")
        if user_confirm == "Y":



main()