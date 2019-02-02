#!/usr/bin/env python3


FRUIT_LIST = ['Apples', 'Pears', 'Oranges', 'Peaches']

def main():

    def series_one(fruit_list):
        print(fruit_list)
        answer = input('What fruit to you want to add?')
        fruit_list.append(answer)
        print(fruit_list)
        index_answer = int(input(f'Please enter a number between 1 and {len(fruit_list)}'))
        print(fruit_list[index_answer - 1])
        # add new fruit begging of list
        fruit_list = ['Pineapple'] + fruit_list
        print(fruit_list)
        fruit_list.insert(0, 'Tomato')
        print(fruit_list)
        for i in fruit_list:
            if i[0] == 'P':
                print(i)

    series_one(FRUIT_LIST)


    def series_two(fruit_list):
        # includes bonus
        print(fruit_list)
        fruit_list.pop()
        print(fruit_list)
        delete_answer = input('Select a fruit to delete')
        fruit_list = fruit_list * 2
        while delete_answer not in fruit_list:
            delete_answer = input('Please select another fruit')
        else:
            for i in fruit_list:
                if i == delete_answer:
                    fruit_list.remove(i)
        print(fruit_list)

    series_two(FRUIT_LIST)


    def series_three(fruit_list):
        acceptable_answers = {'yes', 'no'}
        result = []
        for i in fruit_list:
            answer = input(f'Do you like {i}?')
            while answer.lower() not in acceptable_answers:
                answer = input(f'Please answer yes or no: Do you like {i}?')
                continue
            if answer.lower() != 'no':
                result.append(i)
        print(result)

    series_three(FRUIT_LIST)

    def series_four(fruit_list):
        result = []
        for i in fruit_list:
            result.append(i[::-1])
        fruit_list.pop()
        print(f'Copy of original with letters of each item reversed: {result}')
        print(f'Original with last item removed: {fruit_list}')

    series_four(FRUIT_LIST)

if __name__ == '__main__':
    main()

