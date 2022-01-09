noum = '123456789'
r = {'O', 'X'}
change = ['|  1  |  2  |  3  |', '|  4  |  5  |  6  |', '|  7  |  8  |  9  |']
form = ['|-----|-----|-----|', '|-----|-----|-----|', '|-----|-----|-----|', '|-----|-----|-----|']
com = [['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'], ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],
       ['3', '5', '7'], ['1', '5', '9']]
print('|-----|-----|-----|')
print('|  1  |  2  |  3  |')
print('|-----|-----|-----|')
print('|  4  |  5  |  6  |')
print('|-----|-----|-----|')
print('|  7  |  8  |  9  |')
print('|-----|-----|-----|')
tab_2 = []
tab_1 = []
com_1 = []
y = True
while y:
    choice = str(input("chose x or o  ").upper())
    y = not (choice in r)
choice_3 = (r - set(choice)).pop()
z = True

while z:
    n = True
    while n:
        choice_2 = str(input('chose a number'))
        n = not (choice_2 in list(noum))
    fuck = noum.replace(choice_2, '')
    tab_1.append(choice_2)
    tab_1 = sorted(tab_1)
    for i in range(3):
        omar = list(change[i])
        for j in range(18):
            if omar[j] == choice_2:
                omar[j] = choice
        change[i] = ''.join(omar)
    if len(tab_1) != 5:
        import random

        if (len(tab_1) == 2):
            for j in range(8):
                if choice_2 in com[j]:
                    h = True
                    while h:
                        pc = int(random.choice(com[j]))
                        if ((pc != int(choice_2)) and (str(pc) in list(noum))):
                            h = False
                    fuck_1 = fuck.replace(str(pc), '')
                    noum = fuck_1
            tab_2.append(str(pc))
            tab_2 = sorted(tab_2)
        else:
            b = True
            while b:
                pc = random.choice(list(fuck))
                fuck_1 = fuck.replace(pc, '')
                noum = fuck_1
                if pc != int(choice_2):
                    b = False
                tab_2.append(pc)
                tab_2 = sorted(tab_2)
        for i in range(3):
            salhi = list(change[i])
            for j in range(18):
                if salhi[j] == str(pc):
                    salhi[j] = choice_3
            change[i] = ''.join(salhi)
    if tab_1 in com:
        print('you are the winner')
        z = False

    elif tab_2 in com:
        print('the pc is the wener')
        z = False
    elif len(tab_1) == 4:
        for i in range(1, 10):
            for j in range(8):
                com[j].append(str(i))
                com_1 = sorted(com[j])
                com[j].pop()
                if tab_1 == com_1:
                    print("yoU are the winner ")
                    z = False
                    break
                com_1.clear()
    elif len(tab_1) == 5:
        for i in range(1, 10):
            for j in range(8):
                for k in range(1, 10):
                    com[j].append(str(i))
                    com[j].append(str(k))
                    com_1 = sorted(com[j])
                    com[j].pop()
                    com[j].pop()
                    if tab_1 == com_1:
                        print("yoy are the winner ")
                        z = False

                    com_1.clear()
    elif (len(tab_1) == 5) and (z):
        print('draw')
        z = False
        break
    elif len(tab_2) > 3:
        for i in range(1, 10):
            for j in range(8):
                com[j].append(str(i))
                com_1 = sorted(com[j])
                com[j].pop()
                if tab_2 == com_1:
                    print("the pc is the winner ")
                    z = False
                    break
                com_1.clear()
    for i in range(3):
        print(form[i])
        print(change[i])
    print('|-----|-----|-----|')
