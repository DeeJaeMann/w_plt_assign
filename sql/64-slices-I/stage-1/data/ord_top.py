#!/usr/bin/env python3
import re
import csv

def read_orders() :
    str_read_file = "./orders.csv"
    str_write_file = "./orders_toppings.csv"

    int_count = 0
    lst_ord_top = []
    file_input = open(str_read_file, 'r')


    # Read the file for reading and parse out the id and toppings
    # append them to a list for writing
    while True:
        int_count += 1
        str_read_line = file_input.readline()
        str_read_line = str_read_line.strip()
        if not str_read_line:
            break
        # print(f"Line {int_count}: {str_line.strip()}")


        obj_id_match = re.match(r"^\d+", str_read_line)  # [0-9]

        if obj_id_match :
            # This is the first comma seperated value
            str_this_id = obj_id_match.group()
            # search the line for the pizza_type
            obj_toppings_match = re.search(r"(small|medium|large),(\d+,?)+$", str_read_line)
            # the returned match will include the pizza_type so we'll substitute that for an empty string
            str_these_toppings = re.sub(r"(small|medium|large),", "", obj_toppings_match.group())
            # split the remaining values into a list
            # TODO: Drop first value - store id
            lst_these_toppings = re.split(",", str_these_toppings)
            # create a dictionary from the id and toppings list
            dct_this_record = {
                'id':str_this_id,
                'toppings':lst_these_toppings
            }
            # append the dictionary to the list
            lst_ord_top.append(dct_this_record)

    file_input.close()

    if len(lst_ord_top) > 0 :
        file_output = open(str_write_file, "w")

        csv_writer = csv.writer(file_output)

        str_separator = ''

        str_toppings = str_separator.join(lst_ord_top[0]['toppings'][0])

        str_write_line = f"{lst_ord_top[0]['id']}"

        str_write_line += str_toppings

        csv_writer.writerow(str_write_line)

        file_output.close()


    # print(f"{lst_ord_top}")
    print(f"{lst_ord_top[0]['id']} {lst_ord_top[0]['toppings'][0]}")

read_orders()