#Slicing Lab

# Returns the sequence that was passed in with its first element and last element exchanged
def exchange_first_last(seq):
    #minimal error checking
    if (len(seq) < 2):
        return seq
    #first_last_switched is a list created from the input sequence
    first_last_switched = list(seq)
    
    #Use the switch capability of the list type
    first_last_switched[0], first_last_switched[len(seq)-1] = first_last_switched[len(seq)-1], first_last_switched[0]
    
    #Check ttype in order to return a sequence of the same type as the input sequence
    if (isinstance(seq, str)):
        return "".join(first_last_switched[0] + seq[1:-1] + first_last_switched[-1])
    else:
        return tuple(first_last_switched)

# Returns a sequence with every other item removed
def remove_every_other_item(seq):
    every_other_item = seq[::2]
    return every_other_item

# Returns a sequence that results from removing the first 4 and last 4 elements from the input sequence and then 
# every other item from the remaining sequence. If the length of the sequence is less than 8, 
# the input sequence is returned unchanged
def remove_first4_last4_and_everyother_item(seq):
    #minimal error checking
    if (len(seq) < 8):
        return seq
    else:
        modified_string = seq[4:-4:2]
        return modified_string

# Returns a sequence with the elements reversed    
def reverse_elements(seq):
    reversed_string = seq[::-1]
    return reversed_string
    
# Returns a new sequence with the last third, then first third, then the middle third in the new order. 
def reorg_by_thirds(seq):
    #Check if the sequence is divisible into 3 parts
    length_of_third = len(seq) // 3
    if (length_of_third > 1):
        first_part = seq[:-length_of_third]
        last_part = seq[-length_of_third:]
        if (isinstance(seq, str)):
            return ("".join(last_part + first_part))
        else:
            return tuple(last_part + first_part)
            
    # if the sequence is too short to be divided into 3 parts return the sequence as passed in
    return seq
    
    

if __name__ == "__main__":
    # run some tests
    a_string = "this is my testing string"
    a_tuple = (2, 54, 13, 12, 5, 32, 24, 11, 61, 26, 4, 7)
    
    assert exchange_first_last(a_string) == "ghis is my testing strint"
    assert exchange_first_last(a_tuple) == (7, 54, 13, 12, 5, 32, 24, 11, 61, 26, 4, 2)

    assert remove_every_other_item(a_string) == "ti sm etn tig"
    assert remove_every_other_item(a_tuple) == (2, 13, 5, 24, 61, 4)    

    assert remove_first4_last4_and_everyother_item(a_string) == " sm etn t"
    assert remove_first4_last4_and_everyother_item(a_tuple) == (5, 24)
    
    assert reverse_elements(a_string) == "gnirts gnitset ym si siht"
    assert reverse_elements(a_tuple) == (7, 4, 26, 61, 11, 24, 32, 5, 12, 13, 54, 2)
    
    assert reorg_by_thirds(a_string) == "g stringthis is my testin"
    assert reorg_by_thirds(a_tuple) == (61, 26, 4, 7, 2, 54, 13, 12, 5, 32, 24, 11)
    
    print("tests passed")