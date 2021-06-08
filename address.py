#!/usr/bin/env python3

# Created by : Jonathan Kene
# Created on : June 7 2021
# This program prints out your address, using default function parameters


def formatted_address(name, street_number, street_name, city, province,
                      postal_code, apartment_num=" "):

    # return the full formal name
    can_mail_format = " "
    can_mail_format = can_mail_format + name.upper() + "\n"

    if apartment_num != "":
        can_mail_format = can_mail_format + apartment_num.upper() + "-"
    can_mail_format = (can_mail_format + street_number.upper() +
                       " " + street_name.upper() + "\n")
    can_mail_format = (can_mail_format + city.upper() + " " + province.upper()
                       + " " + postal_code.upper() + "\n")

    return can_mail_format


def main():
    # gets a users name and prints out their formal name
    user_apartment_num = ""

    user_name = input("Enter your full name: ")
    user_apartment = input("Do you live in an apartment? (y/n): ")
    if user_apartment == "y" or user_apartment == "yes":
        user_apartment_num = input("Enter your apartment number: ")
    user_street_number = input("Enter your street number: ")
    user_street_name = input("Enter your street name: ")
    user_city = input("Enter your city name: ")
    user_province = input("Enter your province initials (i.e, AB, ON, MA): ")
    user_postal_code = input("Enter your postal code (i.e K1C 1K3): ")

    if user_apartment_num != "":
        formatted_string = formatted_address(user_name, user_street_number,
                                             user_street_name, user_city,
                                             user_province, user_postal_code,
                                             user_apartment_num)
    else:
        formatted_string = formatted_address(user_name, user_street_number,
                                             user_street_name, user_city,
                                             user_province,
                                             user_postal_code)

    print(formatted_string)


if __name__ == "__main__":
    main()
