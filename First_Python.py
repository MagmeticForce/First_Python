int, int_2 = 3, 7;
sum = int + int_2;


print ('Hello. Sum is: ');
print (sum);


my_array_of_numbers = [0, 1, 2, 3, 5, 4];


def swap(array_input, first_index_to_swap_input, second_index_to_swap_input):

    """Swap two indices of an array."""
    if (array_input.length <= 0):
        print('Could not perform swap. Array is empty!');
        
    temp = array_input[second_index_to_swap_input];
    array_input[second_index_to_swap_input] = array_input[first_index_to_swap_input];
    array_input[first_index_to_swap_input] = temp;
    
    
