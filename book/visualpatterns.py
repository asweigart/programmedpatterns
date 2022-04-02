def pattern1(step):
    pattern = ''
    for i in range(step):
        pattern += 'O'
    return pattern


def pattern1b(step):
    return 'O' * step


def formula1(step):
    return step


def formula1b(step):
    return 1 * step + 0


def pattern2(step):
    return 'O' + ('O' * step)


def pattern2b(step):
    return ('O' * step) + 'O'


def formula2(step):
    return 1 + step


def formula2b(step):
    return step + 1


def pattern3(step):
    return 'OO' * step


def formula3(step):
    return 2 * step


def pattern4(step):
    return 'O' + ('OO' * step)


def formula4(step):
    return 2 * step + 1


def pattern5(step):
    pattern = 'OOO' * step
    pattern = pattern[1:]
    return pattern


def formula5(step):
    return 3 * step - 1


def forumla5b(step):
    return 3 * (step - 1) + 2


def pattern6(step):
    return 'OOO'


def formula6(step):
    return 3


def pattern7(step):
    return 'OOO' * step


def formula7(step):
    return 3 * step


def pattern8(step):
    return 'OOO' + ('OOO' * step)


def formula8(step):
    return 3 * step + 3


def pattern9(step):
    return ('O' * 10) + ('OO' * step)


def formula9(step):
    return 2 * step + 10


def pattern10(step):
    pattern = 'OOOO' * step
    pattern = pattern[3:]
    return pattern


def formula10(step):
    return 4 * step - 3


def pattern11(step):
    return 'OOOO'


def formula11(step):
    return 4


def pattern12(step):
    return 'O' + ('OOO' * step)


def formula12(step):
    return 3 * step + 1


def pattern13(step):
    return ('OOOOOOOO' * step) + 'OO'


def formula13(step):
    return 8 * step + 2


def pattern14(step):
    return ('OOOOOOOO' * step)[2:]


def formula14(step):
    return 8 * step - 2


def pattern15(step):
    return 'OO' * step + 'OO'


def formula15(step):
    return 2 * step + 2

def pattern16(step):
    return 'O' * step + 'OO'

def formula16(step):
    return step + 2


def pattern17(step):
    return ('OOOOOOOO' * step)[7:]

def formula17(step):
    return 8 * step - 7

def pattern18(step):
    return 'OOO' * step + 'OO'

def formula18(step):
    return 3 * step + 2

def pattern19(step):
    return 'OOOO' * step

def formula19(step):
    return 4 * step

def pattern20(step):
    return 'OOOO' * step + 'OO'

def formula20(step):
    return 4 * step + 2

def pattern21(step):
    return 'OOO' * step + 'OOO'

def formula21(step):
    return 3 * step + 3

def pattern22(step):
    return ('OOOO' * step)[3:]

def formula22(step):
    return 4 * step - 3



def pattern23(step):
    pattern = 'O'
    i = 2
    while True:
        if i > step:
            break
        pattern += 'O'
        i += 1

        if i > step:
            break
        pattern += 'OO'
        i += 1
    return pattern

def pattern23b(step):
    increments = [1, 2]
    incIndex = 0

    pattern = 'O'
    i = 1
    while i < step:
        pattern += 'O' * increments[incIndex]
        i += 1
        incIndex += 1
        if incIndex >= 2:
            incIndex = 0  # Reset incIndex back to 0.
    return pattern

def formula23(step):
    count = 1
    i = 2
    while True:
        if i > step:
            break
        count += 1
        i += 1

        if i > step:
            break
        count += 2
        i += 1
    return count

def formula23b(step):
    increments = [1, 2]
    incIndex = 0

    count = 1
    i = 1
    while i < step:
        count += increments[incIndex]
        i += 1
        incIndex += 1
        if incIndex >= 2:
            incIndex = 0  # Reset incIndex back to 0.
    return count


def pattern24(step):
    pattern = 'O'
    i = 2
    while True:
        if i > step:
            break
        pattern += 'O'
        i += 1

        if i > step:
            break
        pattern += 'OO'
        i += 1

        if i > step:
            break
        pattern += 'OO'
        i += 1
    return pattern

def pattern24b(step):
    increments = [1, 2, 2]
    incIndex = 0

    pattern = 'O'
    i = 1
    while i < step:
        pattern += 'O' * increments[incIndex]
        i += 1
        incIndex += 1
        if incIndex >= 2:
            incIndex = 0  # Reset incIndex back to 0.
    return pattern

def formula24(step):
    count = 1
    i = 2
    while True:
        if i > step:
            break
        count += 1
        i += 1

        if i > step:
            break
        count += 2
        i += 1


        if i > step:
            break
        count += 2
        i += 1
    return count

