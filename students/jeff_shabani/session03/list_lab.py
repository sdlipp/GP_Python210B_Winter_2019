#!/usr/bin/env python3


fruit_list = ['Apples', 'Pears', 'Oranges', 'Peaches']

def main():

    def series_one(f_list):
        print(f_list)
        answer = input('What fruit to you want to add?')
        f_list.append(answer)
        print(f_list)
        index_answer = int(input(f'Please enter a number between 1 and {len(f_list)}'))
        print(f_list[index_answer - 1])
        # add new fruit begging of list
        f_list = ['Pineapple'] + f_list
        print(f_list)
        f_list.insert(0, 'Tomato')
        print(f_list)
        for i in f_list:
            if i[0] == 'P':
                print(i)

    series_one(fruit_list)


    def series_two(f_list):
        # includes bonus
        print(f_list)
        f_list.pop()
        print(f_list)
        delete_answer = input('Select a fruit to delete')
        f_list = f_list * 2
        while delete_answer not in f_list:
            delete_answer = input('Please select another fruit')
        else:
            for i in f_list:
                if i == delete_answer:
                    f_list.remove(i)
        print(f_list)

    series_two(fruit_list)


    def series_three(f_list):
        acceptable_answers = {'yes', 'no'}
        result = []
        for i in f_list:
            answer = input(f'Do you like {i}?')
            while answer.lower() not in acceptable_answers:
                answer = input(f'Please answer yes or no: Do you like {i}?')
                continue
            if answer.lower() != 'no':
                result.append(i)
        print(result)

    series_three(fruit_list)

    def series_four(f_list):
        result = []
        for i in f_list:
            result.append(i[::-1])
        f_list.pop()
        print(f'Copy of original with letters of each item reversed: {result}')
        print(f'Original with last item removed: {f_list}')

    series_four(fruit_list)

if __name__ == '__main__':
    main()

