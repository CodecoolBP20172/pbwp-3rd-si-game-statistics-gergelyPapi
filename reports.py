
# Report functions


def count_items(file_name):
    with open(file_name) as text_file:
        count = sum(1 for line in text_file)
    return count


def decide(file_name, year):
    with open(file_name) as text_file:
        text_file_converted_to_list = [
            [item for item in line.strip().split("\t")] for line in text_file]
        for list_in_converted in text_file_converted_to_list:
            if list_in_converted[2] == str(year):
                return True
        return False


def get_latest(file_name):
    with open(file_name) as text_file:
        text_file_converted_to_list = [
            [item for item in line.strip().split("\t")] for line in text_file]
        latest_year = 0
        for list_in_converted in text_file_converted_to_list:
            if int(list_in_converted[2]) > int(latest_year):
                latest_year = list_in_converted[2]
        for list_in_converted in text_file_converted_to_list:
            if latest_year in list_in_converted:
                return(list_in_converted[0])


def count_by_genre(file_name, genre=None):
    with open(file_name) as text_file:
        text_file_converted_to_list = [
            [item for item in line.strip().split("\t")] for line in text_file]
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


def get_line_number_by_title(file_name, title):
    with open(file_name) as text_file:
        text_file_converted_to_list = [
            [item for item in line.strip().split("\t")] for line in text_file]
    for index, list_in_converted in enumerate(
            text_file_converted_to_list, start=1):
        if title in list_in_converted:
            return(index)
        if title not in list_in_converted:
            raise ValueError
