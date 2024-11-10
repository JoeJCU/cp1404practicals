
import csv

from setuptools.config.expand import read_files

from guitar import guitar_class

def main():
    filename = 'guitars.csv'
    guitars = []

    read_file = open(filename, 'r')
    read_file.readline()

    for data in read_file:
        guitar = guitar_class(data[0], int(data[1]), float(data[2]))   #need to change the format of the data passing in, into int and float
        guitars.append(guitar)
    read_file.close()

    print("Unsorted Guitars")
    for guitar in  guitars:
        print(guitar)

    guitars.sort()  # sorting
    print("\n Sorted Guitars: ")

main()