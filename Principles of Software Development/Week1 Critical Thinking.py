#!/usr/bin/env python
# Week1 Critical Thinking Text Editor 
""" Text Editor 
(1) Prompt the user to enter a string of text.  
(2) Implement the print_menu() function to print the menu.  
(3) Implement the execute_menu() function.
(4) Call print_menu() and prompt for the user's choice of menu options.  
(5) Implement the get_num_of_non_WS_characters() function that returns the number of characters in the string, excluding all whitespace.  
(6) Implement the get_num_of_words() function.  
(7) Implement the fix_capitalization() function. lowercase letters at the beginning of sentences are replaced with uppercase letters.   
"""

def print_menu():
    menu={'c':'Number of non-whitespace characters',
          'w':'Number of words',
          'f':'Fix capitalization',
          'q':'Quit'}
    print('\nMENU')
    for key, value in menu.items():
        print(f'{key} - {value}', end='\n')

def get_num_of_non_WS_characters(input_str):
    num=sum( 0 if i.isspace() else 1 for i in input_str)
    return num

def get_num_of_words(input_str):
    return len(input_str.split())

def fix_capitalization(input_str):
    entry=input_str.split()
    num=0
    newString=''
    newList=[]
    for index, item in enumerate(entry):
        if index==0 and item[0].islower():
            item = item[0].upper() + item[1:]
            num+=1
        if item.endswith(('.', '?')) and index < len(entry) - 1:
            entry[index+1] = entry[index+1][0].upper() + entry[index+1][1:]
            num+=1
        newList.append(item)
    newString=' '.join(newList)
    return num, newString


def execute_menu(choice, sample):
    if choice=='c':
        print("Number of non-whitespace characters:", get_num_of_non_WS_characters(sample))
    elif choice=='w':
        print("Number of words:", get_num_of_words(sample))
    elif choice=='f':
        num, edit=fix_capitalization(sample)
        print("Number of letters capitalized:", num,'\nEdited text:', edit)

def main():
    sample=input('Enter a sample text:\n')
    print(f'\nYou entered: {sample}')
    print_menu()
    while True:
        try:
            choice=input('\nChoose an option:\n')
            if choice in['q']:
                break
            elif choice in ['c','w','f']:
                execute_menu(choice, sample)
                print_menu()
            else:
                raise ValueError
        except ValueError:
            print('Value Error')

if __name__ == '__main__':
    main()
