
import csv


def second_main():
    data_country_wins, data_champs_wins = main()
    country_p(data_country_wins)
    champs_p(data_champs_wins)

def main():
    data_champs_wins = {
    } #dict
    # data_whole = []
    data_country_wins = []

    with open('wimbledon.csv', "r", encoding="utf-8-sig") as in_file:
        read = csv.reader(in_file) # reading the data in the csv

        for read_row in read: #iterating through each row in the data
            champ_wins = read_row[2]
            if champ_wins in data_champs_wins:
                data_champs_wins[champ_wins] += 1 # adding the champ into the dict
            else:
                data_champs_wins[champ_wins] = 1 #incrmenting the added champ in the dict

            countrys = read_row[1]
            if countrys not in data_country_wins:
                data_country_wins.append(countrys) #adding the countrys into the list by checking if they aren't already in the list made

    return champ_wins, data_country_wins, data_champs_wins



def country_p(country_printed):
    print("These 12 countries have won Wimbledon: ")
    country_printed.sort() #soring all the countries alphabetically
    print(", ".join(sorted(country_printed))) #printing the countries

def champs_p(champs_printed):
    print("Champions: ")
    for champ_name, champs_wins  in champs_printed.items():
        print(f"{champ_name}: {champs_wins}") # print from the dic


second_main()

