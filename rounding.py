#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Jan 2023
# This program rounds numbers

import math


def converter(decimal, decimal_places):
    # rounding a number
    decimal[0] = decimal[0] * pow(10, decimal_places) + 0.5
    decimal[0] = int(decimal[0])
    decimal[0] = decimal[0] / pow(10, decimal_places)


def main():
    decimal = []

    print("This program rounds numbers.")
    str_temp_decimal = input("Enter the number you would like to round: ")
    str_decimal_places = input(
        "Enter the number of decimal places you want to be rounded: "
    )

    try:
        temp_decimal = float(str_temp_decimal)
        decimal.append(temp_decimal)
        decimal_places = int(str_decimal_places)

        converter(decimal, decimal_places)

        print("Your number rounded is: {0}".format(decimal[0]))
    except ValueError:
        print("That is an invalid input.")


if __name__ == "__main__":
    main()
