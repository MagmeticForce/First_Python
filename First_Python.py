

int, int_2 = 3, 7;
sum = int + int_2;


print ('Hello. Sum is: ');
print (sum);


my_array_of_numbers = [5, 6, 7, 8, 10, 9];

print ('Initial array:');

# Print initial array:
for each_indiviual_index in my_array_of_numbers:
#for (var current_index = 0; current_index < my_array_of_numbers; current_index++):
    print (each_indiviual_index);
    
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

# Print the array:
print ('Array after swap:');
for each_indiviual_index in my_array_of_numbers:
    print (each_indiviual_index);
