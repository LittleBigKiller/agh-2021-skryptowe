import re

def match_words(string):
    pat_letters = re.compile(r'\D+')
    res_letters = pat_letters.finditer(string)
    
    return res_letters

def match_numbers(string):
    pat_numbers = re.compile(r'\d+')
    res_numbers = pat_numbers.finditer(string)
    
    return res_numbers


if __name__ == '__main__':
    test_string = input()

    matches = []

    word_res = match_words(test_string)        
    number_res = match_numbers(test_string)
    matches.extend(word_res)
    matches.extend(number_res)
    
    match_list = []
    for match in matches:
        match_list.append([match.start(), match.group()])

    match_list.sort()

    nml = []
    for _,cont in match_list:
        nml.extend(cont.split(' '))

    nml = [x for x in nml if x]

    for match in nml:
        if match.isnumeric():
            print(f'Liczba: {match}')
        else:
            print(f'Wyraz: {match}')