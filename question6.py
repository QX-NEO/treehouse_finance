import re
from datetime import datetime


def find_dates(sentence_input):
    case = []
    catch_a = re.findall(
        "[0-9][0-9][0-9][0-9]/[0-9][0-9]/[0-9][0-9]", sentence_input)
    catch_b = re.findall(
        "[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]", sentence_input)
    catch_c = re.findall(
        "[0-9][0-9] [A-Z][a-z][a-z] [0-9][0-9][0-9][0-9]", sentence_input)
    case = catch_a + catch_b + catch_c
    return count_freq(case)


def catch_date(date_input):
    a = False
    try:
        datetime_object = datetime.strptime(date_input, '%Y/%m/%d')
        a = True
    except:
        next
    try:
        datetime_object = datetime.strptime(date_input, '%m/%d/%Y')
        a = True

    except:
        next
    try:
        datetime_object = datetime.strptime(date_input, '%d %b %Y')
        a = True
    except:
        next
    try:
        datetime_object = datetime.strptime(date_input, '%d/%m/%Y')
        a = True
    except:
        next
    return a


def count_freq(cases):
    count = 0
    for i in cases:
        count += catch_date(i)
    return count


with open('date.txt') as file:
    lines = file.readlines()
    string_line = ""
    for i in lines:
        string_line = string_line + i.split('\n')[0]

print("Number of dates occured in the sentence", find_dates(string_line))