def formula24b(step):
    increments = [1, 2, 2]
    incIndex = 0

    count = 1
    i = 1
    while i < step:
        count += increments[incIndex]
        i += 1
        incIndex += 1
        if incIndex >= 2:
            incIndex = 0  # Reset incIndex back to 0.
    return count

def pattern25(step):
    pattern = 'O'
    i = 2
    while True:
        if i > step:
            break
        pattern += 'O'
        i += 1

        if i > step:
            break
        pattern += ''
        i += 1

    return pattern


def pattern25b(step):
    pattern = 'O'
    i = 2
    while True:
        if i > step:
            break
        pattern += 'O'
        i += 2

    return pattern


def formula25(step):
    count = 1
    i = 2
    while True:
        if i > step:
            break
        count += 1
        i += 1

        if i > step:
            break
        count += 0
        i += 1

    return count


def formula25b(step):
    count = 1
    i = 2
    while True:
        if i > step:
            break
        count += 1
        i += 2

    return count



def pattern26(step):
    pattern = 'O'
    i = 2
    while True:
        if i > step:
            break
        pattern += 'O'
        i += 1

        if i > step:
            break
        pattern += ''
        i += 1

        if i > step:
            break
        pattern += ''
        i += 1
    return pattern



def pattern26b(step):
    pattern = 'O'
    i = 2
    while True:
        if i > step:
            break
        pattern += 'O'
        i += 3

    return pattern


def formula26(step):
    count = 1
    i = 2
    while True:
        if i > step:
            break
        count += 1
        i += 1

        if i > step:
            break
        count += 0
        i += 1

        if i > step:
            break
        count += 0
        i += 1

    return count


def formula26b(step):
    count = 1
    i = 2
    while True:
        if i > step:
            break
        count += 1
        i += 3

    return count




def pattern27(step):
    pattern = 'OOOO'
    i = 2
    while True:
        if i > step:
            break
        pattern += 'O'
        i += 1

        if i > step:
            break
        pattern += 'OO'
        i += 1

        if i > step:
            break
        pattern += 'OOO'
        i += 1
    return pattern


def pattern27b(step):
    increments = [1, 2, 3]
    incIndex = 0

    pattern = 'OOOO'
    i = 1
    while i < step:
        pattern += 'O' * increments[incIndex]
        i += 1
        incIndex += 1
        if incIndex >= 3:
            incIndex = 0  # Reset incIndex back to 0.
    return pattern


def formula27(step):
    count = 4
    i = 2
    while True:
        if i > step:
            break
        count += 1
        i += 1

        if i > step:
            break
        count += 2
        i += 1

        if i > step:
            break
        count += 3
        i += 1
    return count

def formula27b(step):
    increments = [1, 2, 3]
    incIndex = 0

    count = 4
    i = 1
    while i < step:
        count += increments[incIndex]
        i += 1
        incIndex += 1
        if incIndex >= 3:
            incIndex = 0  # Reset incIndex back to 0.
    return count




def pattern28(step):
    pattern = 'OOOOO'
    i = 2
    while True:
        if i > step:
            break
        pattern += ''
        i += 1

        if i > step:
            break
        pattern += ''
        i += 1

        if i > step:
            break
        pattern += ''
        i += 1

        if i > step:
            break
        pattern += ''
        i += 1

        if i > step:
            break
        pattern += 'OOOOO'
        i += 1
    return pattern


def pattern28b(step):
    pattern = 'OOOOO'
    i = 2
    while True:
        i += 4

        if i > step:
            break
        pattern += 'OOOOO'
        i += 1
    return pattern


def formula28(step):
    count = 5
    i = 2
    while True:
        if i > step:
            break
        count += 0
        i += 1

        if i > step:
            break
        count += 0
        i += 1

        if i > step:
            break
        count += 0
        i += 1

        if i > step:
            break
        count += 0
        i += 1

        if i > step:
            break
        count += 5
        i += 1
    return count

def formula28b(step):
    count = 5
    i = 2
    while True:
        i += 4

        if i > step:
            break
        count += 5
        i += 1
    return count



def pattern29(step):
    pattern = 'O'
    i = 2
    while True:
        if i > step:
            break
        pattern += 'O'
        i += 1

        if i > step:
            break
        pattern += ''
        i += 1

        if i > step:
            break
        pattern += 'OO'
        i += 1

        if i > step:
            break
        pattern += ''
        i += 1

    return pattern


