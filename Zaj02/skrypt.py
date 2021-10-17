import re

def match_word(string):
    pat_letters = re.compile(r'[^\d|^\s]+')
    res_letters = pat_letters.search(string)
    
    if res_letters:
        return (res_letters.start(), res_letters.group())
    else:
        return None

def match_number(string):
    pat_numbers = re.compile(r'\d+')
    res_numbers = pat_numbers.search(string)
    
    if res_numbers:
        return (res_numbers.start(), res_numbers.group())
    else:
        return None



if __name__ == '__main__':
    while True:
        try:
            test_string = input()
            word_res = match_word(test_string)        
            number_res = match_number(test_string)
            
            if number_res and word_res:
                if number_res < word_res:
                    print('Liczba: {}'.format(number_res[1]))
                    print('Wyraz: {}'.format(word_res[1]))
                else:
                    print('Wyraz: {}'.format(word_res[1]))
                    print('Liczba: {}'.format(number_res[1]))
            elif word_res:
                print('Wyraz: {}'.format(word_res[1]))
            elif number_res:
                print('Liczba: {}'.format(number_res[1]))
        except:
            break