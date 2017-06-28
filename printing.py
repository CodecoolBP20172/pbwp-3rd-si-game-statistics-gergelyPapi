
# Printing functions

from reports import *

print(count_games("game_stat.txt"))
print(decide("game_stat.txt", str(2200)))
print(get_latest("game_stat.txt"))
print(count_by_genre("game_stat.txt", "RPG"))
print(get_line_number_by_title("game_stat.txt", "Lofasz"))
