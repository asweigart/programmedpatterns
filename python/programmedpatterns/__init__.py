# These are example solutions for each of the puzzles.

import sys

NUM_DESC = {
    15: 'Number of Os, Xs:',
    44: 'Number of filled hexagons:',
    53: 'Number of segments:',
    58: 'Number of segments:',
    59: 'Number of black tiles, white tiles:',
    66: 'Number of Os, Xs:',
}


def getPatternMultilineString(patternNum, startIteration=1, endIteration=3, sep='  '):
    # Return a multiline string with the first three iterations of the pattern.
    pats = []
    for i in range(startIteration, endIteration + 1):
        pats.append(eval('vis%d(%d)' % (patternNum, i)).splitlines())

    maxNumLines = max([len(x) for x in pats])

    patMaxLens = []
    for i in range(startIteration, endIteration + 1):
        patMaxLens.append(max([len(line) for line in pats[i - startIteration]]))

    lines = []
    for i in range(maxNumLines):
        line = ''
        for j, pat in enumerate(pats):
            if i < len(pat):
                line += pat[i].ljust(patMaxLens[j], ' ')
            else:
                line += ' ' * patMaxLens[j]

            line += sep

        lines.append(line.rstrip())

    # Add the number line:
    lines.append(NUM_DESC.get(patternNum, 'Number of Os:'))
    nums = []
    for i in range(startIteration, endIteration + 1):
        nums.append(eval('num%d(%d)' % (patternNum, i)))

    line = ''
    for i in range(startIteration, endIteration + 1):
        line += str(nums[i - startIteration]).ljust(patMaxLens[i - startIteration] + len(sep), ' ')
    lines.append(line.rstrip())

    return '\n'.join(lines)


def vis1(n):  # DONE
    """
    O  OO  OOO
       OO  OOO
           OOO
    Number of Os:
    1  4   9"""
    result = []
    for i in range(1, n + 1):
        result.append('O' * n + '\n')
    return ''.join(result).rstrip()


def num1(n):  # DONE
    return n * n


def vis2(n):  # DONE
    """
    O  .O  ..O
       OO  ..O
           OOO
    Number of Os:
    1  3   5"""
    result = []
    for i in range(n - 1):
        result.append(('.' * (n - 1) + 'O') + '\n')
    result.append('O' * n)
    return ''.join(result).rstrip()


def num2(n):  # DONE
    return 1 + (2 * (n - 1))


def vis3(n):  # DONE
    """
    O  O   O
       OO  OO
           OOO
    Number of Os:
    1  3   6"""
    result = []
    for i in range(1, n + 1):
        result.append(('O' * i) + '\n')
    return ''.join(result).rstrip()


def num3(n):  # DONE
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def vis4(n):  # DONE
    """
    O.O  O...O  O.....O
    .O   .O.O   .O...O
    O.O  ..O    ..O.O
         .O.O   ...O
         O...O  ..O.O
                .O...O
                O.....O
    Number of Os:
    5    9      13"""
    result = ''
    for i in range(n):
        result += '.' * i
        result += 'O'
        result += '.' * (2 * (n - 1 - i) + 1)
        result += 'O\n'

    result += ('.' * n) + 'O\n'

    for i in range(n - 1, -1, -1):
        result += '.' * i
        result += 'O'
        result += '.' * (2 * (n - 1 - i) + 1)
        result += 'O\n'

    return result.rstrip()


def num4(n):  # DONE
    return n * 4 + 1


def vis5(n):  # DONE
    """
    .OO  ..OOO  ...OOOO
    O.O  ...OO  ....OOO
    OOO  O..OO  ....OOO
         OOOO   O...OOO
         OOO    OOOOO
                OOOO
                OOOO
    Number of Os:
    7    15     27"""
    result = ''

    result += ('.' * n) + ('O' * (n + 1)) + '\n'
    for i in range(n - 1):
        result += ('.' * (n + 1)) + ('O' * n) + '\n'

    result += 'O' + ('.' * n) + ('O' * n) + '\n'

    result += 'O' * (n + 2) + '\n'
    for i in range(n - 1):
        result += 'O' * (n + 1) + '\n'
    return result


def num5(n):  # DONE
    return 3 + (2 * ((n + 1) * n))


def vis6(n):
    # NOTE: This is a difficult puzzle.
    # NOTE: This is similar to the Sierpinski triangle in pattern #41
    # NOTE: More than one character is needed to draw each shape.
    r"""
     /\
    /__\
   /\  /\
  /__\/__\
    """
    pass


