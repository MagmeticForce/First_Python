from enum import Enum


int, int_2 = 3, 7;
sum = int + int_2;


my_array = [0, 1, 2, 3]
print ('Hello. Second-to-last index is: ');
print(my_array[-2]) # -2 means "second-to-last index"


print ('Sum is: ');
print (sum);


my_array_of_numbers = [5, 6, 7, 8, 10, 9];

print ('Initial array:');

# Print initial array:
for each_indiviual_index in my_array_of_numbers:
#for (var current_index = 0; current_index < my_array_of_numbers; current_index++):
    print (each_indiviual_index);
    
# Function definition for "swap()"
def swap(array_input, first_index_to_swap_input, second_index_to_swap_input):

    """Swap two indices of an array."""
    
    # If the array is empty, do not proceed and print a message: 
    if (len(array_input) <= 0):
        print('Could not perform swap. Array is empty!');
        return my_array_of_numbers;
      
    # If either of the indices are too large, do not proceed and print a message: 
    if (first_index_to_swap_input >= len(array_input) or second_index_to_swap_input >= len(array_input)):
        print('Could not perform swap. One of your indices are too large!');
        return my_array_of_numbers;
    
    # If either of the indices are too small, do not proceed and print a message: 
    if (first_index_to_swap_input < 0 or second_index_to_swap_input < 0):
        print('Could not perform swap. One of your indices are too small!');
        return my_array_of_numbers;

    temp = array_input[second_index_to_swap_input];
    array_input[second_index_to_swap_input] = array_input[first_index_to_swap_input];
    array_input[first_index_to_swap_input] = temp;
    
    return my_array_of_numbers;

my_array_of_numbers = swap(my_array_of_numbers, 4, 5);

# Now order in descending order:
my_array_of_numbers = swap(my_array_of_numbers, 0, 5);
my_array_of_numbers = swap(my_array_of_numbers, 1, 4);
my_array_of_numbers = swap(my_array_of_numbers, 2, 3);

# Print the array:
print ('Array after swap:');
for each_indiviual_index in my_array_of_numbers:
    print (each_indiviual_index);
    
class Person:
    
    # The __init()__ function is similar to the constructor, which is known as "__new__()" in Python.
    # __init()__ is run after __new()__ and is used more frequently. __new()__ is for more advanced
    # things (one thing you can use it for is ensuring only one instance of an object exists...this
    # is called a "singleton").
    # The first argument of any function inside of a class must be "self", which refers to the current object.
    def __init__(self, name_input, age_input):
        # Create new parameters "name" and "age" for this object:
        self.name = name_input
        self.age = age_input
        
    # Create new parameter "creature"
    creature = "Unspecified"
    
    def talk(self, speaker_input, speech_input):
        print(speaker_input, ": ", speech_input)
                            
class Human (Person):
    
    def __init__(self, name_input, age_input):
        # Create new parameters "name" and "age" for this object:
        self.name = name_input
        self.age = age_input
        
    creature = "Human"
    
    hair_color = 0 # Python doens't like it when you create a variable but don't assign it anything, unlike Java or C++.
                   # Assign your variables default values.
    
class Alien (Person):
    
    def __init__(self, name_input, age_input):
        # Create new parameters "name" and "age" for this object:
        self.name = name_input
        self.age = age_input
    
    creature = "Alien"
    
class Hair_Color(Enum):
    BLACK = 0
    BROWN = 1
    BLOND = 2
    RED = 3
    WHITE = 4
    
Rosie = Person("Rosie", 18)
Rosie.hair_color = Hair_Color.BROWN

print (Rosie.name)
print (Rosie.hair_color)
Rosie.talk(Rosie.name, "Hello! I hope you have a wonderful day!")

    
    
