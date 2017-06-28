
# Report functions

'''
What is the title of the most played game (i.e. sold the most copies)?
Expected name of the function: get_most_played(file_name)
Expected output of the function: (string)
Other expectation:  if there is more than one, then return the first from the file
'''


def get_most_played(file_name):
    with open(file_name) as text_file:
        text_file_converted_to_list = [[item for item in line.strip().split("\t")] for line in text_file]
        most_played_game = 0
        for list_in_converted in text_file_converted_to_list:
            if float(list_in_converted[1]) > float(most_played_game):
                most_played_game = list_in_converted[1]
        for list_in_converted in text_file_converted_to_list:
            if most_played_game in list_in_converted:
                return(str(list_in_converted[0]))

'''
How many copies have been sold total?
Expected name of the function: sum_sold(file_name)
Expected output of the function: (number)
'''

def sum_sold(file_name):
    with open(file_name) as text_file:
        text_file_converted_to_list = [[item for item in line.strip().split("\t")] for line in text_file]
    sum_sold_number = 0
    for list_in_converted in text_file_converted_to_list:
            sum_sold_number += float(list_in_converted[1])
    return sum_sold_number

'''
What is the average selling?
Expected name of the function: get_selling_avg(file_name)
Expected output of the function: (number)
'''

def get_selling_avg(file_name):
    with open(file_name) as text_file:
        text_file_converted_to_list = [[item for item in line.strip().split("\t")] for line in text_file]
        sum_sold_number = 0
        sold_instances_count = 0
        for list_in_converted in text_file_converted_to_list:
                sum_sold_number += float(list_in_converted[1])
                sold_instances_count += 1
        return (sum_sold_number/sold_instances_count)

'''
How many characters long is the longest title?
Expected name of the function: count_longest_title(file_name)
Expected output of the function: (number)
'''

def count_longest_title(file_name):
    with open(file_name) as text_file:
        text_file_converted_to_list = [[item for item in line.strip().split("\t")] for line in text_file]
        longest_string = 0
        for list_in_converted in text_file_converted_to_list:
            if longest_string < len(list_in_converted[0]):
                longest_string = len(list_in_converted[0])
        return longest_string

'''
What is the average of the release dates?
Expected name of the function: get_date_avg(file_name)
Expected output of the function: average year (number)
Other expectation: the return value must be the rounded up average
'''

def get_date_avg(file_name):
    with open(file_name) as text_file:
        text_file_converted_to_list = [[item for item in line.strip().split("\t")] for line in text_file]
        sum_of_date = 0
        date_count = 0
        for list_in_converted in text_file_converted_to_list:
                sum_of_date += float(list_in_converted[2])
                date_count += 1
        return (round(sum_of_date/date_count))

'''
What properties has a game?
Expected name of the function: get_game(file_name, title) .
Expected output of the function: a list of all the properties of the game (a list of various type).
Details: the function get a parameter named game.
This is the title of the game (string).
This is an existent game.
The function return a list of the properties of this game including the title.
An example return value: ["Minecraft",23.0,2009,"Survival game","Microsoft"].
'''

def get_game(file_name, title):
    with open(file_name) as text_file:
        text_file_converted_to_list = [[item for item in line.strip().split("\t")] for line in text_file]
    for list_in_converted in text_file_converted_to_list:
        if title == list_in_converted[0]:
            return list_in_converted
