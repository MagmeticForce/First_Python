import csv

# ############# #
# CONTENTS
# 1. read_csv_file() definition
# 2. Reading episodes.csv
# 3. Reading sloth-theft.csv
# 4. Reading db-lesson-scores-bad-data.csv
#   a. Function Definitions
#   b. Main Code
# 5. Reading Movie-Ratings.csv
#   a. Function Definitions
#   b. Main Code
# ############# #






# ######################################################## #
# ######################################################## #
# ######################################################## #
# 1. READ_CSV_FILE() DEFINITION                            #
# ######################################################## #
# ######################################################## #
# ######################################################## #

def read_csv_file(file_name_input):
    '''
    Reads things inside of a CSV file
    
    Parameters
    ----------
    file_name : string
        Name of the CSV file in the current folder.

    Returns
    -------
    data_set : List of dictionaries
        Data set.
    
    '''
    # Create the thing that will hold the stuff in the CSV file
    data_set_output = []

    # Open the file and store it into a "file" parameter.
    # ./ means "the current folder"
    with open('./' + file_name_input) as file:
    # This "with" statement will automatically close the file as soon
    # as it's done with it 

        # Take the file's contents, arrange it into a list of dictionaries
        # via DictReader(), and store it into a parameter called "file_csv"
        file_csv = csv.DictReader(file)
        # Put each row into the data_set_output
        for each_row in file_csv:
            data_set_output.append(each_row)
        return data_set_output
    





# ######################################################## #
# ######################################################## #
# ######################################################## #
# 2. READING EPISODES.CSV                                  #
# ######################################################## #
# ######################################################## #
# ######################################################## #

episodes = read_csv_file('episodes.csv')
# The data type of "episodes" is a list
# Each element of the list is a dictionary
# data type.

print(episodes)
# You can just tell Python to
# print a list, and it'll just do it.
# You don't have to make a loop or
# anything.

# However, if you're printing a list of
# dictionaries, and you only want a specific
# value of each dictionary, you'll need a
# loop.
for each_episode in episodes:
    print(each_episode["Length"])

# Tip: accessing dictionary values are just like accessing array values,
# but instead of putting an index, you put the parameter name.






# ######################################################## #
# ######################################################## #
# ######################################################## #
# 3. READING SLOTH-THEFT.CSV                               #
# ######################################################## #
# ######################################################## #
# ######################################################## #

sloth_thieves = read_csv_file("sloth-theft.csv")
print ("Number of sloths: " + str(len(sloth_thieves)))

for each_sloth in sloth_thieves:
    print(each_sloth["Name"] + " stole $" + each_sloth["Amount stolen"])
    # You can also do print(each_sloth["Name"], "stole $", each_sloth["Amount stolen"]),
    # and this automatically puts spaces between the three items... but then there will
    # be a spac between the dollar sign and the amount.

total_amount_stolen = 0

for each_sloth in sloth_thieves:
    total_amount_stolen += (float(each_sloth["Amount stolen"]))

print("Total amount stolen:", total_amount_stolen)

print("-----------------------------------------------------")






# ######################################################## #
# ######################################################## #
# ######################################################## #
# 4. READING DB-LESSON-SCORES-BAD-DATA.CSV                 #
# ######################################################## #
# ######################################################## #
# ######################################################## #



# ######################################################## #
# ######################################################## #
# ######################################################## #
# 4.a. READING DB-LESSON-SCORES-BAD-DATA.CSV: FUNCTION     # 
#      DEFINITIONS                                         #
# ######################################################## #
# ######################################################## #
# ######################################################## #

def the_score_is_okay(score_value_input):
    # if score_value_input can't be convrted to a number, return false
    try:
        score_value_input = float(score_value_input)
    except ValueError:
        return False

    if score_value_input < 0 or score_value_input > 100:
        return False

    # If none of those conditions are the case...
    return True

def the_record_is_okay(record_input):
    if record_input["Goat"] == "" or record_input["Goat"] == None:
        return False
    
    if not the_score_is_okay(record_input["Before"]) or not the_score_is_okay(record_input["After"]):
        return False
    
    # If none of those conditions are the case...
    return True



# ######################################################## #
# ######################################################## #
# ######################################################## #
# 4.b. READING DB-LESSON-SCORES-BAD-DATA.CSV: MAIN CODE    #
# ######################################################## #
# ######################################################## #
# ######################################################## #

goat_scores_data = read_csv_file("db-lesson-scores-bad-data.csv")
print ("Number of records:" + str(len(goat_scores_data)))

for each_piece_of_data in goat_scores_data:
    print(each_piece_of_data["Goat"])

print(goat_scores_data[7]["Goat"], "has score", goat_scores_data[7]["Before"], ". Why is it 2 numbers? Remember, the CSV data is bad. The writer of the CSV forgot to put a comma between the two scores, so this is what happens.")

total_before = 0
total_after = 0

print("Goat score totals:")

for each_piece_of_data in goat_scores_data:
    # print("Currently evaluating goat", each_piece_of_data["Goat"])
    if the_record_is_okay(each_piece_of_data):
        total_before += float(each_piece_of_data["Before"])
        total_after += float(each_piece_of_data["After"])

print("Total before: " + str(total_before))
print("Total after: " + str(total_after))






