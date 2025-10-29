import csv

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