def num6(n):
    return ((n * (n + 1)) // 2) * 3


def vis7(n):  # DONE
    """
    OOO  OO   OO
         OOO  OO
              OOO
    Number of Os:
    3    5    7"""
    result = ''
    for i in range(n - 1):
        result += 'OO\n'
    result += 'OOO\n'
    return result


def num7(n):  # DONE
    return 2 * (n - 1) + 3


def vis8(n):  # DONE
    """
    OO  OO   OOO
        OOO  OOO
             OOOO
    Number of Os:
    2   4    7"""
    result = ''
    for i in range(1, n + 1):
        result += 'O' * (n)
        if i == n:
            result += 'O\n'
        else:
            result += '\n'
    return result


def num8(n):  # DONE
    return ((n * (n + 1)) // 2) + 1


def vis9(n):  # DONE
    """
    O    OO    OOO
    OO   OOO   OOOO
    OOO  OOOO  OOOOO
    Number of Os:
    6    9     12"""
    result = 'O' * (n - 1) + 'O\n'
    result += 'O' * (n - 1) + 'OO\n'
    result += 'O' * (n - 1) + 'OOO\n'
    return result


def num9(n):  # DONE
    return (n - 1) * 3 + 6


def vis10(n):  # DONE
    """
    O  OO  OOO
       O   OO
    Number of Os:
    1  3   5"""
    result = 'O' * n + '\n'
    result += 'O' * (n - 1) + '\n'
    return result


def num10(n):  # DONE
    return (n - 1) * 2 + 1


def vis11(n):  # DONE
    """
    O   O    O
    OO  O    O
        OOO  O
             OOOO
    Number of Os:
    3   5    7"""
    result = 'O\n' * n
    result += 'O' * (n + 1) + '\n'
    return result


def num11(n):  # DONE
    return 2 * n + 1


def vis12(n):  # DONE
    """
    OO  OOO  OOOO
    OO  OOO  OOOO
        OOO  OOOO
             OOOO
    Number of Os:
    4   9    16"""
    result = ''
    for i in range(1, n + 2):
        result += 'O' * (n + 1) + '\n'
    return result


def num12(n):  # DONE
    return (n + 1) ** 2


def vis13(n):  # DONE
    """
    O  O   O
       OO  OO
           OOO
    Number of Os:
    1  3   6"""
    result = ''
    for i in range(1, n + 1):
        result += 'O' * i + '\n'
    return result


def num13(n):  # DONE
    return (n * (n + 1)) // 2


def vis14(n):  # DONE
    """
    O       O       O
    OOOOOO  OOOOOO  OOOOOO
            OOOOOO  OOOOOO
                    OOOOOO
    Number of Os:
    7       13      19"""
    result = 'O\n'
    for i in range(n):
        result += 'OOOOOO\n'
    return result


def num14(n):  # DONE
    return 1 + (n * 6)


def vis15(n):  # DONE
    """
    .O   .O.O   .O.O.O
    OXO  OXOXO  OXOXOXO
    .O   .O.O   .O.O.O
    Number of Os, Xs:
    (4, 1)(7, 2) (10, 3)"""
    # NOTE: Use 'O' for circles, 'X' for squares.
    result = '.O' * n + '\n'
    result += 'O' + ('XO' * n) + '\n'
    result += '.O' * n + '\n'
    return result


def num15(n):  # DONE
    # Returns a tuple of (Os, Xs)
    return (4 + (n - 1) * 3, n)


def vis16(n):  # DONE
    """
    O  .O   ..O
       OOO  .OOO
            OOOOO
    Number of Os:
    1  4    9"""
    result = ''

    for i in range(n):
        result += ('.' * (n - i - 1)) + ('O' * (i * 2 + 1)) + '\n'
    return result


def num16(n):  # DONE
    return n**2


def vis17(n):  # DONE
    """
    .O   ..O    ...O
    OOO  ..O    ...O
         OOOOO  ...O
                OOOOOOO
    Number of Os:
    4    7      10"""
    result = ''
    for i in range(n):
        result += '.' * n + 'O\n'
    result += 'O' * (n * 2 + 1) + '\n'
    return result


def num17(n):  # DONE
    return n * 3 + 1


def vis18(n):  # DONE
    """
    O   O     O
    OO  OOO   OOO
        ..OO  ..OOO
              ....OO
    Number of Os:
    3   6     9"""
    result = 'O\n'

    for i in range(n - 1):
        result += '.' * (i * 2) + 'OOO\n'

    result += '.' * ((n - 1) * 2) + 'OO\n'
    return result


def num18(n):  # DONE
    return n * 3


def vis19(n):  # DONE
    """
    .O   .O    .O
    OOO  OOOO  OOOOO
    .O   OOOO  OOOOO
         .O    OOOOO
               .O
    Number of Os:
    5    10    17"""
    result = '.O\n'

    for i in range(n):
        result += 'O' * (n + 2) + '\n'

    result += '.O\n'
    return result


def num19(n):  # DONE
    return 2 + n * (n + 2)


def vis20(n):
    result = ''
    return result


def num20(n):
    return -1


def vis21(n):
    result = ''
    return result


def num21(n):
    return -1


def vis22(n):
    result = ''
    return result


def num22(n):
    return -1


def vis23(n):
    # NOTE: Use 'O' for red, 'X' for green, 'M' for yellow.
    result = ''
    return result


def num23(n):
    return -1


def vis24(n):
    # NOTE: Use 'O' for red, 'X' for blue.
    result = ''
    return result


def num24(n):
    return -1


def vis25(n):
    # NOTE: Use 'O' for red, 'X' for blue.
    result = ''
    return result


def num25(n):
    return -1


def vis26(n):
    # NOTE: Use 'O' for red, 'X' for blue.
    result = ''
    return result


def num26(n):
    return -1


def vis27(n):
    # NOTE: Use 'O' for red, 'X' for blue.
    result = ''
    return result


def num27(n):
    return -1


def vis28(n):
    # NOTE: This pattern is in 3D and can't be drawn in ASCII.
    raise NotImplementedError


def num28(n):
    return -1


def vis29(n):
    # NOTE: This is not a visual pattern.
    raise NotImplementedError


def num29(n):
    # NOTE: The return value is a tuple (cash card, purchase)
    return -1


def vis30(n):
    # NOTE: This pattern is drawn rotated 45 degrees.
    result = ''
    return result


def num30(n):
    return -1


def vis31(n):
    result = ''
    return result


def num31(n):
    return -1


def vis32(n):
    result = ''
    return result


def num32(n):
    return -1


def vis33(n):
    result = ''
    return result


def num33(n):
    return -1


def vis34(n):
    result = ''
    return result


def num34(n):
    return -1


def vis35(n):
    # NOTE: This pattern draws each bar as a 3x1 "OOO" character.
    result = ''
    return result


def num35(n):
    return -1


def vis36(n):
    # NOTE: This pattern is in 3D and can't be drawn in ASCII.
    raise NotImplementedError


def num36(n):
    return -1


def vis37(n):
    # NOTE: More than one character is needed to draw each shape.
    result = ''
    return result


def num37(n):
    return -1


def vis38(n):
    # NOTE: This pattern's triangles can't be drawn in ASCII.
    raise NotImplementedError


def num38(n):
    # NOTE: This returns a tuple of (segments, unit triangles).
    return -1


def vis39(n):
    # NOTE: This pattern is in 3D and can't be drawn in ASCII.
    raise NotImplementedError


def num39(n):
    return -1


def vis40(n):
    # NOTE: This pattern is in 3D and can't be drawn in ASCII.
    raise NotImplementedError


def num40(n):
    return -1


def vis41(n):
    # NOTE: This is similar to the Sierpinski triangle in pattern #5.
    # NOTE: More than one character is needed to draw each shape.
    r"""
       /\
      /##\
     /\  /\
    /##\/##\
   /\      /\
  /##\    /##\
 /\  /\  /\  /\
/##\/##\/##\/##\
    """


def num41(n):
    # NOTE: Returns a tuple (shaded triangles, unshaded triangles)
    return (-1, -1)


def vis42(n):
    # NOTE: More than one character is needed to draw each shape.
    r"""
     /\ /\ /\ /\ /\
    |  |  |  |  |  |
     \/ \/ \/ \/ \/
    """
    result = ''
    return result


def num42(n):
    # NOTE: More than one character is needed to draw each shape.
    result = ''
    return result


def vis43(n):
    result = ''
    return result


def num43(n):
    return -1


def vis44(n):  # DONE
    r"""
    ....__      ....__....__      ....__....__....__
    .__/##\__   .__/##\__/##\__   .__/##\__/##\__/##\__
    /##\##/##\  /##\##/##\##/##\  /##\##/##\##/##\##/##\
    \##/..\##/  \##/..\##/..\##/  \##/..\##/..\##/..\##/
    /##\__/##\  /##\__/##\__/##\  /##\__/##\__/##\__/##\
    \##/##\##/  \##/##\##/##\##/  \##/##\##/##\##/##\##/
    ...\##/     ...\##/..\##/     ...\##/..\##/..\##/
    Number of filled hexagons:
    6           10                14"""
    line1 = r'....__' * (n)
    line2 = r'.__' + (r'/##\__' * (n))
    line3 = '/##\\' + ('##/##\\' * (n))
    line4 = r'\##/' + (r'..\##/' * (n))
    line5 = '/##\\' + ('__/##\\' * (n))
    line6 = r'\##/' + (r'##\##/' * (n))
    line7 = '.' + (r'..\##/' * (n))

    return '\n'.join([line1, line2, line3, line4, line5, line6, line7])


def num44(n):  # DONE
    return 6 + ((n - 1) * 4)


def vis45(n):
    result = ''
    return result


def num45(n):
    return -1


def vis46(n):
    # NOTE: This pattern is in 3D and can't be drawn in ASCII.
    raise NotImplementedError


r"""
  __
 /  /|
/__/ |
|  | /
|__|/ TODO - figure out how to draw 3D cubes in a standard way
"""


def num46(n):
    # NOTE: Returns a tuple (surface area, volume)
    return (-1, -1)


def vis47(n):
    # NOTE: This pattern is in 3D and can't be drawn in ASCII.
    raise NotImplementedError


def num47(n):
    # NOTE: Returns a tuple (surface area, volume)
    return (-1, -1)


def vis48(n):
    # NOTE: This pattern is in 3D and can't be drawn in ASCII.
    raise NotImplementedError


def num48(n):
    # NOTE: Returns a tuple (surface area, volume)
    return (-1, -1)


def vis49(n):
    # NOTE: This is not a visual pattern, but we can still output the numbers in order.
    result = ''
    return result


def num49(n):
    return -1


def vis50(n):  # DONE
    # NOTE: There is no way we can implement this pattern with ASCII characters.
    raise NotImplementedError


def num50(n):  # DONE
    # NOTE: Returns a tuple (yellow squares, green triangles)
    return -1


def vis51(n):
    # NOTE: More than one character is needed to draw each shape.
    result = ''
    return result


def num51(n):
    return -1


def vis52(n):
    # NOTE: This pattern is in 3D.
    raise NotImplementedError


def num52(n):
    return -1


def vis53(n):  # DONE
    r"""
    .__    .__.__    .__.__.__
    |..|\  |..|..|\  |..|..|..|\
    |__|/  |__|__|/  |__|__|__|/
    Number of segments:
    6      9         12"""
    line1 = '.__' * n
    line2 = '|' + ('..|' * n) + '\\'
    line3 = '|' + ('__|' * n) + '/'

    return '\n'.join([line1, line2, line3])


def num53(n):  # DONE
    # NOTE: Returns number of segments, not number of shapes.
    return 3 + (3 * n)


def vis54(n):  # DONE
    r"""
    .__.__   .__.__.__   .__.__.__.__
    |..|..|  |..|..|..|  |..|..|..|..|
    |__|__|  |__|__|__|  |__|__|__|__|

    7        10          13"""
    line1 = '.__' * (n + 1)
    line2 = '|' + ('..|' * (n + 1))
    line3 = '|' + ('__|' * (n + 1))

    return '\n'.join([line1, line2, line3])


def num54(n):  # DONE
    # NOTE: Returns the number of segments, not the number of squares.
    return 1 + ((n + 1) * 3)


def vis55(n):  # DONE
    # NOTE: More than one character is needed to draw each shape.
    r"""
    .__./\   .__.__./\   .__.__.__./\
    |..|..\  |..|..|..\  |..|..|..|..\
    |__|../  |__|__|../  |__|__|__|../
    ....\/   .......\/   ..........\/

    8        11          14"""
    line1 = '.__' * n + './\\'
    line2 = '|' + ('..|' * n) + '..\\'
    line3 = '|' + ('__|' * n) + '../'
    line4 = '.' + ('...' * n) + '\\/'
    return '\n'.join([line1, line2, line3, line4])


def num55(n):  # DONE
    return 5 + (n * 3)


def vis56(n):
    # NOTE: More than one character is needed to draw each shape.
    r"""
        ____    ____
 /\    /\  /   /\  /\
/__\  /__\/   /__\/__\
"""


def num56(n):
    # NOTE: Returns the number of segments, not the number of shapes.
    return -1


def vis57(n):
    r"""
     __    __ __    __ __ __
    |  |  |  |  |  |  |  |  |
    |__|  |__|__|  |__|__|__|"""


def num57(n):
    # NOTE: Returns the number of segments, not the number of shapes.
    return -1


def vis58(n):  # DONE
    # NOTE: More than one character is needed to draw each shape.
    r"""
    ./\   ./\      ./\..../\
    /..\  /..\__   /..\__/..\
    \__/  \__/..\  \__/..\__/
          ...\../  ...\../
          ....\/   ....\/
    Number of segments:
    5     9        13"""
    line1 = (r'./\...' * ((n + 1) // 2)).rstrip('.')
    if n % 2 == 0:
        line2 = r'/..\__' * (n // 2)
        line3 = r'\__/..' * (n // 2) + '\\'
    else:
        line2 = r'/..\__' * (n // 2) + '/..\\'
        line3 = r'\__/..' * (n // 2) + r'\__/'
    line4 = ('.' + (r'..\../' * (n // 2))).rstrip('.')
    line5 = ('.' + (r'...\/.' * (n // 2))).rstrip('.')

    return '\n'.join([line1, line2, line3, line4, line5])


def num58(n):  # DONE
    # NOTE: Returns the number of segments, not the number of shapes.
    return 5 + (4 * (n - 1))


def vis59(n):  # DONE
    # NOTE: More than one character is needed to draw each shape.

    r"""
    .__.__.__   .__.__.__.__   .__.__.__.__.__
    |..|..|..|  |..|..|..|..|  |..|..|..|..|..|
    |__|__|__|  |__|__|__|__|  |__|__|__|__|__|
    |..|##|..|  |..|#####|..|  |..|########|..|
    |..|..|..|  |..|#####|..|  |..|########|..|
    |__|__|__|  |..|..|..|..|  |..|########|..|
                |__|__|__|__|  |..|..|..|..|..|
                               |__|__|__|__|__|
    Number of black tiles, white tiles:
    (1, 8)      (4, 12)        (9, 16)"""
    result = '.__' * (n + 2) + '\n'
    result += '|..' * (n + 2) + '|\n'
    result += '|__' * (n + 2) + '|\n'
    for i in range(n):
        result += '|..|' + ('#' * (n * 2)) + ('#' * (n - 1)) + '|..|\n'
    result += '|..' * (n + 2) + '|\n'
    result += '|__' * (n + 2) + '|\n'
    return result


def num59(n):  # DONE
    return (n * n, 4 + (4 * n))


def vis60(n):
    # NOTE: More than one character is needed to draw each shape.
    r"""
                    __
                   / /
                  /_/
                 / /
              __/_/
             / / /
      __    /_/_/
     / /   / / /
    /_/   /_/_/"""
    result = ''
    return result


def num60(n):
    return n**2 + n


def vis61(n):
    # NOTE: The visual on visualpatterns.org for this pattern is wrong, it should be:
    """
    O  O  OO  OO  OOOO
       O  OO  OO  OOOO
              OO  OOOO
              OO  OOOO"""

    result = ''
    return result


def num61(n):
    return -1


def vis62(n):
    # NOTE: The visual on visualpatterns.org for this pattern is wrong, it should be:
    """
    O  O  OOO  OOO
       O  OOO  OOO
       O  OOO  OOO
               OOO
               OOO
               OOO
               OOO
               OOO
               OOO"""


def num62(n):
    return -1


def vis63(n):
    # NOTE: The visual on visualpatterns.org for this pattern is wrong, it should be:
    """
    OOOO  OOOOOOOO  OOOOOOOO  OOOOOOOO  OOOOOOOO
                    OOOO      OOOOOOOO  OOOOOOOO
                                        OOOO"""


def num63(n):
    return -1


def vis64(n):
    result = ''
    return result


def num64(n):
    return -1


def vis65(n):
    result = ''
    return result


def num65(n):
    return -1


def vis66(n):  # DONE
    """
    ..O  ...O  ...OO
    .OO  ..OO  ..OOO
    OOX  .OOO  .OOOO
         OOXX  OOXXX
    Number of Os, Xs
    (5, 1)(8, 2)(11, 3)"""
    extraColumns = 'O' * (n - 1)

    # line1 = ('...' + extraColumns)
    line2 = '..O' + extraColumns
    line3 = '.OO' + extraColumns
    line4 = 'OOX' + ('X' * (n - 1))

    if n == 1:
        return '\n'.join([line2, line3, line4])
    else:
        return ('...' + extraColumns) + '\n' + '\n'.join([line2, line3, line4])


def num66(n):  # DONE
    # Return number of Os, Xs
    return (5 + ((n - 1) * 3), n)


def vis67(n):
    result = ''
    return result


def num67(n):
    return -1


def vis68(n):
    result = ''
    return result


def num68(n):
    return -1


def vis69(n):
    result = ''
    return result


def num69(n):
    return -1


def vis70(n):
    result = ''
    return result


def num70(n):
    return -1


def vis71(n):
    result = ''
    return result


def num71(n):
    return -1


def vis72(n):
    result = ''
    return result


def num72(n):
    return -1


def vis73(n):
    result = ''
    return result


def num73(n):
    return -1


def vis74(n):
    result = ''
    return result


def num74(n):
    return -1


def vis75(n):
    result = ''
    return result


def num75(n):
    return -1


def vis76(n):
    result = ''
    return result


def num76(n):
    return -1


def vis77(n):
    result = ''
    return result


def num77(n):
    return -1


def vis78(n):
    result = ''
    return result


def num78(n):
    return -1


def vis79(n):
    result = ''
    return result


def num79(n):
    return -1


def vis80(n):
    result = ''
    return result


def num80(n):
    return -1


def vis81(n):
    result = ''
    return result


def num81(n):
    return -1


def vis82(n):
    result = ''
    return result


def num82(n):
    return -1


def vis83(n):
    result = ''
    return result


def num83(n):
    return -1


def vis84(n):
    result = ''
    return result


def num84(n):
    return -1


def vis85(n):
    result = ''
    return result


def num85(n):
    return -1


def vis86(n):
    result = ''
    return result


def num86(n):
    return -1


def vis87(n):
    result = ''
    return result


def num87(n):
    return -1


def vis88(n):
    result = ''
    return result


def num88(n):
    return -1


def vis89(n):
    result = ''
    return result


def num89(n):
    return -1


def vis90(n):
    result = ''
    return result


def num90(n):
    return -1


def vis91(n):
    result = ''
    return result


def num91(n):
    return -1


def vis92(n):
    result = ''
    return result


def num92(n):
    return -1


def vis93(n):
    result = ''
    return result


def num93(n):
    return -1


def vis94(n):
    result = ''
    return result


def num94(n):
    return -1


def vis95(n):
    result = ''
    return result


def num95(n):
    return -1


def vis96(n):
    result = ''
    return result


def num96(n):
    return -1


def vis97(n):
    result = ''
    return result


def num97(n):
    return -1


def vis98(n):
    result = ''
    return result


def num98(n):
    return -1


def vis99(n):
    result = ''
    return result


def num99(n):
    return -1


def vis100(n):
    result = ''
    return result


def num100(n):
    return -1


def vis101(n):
    result = ''
    return result


def num101(n):
    return -1


def vis102(n):
    result = ''
    return result


def num102(n):
    return -1


def vis103(n):
    result = ''
    return result


def num103(n):
    return -1


def vis104(n):
    result = ''
    return result


def num104(n):
    return -1


def vis105(n):
    result = ''
    return result


def num105(n):
    return -1


def vis106(n):
    result = ''
    return result


def num106(n):
    return -1


def vis107(n):
    result = ''
    return result


def num107(n):
    return -1


def vis108(n):
    result = ''
    return result


def num108(n):
    return -1


def vis109(n):
    result = ''
    return result


def num109(n):
    return -1


def vis110(n):
    result = ''
    return result


def num110(n):
    return -1


def vis111(n):
    result = ''
    return result


def num111(n):
    return -1


def vis112(n):
    result = ''
    return result


def num112(n):
    return -1


def vis113(n):
    result = ''
    return result


def num113(n):
    return -1


def vis114(n):
    result = ''
    return result


def num114(n):
    return -1


def vis115(n):
    result = ''
    return result


def num115(n):
    return -1


def vis116(n):
    result = ''
    return result


def num116(n):
    return -1


def vis117(n):
    result = ''
    return result


def num117(n):
    return -1


def vis118(n):
    result = ''
    return result


def num118(n):
    return -1


def vis119(n):
    result = ''
    return result


def num119(n):
    return -1


def vis120(n):
    result = ''
    return result


def num120(n):
    return -1


def vis121(n):
    result = ''
    return result


def num121(n):
    return -1


def vis122(n):
    result = ''
    return result


def num122(n):
    return -1


def vis123(n):
    result = ''
    return result


def num123(n):
    return -1


def vis124(n):
    result = ''
    return result


def num124(n):
    return -1


def vis125(n):
    result = ''
    return result


def num125(n):
    return -1


def vis126(n):
    result = ''
    return result


def num126(n):
    return -1


def vis127(n):
    result = ''
    return result


def num127(n):
    return -1


def vis128(n):
    result = ''
    return result


def num128(n):
    return -1


def vis129(n):
    result = ''
    return result


def num129(n):
    return -1


def vis130(n):
    result = ''
    return result


def num130(n):
    return -1


def vis131(n):
    result = ''
    return result


def num131(n):
    return -1


def vis132(n):
    result = ''
    return result


def num132(n):
    return -1


def vis133(n):
    result = ''
    return result


def num133(n):
    return -1


def vis134(n):
    result = ''
    return result


def num134(n):
    return -1


def vis135(n):
    result = ''
    return result


def num135(n):
    return -1


def vis136(n):
    result = ''
    return result


def num136(n):
    return -1


def vis137(n):
    result = ''
    return result


def num137(n):
    return -1


def vis138(n):
    result = ''
    return result


def num138(n):
    return -1


def vis139(n):
    result = ''
    return result


def num139(n):
    return -1


def vis140(n):
    result = ''
    return result


def num140(n):
    return -1


def vis141(n):  # DONE
    """
    OO   OOO    OOOO
    OOO  OOOOO  OOOOOOO
    OOO  OOOOO  OOOOOOO
         OOOOO  OOOOOOO
                OOOOOOO
    Number of Os:
    8    18     32"""
    result = 'O' + ('O' * n) + '\n'
    for i in range(n + 1):
        result += 'O' * ((n * 2) + 1) + '\n'
    return result.rstrip()


def num141(n):  # DONE
    return (n + 2) * (n * 2 + 1) - n


def vis142(n):
    result = ''
    return result


def num142(n):
    return -1


def vis143(n):
    result = ''
    return result


def num143(n):
    return -1


def vis144(n):
    result = ''
    return result


def num144(n):
    return -1


def vis145(n):
    result = ''
    return result


def num145(n):
    return -1


def vis146(n):
    result = ''
    return result


def num146(n):
    return -1


def vis147(n):
    result = ''
    return result


def num147(n):
    return -1


def vis148(n):
    result = ''
    return result


def num148(n):
    return -1


def vis149(n):
    result = ''
    return result


def num149(n):
    return -1


def vis150(n):
    result = ''
    return result


def num150(n):
    return -1


def vis151(n):
    result = ''
    return result


def num151(n):
    return -1


def vis152(n):  # DONE
    """
    ..O    ...O     ....O
    .O.O   ..O.O    ...O.O
    O.O.O  .O...O   ..O...O
           O.O.O.O  .O.....O
                    O.O.O.O.O
    Number of Os:
    6      9        12"""
    result = '.' * (n + 1) + 'O\n'
    for i in range(n):
        result += ('.' * (n - i)) + 'O' + ((i * 2 + 1) * '.') + 'O\n'
    result += 'O.' * (n + 1) + 'O'

    return result


def num152(n):  # DONE
    return 3 + (3 * n)


def vis153(n):
    result = ''
    return result


def num153(n):
    return -1


def vis154(n):
    result = ''
    return result


def num154(n):
    return -1


def vis155(n):
    result = ''
    return result


def num155(n):
    return -1


def vis156(n):
    result = ''
    return result


def num156(n):
    return -1


def vis157(n):
    result = ''
    return result


def num157(n):
    return -1


def vis158(n):
    result = ''
    return result


def num158(n):
    return -1


def vis159(n):
    result = ''
    return result


def num159(n):
    return -1


def vis160(n):
    result = ''
    return result


def num160(n):
    return -1


def vis161(n):
    result = ''
    return result


def num161(n):
    return -1


def vis162(n):
    result = ''
    return result


def num162(n):
    return -1


def vis163(n):
    result = ''
    return result


def num163(n):
    return -1


def vis164(n):
    result = ''
    return result


def num164(n):
    return -1


def vis165(n):
    result = ''
    return result


def num165(n):
    return -1


def vis166(n):
    result = ''
    return result


def num166(n):
    return -1


def vis167(n):
    result = ''
    return result


def num167(n):
    return -1


def vis168(n):
    result = ''
    return result


def num168(n):
    return -1


def vis169(n):
    result = ''
    return result


def num169(n):
    return -1


def vis170(n):
    result = ''
    return result


def num170(n):
    return -1


def vis171(n):
    result = ''
    return result


def num171(n):
    return -1


def vis172(n):
    result = ''
    return result


def num172(n):
    return -1


def vis173(n):
    result = ''
    return result


def num173(n):
    return -1


def vis174(n):
    result = ''
    return result


def num174(n):
    return -1


def vis175(n):
    result = ''
    return result


def num175(n):
    return -1


def vis176(n):
    result = ''
    return result


def num176(n):
    return -1


def vis177(n):
    result = ''
    return result


def num177(n):
    return -1


def vis178(n):
    result = ''
    return result


def num178(n):
    return -1


def vis179(n):
    result = ''
    return result


def num179(n):
    return -1


def vis180(n):
    result = ''
    return result


def num180(n):
    return -1


def vis181(n):
    result = ''
    return result


def num181(n):
    return -1


def vis182(n):
    result = ''
    return result


def num182(n):
    return -1


def vis183(n):
    result = ''
    return result


def num183(n):
    return -1


def vis184(n):
    result = ''
    return result


def num184(n):
    return -1


def vis185(n):
    result = ''
    return result


def num185(n):
    return -1


def vis186(n):
    result = ''
    return result


def num186(n):
    return -1


def vis187(n):
    result = ''
    return result


def num187(n):
    return -1


def vis188(n):
    result = ''
    return result


def num188(n):
    return -1


def vis189(n):
    result = ''
    return result


def num189(n):
    return -1


def vis190(n):
    result = ''
    return result


def num190(n):
    return -1


def vis191(n):
    result = ''
    return result


def num191(n):
    return -1


def vis192(n):
    result = ''
    return result


def num192(n):
    return -1


def vis193(n):
    result = ''
    return result


def num193(n):
    return -1


def vis194(n):
    result = ''
    return result


def num194(n):
    return -1


def vis195(n):
    result = ''
    return result


def num195(n):
    return -1


def vis196(n):
    result = ''
    return result


def num196(n):
    return -1


def vis197(n):
    result = ''
    return result


def num197(n):
    return -1


def vis198(n):
    result = ''
    return result


def num198(n):
    return -1


def vis199(n):
    result = ''
    return result


def num199(n):
    return -1


def vis200(n):
    result = ''
    return result


def num200(n):
    return -1


def vis201(n):
    result = ''
    return result


def num201(n):
    return -1


def vis202(n):
    result = ''
    return result


def num202(n):
    return -1


def vis203(n):
    result = ''
    return result


def num203(n):
    return -1


def vis204(n):
    result = ''
    return result


def num204(n):
    return -1


def vis205(n):
    result = ''
    return result


def num205(n):
    return -1


def vis206(n):
    result = ''
    return result


def num206(n):
    return -1


def vis207(n):
    result = ''
    return result


def num207(n):
    return -1


def vis208(n):
    result = ''
    return result


def num208(n):
    return -1


def vis209(n):
    result = ''
    return result


def num209(n):
    return -1


def vis210(n):
    result = ''
    return result


def num210(n):
    return -1


def vis211(n):
    result = ''
    return result


def num211(n):
    return -1


def vis212(n):
    result = ''
    return result


def num212(n):
    return -1


def vis213(n):
    result = ''
    return result


def num213(n):
    return -1


def vis214(n):
    result = ''
    return result


def num214(n):
    return -1


def vis215(n):
    result = ''
    return result


def num215(n):
    return -1


def vis216(n):
    result = ''
    return result


def num216(n):
    return -1


def vis217(n):
    result = ''
    return result


def num217(n):
    return -1


def vis218(n):
    result = ''
    return result


def num218(n):
    return -1


def vis219(n):
    result = ''
    return result


def num219(n):
    return -1


def vis220(n):
    result = ''
    return result


def num220(n):
    return -1


def vis221(n):
    result = ''
    return result


def num221(n):
    return -1


def vis222(n):
    result = ''
    return result


def num222(n):
    return -1


def vis223(n):
    result = ''
    return result


def num223(n):
    return -1


def vis224(n):
    result = ''
    return result


def num224(n):
    return -1


def vis225(n):
    result = ''
    return result


def num225(n):
    return -1


def vis226(n):
    result = ''
    return result


def num226(n):
    return -1


def vis227(n):
    result = ''
    return result


def num227(n):
    return -1


def vis228(n):
    result = ''
    return result


def num228(n):
    return -1


def vis229(n):
    result = ''
    return result


def num229(n):
    return -1


def vis230(n):
    result = ''
    return result


def num230(n):
    return -1


def vis231(n):
    result = ''
    return result


def num231(n):
    return -1


def vis232(n):
    result = ''
    return result


def num232(n):
    return -1


def vis233(n):
    result = ''
    return result


def num233(n):
    return -1


def vis234(n):
    result = ''
    return result


def num234(n):
    return -1


def vis235(n):
    result = ''
    return result


def num235(n):
    return -1


def vis236(n):
    result = ''
    return result


def num236(n):
    return -1


def vis237(n):
    result = ''
    return result


def num237(n):
    return -1


def vis238(n):
    result = ''
    return result


def num238(n):
    return -1


def vis239(n):
    result = ''
    return result


def num239(n):
    return -1


def vis240(n):
    result = ''
    return result


def num240(n):
    return -1


def vis241(n):
    result = ''
    return result


def num241(n):
    return -1


def vis242(n):
    result = ''
    return result


def num242(n):
    return -1


def vis243(n):
    result = ''
    return result


def num243(n):
    return -1


def vis244(n):
    result = ''
    return result


def num244(n):
    return -1


def vis245(n):
    result = ''
    return result


def num245(n):
    return -1


def vis246(n):
    result = ''
    return result


def num246(n):
    return -1


def vis247(n):
    result = ''
    return result


def num247(n):
    return -1


def vis248(n):
    result = ''
    return result


def num248(n):
    return -1


def vis249(n):
    result = ''
    return result


def num249(n):
    return -1


def vis250(n):
    result = ''
    return result


def num250(n):
    return -1


def vis251(n):
    result = ''
    return result


def num251(n):
    return -1


def vis252(n):
    result = ''
    return result


def num252(n):
    return -1


def vis253(n):
    result = ''
    return result


def num253(n):
    return -1


def vis254(n):
    result = ''
    return result


def num254(n):
    return -1


def vis255(n):
    result = ''
    return result


def num255(n):
    return -1


def vis256(n):
    result = ''
    return result


def num256(n):
    return -1


def vis257(n):
    result = ''
    return result


def num257(n):
    return -1


def vis258(n):
    result = ''
    return result


def num258(n):
    return -1


def vis259(n):
    result = ''
    return result


def num259(n):
    return -1


def vis260(n):
    result = ''
    return result


def num260(n):
    return -1


def vis261(n):
    result = ''
    return result


def num261(n):
    return -1


def vis262(n):
    result = ''
    return result


def num262(n):
    return -1


def vis263(n):
    result = ''
    return result


def num263(n):
    return -1


def vis264(n):
    result = ''
    return result


def num264(n):
    return -1


def vis265(n):
    result = ''
    return result


def num265(n):
    return -1


def vis266(n):
    result = ''
    return result


def num266(n):
    return -1


def vis267(n):
    result = ''
    return result


def num267(n):
    return -1


def vis268(n):
    result = ''
    return result


def num268(n):
    return -1


def vis269(n):
    result = ''
    return result


def num269(n):
    return -1


def vis270(n):
    result = ''
    return result


def num270(n):
    return -1


def vis271(n):
    result = ''
    return result


def num271(n):
    return -1


def vis272(n):
    result = ''
    return result


def num272(n):
    return -1


def vis273(n):
    result = ''
    return result


def num273(n):
    return -1


def vis274(n):
    result = ''
    return result


def num274(n):
    return -1


def vis275(n):
    result = ''
    return result


def num275(n):
    return -1


def vis276(n):
    result = ''
    return result


def num276(n):
    return -1


def vis277(n):
    result = ''
    return result


def num277(n):
    return -1


def vis278(n):
    result = ''
    return result


def num278(n):
    return -1


def vis279(n):
    result = ''
    return result


def num279(n):
    return -1


def vis280(n):
    result = ''
    return result


def num280(n):
    return -1


def vis281(n):
    result = ''
    return result


def num281(n):
    return -1


def vis282(n):
    result = ''
    return result


def num282(n):
    return -1


def vis283(n):
    result = ''
    return result


def num283(n):
    return -1


def vis284(n):
    result = ''
    return result


def num284(n):
    return -1


def vis285(n):
    result = ''
    return result


def num285(n):
    return -1


def vis286(n):
    result = ''
    return result


def num286(n):
    return -1


def vis287(n):
    result = ''
    return result


def num287(n):
    return -1


def vis288(n):
    result = ''
    return result


def num288(n):
    return -1


def vis289(n):
    result = ''
    return result


def num289(n):
    return -1


def vis290(n):
    result = ''
    return result


def num290(n):
    return -1


def vis291(n):
    result = ''
    return result


def num291(n):
    return -1


def vis292(n):
    result = ''
    return result


def num292(n):
    return -1


def vis293(n):
    result = ''
    return result


def num293(n):
    return -1


def vis294(n):
    result = ''
    return result


def num294(n):
    return -1


def vis295(n):
    result = ''
    return result


def num295(n):
    return -1


def vis296(n):
    result = ''
    return result


def num296(n):
    return -1


def vis297(n):
    result = ''
    return result


def num297(n):
    return -1


def vis298(n):
    result = ''
    return result


def num298(n):
    return -1


def vis299(n):
    result = ''
    return result


def num299(n):
    return -1


def vis300(n):
    result = ''
    return result


def num300(n):
    return -1


def vis301(n):
    result = ''
    return result


def num301(n):
    return -1


def vis302(n):
    result = ''
    return result


def num302(n):
    return -1


def vis303(n):
    result = ''
    return result


def num303(n):
    return -1


def vis304(n):
    result = ''
    return result


def num304(n):
    return -1


def vis305(n):
    result = ''
    return result


def num305(n):
    return -1


def vis306(n):
    result = ''
    return result


def num306(n):
    return -1


def vis307(n):
    result = ''
    return result


def num307(n):
    return -1


def vis308(n):
    result = ''
    return result


def num308(n):
    return -1


def vis309(n):
    result = ''
    return result


def num309(n):
    return -1


def vis310(n):
    result = ''
    return result


def num310(n):
    return -1


def vis311(n):
    result = ''
    return result


def num311(n):
    return -1


def vis312(n):
    result = ''
    return result


def num312(n):
    return -1


def vis313(n):
    result = ''
    return result


def num313(n):
    return -1


def vis314(n):
    result = ''
    return result


def num314(n):
    return -1


def vis315(n):
    result = ''
    return result


def num315(n):
    return -1


def vis316(n):
    result = ''
    return result


def num316(n):
    return -1


def vis317(n):
    result = ''
    return result


def num317(n):
    return -1


def vis318(n):
    result = ''
    return result


def num318(n):
    return -1


def vis319(n):
    result = ''
    return result


def num319(n):
    return -1


def vis320(n):
    result = ''
    return result


def num320(n):
    return -1


def vis321(n):
    result = ''
    return result


def num321(n):
    return -1


def vis322(n):
    result = ''
    return result


def num322(n):
    return -1


def vis323(n):
    result = ''
    return result


def num323(n):
    return -1


def vis324(n):
    result = ''
    return result


def num324(n):
    return -1


def vis325(n):
    result = ''
    return result


def num325(n):
    return -1


def vis326(n):
    result = ''
    return result


def num326(n):
    return -1


def vis327(n):
    result = ''
    return result


def num327(n):
    return -1


def vis328(n):
    result = ''
    return result


def num328(n):
    return -1


def vis329(n):
    result = ''
    return result


def num329(n):
    return -1


def vis330(n):
    result = ''
    return result


def num330(n):
    return -1


def vis331(n):
    result = ''
    return result


def num331(n):
    return -1


def vis332(n):
    result = ''
    return result


def num332(n):
    return -1


def vis333(n):
    result = ''
    return result


def num333(n):
    return -1


def vis334(n):
    result = ''
    return result


def num334(n):
    return -1


def vis335(n):
    result = ''
    return result


def num335(n):
    return -1


def vis336(n):
    result = ''
    return result


def num336(n):
    return -1


def vis337(n):
    result = ''
    return result


def num337(n):
    return -1


def vis338(n):
    result = ''
    return result


def num338(n):
    return -1


def vis339(n):
    result = ''
    return result


def num339(n):
    return -1


def vis340(n):
    result = ''
    return result


def num340(n):
    return -1


def vis341(n):
    result = ''
    return result


def num341(n):
    return -1


def vis342(n):
    result = ''
    return result


def num342(n):
    return -1


def vis343(n):
    result = ''
    return result


def num343(n):
    return -1


def vis344(n):
    result = ''
    return result


def num344(n):
    return -1


def vis345(n):
    result = ''
    return result


def num345(n):
    return -1


def vis346(n):
    result = ''
    return result


def num346(n):
    return -1


def vis347(n):
    result = ''
    return result


def num347(n):
    return -1


def vis348(n):
    result = ''
    return result


def num348(n):
    return -1


def vis349(n):
    result = ''
    return result


def num349(n):
    return -1


def vis350(n):
    result = ''
    return result


def num350(n):
    return -1


def vis351(n):
    result = ''
    return result


def num351(n):
    return -1


def vis352(n):
    result = ''
    return result


def num352(n):
    return -1


def vis353(n):
    result = ''
    return result


def num353(n):
    return -1


def vis354(n):
    result = ''
    return result


def num354(n):
    return -1


def vis355(n):
    result = ''
    return result


def num355(n):
    return -1


def vis356(n):
    result = ''
    return result


def num356(n):
    return -1


def vis357(n):
    result = ''
    return result


def num357(n):
    return -1


def vis358(n):
    result = ''
    return result


def num358(n):
    return -1


def vis359(n):
    result = ''
    return result


def num359(n):
    return -1


def vis360(n):
    result = ''
    return result


def num360(n):
    return -1


def vis361(n):
    result = ''
    return result


def num361(n):
    return -1


def vis362(n):
    result = ''
    return result


def num362(n):
    return -1


def vis363(n):
    result = ''
    return result


def num363(n):
    return -1


def vis364(n):
    result = ''
    return result


def num364(n):
    return -1


def vis365(n):
    result = ''
    return result


def num365(n):
    return -1


def vis366(n):
    result = ''
    return result


def num366(n):
    return -1


def vis367(n):
    result = ''
    return result


def num367(n):
    return -1


def vis368(n):
    result = ''
    return result


def num368(n):
    return -1


def vis369(n):
    result = ''
    return result


def num369(n):
    return -1


def vis370(n):
    result = ''
    return result


def num370(n):
    return -1


def vis371(n):
    result = ''
    return result


def num371(n):
    return -1


def vis372(n):
    result = ''
    return result


def num372(n):
    return -1


def vis373(n):
    result = ''
    return result


def num373(n):
    return -1


def vis374(n):
    result = ''
    return result


def num374(n):
    return -1


def vis375(n):
    result = ''
    return result


def num375(n):
    return -1


def vis376(n):
    result = ''
    return result


def num376(n):
    return -1


def vis377(n):
    result = ''
    return result


def num377(n):
    return -1


def vis378(n):
    result = ''
    return result


def num378(n):
    return -1


def vis379(n):
    result = ''
    return result


def num379(n):
    return -1


def vis380(n):
    result = ''
    return result


def num380(n):
    return -1


def vis381(n):
    result = ''
    return result


def num381(n):
    return -1


def vis382(n):
    result = ''
    return result


def num382(n):
    return -1


def vis383(n):
    result = ''
    return result


def num383(n):
    return -1


def vis384(n):
    result = ''
    return result


def num384(n):
    return -1


def vis385(n):
    result = ''
    return result


def num385(n):
    return -1


def vis386(n):
    result = ''
    return result


def num386(n):
    return -1


def vis387(n):
    result = ''
    return result


def num387(n):
    return -1


def vis388(n):
    result = ''
    return result


def num388(n):
    return -1


def vis389(n):
    result = ''
    return result


def num389(n):
    return -1


def vis390(n):
    result = ''
    return result


def num390(n):
    return -1


def vis391(n):
    result = ''
    return result


def num391(n):
    return -1


def vis392(n):
    result = ''
    return result


def num392(n):
    return -1


def vis393(n):
    result = ''
    return result


def num393(n):
    return -1


def vis394(n):
    result = ''
    return result


def num394(n):
    return -1


def vis395(n):
    result = ''
    return result


def num395(n):
    return -1


def vis396(n):
    result = ''
    return result


def num396(n):
    return -1


def vis397(n):
    result = ''
    return result


def num397(n):
    return -1


def vis398(n):
    result = ''
    return result


def num398(n):
    return -1


def vis399(n):
    result = ''
    return result


def num399(n):
    return -1


def vis400(n):
    result = ''
    return result


def num400(n):
    return -1


def vis401(n):
    result = ''
    return result


def num401(n):
    return -1


def vis402(n):
    result = ''
    return result


def num402(n):
    return -1


def vis403(n):
    result = ''
    return result


def num403(n):
    return -1


def vis404(n):
    result = ''
    return result


def num404(n):
    return -1


def vis405(n):
    result = ''
    return result


def num405(n):
    return -1


def vis406(n):
    result = ''
    return result


def num406(n):
    return -1


def vis407(n):
    result = ''
    return result


def num407(n):
    return -1


def vis408(n):
    result = ''
    return result


def num408(n):
    return -1


def vis409(n):
    result = ''
    return result


def num409(n):
    return -1


def vis410(n):
    result = ''
    return result


def num410(n):
    return -1


def vis411(n):
    result = ''
    return result


def num411(n):
    return -1


def vis412(n):
    result = ''
    return result


def num412(n):
    return -1


def vis413(n):
    result = ''
    return result


def num413(n):
    return -1


def vis414(n):
    result = ''
    return result


def num414(n):
    return -1


def vis415(n):
    result = ''
    return result


def num415(n):
    return -1


def vis416(n):
    result = ''
    return result


def num416(n):
    return -1


def vis417(n):
    result = ''
    return result


def num417(n):
    return -1


def vis418(n):
    result = ''
    return result


def num418(n):
    return -1


def vis419(n):
    result = ''
    return result


def num419(n):
    return -1


def vis420(n):
    result = ''
    return result


def num420(n):
    return -1


def vis421(n):
    result = ''
    return result


def num421(n):
    return -1


def vis422(n):
    result = ''
    return result


def num422(n):
    return -1


def vis423(n):
    result = ''
    return result


def num423(n):
    return -1


def vis424(n):
    result = ''
    return result


def num424(n):
    return -1


def vis425(n):
    result = ''
    return result


def num425(n):
    return -1


def vis426(n):
    result = ''
    return result


def num426(n):
    return -1


def vis427(n):
    result = ''
    return result


def num427(n):
    return -1


def vis428(n):
    result = ''
    return result


def num428(n):
    return -1


def vis429(n):
    result = ''
    return result


def num429(n):
    return -1


def vis430(n):
    result = ''
    return result


def num430(n):
    return -1


def vis431(n):
    result = ''
    return result


def num431(n):
    return -1


def vis432(n):
    result = ''
    return result


def num432(n):
    return -1


def vis433(n):
    result = ''
    return result


def num433(n):
    return -1


def vis434(n):
    result = ''
    return result


def num434(n):
    return -1


def vis435(n):
    result = ''
    return result


def num435(n):
    return -1


def vis436(n):
    result = ''
    return result


def num436(n):
    return -1


def vis437(n):
    result = ''
    return result


def num437(n):
    return -1


def vis438(n):
    result = ''
    return result


def num438(n):
    return -1


def vis439(n):
    result = ''
    return result


def num439(n):
    return -1


def vis440(n):
    result = ''
    return result


def num440(n):
    return -1


def vis441(n):
    result = ''
    return result


def num441(n):
    return -1


def vis442(n):
    result = ''
    return result


def num442(n):
    return -1


def vis443(n):
    result = ''
    return result


def num443(n):
    return -1


def vis444(n):
    result = ''
    return result


def num444(n):
    return -1


def vis445(n):
    result = ''
    return result


def num445(n):
    return -1


def vis446(n):
    result = ''
    return result


def num446(n):
    return -1


def vis447(n):
    result = ''
    return result


def num447(n):
    return -1


def vis448(n):
    result = ''
    return result


def num448(n):
    return -1


def vis449(n):
    result = ''
    return result


def num449(n):
    return -1


def vis450(n):
    result = ''
    return result


def num450(n):
    return -1


def vis451(n):
    result = ''
    return result


def num451(n):
    return -1


def vis452(n):
    result = ''
    return result


def num452(n):
    return -1


def vis453(n):
    result = ''
    return result


def num453(n):
    return -1


def vis454(n):
    result = ''
    return result


def num454(n):
    return -1


def vis455(n):
    result = ''
    return result


def num455(n):
    return -1


def vis456(n):
    result = ''
    return result


def num456(n):
    return -1


def vis457(n):
    result = ''
    return result


def num457(n):
    return -1


def vis458(n):
    result = ''
    return result


def num458(n):
    return -1


def vis459(n):
    result = ''
    return result


def num459(n):
    return -1


def vis460(n):
    result = ''
    return result


def num460(n):
    return -1


def vis461(n):
    result = ''
    return result


def num461(n):
    return -1


def vis462(n):
    result = ''
    return result


def num462(n):
    return -1


def vis463(n):
    result = ''
    return result


def num463(n):
    return -1


def vis464(n):
    result = ''
    return result


def num464(n):
    return -1


def vis465(n):
    result = ''
    return result


def num465(n):
    return -1


def vis466(n):
    result = ''
    return result


def num466(n):
    return -1


def vis467(n):
    result = ''
    return result


def num467(n):
    return -1


def vis468(n):
    result = ''
    return result


def num468(n):
    return -1


def vis469(n):
    result = ''
    return result


def num469(n):
    return -1


def vis470(n):
    result = ''
    return result


def num470(n):
    return -1


def vis471(n):
    result = ''
    return result


def num471(n):
    return -1


def vis472(n):
    result = ''
    return result


def num472(n):
    return -1


def vis473(n):
    result = ''
    return result


def num473(n):
    return -1


def vis474(n):
    result = ''
    return result


def num474(n):
    return -1


def vis475(n):
    result = ''
    return result


def num475(n):
    return -1


def vis476(n):
    result = ''
    return result


def num476(n):
    return -1


def vis477(n):
    result = ''
    return result


def num477(n):
    return -1


def vis478(n):
    result = ''
    return result


def num478(n):
    return -1


def vis479(n):
    result = ''
    return result


def num479(n):
    return -1


def vis480(n):
    result = ''
    return result


def num480(n):
    return -1