def formula29(step):
    count = 1
    i = 2
    while True:
        if i > step:
            break
        count += 1
        i += 1

        if i > step:
            break
        count += 0
        i += 1

        if i > step:
            break
        count += 2
        i += 1

        if i > step:
            break
        count += 0
        i += 1
    return count




def pattern30(step):
    pattern = 'O'
    i = 2
    while True:
        if i > step:
            break
        pattern += 'OO'
        i += 1

        if i > step:
            break
        pattern += 'O'
        i += 1
    return pattern


def formula30(step):
    count = 1
    i = 2
    while True:
        if i > step:
            break
        count += 2
        i += 1

        if i > step:
            break
        count += 1
        i += 1
    return count


def pattern31(step):
    pattern = 'OOOO'
    i = 2
    while True:
        if i > step:
            break
        pattern += 'O'
        i += 1

        if i > step:
            break
        pattern += ''
        i += 1

        if i > step:
            break
        pattern += 'O'
        i += 1
    return pattern


def formula31(step):
    count = 4
    i = 2
    while True:
        if i > step:
            break
        count += 1
        i += 1

        if i > step:
            break
        count += 0
        i += 1

        if i > step:
            break
        count += 1
        i += 1
    return count




def pattern32(step):
    pattern = 'O'
    i = 2
    while True:
        if i > step:
            break
        pattern += 'OOO'
        i += 1

        if i > step:
            break
        pattern += ''
        i += 1
    return pattern


def formula32(step):
    count = 1
    i = 2
    while True:
        if i > step:
            break
        count += 3
        i += 1

        if i > step:
            break
        count += 0
        i += 1
    return count



def pattern33(step):
    pattern = 'OOO'
    i = 2
    while True:
        if i > step:
            break
        pattern += ''
        i += 1

        if i > step:
            break
        pattern += 'OOO'
        i += 1
    return pattern


def formula33(step):
    count = 3
    i = 2
    while True:
        if i > step:
            break
        count += 0
        i += 1

        if i > step:
            break
        count += 3
        i += 1
    return count



def pattern34(step):
    pattern = 'O'
    i = 2
    while True:
        if i > step:
            break
        pattern += 'OO'
        i += 1

        if i > step:
            break
        pattern += 'OOO'
        i += 1
    return pattern


def formula34(step):
    count = 1
    i = 2
    while True:
        if i > step:
            break
        count += 2
        i += 1

        if i > step:
            break
        count += 3
        i += 1
    return count



def pattern35(step):
    pattern = 'O'
    i = 2
    while True:
        if i > step:
            break
        pattern += ''
        i += 1

        if i > step:
            break
        pattern += ''
        i += 1

        if i > step:
            break
        pattern += 'OO'
        i += 1
    return pattern


def formula35(step):
    count = 1
    i = 2
    while True:
        if i > step:
            break
        count += 0
        i += 1

        if i > step:
            break
        count += 0
        i += 1

        if i > step:
            break
        count += 2
        i += 1
    return count



def pattern36(step):
    pattern = 'O'
    i = 2
    while True:
        if i > step:
            break
        pattern += ''
        i += 1

        if i > step:
            break
        pattern += 'OO'
        i += 1

        if i > step:
            break
        pattern += ''
        i += 1
    return pattern


def formula36(step):
    count = 1
    i = 2
    while True:
        if i > step:
            break
        count += 0
        i += 1

        if i > step:
            break
        count += 2
        i += 1

        if i > step:
            break
        count += 0
        i += 1
    return count




def pattern37(step):
    pattern = 'O'
    i = 2
    while True:
        if i > step:
            break
        pattern += 'OO'
        i += 1

        if i > step:
            break
        pattern += ''
        i += 1

        if i > step:
            break
        pattern += ''
        i += 1
    return pattern


def formula37(step):
    count = 1
    i = 2
    while True:
        if i > step:
            break
        count += 2
        i += 1

        if i > step:
            break
        count += 0
        i += 1

        if i > step:
            break
        count += 0
        i += 1
    return count




def pattern38(step):
    pattern = 'OO'
    i = 2
    while True:
        if i > step:
            break
        pattern += 'OOO'
        i += 1

        if i > step:
            break
        pattern += 'OO'
        i += 1

        if i > step:
            break
        pattern += 'O'
        i += 1
    return pattern


def formula38(step):
    count = 2
    i = 2
    while True:
        if i > step:
            break
        count += 3
        i += 1

        if i > step:
            break
        count += 2
        i += 1

        if i > step:
            break
        count += 1
        i += 1
    return count


def pattern39(step):
    row = ('O' * step) + '\n'
    pattern = row * step
    return pattern

def formula39(step):
    width = step
    height = step
    return width * height



