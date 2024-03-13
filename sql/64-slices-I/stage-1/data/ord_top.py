#!/usr/bin/env python3
import re
import csv

def read_orders() :
    str_read_file = "./orders_raw.csv"
    str_write_ord_top = "./orders_toppings.csv"
    str_write_orders = "./orders.csv"

    int_count = 1
    lst_ord_top = []
    file_input = open(str_read_file, 'r')


    # Read the file for reading and parse out the id and toppings
    # append them to a list for writing
    while True:

        str_read_line = file_input.readline()
        str_read_line = str_read_line.strip()
        if not str_read_line:
            break

        obj_id_match = re.match(r"^\d+", str_read_line)  # [0-9]

        if obj_id_match :
            # This is the first comma seperated value
            str_this_id = obj_id_match.group()
            # Sort of proof-of-concept using lookarounds to locate data
            # NOTE: lookarounds require fixed length
            #TODO: Refactor this to 1 re.search to pull everything at once using capture groups

            # Get the customer ref
            obj_customer_match = re.search(r"(?<=,)\d*(?=,\d{4})", str_read_line)
            str_this_customer = obj_customer_match.group()
            # Get the date
            obj_date_match = re.search(r"(?<=,)\d{4}-\d{2}-\d{2}(?=,)", str_read_line)
            str_this_date = obj_date_match.group()
            # Get the pizza type
            obj_pizza_match = re.search(r"(small|medium|large)", str_read_line)
            str_this_pizza = obj_pizza_match.group()
            match str_this_pizza :
                case 'small' :
                    str_this_pizza = "1"
                case 'medium' :
                    str_this_pizza = "2"
                case 'large' :
                    str_this_pizza = "3"
            # Get the store id
            obj_store_match = re.search(r"(?<=[a-z],)\d", str_read_line)
            str_this_store = obj_store_match.group()

            # search the line for the pizza_type
            obj_toppings_match = re.search(r"(?<=[a-z],\d,)(\d,?)+$", str_read_line)
            str_these_toppings = obj_toppings_match.group()
            # split the remaining values into a list
            lst_these_toppings = re.split(",", str_these_toppings)
            # create a dictionary from the id and toppings list
            dct_this_record = {
                'id':str_this_id,
                'customer':str_this_customer,
                'date':str_this_date,
                'pizza_type':str_this_pizza,
                'store':str_this_store,
                'toppings':lst_these_toppings
            }
            # append the dictionary to the list
            lst_ord_top.append(dct_this_record)

    file_input.close()

    # Copy the list to write the corrected file after orders_toppings is complete
    lst_ord_fixed = lst_ord_top.copy()

    # check if our list has any elements
    if len(lst_ord_top) > 0 :
        # Open our destination file for writing
        file_ord_top = open(str_write_ord_top, "w")

        csv_writer = csv.writer(file_ord_top)

        print(f"Writing {str_write_ord_top}")

        # Add our heading
        lst_heading = ['id','order','topping']
        csv_writer.writerow(lst_heading)

        # loop as long as we have elements in the list
        while len(lst_ord_top) > 0 :



            # remove the first dictionary for processing
            dct_this_record = lst_ord_top.pop(0)

            lst_toppings = dct_this_record['toppings']

            # loop as long as our topping list has elements
            while len(lst_toppings) > 0 :
                # remove the first topping value 
                str_topping = lst_toppings.pop(0)

                # create a list to write our line
                lst_write_line = [
                    str(int_count),
                    dct_this_record['id'],
                    str_topping
                ]

                csv_writer.writerow(lst_write_line)

                int_count += 1 #

        file_ord_top.close()

        print(f"Writing {str_write_orders}")

        # Open the orders.csv file for writing
        file_ord = open(str_write_orders, "w")
        csv_writer = csv.writer(file_ord)

        lst_heading = [
            'id',
            'customer',
            'date',
            'pizza_type',
            'store'
        ]
        csv_writer.writerow(lst_heading)

        while len(lst_ord_fixed) > 0 :
            dct_this_record = lst_ord_fixed.pop(0)

            lst_this_row = [
                dct_this_record['id'],
                dct_this_record['customer'],
                dct_this_record['date'],
                dct_this_record['pizza_type'],
                dct_this_record['store']
            ]

            csv_writer.writerow(lst_this_row)
        
        file_ord.close()


read_orders()