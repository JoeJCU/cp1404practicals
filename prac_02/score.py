import random

def main():
    score = int(input("Enter your score: "))
    result = userscore(score) #'result' is equal to the output of the function. The uer input 'score' is inputted into the function as 'score'

    print(result)

    #random
    score = random.randint(-100,100)
    print(score)
    result = userscore(score)

def userscore(score):
    if score < 0:
        print("Invalid Score")
    else:
        if score > 100:
            print("Excellent")
        if score > 90:
            print("Excellent")
        if score > 50:
            print("Passable")
    if score > 0:
        print("Bad")
        

        

main() #call the main function


# score = float(input("Enter score: "))
# if score < 0:
#     print("Invalid score")
# else:
#     if score > 100:
#         print("Invalid score")
#     if score > 50:
#         print("Passable")
#     if score > 90:
#         print("Excellent")
# if score < 50:
#     print("Bad")