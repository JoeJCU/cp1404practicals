
import csv

from kivy.input.providers.probesysfs import read_line


def main():
    data_champs_wins = {

    } #dict
    data_whole = []
    data_country_wins = []

    with open('wimbledon.csv', "r", encoding="utf-8-sig") as in_file:
        read = csv.reader(in_file) # reading the data in the csv
        for read_row in read: #iterating through each row in the data
            champ_wins = read_row[2]
            if champ_wins in data_champs_wins:
                data_champs_wins[champ_wins] += 1 # adding the champ into the dict
            else:
                data_champs_wins[champ_wins] = 1 #incrmenting the added champ in the dict














main()