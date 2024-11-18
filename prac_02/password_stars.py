def main():
    """Main Function"""
    min_password = 10
    final_password = get_password(min_password)
    convert(final_password)


def get_password(min_password):
    """User password input Check"""
    password = input("Enter your password: ")
    while len(password) < min_password: #check
        print("Password doesn't meet the minimum length!")
        password = input("Enter your password: ")

    return password
def convert(final_password):
    """Convertion"""
    stars = '*' * len(final_password)
    print(stars)



main()