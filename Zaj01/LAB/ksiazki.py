import sys

def process_params(instring):
    dic = {}

    for line in instring:
        line = line.split(':')

        if len(line) != 2:
            continue

        try:
            dic[line[0]] = int(line[1])
        except:
            continue

    return dic

def process_input(lines, book_dict):
    bhd = {}
    bd = dict(book_dict)

    for line in lines:
        if line[1] not in bd.keys():
            continue
        if line[2] == 'pozycz':
            if bd[line[1]] > 0:
                bd[line[1]] -= 1
                if line[0] not in bhd.keys():
                    bhd[line[0]] = [line[1]]
                else:
                    bhd[line[0]].append(line[1])
        elif line[2] == 'zwroc':
            if line[0] not in bhd.keys():
                continue
            if line[1] in bhd[line[0]]:
                bhd[line[0]].remove(line[1])
                bd[line[1]] += 1

    
    return bhd, bd


if __name__ == '__main__':
    book_nums = process_params(sys.argv[1:])

    uin = sys.stdin.readlines()
    uin = [x.rstrip().split() for x in uin if len(x.rstrip().split()) == 3]

    book_holders, book_nums = process_input(uin, book_nums)

    print('\nKsiążki wypożyczone:')
    for k in book_holders:
        if book_holders[k]:
            print(f'\t{k}: {", ".join(book_holders[k])}')

    print('\nKsiążki w bibliotece:')
    for k in book_nums:
        if book_nums[k]:
            print(f'\t{k}: {book_nums[k]}')