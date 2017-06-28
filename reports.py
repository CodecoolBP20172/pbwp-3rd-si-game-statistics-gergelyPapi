
# Report functions

'''
How many games are in the file?
Expected name of the function: count_games(file_name)
Expected output of the function: a number
'''


def count_games(file_name):
    with open(file_name) as text_file:
        count = sum(1 for line in text_file)
    print(count)
    return count


'''
Is there a game from a given year?
Expected name of the function: decide(file_name, year)
Expected output of the function: boolean value
'''


def decide(file_name, year):
    with open(file_name) as text_file:
        text_file_converted_to_list = [[item for item in line.strip().split("\t")] for line in text_file]
        for list_in_converted in text_file_converted_to_list:
            if list_in_converted[2] == str(year):
                #print(line_info_list)
                #print(True)
                return True
        print(False)
        return False

#PM:
#How to separate the list items based on tab or newline?
#How to iterate through the items of lists in lists, without defining the lists?
#How to print specific item from the found list after an attribute?
#What has to be included in export, printing.py-s?

#Which was the latest game?
#Expected name of the function: get_latest(file_name)
#Expected output of the function: the title of the latest game as a string
#Other expectation: if there is more than one, then return the first from the file

def get_latest(file_name):
    with open(file_name) as text_file:
        text_file_converted_to_list = [[item for item in line.strip().split("\t")] for line in text_file]
        latest_game_year = 0
        for list_in_converted in text_file_converted_to_list:
            if int(list_in_converted[2]) > int(latest_game_year):
                latest_game_year = list_in_converted[2]
        for list_in_converted in text_file_converted_to_list:
            if latest_game_year in list_in_converted:
                return(list_in_converted[0])

#How many games do we have by genre?
#Expected name of the function: count_by_genre(file_name, genre)
#Expected output of the function: a number

def count_by_genre(file_name, genre=None):
    with open(file_name) as text_file:
        text_file_converted_to_list = [[item for item in line.strip().split("\t")] for line in text_file]
        genre_dict = {}
        for list_in_converted in text_file_converted_to_list:
            for items in list_in_converted:
                key, value = list_in_converted[3], 0
            genre_dict[key] = value
        for key, value in genre_dict.items():
            for list_in_converted in text_file_converted_to_list:
                if key in list_in_converted:
                    genre_dict[key] = genre_dict[key] + 1
        return(genre_dict[genre])


'''
What is the line number of the given game (by title)?
Expected name of the function: get_line_number_by_title(file_name, title)
Expected output of the function: a number (if there is no game found, then raises ValueError exception)
'''


def get_line_number_by_title(file_name, title=None):
    with open(file_name) as text_file:
        text_file_converted_to_list = [[item for item in line.strip().split("\t")] for line in text_file]
    for index, list_in_converted in enumerate(text_file_converted_to_list, start=1):
        if title in list_in_converted:
            print(index)
