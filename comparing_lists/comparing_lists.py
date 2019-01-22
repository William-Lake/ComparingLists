import os
import sys
from target_list import Target_List

'''
1. Get the two lists to compare from the user
    1. What do we call this list?
    2. What will the delimiter be?
    3. What are the values?
2. Provide output re: List comparison
    1. INNER JOIN - What they have in common
    2. LEFT JOIN - What's in list 1, not in list 2
    3. RIGHT JOIN - What's in list 2, not in list 1
'''

clear = lambda: os.system('cls')

def gather_input(prompt,single_line=True):

    clear()

    response = ''

    while True:

        print(prompt)

        if single_line: response = sys.stdin.readline().strip()

        else:

            print('When finished, press Ctrl + Z, then Enter, when finished.')

            response = sys.stdin.read()

        if len(response) > 0: return response

        print('Please provide some input.\n\n')

def gather_list():

    list_name = gather_input('List Name?')

    list_delimiter = gather_input('List Delimiter? If you want to use newline, type \'\\n\'')

    if list_delimiter == '\\n': list_delimiter = '\n'

    list_data = gather_input('List Data?',single_line=False)

    list_items = list_data.split(list_delimiter)

    if len(list_items[len(list_items) - 1].strip()) == 0: del list_items[len(list_items) - 1]

    comparison_list = Target_List(list_name,list_items)

    return comparison_list

def provide_output(title,items):

    print('+------------------------+')

    print(title)

    print('======================')

    for item in items: print(item)

    print('+------------------------+')

def main():

    while True:

        clear()

        first_list = gather_list()

        second_list = gather_list()

        inner_join = list(set(first_list.items).intersection(second_list.items))

        left_join = list(set(first_list.items).difference(second_list.items))

        right_join = list(set(second_list.items).difference(first_list.items))

        clear()

        provide_output('Items in both \'{}\' and \'{}\' ({} total)'.format(first_list.name,second_list.name,len(inner_join)),inner_join)

        provide_output('Items in \'{}\', and not in \'{}\' ({} total)'.format(first_list.name,second_list.name,len(left_join)),left_join)

        provide_output('Items in \'{}\', and not in \'{}\' ({} total)'.format(second_list.name,first_list.name,len(right_join)),right_join)

        print('\nWould you like to do another?')

        do_another = sys.stdin.readline().strip().upper()[0] == 'Y'

        clear()

        if do_another == False: break