def pattern40(step):
    row = ('OO' * step) + '\n'
    pattern = row * step
    return pattern

def formula40(step):
    width = step * 2
    height = step
    return width * height




def pattern41(step):
    row = ('O' * step) + '\n'
    pattern = row * (step * 2)
    return pattern

def formula41(step):
    width = step
    height = step * 2
    return width * height





def pattern42(step):
    row = ('OO' * step) + '\n'
    pattern = row * (step * 2)
    return pattern

def formula42(step):
    width = step * 2
    height = step * 2
    return width * height





def pattern43(step):
    row = ('OOO' * step) + '\n'
    pattern = row * (step * 2)
    return pattern

def formula43(step):
    width = step * 3
    height = step * 2
    return width * height





def pattern44(step):
    row = ('OO' * step) + 'OO\n'
    pattern = row * (step * 2)
    return pattern

def formula44(step):
    width = (step * 2) + 2
    height = step * 2
    return width * height





def pattern45(step):
    row = ('OO' * step) + 'OOO\n'
    pattern = (row * step) + row + row
    return pattern

def formula45(step):
    width = (step * 2) + 3
    height = step + 2
    return width * height




def pattern46(step):
    row = ('OO' * step) + '\n'
    pattern = row * (step * 3)
    return pattern

def formula46(step):
    width = step * 2
    height = step * 3
    return width * height




def pattern47(step):
    row = ('OO' * step) + 'O\n'
    pattern = row * (step * 3)
    return pattern

def formula47(step):
    width = (step * 2) + 1
    height = step * 3
    return width * height




def pattern48(step):
    row = ('O' * step) + 'OOOOO\n'
    pattern = row * (step * 2)
    return pattern

def formula48(step):
    width = step + 5
    height = step * 2
    return width * height




def pattern49(step):
    row = ('OOO' * step) + 'O\n'
    pattern = row * (step * 3) + row
    return pattern

def formula49(step):
    width = (step * 3) + 1
    height = (step * 3) + 1
    return width * height






def pattern50(step):
    row = ('O' * step) + '\n'
    pattern = row * (step * 4) + row
    return pattern

def formula50(step):
    width = step
    height = (step * 4) + 1
    return width * height




def pattern51(step):
    row = ('OOOO' * step) + 'OO\n'
    pattern = row * (step * 4) + row + row
    return pattern

def formula51(step):
    width = (step * 4) + 2
    height = (step * 4) + 2
    return width * height




def pattern52(step):
    row = ('OOOO' * step) + 'OO\n'
    pattern = row * (step * 2) + row + row + row
    return pattern

def formula52(step):
    width = (step * 4) + 2
    height = (step * 2) + 3
    return width * height




def pattern53(step):
    row = ('OOOO' * step) + '\n'
    pattern = (row * step) + row + row
    return pattern

def formula53(step):
    width = step * 4
    height = step + 2
    return width * height




def pattern54(step):
    row = ('O' * step) + 'OO\n'
    pattern = row * (step * 2)
    return pattern

def formula54(step):
    width = step + 2
    height = step * 2
    return width * height




def pattern55(step):
    row = ('OOOO' * step) + 'OOO\n'
    pattern = row * (step * 2)
    return pattern

def formula55(step):
    width = (step * 4) + 3
    height = step * 2
    return width * height


def pattern56(step):
    size = 1
    for i in range(2, step + 1):
        if i % 2 == 0:
            size += 1
    row = ('O' * size) + '\n'
    pattern = row * size
    return pattern

def formula56(step):
    size = 1
    for i in range(2, step + 1):
        if i % 2 == 0:
            size += 1
    return size * size

def pattern57(step):
    size = 1
    for i in range(2, step + 1):
        if i % 2 == 1:
            size += 1
    row = ('O' * size) + '\n'
    pattern = row * size
    return pattern

def pattern57b(step):
    if step == 1:
        return 'O'
    else:
        return pattern56(step - 1)


def formula57(step):
    size = 1
    for i in range(2, step + 1):
        if i % 2 == 1:
            size += 1
    return size * size


def formula57b(step):
    if step == 1:
        return 1
    else:
        return formula56(step - 1)


def pattern58(step):
    width = 1
    height = 1
    for i in range(2, step + 1):
        if i % 2 == 0:
            height += 1
        else:
            width += 1
    row = ('O' * width) + '\n'
    pattern = row * height
    return pattern

def formula58(step):
    width = 1
    height = 1
    for i in range(2, step + 1):
        if i % 2 == 0:
            height += 1
        else:
            width += 1
    return width * height


