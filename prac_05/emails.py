
email_dicts = {

}

def main():
    while True:
        user_email = input("Enter your email: ").split()  # input and splits all the words up in the user emails
        print(f"Text: {user_email}")
        if user_email == "":
            continue # restarts the loop so that the user have to re enter/enter their email=

        user_name = user_email.split('@')
        print(user_name
              )


main()