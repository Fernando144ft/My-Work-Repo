# Fernando Parra
# Team Management Program csv file input/output
# 10/26/2024
# This python file hold the read and write functions for the csv file
import csv

FILE = "players.csv"

def open_csv():
    # Open and read the csv file
    object_list_csv = []
    with open(FILE, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            dict_object = {"name": row[0], "position": row[1], "at bats": row[2], "hits": row[3]}
            object_list_csv.append(dict_object)
        return object_list_csv

def save_csv(edited_objects_list):
    # Saves the monthly sales list to the csv file
    with open(FILE, "w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        for object in edited_objects_list:
            name = object["name"]
            position = object["position"]
            at_bats = object["at bats"]
            hits = object["hits"]
            single_list = [name, position, at_bats, hits]
            writer.writerow(single_list)