# ######################################################## #
# ######################################################## #
# ######################################################## #
# 5. READING MOVIE RATINGS.CSV                             #
# ######################################################## #
# ######################################################## #
# ######################################################## #



# ######################################################## #
# ######################################################## #
# ######################################################## #
# 5.a. READING MOVIE RATINGS.CSV: FUNCTION DEFINITIONS     #
# ######################################################## #
# ######################################################## #
# ######################################################## #

# Why I put so mch effort into this practice problem (from https://python.skilling.us/lesson/cleaning-0)
# * It's great practice, as I may encounter something like this in the real-world
# * I may find that I'll want to re-use this code

def this_character_is_a_letter(character_input):

    if character_input == "A" or character_input == "a":
        return True
    elif character_input == "B" or character_input == "b":
        return True
    elif character_input == "C" or character_input == "c":
        return True
    elif character_input == "D" or character_input == "d":
        return True
    elif character_input == "E" or character_input == "e":
        return True
    elif character_input == "F" or character_input == "f":
        return True
    elif character_input == "G" or character_input == "g":
        return True
    elif character_input == "H" or character_input == "h":
        return True
    elif character_input == "I" or character_input == "i":
        return True
    elif character_input == "J" or character_input == "j":
        return True
    elif character_input == "K" or character_input == "k":
        return True
    elif character_input == "L" or character_input == "l":
        return True
    elif character_input == "M" or character_input == "m":
        return True
    elif character_input == "N" or character_input == "n":
        return True
    elif character_input == "O" or character_input == "o":
        return True
    elif character_input == "P" or character_input == "p":
        return True
    elif character_input == "Q" or character_input == "q":
        return True
    elif character_input == "R" or character_input == "r":
        return True
    elif character_input == "S" or character_input == "s":
        return True
    elif character_input == "T" or character_input == "t":
        return True
    elif character_input == "U" or character_input == "u":
        return True
    elif character_input == "V" or character_input == "v":
        return True
    elif character_input == "W" or character_input == "w":
        return True
    elif character_input == "X" or character_input == "x":
        return True
    elif character_input == "Y" or character_input == "y":
        return True
    elif character_input == "Z" or character_input == "z":
        return True
    else:
        return False

def remove_anything_that_isnt_a_letter_in(string_input):
    string_output = string_input
    current_character = 0
    last_character_that_is_a_letter = -1
    first_half_of_string = ""
    second_half_of_string = ""

    # Go through the entire string from left-to-right, and each time a non-letter is encountered, get rid of it.
    while current_character < len(string_output):

        if not this_character_is_a_letter(string_output[current_character]):

            # Get rid of the current character from the string. To do so, do the following.
            
            # 1) Get everything that is before the current character
            if current_character > 0:
                first_half_of_string = string_output[0 : current_character]
            else:
                first_half_of_string = ""   # This could potentially trigger an error. Consider replacing with ""
                                            # (although also be mindful that "" might somehow count as an additional
                                            # character like a space or something)

            # 2) Get everything that is after the current character
            if current_character != len(string_output) - 1:
                second_half_of_string = string_output[current_character + 1 : len(string_output)]
            else:
                second_half_of_string = ""

            # 3) Put these two halves together, and now you have the string except with the current character removed
            string_output = first_half_of_string + second_half_of_string

            # Removing this character will offset the current_character, because now that current_character is
            # gone, "current_character" will now point to the next character, which is bad because we will evntually
            # move onto the next character, so we will skip a character. (Just keep reading, it will make sense.)
            current_character -= 1
        # Move onto the next character
        current_character += 1
        # According to this logic, if we ended up removing a character, it would look something like this (the down arrow 
        # points at the current character):
        #   v
        # gg hij 1k
        #
        #   v
        # gghij 1k (Remove character)
        #
        #  v
        # gghij 1k (current_character -= 1)
        #
        #   v
        # gghij 1k (current_character += 1)
        # Meanwhile, if we did not remove a character:
        #   v
        # gghij 1k
        #
        #    v
        # gghij 1k (current_character += 1)

    return string_output


#def record_is_valid (record_input):
# Maybe bfore this, convert it to caps. See if Python has a built-in toUpperCase() thing
#    try:
#        # j
#         
#    except ValueError:
#        # j
#
# In here or in the main code: see if the resulting string from remove_anything_that_isnt_a_letter_in()
# matches one of the three valid genres.
# Then you also must do the critics average and audience rating average by adding anything that IS a number.
#



# ######################################################## #
# ######################################################## #
# ######################################################## #
# 5.b. READING MOVIE RATINGS.CSV: MAIN CODE                #
# ######################################################## #
# ######################################################## #
# ######################################################## #

movie_ratings_data = read_csv_file("movie-ratings.csv")
print(movie_ratings_data)

current_row = 2

# print("'" + remove_anything_that_isnt_a_letter_in(movie_ratings_data[17]["Genre"]) + "'")

for each_movie in movie_ratings_data:
    # save string before removal
    # save string after removal
    # if two strings don't match, entry is invalid
    # elif string doesn't match one of the three valid genres, string is invalud
    # else string is valid
    print(str(current_row) + " " + remove_anything_that_isnt_a_letter_in(each_movie["Genre"]))
    current_row += 1

print ("Done!")
print ("----------------------------------------------------------")
