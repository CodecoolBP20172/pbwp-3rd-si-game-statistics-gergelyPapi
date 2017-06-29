
# Report functions


def get_most_played(file_name):
    with open(file_name) as text_file:
        text_file_converted_to_list = [
            [item for item in line.strip().split("\t")] for line in text_file]
        most_played_game = 0
        for list_in_converted in text_file_converted_to_list:
            if float(list_in_converted[1]) > float(most_played_game):
                most_played_game = list_in_converted[1]
        for list_in_converted in text_file_converted_to_list:
            if most_played_game in list_in_converted:
                return(str(list_in_converted[0]))


def sum_sold(file_name):
    with open(file_name) as text_file:
        text_file_converted_to_list = [
            [item for item in line.strip().split("\t")] for line in text_file]
    sum_sold_number = 0
    for list_in_converted in text_file_converted_to_list:
        sum_sold_number += float(list_in_converted[1])
    return sum_sold_number


def get_selling_avg(file_name):
    with open(file_name) as text_file:
        text_file_converted_to_list = [
            [item for item in line.strip().split("\t")] for line in text_file]
        sum_sold_number = 0
        sold_instances_count = 0
        for list_in_converted in text_file_converted_to_list:
            sum_sold_number += float(list_in_converted[1])
            sold_instances_count += 1
        return (sum_sold_number / sold_instances_count)


def count_longest_title(file_name):
    with open(file_name) as text_file:
        text_file_converted_to_list = [
            [item for item in line.strip().split("\t")] for line in text_file]
        longest_string = 0
        for list_in_converted in text_file_converted_to_list:
            if longest_string < len(list_in_converted[0]):
                longest_string = len(list_in_converted[0])
        return longest_string


def get_date_avg(file_name):
    with open(file_name) as text_file:
        text_file_converted_to_list = [
            [item for item in line.strip().split("\t")] for line in text_file]
        sum_of_date = 0
        date_count = 0
        for list_in_converted in text_file_converted_to_list:
            sum_of_date += float(list_in_converted[2])
            date_count += 1
        return (round(sum_of_date / date_count))


def get_game(file_name, title):
    with open(file_name) as text_file:
        text_file_converted_to_list = [
            [item for item in line.strip().split("\t")] for line in text_file]
    for list_in_converted in text_file_converted_to_list:
        if title == list_in_converted[0]:
            return [str(list_in_converted[0]), float(list_in_converted[1]), float(
                list_in_converted[2]), str(list_in_converted[3]), str(list_in_converted[4])]


def count_grouped_by_genre(file_name):
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
        return(genre_dict)


def get_date_ordered(file_name):
    with open(file_name) as text_file:
        text_file_converted_to_list = [
            [item for item in line.strip().split("\t")] for line in text_file]
        year_list_units = []
        for list_in_converted in text_file_converted_to_list:
            ordering_unit = []
            ordering_unit.append(list_in_converted[2])
            ordering_unit.append(list_in_converted[0])
            year_list_units.append(ordering_unit)
        year_list_units_sorted = sorted(year_list_units, key=str, reverse=True)
        final_sorted_list = []
        for units in year_list_units_sorted:
            units.remove(units[0])
            final_sorted_list.append(units[0])
        return final_sorted_list
