import sys
import re

def match_oc(lines):
    if re.search(r'\/\*[\r\n|\n]*', lines):
        return True
    else:
        return False
    
def match_occ(lines):
    if re.search(r'\/\*.*', lines):
        return True
    else:
        return False

def match_cc(lines):
    if re.search(r'\*\/[\r\n|\n]+', lines):
        return True
    else:
        return False

def main(fold=False):
    f = open("./main.c", "r")

    in_comment = False
    comment_started = False
    ret_str = ""

    for line in f.readlines():
        if not in_comment:
            if match_oc(line):
                in_comment = True
            elif match_occ(line):
                in_comment = True
                ret_str += re.sub(r'\/\*', r'\/\/ ', line)
            else:
                ret_str += line
        else:
            if match_cc(line):
                in_comment = False
                comment_started = False
            else:
                if not fold or (fold and not comment_started):
                    ret_str += '// ' + line
                    comment_started = True
                else:
                    ret_str = ret_str[0:-2] + ' ' + line
    return ret_str
                
if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '--fold':
            print(main(True))
        else:
            print(main())
    else:
        print(main())