def pattern59(step):
    width = 4
    height = 2
    for i in range(2, step + 1):
        if i % 2 == 0:
            width += 2
            height += 1
        else:
            width += 2
            height += 2
    row = ('O' * width) + '\n'
    pattern = row * height
    return pattern


def formula59(step):
    width = 4
    height = 2
    for i in range(2, step + 1):
        if i % 2 == 0:
            width += 2
            height += 1
        else:
            width += 2
            height += 2
    return width * height



def pattern60(step):
    size = 1
    for i in range(2, step + 1):
        if i % 4 == 2:
            size += 3
    row = ('O' * size) + '\n'
    pattern = row * size
    return pattern


def formula60(step):
    size = 1
    for i in range(2, step + 1):
        if i % 4 == 2:
            size += 3
    return size * size




def pattern61(step):
    size = 1
    for i in range(2, step + 1):
        if i % 2 == 0:
            size += 2
        else:
            size -= 1
    row = ('O' * size) + '\n'
    pattern = row * size
    return pattern


def formula61(step):
    size = 1
    for i in range(2, step + 1):
        if i % 2 == 0:
            size += 2
        else:
            size -= 1
    return size * size




def pattern62(step):
    width = 1
    height = 1
    for i in range(2, step + 1):
        if i % 2 == 0:
            width += 2
            height += 2
        else:
            height -= 1
    row = ('O' * width) + '\n'
    pattern = row * height
    return pattern


def formula62(step):
    width = 1
    height = 1
    for i in range(2, step + 1):
        if i % 2 == 0:
            width += 2
            height += 2
        else:
            height -= 1
    return width * height




def pattern63(step):
    width = 1
    height = 1
    for i in range(2, step + 1):
        if i % 4 == 2:
            width += 2
            height += 1
        elif i % 4 == 0:
            width -= 1
            height -= 1
    row = ('O' * width) + '\n'
    pattern = row * height
    return pattern


def formula63(step):
    width = 1
    height = 1
    for i in range(2, step + 1):
        if i % 4 == 2:
            width += 2
            height += 1
        elif i % 4 == 0:
            width -= 1
            height -= 1
    return width * height




def pattern64(step):
    width = 5
    height = 1
    for i in range(2, step + 1):
        if i % 2 == 0:
            width -= 1
            height += 1
        elif i % 2 == 1:
            width += 3
            height += 4
    row = ('O' * width) + '\n'
    pattern = row * height
    return pattern


def formula64(step):
    width = 5
    height = 1
    for i in range(2, step + 1):
        if i % 2 == 0:
            width -= 1
            height += 1
        elif i % 2 == 1:
            width += 3
            height += 4
    return width * height





def pattern65(step):
    width = 1
    height = 1
    for i in range(2, step + 1):
        if i % 3 == 0:
            width += 3
            height += 2
        elif i % 3 == 1:
            width -= 1
            height -= 1
    row = ('O' * width) + '\n'
    pattern = row * height
    return pattern


def formula65(step):
    width = 1
    height = 1
    for i in range(2, step + 1):
        if i % 3 == 0:
            width += 3
            height += 2
        elif i % 3 == 1:
            width -= 1
            height -= 1
    return width * height




def pattern66(step):
    width = 1
    height = 3
    for i in range(2, step + 1):
        if i % 3 == 2:
            width += 4
        elif i % 3 == 0:
            width += 2
            height -= 2
        elif i % 3 == 1:
            width += 1
            height += 2
    row = ('O' * width) + '\n'
    pattern = row * height
    return pattern


def formula66(step):
    width = 1
    height = 3
    for i in range(2, step + 1):
        if i % 3 == 2:
            width += 4
        elif i % 3 == 0:
            width += 2
            height -= 2
        elif i % 3 == 1:
            width += 1
            height += 2
    return width * height






def pattern67(step):
    width = 4
    height = 3
    for i in range(2, step + 1):
        if i % 2 == 0:
            width += 3
        elif i % 2 == 1:
            width += 2
            height += 1
    row = ('O' * width) + '\n'
    pattern = row * height
    return pattern


def formula67(step):
    width = 4
    height = 3
    for i in range(2, step + 1):
        if i % 2 == 0:
            width += 3
        elif i % 2 == 1:
            width += 2
            height += 1
    return width * height






def pattern68(step):
    width = 2
    height = 3
    for i in range(2, step + 1):
        if i % 4 == 2:
            width += 4
            height -= 1
        elif i % 4 == 3:
            width += 2
            height += 2
        elif i % 4 == 0:
            width += 4
            height -= 2
        elif i % 4 == 1:
            height += 2
    row = ('O' * width) + '\n'
    pattern = row * height
    return pattern


