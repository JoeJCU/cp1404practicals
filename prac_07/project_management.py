"""
Project Management System

Joe David Mathew
7/11/24
"""


import csv
import datetime
from binascii import Incomplete
from html.parser import incomplete



from project import Project

filename = 'projects.txt'

MENU = ("- (L)oad projects  \n"
        "- (S)ave projects)  \n"
        "- (D)isplay projects  \n"
        "- (F)ilter projects by date \n"
        "- (A)dd new project  \n"
        "- (U)pdate project \n"
        "- (Q)uit")

def main():

    print(MENU)
    choice = input(">> ").upper()
    while choice != "Q":
        if choice == "L":
            input_filename = input("Please enter a filename to load from: ")
            projects = load_data(filename)
            print(f"Loaded projects.")
        elif choice == "D":
            display_data(projects)
        elif choice == "S":
            save_project(projects)
        elif choice == "U":
            projects = update_project(projects)
        elif choice == "A":
            projects == add_project(projects)








        else:
            print("Not a valid choice")
        print(MENU)
        choice = input(">> ").upper()
    print("Thanks for using this Project Manager!")



def load_data(filename):
    projects_loaded = []
    with open(filename, 'r') as file:
        next(file)  # Skip the header
        for line in file:
            data = line.strip().split('\t')  # Assuming comma-separated values
            if len(data) == 5:
                project = Project(data[0], data[1], int(data[2]), float(data[3]), int(data[4]))
                projects_loaded.append(project)

    return projects_loaded



def add_projects(projects):
    print("Let's add a new project")

    date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    # print(f"That day is/was {date.strftime('%A')}")
    # print(date.strftime("%d/%m/%Y"))

    name = input("Name: ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, date_string, priority, cost_estimate, completion))

    return projects



def display_data(projects_loaded):
    incomplete = [item for item in projects_loaded if not item.if_completed()]
    complete = [item for item in projects_loaded if item.if_completed()]

    print("\nImcomplete Porjects")
    for project in incomplete:
            print(f"{project}")

    print("\nComplete Projects")
    for project in complete:
            print(f"{project}")


def save_project():




main()