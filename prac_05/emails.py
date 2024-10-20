
email_dicts = {

} #dict

def main():
    while True:
        user_email = input("Enter your email: ")  # input and splits all the words up in the user emails
        # print(f"Text: {user_email}")
        if user_email == "":
            continue # restarts the loop so that the user have to re enter/enter their email=

        user_name = user_email.split('@')[0] #splits the input at '@'
        # print(user_name)

        user_confirm = input(f"Is your name {user_name}?(y/n)")
        if user_confirm != "y":
        #     print(user_name)
        # else:
            user_name = input("Enter your name: ")

        #adding the name to the email_dicts dict
        for name in user_name:
            email_dicts[name] = user_name


        # displays all names and the email
        for name, email in email_dicts.items():
            print(f"name:{name}, email: {email})")




main()