# String formatting exercise

# Returns input unaltered if it is not a tuple or if it does not have exactly 4 elements. If the input tuple has 4
# elements, returns a string of the formatted elements of the tuple
def task1_formatter(in_tuple):
    if (isinstance(in_tuple, tuple) == False):
        return in_tuple
    if (len(in_tuple) != 4):
        return in_tuple
    
    # in_tuple is a tuple with 4 elements
    formatter = "file_{:03d} : {: 5.2f}, {:.2e}, {:.2e}"
    return (formatter.format(int(in_tuple[0]), float(in_tuple[1]), float(in_tuple[2]), float(in_tuple[3])))

# Does the same thing as task1_formatter in a different way
def task2_formatter(in_tuple):
    if (isinstance(in_tuple, tuple) == False):
        return in_tuple
    if (len(in_tuple) != 4):
        return in_tuple
    
    # in_tuple is a tuple with 4 elements
    file = "{:03d}".format(in_tuple[0])
    float_str = "{: 5.2f}".format(in_tuple[1])
    scientific_str1 = "{:.2e}".format(in_tuple[2])
    scientific_str2 = "{:.2e}".format(in_tuple[3])
    return (f"file_{file} : {float_str}, {scientific_str1}, {scientific_str2}")
    
# Returns a string formatted with the elements of an in_tuple t = (1,2,3) as "'the 3 numbers are: 1, 2, 3'"   
def task3_formatter(in_tuple):
    # since we need to add the number of elements of the tuple to the formatted string, create a new tuple
    # with the length of the input_tuple as it's first element and the elements of input_tuple as the rest
    # as the first element of a new tuple and 
    num_elements = len(in_tuple)
    if (num_elements < 1):
        return "the tuple has no elements"
    length = (num_elements,)
    t = tuple(length + in_tuple)
    
    # pass the new tuple to the formatter and return the formatted string
    return (formatter(t))

# Formatter function for Task 3. 
def formatter(t):
    # Format the first part of the string
    format_string = "the {:d} numbers are:"
    
    # Add formatting elements as needed for the number of elements in the tuple
    for i in range(1,len(t)):
        format_string += " {:d},"
        
    # remove the trailing comma at the end of the last element
    format_string = format_string[0:-1]
    
    # return the formatted string
    return (format_string.format(*t))

def task4_formatter(in_tuple):
    # return error message if tuple does not have 5 elements
    if (len(in_tuple) != 5):
        return "this tuple does not have exactly 5 elements"
    
    #slice the tuple into first 2 elements, middle and last 2 elements
    # format string with the first part of the tuple without trailing blank as this will be the end of the new tuple
    formatter = "{:02d} {:02d}"
    first_str = formatter.format(*in_tuple[:2])
    
    # format string with the middle of the tuple
    formatter = "{:02d} "
    middle_str = formatter.format(in_tuple[2])
    
    # format string with the last part of the tuple and trailing blank as this is the first part of the new tuple
    formatter = "{:02d} {:02d} "
    last_str = formatter.format(*in_tuple[-2:])
    
    # Complete the string in the new order and return
    return(last_str + middle_str + first_str)

def task5_formatter(in_list):
    # return error if length of list is less than one pair of values or not an even number indicating that the 
    # list does not have a pair of values
    if (len(in_list) < 2 or (len(in_list) % 2 != 0)):
        return "this list does not have pairs of values"
    
    # initialize formatted string
    formatted_string = ""
    
    # process pairs of elements in the list"
    for i in range(0, len(in_list), 2):
    
        # Use Upper case to begin the string and lower case after that
        if (i == 0):
            formatted_string += f"The weight of a"
        else:
            formatted_string += f"the weight of a"
        
        # Add 'n' to make 'an' for words beginning with vowels
        if (in_list[i][0] in ["a", "e", "i", "o", "u"]):
            formatted_string += 'n'
        
        # format string as needed
        formatted_string += f" {in_list[i][:-1]} is {in_list[i+1]} and "
    
    # List is complete, remove trailing blank and 'and' at end of string and return
    return formatted_string[:-5]
    
def print_border():
    print("-" * 50)
    return
    
def print_heading(edge_str):
    # defing edge char and column names
    
    columns = ["{:32}".format("Name"), "{:4}".format("Age"), "{:7}".format("Earns")]
    
    # build heading string
    heading_str = edge_str
    for i in range(len(columns)):
        heading_str += columns[i] + edge_str
    
    # remove trailing blank
    print(heading_str[:-1])
    return

def print_lines(in_list, edge_str):

    # We need to step in threes, so in order to stay within range
    max_index = len(in_list) - 2
    
    # Format each element of the list needed for a line and print
    for i in range(0, max_index, 3):
        line_str = edge_str
        line_str += "{:32}".format(in_list[i]) + edge_str
        line_str += "{:4}".format(in_list[i+1]) + edge_str
        line_str += "{:7}".format(in_list[i+2]) + edge_str
        # remove trailing blank
        print(line_str[:-1])
    return

   
def print_task6_table(in_list):
    #define an edge char to be used for the heading and each line in the table
    edge_str = "| "
    print_border()
    print_heading(edge_str)
    print_border()
    print_lines(in_list, edge_str)
    print_border()
    return
    

if __name__ == "__main__":
    # 
    tuple1 = (2, 123.4567, 10000, 12345.67)
    tuple3 = (5, 6, 7, 8, 9, 10, 11, 12, 13)
    tuple4 = (4, 30, 2017, 2, 27)
    list5 = ['oranges', 1.3, 'lemons', 1.1]
    list6 = ['Infant', 0, 0, 'Child', 5, 1, 'Teenager', 15, 10, 'Young Adult', 23, 50, 'Adult' , 40, 10000, 'Senior', 60, 100000, 'Centenarian' , 100, 0]
    
    
    
    assert task1_formatter(tuple1) == 'file_002 :  123.46, 1.00e+04, 1.23e+04'
    
    assert task2_formatter(tuple1) == 'file_002 :  123.46, 1.00e+04, 1.23e+04'
    
    assert task3_formatter(tuple3) == 'the 9 numbers are: 5, 6, 7, 8, 9, 10, 11, 12, 13'
    
    assert task4_formatter(tuple4) == '02 27 2017 04 30'
    
    assert task5_formatter(list5) == 'The weight of an orange is 1.3 and the weight of a lemon is 1.1'
    
    print("tests passed")
    
    print_task6_table(list6)
    
    
    
    