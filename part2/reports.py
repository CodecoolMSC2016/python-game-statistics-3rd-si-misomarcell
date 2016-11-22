# Report functions
def read_file(filename = "game_stat.txt"):
    array = []
    with open(filename, "r") as ins:   
        for line in ins:
            array.append(line)
    return array

def get_most_played(file_name):
    game_list = read_file(file_name)
    current_max = 0
    current_max_title = ""
    for i in game_list:
        title, copies, release, genre, publisher = i.split("\t")
        if float(copies) > current_max:
            current_max = float(copies)
            current_max_title = title
    return current_max_title

def sum_sold(file_name):
    game_list = read_file(file_name)
    sum = 0
    for i in game_list:
        title, copies, release, genre, publisher = i.split("\t")
        sum = sum + float(copies)
    return sum

def get_selling_avg(file_name):
    game_list = read_file(file_name)
    sum = 0
    count = 0
    for i in game_list:
        title, copies, release, genre, publisher = i.split("\t")
        count = count + 1
        sum = sum + float(copies)
    return sum / count

def count_longest_title(file_name):
    game_list = read_file(file_name)
    longest = 0
    for i in game_list:
        title, copies, release, genre, publisher = i.split("\t")
        if len(title) > longest:
            longest = int(len(title))
    return longest

def get_date_avg(file_name):
    game_list = read_file(file_name)
    sum = 0
    count = 0
    for i in game_list:
        title, copies, release, genre, publisher = i.split("\t")
        count = count + 1
        sum = sum + int(release)
    return int(sum / count)

def get_game(file_name, title):
    game_list = read_file(file_name)
    for i in game_list:
        title_file, copies, release, genre, publisher = i.split("\t")
        if title == title_file:
            return "value: [" + title + "'," + copies +"'," + release + "'," + genre + "'," + publisher +"]"
print(get_game("game_stat.txt", "Minecraft"))