def formula68(step):
    width = 2
    height = 3
    for i in range(2, step + 1):
        if i % 4 == 2:
            width += 4
            height -= 1
        elif i % 4 == 3:
            width += 2
            height += 2
        elif i % 4 == 0:
            width += 4
            height -= 2
        elif i % 4 == 1:
            height += 2
    return width * height







def pattern69(step):
    width = 4
    height = 3
    for i in range(2, step + 1):
        if i % 2 == 0:
            width += 2
            height += 1
        elif i % 2 == 1:
            height += 1
    row = ('O' * width) + '\n'
    pattern = row * height
    return pattern


def formula69(step):
    width = 4
    height = 3
    for i in range(2, step + 1):
        if i % 2 == 0:
            width += 2
            height += 1
        elif i % 2 == 1:
            height += 1
    return width * height






def pattern70(step):
    width = 3
    height = 3
    for i in range(2, step + 1):
        if i % 2 == 0:
            height += 2
        elif i % 2 == 1:
            width += 2
            height += 1
    row = ('O' * width) + '\n'
    pattern = row * height
    return pattern


def formula70(step):
    width = 3
    height = 3
    for i in range(2, step + 1):
        if i % 2 == 0:
            height += 2
        elif i % 2 == 1:
            width += 2
            height += 1
    return width * height






def pattern71(step):
    width = 2
    height = 1
    for i in range(2, step + 1):
        if i % 3 == 2:
            width += 1
        elif i % 3 == 0:
            width += 3
            height += 3
        elif i % 3 == 1:
            width += 4
    row = ('O' * width) + '\n'
    pattern = row * height
    return pattern


def formula71(step):
    width = 2
    height = 1
    for i in range(2, step + 1):
        if i % 3 == 2:
            width += 1
        elif i % 3 == 0:
            width += 3
            height += 3
        elif i % 3 == 1:
            width += 4
    return width * height






def pattern72(step):
    width = 3
    height = 2
    for i in range(2, step + 1):
        if i % 3 == 2:
            width -= 1
        elif i % 3 == 0:
            width -= 1
            height += 1
        elif i % 3 == 1:
            width += 2
            height -= 1
    row = ('O' * width) + '\n'
    pattern = row * height
    return pattern


def formula72(step):
    width = 3
    height = 2
    for i in range(2, step + 1):
        if i % 3 == 2:
            width -= 1
        elif i % 3 == 0:
            width -= 1
            height += 1
        elif i % 3 == 1:
            width += 2
            height -= 1
    return width * height




def pattern73(step):
    pattern = ''
    for i in range(1, step + 1):
        pattern += ('O' * i) + '\n'
    return pattern

def pattern73b(step):
    pattern = ''
    i = 1
    while True:
        pattern += ('O' * i) + '\n'
        if i == step:
            break
        i += 1
    return pattern

def formula73(step):
    count = 0
    for i in range(1, step + 1):
        count += i
    return count

def formula73b(step):
    return (step * (step + 1)) // 2


def pattern74(step):
    pattern = ''
    for i in range(step, 0, -1):
        pattern += ('O' * i) + '\n'
    return pattern

def formula74(step):
    count = 0
    for i in range(step, 0, -1):
        count += i
    return count

def pattern75(step):
    pattern = 'O\nOO\n'
    for i in range(2, step + 2):
        pattern += 'O' + ('O' * i) + '\n'
    return pattern

def formula75(step):
    count = 3
    for i in range(2, step + 2):
        count += i + 2
    return count

def pattern76(step):
    pattern = 'O\n'
    width = 3
    for i in range(2, step + 1):
        pattern += ('O' * width) + '\n'
        width += 2
    return pattern

def formula76(step):
    count = 1

    width = 3
    for i in range(2, step + 1):
        count += width
        width += 2
    return count

def formula76b(step):
    return (step * (2 * step)) // 2


def pattern77(step):
    pattern = ''
    for i in range(1, step + 1):
        pattern += ('O' * i) + '\n'
    for i in range(step, 0, -1):
        pattern += ('O' * i) + '\n'
    return pattern

def formula77(step):
    return (step * (step + 1))


def pattern78(step):
    pattern = ''
    for i in range(0, step):
        pattern += ('O' * step) + ('O' * i) + '\n'
    return pattern

def formula78(step):
    count = 0
    for i in range(0, step):
        count += step + i
    return count


def pattern79(step):
    pattern = 'O\n'
    rowWidth = 3
    for i in range(2, step + 1):
        pattern += ('O' * rowWidth) + '\n'
        rowWidth += 2
        pattern += ('O' * rowWidth) + '\n'
        rowWidth += 2
    return pattern

