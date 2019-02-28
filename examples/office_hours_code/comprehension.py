'''
A couple of demos on recursion
'''

def remove_proper_nouns(data_list):
    '''
    Removes proper nours from a list of strings
    '''
    output_list = []
    for noun in data_list:
        if noun[0].islower():
            output_list.append(noun)
    return output_list

def throw_party(agent_list):
    '''
    Decides what agents get a party
    You have to have more than 50 missions and
    you can't be undercover
    '''
    output_list = []
    for agent_info in agent_list:
        if agent_info["missions"] >= 50 and not agent_info["undercover"]:
            output_list.append(agent_info["full_name"])
    return output_list

def main():
    '''
    Main flow
    '''
    # First example
    original_word_list = ['beetle', 'muzzle', 'Brian', 'in', 'Rucastles',
                          'Teresa', 'while', 'he', 'Washington', 'and']
    word_list = remove_proper_nouns(original_word_list)
    print(word_list)

    # Now with list comprehension (one line versus four)
    second_word_list = [x for x in original_word_list if x[0].islower()]
    print(second_word_list)

    # Second example
    current_agents = [
        {
            'full_name': 'James Bond',
            'missions': 55,
            'undercover': False
        },
        {
            'full_name': 'Q',
            'missions': 37,
            'undercover': True
        },
        {
            'full_name': 'M',
            'missions': 75,
            'undercover': False
        },
        {
            'full_name': 'KR',
            'missions': 25,
            'undercover': True
        }
    ]
    print(throw_party(current_agents))

    # Now, using comprehension
    party_list = [agent["full_name"] for agent in current_agents if agent["missions"] >= 50 and not agent["undercover"]]
    print(party_list)

if __name__ == "__main__":
    main()
