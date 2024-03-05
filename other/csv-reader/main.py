#!/usr/bin/env python3.12

import csv

str_dir = "./data/"

str_input = input("Enter an animal type (cats or dogs): ")

try :
    with open(str_dir + str_input + ".csv", mode='r') as csvfile :
        this_reader = csv.reader(csvfile, delimiter=",")
        for line in this_reader :
            print(f"{line}")
except :
    print(f"Sorry, we don't have any {str_input} here.")
finally :
    print("Goodbye!")