def formula79(step):
    count = 1
    rowWidth = 3
    for i in range(2, step + 1):
        count += rowWidth
        rowWidth += 2
        count += rowWidth
        rowWidth += 2
    return count


def pattern80(step):
    pattern = ''
    for i in range(1, step + 1):
        pattern += ('O' * i) + '\n'
    for i in range(step - 1, 0, -1):
        pattern += ('O' * i) + '\n'
    return pattern

def formula80(step):
    return (step * (step + 1)) - step


def pattern81(step):
    pattern = ''
    for i in range(1, step + 1):
        pattern += ('O' * i) + '\n'
    for i in range(1, step + 1):
        pattern += ('O' * i) + '\n'
    return pattern

def formula81(step):
    return (step * (step + 1))

def pattern82(step):
    pattern = ''
    for i in range(1, step + 1):
        pattern += ('O' * i**2) + '\n'
    return pattern


def formula82(step):
    count = 0
    for i in range(1, step + 1):
        count += i**2
    return count


def pattern83(step):
    pattern = 'O\n'
    rowWidth = 1
    for i in range(2, step + 1):
        pattern += ('O' * rowWidth) + '\n'
        if rowWidth % 2 == 1:
            rowWidth += 1
    return pattern

def formula83(step):
    count = 1
    rowWidth = 1
    for i in range(2, step + 1):
        count += rowWidth
        if rowWidth % 2 == 1:
            rowWidth += 1
    return count

def pattern84(step):
    pattern = ''
    for i in range(1, step + 1):
        pattern += ('O' * i) + '\n'
        pattern += ('O' * i) + '\n'
    return pattern

def formula84(step):
    count = 0
    for i in range(1, step + 1):
        count += i * 2
    return count


def pattern85(step):
    pattern = ''
    for i in range(1, step + 1):
        pattern += 'O' * (i * 2) + '\n'
    return pattern

def formula85(step):
    count = 0
    for i in range(1, step + 1):
        count += i * 2
    return count


def pattern86(step):
    pattern = ''
    for i in range(1, step + 1):
        pattern += 'O' * (i * 3) + '\n'
    return pattern

def formula86(step):
    count = 0
    for i in range(1, step + 1):
        count += i * 3
    return count



def pattern87(step):
    pattern = ''
    for i in range(1, step + 1):
        pattern += 'O' * (i * 2) + '\n'
        pattern += 'O' * (i * 2) + '\n'
    return pattern

def formula87(step):
    count = 0
    for i in range(1, step + 1):
        count += i * 4
    return count





# Tessellation patterns
def pattern88(size):
    tess = [
    r'___|',
    r'_|__',
    ]

    pattern = ''
    for y in range(size):
        for line in tess:
            pattern += (line * size) + '\n'
    return pattern


def pattern89(size):
    tess = [
    r'/  \__',
    r'\__/  ',
    ]

    pattern = ''
    for y in range(size):
        for line in tess:
            pattern += (line * size) + '\n'
    return pattern


def pattern90(size):
    tess = [
    r' /    \     ',
    r'/      \____',
    r'\      /    ',
    r' \____/     ',
    ]

    pattern = ''
    for y in range(size):
        for line in tess:
            pattern += (line * size) + '\n'
    return pattern


def pattern91(size):
    tess = [
    r'_ \ \ \_/ __',
    r' \ \ \___/ _',
    r'\ \ \_____/ ',
    r'/ / / ___ \_',
    r'_/ / / _ \__',
    r'__/ / / \___',
    ]

    pattern = ''
    for y in range(size):
        for line in tess:
            pattern += (line * size) + '\n'
    return pattern


def pattern92(size):
    tess = [
    r'((  )',
    r' ))( ',
    ]

    pattern = ''
    for y in range(size):
        for line in tess:
            pattern += (line * size) + '\n'
    return pattern



def pattern93(size):
    tess = [
    r'/ / __ \ \__',
    r'_/ /  \ \___',
    r' \ \__/ / __',
    r'\ \____/ /  ',
    ]

    pattern = ''
    for y in range(size):
        for line in tess:
            pattern += (line * size) + '\n'
    return pattern


def pattern94(size):
    tess = [
    r'/ / / ____ \ \ \__',
    r'_/ / / __ \ \ \___',
    r'__/ / /  \ \ \____',
    r'_ \ \ \__/ / / ___',
    r' \ \ \____/ / / __',
    r'\ \ \______/ / /  ',
    ]

    pattern = ''
    for y in range(size):
        for line in tess:
            pattern += (line * size) + '\n'
    return pattern


