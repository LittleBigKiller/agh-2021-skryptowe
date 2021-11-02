import sys
import re

def find_functions(lines):
    # (?<!^)            - negative lookbehind, nie na początku
    # \w+               - słowne znaki
    # (?=\s+\()         - positive lookahead, przerwa dowolnej długości i otwarcie nawiasu
    # (?![^\/\*]+\*\/)  - negative lookahead, nie w komentarzu
    fun_magic = re.compile(r'(?<!^)\w+(?=\s+\()(?![^\/\*]+\*\/)')
    
    fun_names = re.findall(fun_magic, lines)

    return ''.join(['Deklaracja funkcji ' + x.strip() + '()\n' for x in fun_names])

def find_comments(lines, fold=False):
    # (?![^\/\*]+\*\/)  - positive lookahead, w komentarzu
    # [^\*\/]+          - dowolne znaki poza '*' i '/', w dowolnej ilości (przynajmniej jeden)
    com_magic = re.compile(r'(?=[^\/\*]+\*\/)[^\*\/]+')

    com_names = re.findall(com_magic, lines)

    if fold:
        return '// ' + '\n//'.join(x.rstrip().replace('\n', ' ') for x in com_names)[1:]
    else:
        return ''.join(x.rstrip().replace('\n', '\n// ') for x in com_names)[1:]

if __name__ == '__main__':
    file_content = open("./main.c", "r").read()

    if len(sys.argv) > 1:
        if sys.argv[1] == '--fold':
            print(find_comments(file_content, True))
        else:
            print(find_comments(file_content))
    else:
        print(find_comments(file_content))
    
    print(find_functions(file_content))

