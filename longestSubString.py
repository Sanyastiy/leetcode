def longstr(somestring):
    strtocount = sorted(set(somestring))
    return print(strtocount,len(strtocount))


while 1:
    rare = input('enter the word. x for exit\n')
    if rare == 'x' or rare == 'X':
        break
    longstr(rare)
