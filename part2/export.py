
# Export functions

from reports import *


def export_answers_into_file(export_file_name):
    result_list = []
    result_list.append(get_most_played("game_stat.txt")))
    result_list.append((sum_sold("game_stat.txt")))
    result_list.append((get_selling_avg("game_stat.txt")))
    result_list.append((count_longest_title("game_stat.txt")))
    result_list.append((get_date_avg("game_stat.txt")))
    write_file = open(export_file_name, "w")
    for items in result_list:
        write_file.write("{0}".format(items) + "\n")
    write_file.close()


export_answers_into_file("export_results_p2.txt")
