"""
CP 1404 Practical 4, Joe David Mathew, taxi simulator
"""
from taxi import Taxi
from silver_service_taxi import Silverservicetaxi

# choice = """
#
# """

def main():
    taxi_list = [  #taxis array
        Taxi("Prius",100),
        Silverservicetaxi("Sport1", 100, 3),
        Silverservicetaxi("Sport2", 100, 1)
    ]

    current_taxi = None
    bill_to_date = 0

    print("Let's drive!")
    print("Options: q)uit, c)choose taxi, d)drive")
    option = input(">>> ")

    while option != "q":

        if option == "c":
            choosen_taxi = taxi_choose(taxi_list)
            current_taxi = taxi_list[choosen_taxi]
            print(current_taxi)
            print(f"Bill to date: ${bill_to_date}")
        elif option == "d":
            if current_taxi == None:
                print("You need to choose a taxi before you can drive")
            else:
                taxi_drive(current_taxi, bill_to_date)
        else:
            print("Invalid selection")

        print("Options: q)uit, c)choose taxi, d)drive")
        option = input(">>> ")


def taxi_drive(current_taxi, bill_to_date):
    try:
        distance = float(input("Drive how far? "))
        current_taxi.start_fare()

        current_taxi.drive(distance)
        print(f"Your {current_taxi.name} trip cost you: ${current_taxi.get_fare()}")
        bill_to_date += current_taxi.get_fare()
        print(f"Bill to date: ${bill_to_date}")

    except ValueError:
        print("Not a valid number")


def taxi_choose(taxis):
    """Displays the taxis array and allows the user to choose one"""
    list_counter = 0
    print("Taxis Available: ")
    for each_taxi in taxis:
        print(f"{list_counter} - {each_taxi}")
        list_counter += 1 #increments the counter

    taxi_choice = int(input("Choose Taxi: "))
    choice_range = range(len(taxis))
    # print(choice_range)
    while taxi_choice not in choice_range:
        print("Invalid Input, Please choose from the list!")
        taxi_choice = int(input("Choose Taxi: "))

    print(taxi_choice)
    return taxi_choice






main()