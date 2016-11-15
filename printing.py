import pprint
import reports
import os

os.system('clear')
print("Please enter the name of the stats file (leave empty for default)")
filename = input("Filename: ")
if filename == "":
    filename = "game_stat.txt"

def print_main_menu(result = "N/A"):
    os.system('clear')
    menu_items = ["1. How many games are in the file?",
                "2. Is there a game from a given year?",
                "3. Which was the latest game?",
                "4. How many games do we have by genre?",
                "5. What is the line number of the given game (by title)?",
                "6. What is the alphabetical ordered list of the titles?",
                "7. What are the genres?",
                "8. What is the release date of the top sold First-person shooter game?",
                "Enter 'Q' to exit"]
    
    print("\nChoose a function:\n")
    for i in menu_items:
        print("    " + i)
    
    if result != "":
        print("\nResult:")
        pprint.pprint(result)
print_main_menu()

while True:
    inp = input("\nFunction: ")
    inp = inp.lower()

    if inp == "q":      #GAME OVER
        os.system('clear')
        exit()
    elif inp == "1":    #How many games are in the file?
        print_main_menu(reports.count_games(filename))
    elif inp == "2":    #Is there a game from a given year?
        year = input("Year: ")
        print_main_menu(reports.decide(filename, year))
    elif inp == "3":    #Which was the latest game?
        print_main_menu(reports.get_latest(filename))
    elif inp == "4":    #How many games do we have by genre?
        list_of_genres = str(reports.get_genres(filename))
        list_of_genres = list_of_genres.replace("'", "")
        print("List of genres: " + list_of_genres) 
        genre = input("Genre: ")
        print_main_menu(reports.count_by_genre(filename, genre))
    elif inp == "5":    #What is the line number of the given game (by title)?
        title = input("Title: ")
        print_main_menu(reports.get_line_number_by_title(filename, title))
    elif inp == "6":    #What is the alphabetical ordered list of the titles?
        print_main_menu(reports.sort_abc(filename))
    elif inp == "7":    #What are the genres?
        print_main_menu(reports.get_genres(filename))
    elif inp == "8":    #What is the release date of the top sold First-person shooter game?
        print_main_menu(reports.when_was_top_sold_fps(filename))