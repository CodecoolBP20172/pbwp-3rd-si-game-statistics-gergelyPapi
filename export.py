
# Export functions

from reports import *


def export_answers_into_file(export_file_name):
    result_list = []
    result_list.append((count_games("game_stat.txt")))
    result_list.append((decide("game_stat.txt", str(2002))))
    result_list.append((get_latest("game_stat.txt")))
    result_list.append((count_by_genre("game_stat.txt", "RPG")))
    result_list.append(
        (get_line_number_by_title(
            "game_stat.txt",
            "Counter-Strike")))
    write_file = open(export_file_name, "w")
    for items in result_list:
        write_file.write("{0}".format(items) + "\n")
    write_file.close()


export_answers_into_file("export_results.txt")
