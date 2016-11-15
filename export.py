import reports
import os

os.system('clear')
print("Please enter the name of the STATS file (leave empty for default)")
filename = input("Filename: ")
if filename == "":
    filename = "game_stat.txt"

print("Please enter the name of the OUTPUT file (leave empty for default)")
des_file = input("Filename: ")
if des_file == "":
    des_file = "game_export.txt"

# Export functions
file = open(des_file, 'w')

file.write("1. How many games are in the file?\n" + 
            str(reports.count_games(filename)) +"\n\\n")

year = input("Is there a game from a given year?: ")
file.write("2. Is there a game from a given year?\n" +
            str(reports.decide(filename, year)) + "\n\n")

file.write("3. Which was the latest game?\n" +
            str(reports.get_latest(filename)) + "\n\n")

genre = input("How many games do we have by genre?: ")
file.write("4. How many games do we have by genre?\n" +
            str(reports.count_by_genre(filename, genre)) + "\n\n")

title = input("What is the line number of the given game (by title)?: ")
file.write("5. What is the line number of the given game (by title)?\n" +
            str(reports.get_line_number_by_title(filename, title)) + "\n\n")

file.write("6. What is the alphabetical ordered list of the titles?\n" +
            str(reports.sort_abc(filename)) + "\n\n")

file.write("7. What are the genres?\n" +
            str(reports.get_genres(filename)) + "\n\n")

file.write("8. What is the release date of the top sold First-person shooter game?\n" +
            str(reports.when_was_top_sold_fps(filename)) + "\n\n")

file.close()
print("Export successful! (" + des_file + ")")