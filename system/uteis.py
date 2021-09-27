from datetime import datetime
from time import sleep
import math
import sqlite3
import json
import math


def line(tam=42):
    """
    Standard line structure using '_';
    :param tam: 42
    :return: '-'
    """
    return '-' * tam


def header(header_text):
    """
    Standard header structure for better visualization of information in print;
    :param header_text: The centered header text.
    :return: header_text
    """
    print(line())
    print(header_text.center(42))
    print(line())

def day(msg):
    """
    Contains rules for allowing numeric inputs from 01 to 31, as well as two-digit standardization;
    :param msg: input day
    :return: day
    """
    while True:
        day = input(msg)
        if not day.isnumeric():
            print('Invalid Date. Enter date in numeral: ')
        else:
            day = int(day)
            if day > 31:
                print('Invalid Date. Enter number from 01 to 31: ')
            else:
                break
    return str(day).zfill(2)


def month(msg):
    """
    contains rules for allowing numeric inputs from 01 to 12, as well as two-digit standardization;
    :param msg: month input
    :return: month
    """
    while True:
        month = input(msg)
        if not month.isnumeric():
            print('Invalid Date. Enter date in numeral: ')
        else:
            month = int(month)
            if month > 12:
                print('Invalid Date. Enter number from 01 to 12: ')
            else:
                break
    return str(month).zfill(2)


def year(msg):
    """
    Contains rules for allowing numeric inputs with four-digit standardization;
    :param msg: year input
    :return: year
    """
    while True:
        year = input(msg)
        if not year.isnumeric():
            print('Invalid Date. Enter date in numeral:')
        elif int(year) >= datetime.now().year:
            print('Invalid year. Check and retype')
        else:
            break
    return str(year).zfill(2)

def text_input(msg):
    """
    Use of text, blocking value inputs;
    :param msg: text input
    :return: text
    """

    while True:
        text = input(msg).upper().strip()
        if text.isnumeric():
            print(f'{msg} Invalid. Type text format: ')
        else:
            break
    return text

def value_input(msg, value=0):
    """
    Use of valuees, being standardized in float with two decimal places.
    :param msg:  value input
    :param value:
    :return: value
    """

    while True:
        value = input(msg)
        if not value.replace('.', '').isdecimal():
            print('Incorrect information! Enter the value.')
        else:
            value = round(float(value), 2)
            break
    return value