def pattern95(size):
    tess = [
    r'   \__   \__',
    r'\__/  \__/  ',
    r'   \     \  ',
    r' __/   __/  ',
    r'/  \__/  \__',
    r'   /     /  ',
    ]

    pattern = ''
    for y in range(size):
        for line in tess:
            pattern += (line * size) + '\n'
    return pattern


def pattern96(size):
    tess = [
    r'__ \ ^ / _',
    r'  \ VVV / ',
    r' ()|   |()',
    r'^ / ___ \ ',
    r'VV /   \ V',
    r'  |() ()| ',
    ]

    pattern = ''
    for y in range(size):
        for line in tess:
            pattern += (line * size) + '\n'
    return pattern


def pattern97(size):
    tess = [
    r'__  |  _',
    r'| \_|_/ ',
    r'|  ___  ',
    r'|_/ | \_',
    ]

    pattern = ''
    for y in range(size):
        for line in tess:
            pattern += (line * size) + '\n'
    return pattern




def pattern98(size):
    tess = [
    r' /\  \/  ',
    r'<  >     ',
    r' \/  /\  ',
    r'    <  > ',
    ]

    pattern = ''
    for y in range(size):
        for line in tess:
            pattern += (line * size) + '\n'
    return pattern





def pattern99(size):
    tess = [
    r'  /  /\   ',
    r' /  /  \  ',
    r'/  / \  \ ',
    r'\  \ /  / ',
    r' \  /  /  ',
    r'  \/  /   ',
    ]

    pattern = ''
    for y in range(size):
        for line in tess:
            pattern += (line * size) + '\n'
    return pattern





def pattern100(size):
    tess = [
    r' //  /\\  \ / ',
    r'//  /  \\  /  ',
    r'/  / \  \\/  /',
     '\\  \\ /  //  /\\',
    r'\\  /  //  /  ',
    r' \\/  //  / \ ',
    ]

    pattern = ''
    for y in range(size):
        for line in tess:
            pattern += (line * size) + '\n'
    return pattern




def pattern101(size):
    tess = [
    r' /  /\  \ / ',
    r'/  /  \  /  ',
    r'  / \  \/  /',
     '  \\ /  /  /\\',
    r'\  /  /  /  ',
    r' \/  /  / \ ',
    ]

    pattern = ''
    for y in range(size):
        for line in tess:
            pattern += (line * size) + '\n'
    return pattern




def pattern102(size):
    tess = [
    r' / |__  ',
    r'/     |_',
    r'\   __| ',
    r' \_|    ',
    ]

    pattern = ''
    for y in range(size):
        for line in tess:
            pattern += (line * size) + '\n'
    return pattern




def pattern103(size):
    tess = [
    r'__  | |___  | |_',
    r'  | |___  | |___',
    r'| |___  | |___  ',
    r'|___  | |___  | ',
    ]

    pattern = ''
    for y in range(size):
        for line in tess:
            pattern += (line * size) + '\n'
    return pattern




def pattern104(size):
    tess = [
    r'|   ',
    r'|___',
    ]

    pattern = ''
    for y in range(size):
        for line in tess:
            pattern += (line * size) + '\n'
    return pattern




def pattern105(size):
    tess = [
    r'/\  /____\__',
    r'  \/  \    /',
    r'___\__/\  /_',
    r'\    /  \/  ',
    ]

    pattern = ''
    for y in range(size):
        for line in tess:
            pattern += (line * size) + '\n'
    return pattern




def pattern106(size):
    tess = [
    '|_| |_   _',
    '|_   _|_| ',
    ' _|_| |_  ',
    '| |_   _|_',
    '   _|_| |_',
    ]

    pattern = ''
    for y in range(size):
        for line in tess:
            pattern += (line * size) + '\n'
    return pattern




def pattern107(size):
    tess = [
    r'\/\/',
    r'/ / ',
    r'\/\/',
     ' \\ \\',
    ]

    pattern = ''
    for y in range(size):
        for line in tess:
            pattern += (line * size) + '\n'
    return pattern




def pattern108(size):
    tess = [
    r'__   \______   \____',
    r'  \   \  /  \   \  /',
    r'  /\   \/   /\   \/ ',
    r' /__\__/   /__\__/  ',
    r'/         /         ',
    r'\______   \______   ',
    r' \  /  \   \  /  \  ',
    r'  \/   /\   \/   /\ ',
     '__/   /__\\__/   /__\\',
    r'     /         /    ',
    ]

    pattern = ''
    for y in range(size):
        for line in tess:
            pattern += (line * size) + '\n'
    return pattern


