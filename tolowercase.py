def TLC(some_string):
    uppers = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
              "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lowers = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
              "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    count = -1
    result = ""
    ourstr = list()
    for i in some_string:
        count += 1
        ourstr.append(i)
        if i in uppers:
            ourstr[count] = lowers[uppers.index(i)]
    result = "".join(ourstr)
    return print(result)


TLC(input("enter string to make to lowercase\n"))
