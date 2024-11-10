"""
Project Management System

Joe David Mathew
7/11/24
"""


import csv
import datatime

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
            projects = load_data(filename, projects)





        else:
            print("Not a valid choice")
        print(MENU)
        choice = input(">> ").upper()
    save_project_data(DEFAULT_FILE_NAME, projects)
    print("Thanks for using this project manager!")



def load_data(filename, project):
    projects_loaded = []
    read_file = open(filename, 'r')
    read_file.readline()
    next(read_file) #skipping the header

    for data in read_file:
        project = Project(data[0], data[1], int(data[2]), float(data[3]), int(data[2]))
        projects_loaded.append(project)

    read_file.close()

    return project




main()