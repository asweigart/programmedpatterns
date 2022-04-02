import pytest
import visualpatterns as vp

'''
def test_1():  # n
    assert vp.pattern1(1) == 'O'
    assert vp.pattern1(2) == 'OO'
    assert vp.pattern1(3) == 'OOO'
    assert vp.pattern1(10) == 'O' * 10

    for i in range(1, 100):
        assert vp.pattern1(i) == vp.pattern1b(i)

    assert vp.formula1(1) == 1
    assert vp.formula1(2) == 2
    assert vp.formula1(3) == 3
    assert vp.formula1(10) == 10

    for i in range(1, 100):
        assert vp.formula1(i) == vp.formula1b(i)

def test_2():  # n + 1
    assert vp.pattern2(1) == 'OO'
    assert vp.pattern2(2) == 'OOO'
    assert vp.pattern2(3) == 'OOOO'
    assert vp.pattern2(10) == 'O' * 11

    for i in range(1, 100):
        assert vp.pattern2(i) == vp.pattern2b(i)

    assert vp.formula2(1) == 2
    assert vp.formula2(2) == 3
    assert vp.formula2(3) == 4
    assert vp.formula2(10) == 11

    for i in range(1, 100):
        assert vp.formula2(i) == vp.formula2b(i)

def test_3():  # 2n
    assert vp.pattern3(1) == 'OO'
    assert vp.pattern3(2) == 'OOOO'
    assert vp.pattern3(3) == 'OOOOOO'
    assert vp.pattern3(10) == 'O' * 20

    assert vp.formula3(1) == 2
    assert vp.formula3(2) == 4
    assert vp.formula3(3) == 6
    assert vp.formula3(10) == 20

def test_4():  # 2n + 1
    patternFunc = vp.pattern4
    formulaFunc = vp.formula4

    assert patternFunc(1).rstrip() == 'OOO'
    assert patternFunc(2).rstrip() == 'O' * 5
    assert patternFunc(3).rstrip() == 'O' * 7
    assert patternFunc(10).rstrip() == 'O' * 21

    assert formulaFunc(1) == 3
    assert formulaFunc(2) == 5
    assert formulaFunc(3) == 7
    assert formulaFunc(10) == 21


def test_5():  # 3n - 1
    patternFunc = vp.pattern5
    formulaFunc = vp.formula5

    assert patternFunc(1).rstrip() == 'OO'
    assert patternFunc(2).rstrip() == 'O' * 5
    assert patternFunc(3).rstrip() == 'O' * 8
    assert patternFunc(10).rstrip() == 'O' * 29

    assert formulaFunc(1) == 2
    assert formulaFunc(2) == 5
    assert formulaFunc(3) == 8
    assert formulaFunc(10) == 29


def test_6():  # 3
    patternFunc = vp.pattern6
    formulaFunc = vp.formula6

    for i in range(1, 100):
        assert patternFunc(i).rstrip() == 'OOO'
        assert formulaFunc(i) == 3


def test_7():  # 3n
    patternFunc = vp.pattern7
    formulaFunc = vp.formula7

    assert patternFunc(1).rstrip() == 'O' * 3
    assert patternFunc(2).rstrip() == 'O' * 6
    assert patternFunc(3).rstrip() == 'O' * 9
    assert patternFunc(10).rstrip() == 'O' * 30

    assert formulaFunc(1) == 3
    assert formulaFunc(2) == 6
    assert formulaFunc(3) == 9
    assert formulaFunc(10) == 30


def test_8():  # 3n + 3, or 3(n + 1)
    patternFunc = vp.pattern8
    formulaFunc = vp.formula8

    assert patternFunc(1).rstrip() == 'O' * 6
    assert patternFunc(2).rstrip() == 'O' * 9
    assert patternFunc(3).rstrip() == 'O' * 12
    assert patternFunc(10).rstrip() == 'O' * 33

    assert formulaFunc(1) == 6
    assert formulaFunc(2) == 9
    assert formulaFunc(3) == 12
    assert formulaFunc(10) == 33


def test_9():  # 2n + 10
    patternFunc = vp.pattern9
    formulaFunc = vp.formula9

    assert patternFunc(1).rstrip() == 'O' * 12
    assert patternFunc(2).rstrip() == 'O' * 14
    assert patternFunc(3).rstrip() == 'O' * 16
    assert patternFunc(10).rstrip() == 'O' * 30

    assert formulaFunc(1) == 12
    assert formulaFunc(2) == 14
    assert formulaFunc(3) == 16
    assert formulaFunc(10) == 30


def test_10():  # 4n - 3
    patternFunc = vp.pattern10
    formulaFunc = vp.formula10

    assert patternFunc(1).rstrip() == 'O' * 1
    assert patternFunc(2).rstrip() == 'O' * 5
    assert patternFunc(3).rstrip() == 'O' * 9
    assert patternFunc(10).rstrip() == 'O' * 37

    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 5
    assert formulaFunc(3) == 9
    assert formulaFunc(10) == 37


def test_11():  # 4
    patternFunc = vp.pattern11
    formulaFunc = vp.formula11

    for i in range(1, 100):
        assert patternFunc(i).rstrip() == 'OOOO'
        assert formulaFunc(i) == 4


def test_12():  # 3n + 1
    patternFunc = vp.pattern12
    formulaFunc = vp.formula12

    assert patternFunc(1).rstrip() == 'O' * 4
    assert patternFunc(2).rstrip() == 'O' * 7
    assert patternFunc(3).rstrip() == 'O' * 10
    assert patternFunc(10).rstrip() == 'O' * 31

    assert formulaFunc(1) == 4
    assert formulaFunc(2) == 7
    assert formulaFunc(3) == 10
    assert formulaFunc(10) == 31


def test_13():  # 8n + 2
    patternFunc = vp.pattern13
    formulaFunc = vp.formula13

    assert patternFunc(1).rstrip() == 'O' * 10
    assert patternFunc(2).rstrip() == 'O' * 18
    assert patternFunc(3).rstrip() == 'O' * 26
    assert patternFunc(10).rstrip() == 'O' * 82

    assert formulaFunc(1) == 10
    assert formulaFunc(2) == 18
    assert formulaFunc(3) == 26
    assert formulaFunc(10) == 82


def test_14():  # 8n - 2
    patternFunc = vp.pattern14
    formulaFunc = vp.formula14

    assert patternFunc(1).rstrip() == 'O' * 6
    assert patternFunc(2).rstrip() == 'O' * 14
    assert patternFunc(3).rstrip() == 'O' * 22
    assert patternFunc(10).rstrip() == 'O' * 78

    assert formulaFunc(1) == 6
    assert formulaFunc(2) == 14
    assert formulaFunc(3) == 22
    assert formulaFunc(10) == 78


def test_15():  # 2(n + 1) or 2n + 2
    patternFunc = vp.pattern15
    formulaFunc = vp.formula15

    assert patternFunc(1).rstrip() == 'O' * 4
    assert patternFunc(2).rstrip() == 'O' * 6
    assert patternFunc(3).rstrip() == 'O' * 8
    assert patternFunc(10).rstrip() == 'O' * 22

    assert formulaFunc(1) == 4
    assert formulaFunc(2) == 6
    assert formulaFunc(3) == 8
    assert formulaFunc(10) == 22


def test_16():  # n + 2
    patternFunc = vp.pattern16
    formulaFunc = vp.formula16

    assert patternFunc(1).rstrip() == 'O' * 3
    assert patternFunc(2).rstrip() == 'O' * 4
    assert patternFunc(3).rstrip() == 'O' * 5
    assert patternFunc(10).rstrip() == 'O' * 12

    assert formulaFunc(1) == 3
    assert formulaFunc(2) == 4
    assert formulaFunc(3) == 5
    assert formulaFunc(10) == 12


def test_17():  # 8n - 7
    patternFunc = vp.pattern17
    formulaFunc = vp.formula17

    assert patternFunc(1).rstrip() == 'O' * 1
    assert patternFunc(2).rstrip() == 'O' * 9
    assert patternFunc(3).rstrip() == 'O' * 17
    assert patternFunc(10).rstrip() == 'O' * 73

    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 9
    assert formulaFunc(3) == 17
    assert formulaFunc(10) == 73


def test_18():  # 3n + 2
    patternFunc = vp.pattern18
    formulaFunc = vp.formula18

    assert patternFunc(1).rstrip() == 'O' * 5
    assert patternFunc(2).rstrip() == 'O' * 8
    assert patternFunc(3).rstrip() == 'O' * 11
    assert patternFunc(10).rstrip() == 'O' * 32

    assert formulaFunc(1) == 5
    assert formulaFunc(2) == 8
    assert formulaFunc(3) == 11
    assert formulaFunc(10) == 32


def test_19():  # 4n
    patternFunc = vp.pattern19
    formulaFunc = vp.formula19

    assert patternFunc(1).rstrip() == 'O' * 4
    assert patternFunc(2).rstrip() == 'O' * 8
    assert patternFunc(3).rstrip() == 'O' * 12
    assert patternFunc(10).rstrip() == 'O' * 40

    assert formulaFunc(1) == 4
    assert formulaFunc(2) == 8
    assert formulaFunc(3) == 12
    assert formulaFunc(10) == 40


def test_20():  # 4n + 2
    patternFunc = vp.pattern20
    formulaFunc = vp.formula20

    assert patternFunc(1).rstrip() == 'O' * 6
    assert patternFunc(2).rstrip() == 'O' * 10
    assert patternFunc(3).rstrip() == 'O' * 14
    assert patternFunc(10).rstrip() == 'O' * 42

    assert formulaFunc(1) == 6
    assert formulaFunc(2) == 10
    assert formulaFunc(3) == 14
    assert formulaFunc(10) == 42


def test_21():  # 3n + 3
    patternFunc = vp.pattern21
    formulaFunc = vp.formula21

    assert patternFunc(1).rstrip() == 'O' * 6
    assert patternFunc(2).rstrip() == 'O' * 9
    assert patternFunc(3).rstrip() == 'O' * 12
    assert patternFunc(10).rstrip() == 'O' * 33

    assert formulaFunc(1) == 6
    assert formulaFunc(2) == 9
    assert formulaFunc(3) == 12
    assert formulaFunc(10) == 33


def test_22():  # 4n - 3
    patternFunc = vp.pattern22
    formulaFunc = vp.formula22

    assert patternFunc(1).rstrip() == 'O' * 1
    assert patternFunc(2).rstrip() == 'O' * 5
    assert patternFunc(3).rstrip() == 'O' * 9
    assert patternFunc(10).rstrip() == 'O' * 37

    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 5
    assert formulaFunc(3) == 9
    assert formulaFunc(10) == 37


def test_23(): # 1D step increase by 1, 2
    patternFunc = vp.pattern23
    formulaFunc = vp.formula23

    assert patternFunc(1).rstrip() == 'O'
    assert patternFunc(2).rstrip() == 'OO'
    assert patternFunc(3).rstrip() == 'OOOO'
    assert patternFunc(10).rstrip() == 'O' * 14

    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 2
    assert formulaFunc(3) == 4
    assert formulaFunc(10) == 14

    for i in range(1, 100):
        assert patternFunc(i).rstrip() == vp.pattern23b(i).rstrip()
        assert formulaFunc(i) == vp.formula23b(i)


def test_24(): # 1D step increase by 1, 2, 2
    patternFunc = vp.pattern24
    formulaFunc = vp.formula24

    assert patternFunc(1).rstrip() == 'O'
    assert patternFunc(2).rstrip() == 'OO'
    assert patternFunc(3).rstrip() == 'OOOO'
    assert patternFunc(4).rstrip() == 'OOOOOO'
    assert patternFunc(5).rstrip() == 'OOOOOOO'


    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 2
    assert formulaFunc(3) == 4
    assert formulaFunc(4) == 6
    assert formulaFunc(5) == 7

def test_25(): # 1D step increase by 1, 0
    patternFunc = vp.pattern25
    formulaFunc = vp.formula25

    assert patternFunc(1).rstrip() == 'O'
    assert patternFunc(2).rstrip() == 'OO'
    assert patternFunc(3).rstrip() == 'OO'
    assert patternFunc(4).rstrip() == 'OOO'
    assert patternFunc(5).rstrip() == 'OOO'
    assert patternFunc(6).rstrip() == 'OOOO'


    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 2
    assert formulaFunc(3) == 2
    assert formulaFunc(4) == 3
    assert formulaFunc(5) == 3
    assert formulaFunc(6) == 4

    for i in range(1, 100):
        assert patternFunc(i).rstrip() == vp.pattern25b(i).rstrip()
        assert formulaFunc(i) == vp.formula25b(i)


def test_26(): # 1D step increase by 1, 0, 0
    patternFunc = vp.pattern26
    formulaFunc = vp.formula26

    assert patternFunc(1).rstrip() == 'O'
    assert patternFunc(2).rstrip() == 'OO'
    assert patternFunc(3).rstrip() == 'OO'
    assert patternFunc(4).rstrip() == 'OO'
    assert patternFunc(5).rstrip() == 'OOO'
    assert patternFunc(6).rstrip() == 'OOO'
    assert patternFunc(7).rstrip() == 'OOO'
    assert patternFunc(8).rstrip() == 'OOOO'


    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 2
    assert formulaFunc(3) == 2
    assert formulaFunc(4) == 2
    assert formulaFunc(5) == 3
    assert formulaFunc(6) == 3
    assert formulaFunc(7) == 3
    assert formulaFunc(8) == 4


    for i in range(1, 100):
        assert patternFunc(i).rstrip() == vp.pattern26b(i).rstrip()
        assert formulaFunc(i) == vp.formula26b(i)


def test_27(): # 1D step increase by 1, 2, 3, start at 4
    patternFunc = vp.pattern27
    formulaFunc = vp.formula27

    assert patternFunc(1).rstrip() == 'OOOO'
    assert patternFunc(2).rstrip() == 'OOOOO'
    assert patternFunc(3).rstrip() == 'OOOOOOO'
    assert patternFunc(4).rstrip() == 'OOOOOOOOOO'
    assert patternFunc(5).rstrip() == 'OOOOOOOOOOO'
    assert patternFunc(6).rstrip() == 'OOOOOOOOOOOOO'
    assert patternFunc(7).rstrip() == 'OOOOOOOOOOOOOOOO'
    assert patternFunc(8).rstrip() == 'OOOOOOOOOOOOOOOOO'


    assert formulaFunc(1) == 4
    assert formulaFunc(2) == 5
    assert formulaFunc(3) == 7
    assert formulaFunc(4) == 10
    assert formulaFunc(5) == 11
    assert formulaFunc(6) == 13
    assert formulaFunc(7) == 16
    assert formulaFunc(8) == 17


    for i in range(1, 100):
        assert patternFunc(i).rstrip() == vp.pattern27b(i).rstrip()
        assert formulaFunc(i) == vp.formula27b(i)


def test_28(): # 1D step increase by 0, 0, 0, 0, 5, starts at 5
    patternFunc = vp.pattern28
    formulaFunc = vp.formula28

    assert patternFunc(1).rstrip() == 'OOOOO'
    assert patternFunc(2).rstrip() == 'OOOOO'
    assert patternFunc(3).rstrip() == 'OOOOO'
    assert patternFunc(4).rstrip() == 'OOOOO'
    assert patternFunc(5).rstrip() == 'OOOOO'
    assert patternFunc(6).rstrip() == 'OOOOOOOOOO'
    assert patternFunc(7).rstrip() == 'OOOOOOOOOO'
    assert patternFunc(11).rstrip() == 'OOOOOOOOOOOOOOO'


    assert formulaFunc(1) == 5
    assert formulaFunc(2) == 5
    assert formulaFunc(3) == 5
    assert formulaFunc(4) == 5
    assert formulaFunc(5) == 5
    assert formulaFunc(6) == 10
    assert formulaFunc(7) == 10
    assert formulaFunc(11) == 15


    for i in range(1, 100):
        assert patternFunc(i).rstrip() == vp.pattern28b(i).rstrip()
        assert formulaFunc(i) == vp.formula28b(i)



def test_29(): # 1D step increase by 1, 0, 2, 0
    patternFunc = vp.pattern29
    formulaFunc = vp.formula29

    assert patternFunc(1).rstrip() == 'O'
    assert patternFunc(2).rstrip() == 'OO'
    assert patternFunc(3).rstrip() == 'OO'
    assert patternFunc(4).rstrip() == 'OOOO'
    assert patternFunc(5).rstrip() == 'OOOO'
    assert patternFunc(6).rstrip() == 'OOOOO'
    assert patternFunc(7).rstrip() == 'OOOOO'
    assert patternFunc(8).rstrip() == 'OOOOOOO'


    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 2
    assert formulaFunc(3) == 2
    assert formulaFunc(4) == 4
    assert formulaFunc(5) == 4
    assert formulaFunc(6) == 5
    assert formulaFunc(7) == 5
    assert formulaFunc(8) == 7


def test_30(): # 1D step increase by 2, 1
    patternFunc = vp.pattern30
    formulaFunc = vp.formula30

    assert patternFunc(1).rstrip() == 'O'
    assert patternFunc(2).rstrip() == 'OOO'
    assert patternFunc(3).rstrip() == 'OOOO'
    assert patternFunc(4).rstrip() == 'OOOOOO'
    assert patternFunc(5).rstrip() == 'OOOOOOO'
    assert patternFunc(6).rstrip() == 'OOOOOOOOO'
    assert patternFunc(7).rstrip() == 'OOOOOOOOOO'
    assert patternFunc(8).rstrip() == 'OOOOOOOOOOOO'


    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 3
    assert formulaFunc(3) == 4
    assert formulaFunc(4) == 6
    assert formulaFunc(5) == 7
    assert formulaFunc(6) == 9
    assert formulaFunc(7) == 10
    assert formulaFunc(8) == 12


def test_31(): # 1D step increase by 1, 0, 1, starts at 4
    patternFunc = vp.pattern31
    formulaFunc = vp.formula31

    assert patternFunc(1).rstrip() == 'OOOO'
    assert patternFunc(2).rstrip() == 'OOOOO'
    assert patternFunc(3).rstrip() == 'OOOOO'
    assert patternFunc(4).rstrip() == 'OOOOOO'
    assert patternFunc(5).rstrip() == 'OOOOOOO'
    assert patternFunc(6).rstrip() == 'OOOOOOO'
    assert patternFunc(7).rstrip() == 'OOOOOOOO'
    assert patternFunc(8).rstrip() == 'OOOOOOOOO'


    assert formulaFunc(1) == 4
    assert formulaFunc(2) == 5
    assert formulaFunc(3) == 5
    assert formulaFunc(4) == 6
    assert formulaFunc(5) == 7
    assert formulaFunc(6) == 7
    assert formulaFunc(7) == 8
    assert formulaFunc(8) == 9


def test_32(): # 1D step increase by 3, 0
    patternFunc = vp.pattern32
    formulaFunc = vp.formula32

    assert patternFunc(1).rstrip() == 'O'
    assert patternFunc(2).rstrip() == 'OOOO'
    assert patternFunc(3).rstrip() == 'OOOO'
    assert patternFunc(4).rstrip() == 'OOOOOOO'
    assert patternFunc(5).rstrip() == 'OOOOOOO'
    assert patternFunc(6).rstrip() == 'OOOOOOOOOO'
    assert patternFunc(7).rstrip() == 'OOOOOOOOOO'
    assert patternFunc(8).rstrip() == 'OOOOOOOOOOOOO'

    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 4
    assert formulaFunc(3) == 4
    assert formulaFunc(4) == 7
    assert formulaFunc(5) == 7
    assert formulaFunc(6) == 10
    assert formulaFunc(7) == 10
    assert formulaFunc(8) == 13


def test_33(): # 1D step increase by 0, 3, starts at 3
    patternFunc = vp.pattern33
    formulaFunc = vp.formula33

    assert patternFunc(1).rstrip() == 'OOO'
    assert patternFunc(2).rstrip() == 'OOO'
    assert patternFunc(3).rstrip() == 'OOOOOO'
    assert patternFunc(4).rstrip() == 'OOOOOO'
    assert patternFunc(5).rstrip() == 'OOOOOOOOO'


    assert formulaFunc(1) == 3
    assert formulaFunc(2) == 3
    assert formulaFunc(3) == 6
    assert formulaFunc(4) == 6
    assert formulaFunc(5) == 9

def test_34(): # 1D step increase by 2, 3
    patternFunc = vp.pattern34
    formulaFunc = vp.formula34

    assert patternFunc(1).rstrip() == 'O'
    assert patternFunc(2).rstrip() == 'OOO'
    assert patternFunc(3).rstrip() == 'OOOOOO'
    assert patternFunc(4).rstrip() == 'OOOOOOOO'
    assert patternFunc(5).rstrip() == 'OOOOOOOOOOO'
    assert patternFunc(6).rstrip() == 'OOOOOOOOOOOOO'
    assert patternFunc(7).rstrip() == 'OOOOOOOOOOOOOOOO'
    assert patternFunc(8).rstrip() == 'OOOOOOOOOOOOOOOOOO'


    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 3
    assert formulaFunc(3) == 6
    assert formulaFunc(4) == 8
    assert formulaFunc(5) == 11
    assert formulaFunc(6) == 13
    assert formulaFunc(7) == 16
    assert formulaFunc(8) == 18

def test_35(): # 1D step increase by 0, 0, 2
    patternFunc = vp.pattern35
    formulaFunc = vp.formula35

    assert patternFunc(1).rstrip() == 'O'
    assert patternFunc(2).rstrip() == 'O'
    assert patternFunc(3).rstrip() == 'O'
    assert patternFunc(4).rstrip() == 'OOO'
    assert patternFunc(5).rstrip() == 'OOO'
    assert patternFunc(6).rstrip() == 'OOO'
    assert patternFunc(7).rstrip() == 'OOOOO'


    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 1
    assert formulaFunc(3) == 1
    assert formulaFunc(4) == 3
    assert formulaFunc(5) == 3
    assert formulaFunc(6) == 3
    assert formulaFunc(7) == 5


def test_36(): # 1D step increase by 0, 2, 0
    patternFunc = vp.pattern36
    formulaFunc = vp.formula36

    assert patternFunc(1).rstrip() == 'O'
    assert patternFunc(2).rstrip() == 'O'
    assert patternFunc(3).rstrip() == 'OOO'
    assert patternFunc(4).rstrip() == 'OOO'
    assert patternFunc(5).rstrip() == 'OOO'
    assert patternFunc(6).rstrip() == 'OOOOO'


    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 1
    assert formulaFunc(3) == 3
    assert formulaFunc(4) == 3
    assert formulaFunc(5) == 3
    assert formulaFunc(6) == 5


def test_37(): # 1D step increase by 2, 0, 0
    patternFunc = vp.pattern37
    formulaFunc = vp.formula37

    assert patternFunc(1).rstrip() == 'O'
    assert patternFunc(2).rstrip() == 'OOO'
    assert patternFunc(3).rstrip() == 'OOO'
    assert patternFunc(4).rstrip() == 'OOO'
    assert patternFunc(5).rstrip() == 'OOOOO'
    assert patternFunc(6).rstrip() == 'OOOOO'
    assert patternFunc(7).rstrip() == 'OOOOO'
    assert patternFunc(8).rstrip() == 'OOOOOOO'


    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 3
    assert formulaFunc(3) == 3
    assert formulaFunc(4) == 3
    assert formulaFunc(5) == 5
    assert formulaFunc(6) == 5
    assert formulaFunc(7) == 5
    assert formulaFunc(8) == 7

def test_38(): # 1D step increase by 3, 2, 1, starts at 2
    patternFunc = vp.pattern38
    formulaFunc = vp.formula38

    assert patternFunc(1).rstrip() == 'OO'
    assert patternFunc(2).rstrip() == 'OOOOO'
    assert patternFunc(3).rstrip() == 'OOOOOOO'
    assert patternFunc(4).rstrip() == 'OOOOOOOO'
    assert patternFunc(5).rstrip() == 'OOOOOOOOOOO'
    assert patternFunc(6).rstrip() == 'OOOOOOOOOOOOO'
    assert patternFunc(7).rstrip() == 'OOOOOOOOOOOOOO'
    assert patternFunc(8).rstrip() == 'OOOOOOOOOOOOOOOOO'


    assert formulaFunc(1) == 2
    assert formulaFunc(2) == 5
    assert formulaFunc(3) == 7
    assert formulaFunc(4) == 8
    assert formulaFunc(5) == 11
    assert formulaFunc(6) == 13
    assert formulaFunc(7) == 14
    assert formulaFunc(8) == 17




def test_39(): # n x n
    patternFunc = vp.pattern39
    formulaFunc = vp.formula39

    assert patternFunc(1).rstrip() == 'O'
    assert patternFunc(2).rstrip() == 'OO\nOO'
    assert patternFunc(3).rstrip() == 'OOO\nOOO\nOOO'
    assert patternFunc(5).rstrip() == 'OOOOO\nOOOOO\nOOOOO\nOOOOO\nOOOOO'

    assert formulaFunc(1) == 1 ** 2
    assert formulaFunc(2) == 2 ** 2
    assert formulaFunc(3) == 3 ** 2
    assert formulaFunc(10) == 10 ** 2


def test_40(): # 2n x n
    patternFunc = vp.pattern40
    formulaFunc = vp.formula40

    assert patternFunc(1).rstrip() == 'OO'
    assert patternFunc(2).rstrip() == 'OOOO\nOOOO'
    assert patternFunc(3).rstrip() == 'OOOOOO\nOOOOOO\nOOOOOO'
    assert patternFunc(5).rstrip() == 'OOOOOOOOOO\nOOOOOOOOOO\nOOOOOOOOOO\nOOOOOOOOOO\nOOOOOOOOOO'

    assert formulaFunc(1) == 2
    assert formulaFunc(2) == 8
    assert formulaFunc(3) == 18
    assert formulaFunc(5) == 50


def test_41(): # n x 2n
    patternFunc = vp.pattern41
    formulaFunc = vp.formula41

    assert patternFunc(1).rstrip() == 'O\nO'
    assert patternFunc(2).rstrip() == 'OO\nOO\nOO\nOO'
    assert patternFunc(3).rstrip() == 'OOO\nOOO\nOOO\nOOO\nOOO\nOOO'
    assert patternFunc(5).rstrip() == 'OOOOO\nOOOOO\nOOOOO\nOOOOO\nOOOOO\nOOOOO\nOOOOO\nOOOOO\nOOOOO\nOOOOO'

    assert formulaFunc(1) == 2
    assert formulaFunc(2) == 8
    assert formulaFunc(3) == 18
    assert formulaFunc(5) == 50



def test_42(): # 2n x 2n
    patternFunc = vp.pattern42
    formulaFunc = vp.formula42

    assert patternFunc(1).rstrip() == 'OO\nOO'
    assert patternFunc(2).rstrip() == 'OOOO\nOOOO\nOOOO\nOOOO'
    assert patternFunc(3).rstrip() == 'OOOOOO\nOOOOOO\nOOOOOO\nOOOOOO\nOOOOOO\nOOOOOO'
    assert patternFunc(5).rstrip() == 'OOOOOOOOOO\nOOOOOOOOOO\nOOOOOOOOOO\nOOOOOOOOOO\nOOOOOOOOOO\nOOOOOOOOOO\nOOOOOOOOOO\nOOOOOOOOOO\nOOOOOOOOOO\nOOOOOOOOOO'

    assert formulaFunc(1) == 4
    assert formulaFunc(2) == 16
    assert formulaFunc(3) == 36
    assert formulaFunc(5) == 100



def test_43(): # 3n x 2n
    patternFunc = vp.pattern43
    formulaFunc = vp.formula43

    assert patternFunc(1).rstrip() == 'OOO\nOOO'
    assert patternFunc(2).rstrip() == 'OOOOOO\nOOOOOO\nOOOOOO\nOOOOOO'
    assert patternFunc(3).rstrip() == 'OOOOOOOOO\nOOOOOOOOO\nOOOOOOOOO\nOOOOOOOOO\nOOOOOOOOO\nOOOOOOOOO'
    assert patternFunc(5).rstrip() == 'OOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOO'

    assert formulaFunc(1) == 6
    assert formulaFunc(2) == 24
    assert formulaFunc(3) == 54
    assert formulaFunc(5) == 150



def test_44(): # 2n+2 x 2n
    patternFunc = vp.pattern44
    formulaFunc = vp.formula44

    assert patternFunc(1).rstrip() == """
OOOO
OOOO"""[1:]
    assert patternFunc(2).rstrip() == """
OOOOOO
OOOOOO
OOOOOO
OOOOOO"""[1:]
    assert patternFunc(3).rstrip() == """
OOOOOOOO
OOOOOOOO
OOOOOOOO
OOOOOOOO
OOOOOOOO
OOOOOOOO"""[1:]
    assert patternFunc(5).rstrip() == """
OOOOOOOOOOOO
OOOOOOOOOOOO
OOOOOOOOOOOO
OOOOOOOOOOOO
OOOOOOOOOOOO
OOOOOOOOOOOO
OOOOOOOOOOOO
OOOOOOOOOOOO
OOOOOOOOOOOO
OOOOOOOOOOOO"""[1:]

    assert formulaFunc(1) == 8
    assert formulaFunc(2) == 24
    assert formulaFunc(3) == 48
    assert formulaFunc(5) == 120




def test_45(): # 2n+3 x 1n+2
    patternFunc = vp.pattern45
    formulaFunc = vp.formula45

    assert patternFunc(1).rstrip() == """
OOOOO
OOOOO
OOOOO"""[1:]
    assert patternFunc(2).rstrip() == """
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO"""[1:]
    assert patternFunc(3).rstrip() == """
OOOOOOOOO
OOOOOOOOO
OOOOOOOOO
OOOOOOOOO
OOOOOOOOO"""[1:]
    assert patternFunc(5).rstrip() == """
OOOOOOOOOOOOO
OOOOOOOOOOOOO
OOOOOOOOOOOOO
OOOOOOOOOOOOO
OOOOOOOOOOOOO
OOOOOOOOOOOOO
OOOOOOOOOOOOO"""[1:]

    assert formulaFunc(1) == 15
    assert formulaFunc(2) == 28
    assert formulaFunc(3) == 45
    assert formulaFunc(5) == 91




def test_46(): # 2n x 3n
    patternFunc = vp.pattern46
    formulaFunc = vp.formula46

    assert patternFunc(1).rstrip() == """
OO
OO
OO"""[1:]
    assert patternFunc(2).rstrip() == """
OOOO
OOOO
OOOO
OOOO
OOOO
OOOO"""[1:]
    assert patternFunc(3).rstrip() == """
OOOOOO
OOOOOO
OOOOOO
OOOOOO
OOOOOO
OOOOOO
OOOOOO
OOOOOO
OOOOOO"""[1:]
    assert patternFunc(5).rstrip() == """
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO"""[1:]

    assert formulaFunc(1) == 6
    assert formulaFunc(2) == 24
    assert formulaFunc(3) == 54
    assert formulaFunc(5) == 150




def test_47(): # 2n+1 x 3n
    patternFunc = vp.pattern47
    formulaFunc = vp.formula47

    assert patternFunc(1).rstrip() == """
OOO
OOO
OOO"""[1:]
    assert patternFunc(2).rstrip() == """
OOOOO
OOOOO
OOOOO
OOOOO
OOOOO
OOOOO"""[1:]
    assert patternFunc(3).rstrip() == """
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO"""[1:]
    assert patternFunc(5).rstrip() == """
OOOOOOOOOOO
OOOOOOOOOOO
OOOOOOOOOOO
OOOOOOOOOOO
OOOOOOOOOOO
OOOOOOOOOOO
OOOOOOOOOOO
OOOOOOOOOOO
OOOOOOOOOOO
OOOOOOOOOOO
OOOOOOOOOOO
OOOOOOOOOOO
OOOOOOOOOOO
OOOOOOOOOOO
OOOOOOOOOOO"""[1:]

    assert formulaFunc(1) == 9
    assert formulaFunc(2) == 30
    assert formulaFunc(3) == 63
    assert formulaFunc(5) == 165





def test_48(): # n+5 x 2n
    patternFunc = vp.pattern48
    formulaFunc = vp.formula48

    assert patternFunc(1).rstrip() == """
OOOOOO
OOOOOO"""[1:]
    assert patternFunc(2).rstrip() == """
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO"""[1:]
    assert patternFunc(3).rstrip() == """
OOOOOOOO
OOOOOOOO
OOOOOOOO
OOOOOOOO
OOOOOOOO
OOOOOOOO"""[1:]
    assert patternFunc(5).rstrip() == """
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO"""[1:]

    assert formulaFunc(1) == 12
    assert formulaFunc(2) == 28
    assert formulaFunc(3) == 48
    assert formulaFunc(5) == 100






def test_49(): # 3n+1 x 3n+1
    patternFunc = vp.pattern49
    formulaFunc = vp.formula49

    assert patternFunc(1).rstrip() == """
OOOO
OOOO
OOOO
OOOO"""[1:]
    assert patternFunc(2).rstrip() == """
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO"""[1:]
    assert patternFunc(3).rstrip() == """
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO"""[1:]
    assert patternFunc(5).rstrip() == """
OOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOO"""[1:]

    assert formulaFunc(1) == 16
    assert formulaFunc(2) == 49
    assert formulaFunc(3) == 100
    assert formulaFunc(5) == 256






def test_50(): # 1n x 4n+1
    patternFunc = vp.pattern50
    formulaFunc = vp.formula50

    assert patternFunc(1).rstrip() == """
O
O
O
O
O"""[1:]
    assert patternFunc(2).rstrip() == """
OO
OO
OO
OO
OO
OO
OO
OO
OO"""[1:]
    assert patternFunc(3).rstrip() == """
OOO
OOO
OOO
OOO
OOO
OOO
OOO
OOO
OOO
OOO
OOO
OOO
OOO"""[1:]
    assert patternFunc(4).rstrip() == """
OOOO
OOOO
OOOO
OOOO
OOOO
OOOO
OOOO
OOOO
OOOO
OOOO
OOOO
OOOO
OOOO
OOOO
OOOO
OOOO
OOOO"""[1:]

    assert formulaFunc(1) == 5
    assert formulaFunc(2) == 18
    assert formulaFunc(3) == 39
    assert formulaFunc(5) == 105




def test_51(): # 4n+2 x 4n+2
    patternFunc = vp.pattern51
    formulaFunc = vp.formula51

    assert patternFunc(1).rstrip() == """
OOOOOO
OOOOOO
OOOOOO
OOOOOO
OOOOOO
OOOOOO"""[1:]
    assert patternFunc(2).rstrip() == """
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO"""[1:]
    assert patternFunc(3).rstrip() == """
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO"""[1:]
    assert patternFunc(5).rstrip() == """
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO"""[1:]

    assert formulaFunc(1) == 36
    assert formulaFunc(2) == 100
    assert formulaFunc(3) == 196
    assert formulaFunc(5) == 484



def test_52(): # 4n+2 x 2n+3
    patternFunc = vp.pattern52
    formulaFunc = vp.formula52

    assert patternFunc(1).rstrip() == """
OOOOOO
OOOOOO
OOOOOO
OOOOOO
OOOOOO"""[1:]
    assert patternFunc(2).rstrip() == """
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO"""[1:]
    assert patternFunc(3).rstrip() == """
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO"""[1:]
    assert patternFunc(5).rstrip() == """
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOO"""[1:]

    assert formulaFunc(1) == 30
    assert formulaFunc(2) == 70
    assert formulaFunc(3) == 126
    assert formulaFunc(5) == 286




def test_53(): # 4n x 1n+2
    patternFunc = vp.pattern53
    formulaFunc = vp.formula53

    assert patternFunc(1).rstrip() == """
OOOO
OOOO
OOOO"""[1:]
    assert patternFunc(2).rstrip() == """
OOOOOOOO
OOOOOOOO
OOOOOOOO
OOOOOOOO"""[1:]
    assert patternFunc(3).rstrip() == """
OOOOOOOOOOOO
OOOOOOOOOOOO
OOOOOOOOOOOO
OOOOOOOOOOOO
OOOOOOOOOOOO"""[1:]
    assert patternFunc(5).rstrip() == """
OOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOO"""[1:]

    assert formulaFunc(1) == 12
    assert formulaFunc(2) == 32
    assert formulaFunc(3) == 60
    assert formulaFunc(5) == 140






def test_54(): # 1n+2 x 2n
    patternFunc = vp.pattern54
    formulaFunc = vp.formula54

    assert patternFunc(1).rstrip() == """
OOO
OOO"""[1:]
    assert patternFunc(2).rstrip() == """
OOOO
OOOO
OOOO
OOOO"""[1:]
    assert patternFunc(3).rstrip() == """
OOOOO
OOOOO
OOOOO
OOOOO
OOOOO
OOOOO"""[1:]
    assert patternFunc(5).rstrip() == """
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO"""[1:]

    assert formulaFunc(1) == 6
    assert formulaFunc(2) == 16
    assert formulaFunc(3) == 30
    assert formulaFunc(5) == 70





def test_55():  # 4n+3 x 2n
    patternFunc = vp.pattern55
    formulaFunc = vp.formula55

    assert patternFunc(1).rstrip() == """
OOOOOOO
OOOOOOO"""[1:]
    assert patternFunc(2).rstrip() == """
OOOOOOOOOOO
OOOOOOOOOOO
OOOOOOOOOOO
OOOOOOOOOOO"""[1:]
    assert patternFunc(3).rstrip() == """
OOOOOOOOOOOOOOO
OOOOOOOOOOOOOOO
OOOOOOOOOOOOOOO
OOOOOOOOOOOOOOO
OOOOOOOOOOOOOOO
OOOOOOOOOOOOOOO"""[1:]
    assert patternFunc(5).rstrip() == """
OOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOOOOOO"""[1:]

    assert formulaFunc(1) == 14
    assert formulaFunc(2) == 44
    assert formulaFunc(3) == 90
    assert formulaFunc(5) == 230





def test_56():  # step increase (1,1),(0,0)
    patternFunc = vp.pattern56
    formulaFunc = vp.formula56

    assert patternFunc(1).rstrip() == """
O"""[1:]
    assert patternFunc(2).rstrip() == """
OO
OO"""[1:]
    assert patternFunc(3).rstrip() == """
OO
OO"""[1:]
    assert patternFunc(4).rstrip() == """
OOO
OOO
OOO"""[1:]
    assert patternFunc(8).rstrip() == """
OOOOO
OOOOO
OOOOO
OOOOO
OOOOO"""[1:]


    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 4
    assert formulaFunc(3) == 4
    assert formulaFunc(4) == 9
    assert formulaFunc(8) == 25





def test_57():  # step increase (0,0),(1,1)
    patternFunc = vp.pattern57
    formulaFunc = vp.formula57

    assert patternFunc(1).rstrip() == """
O"""[1:]
    assert patternFunc(2).rstrip() == """
O"""[1:]
    assert patternFunc(3).rstrip() == """
OO
OO"""[1:]
    assert patternFunc(4).rstrip() == """
OO
OO"""[1:]
    assert patternFunc(5).rstrip() == """
OOO
OOO
OOO"""[1:]

    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 1
    assert formulaFunc(3) == 4
    assert formulaFunc(4) == 4
    assert formulaFunc(5) == 9

    for i in range(1, 100):
        assert patternFunc(i).rstrip() == vp.pattern57b(i).rstrip()
        assert formulaFunc(i) == vp.formula57b(i)




def test_58():  # step increase (0,1),(1,0)
    patternFunc = vp.pattern58
    formulaFunc = vp.formula58

    assert patternFunc(1).rstrip() == """
O"""[1:]
    assert patternFunc(2).rstrip() == """
O
O"""[1:]
    assert patternFunc(3).rstrip() == """
OO
OO"""[1:]
    assert patternFunc(4).rstrip() == """
OO
OO
OO"""[1:]
    assert patternFunc(5).rstrip() == """
OOO
OOO
OOO"""[1:]
    assert patternFunc(6).rstrip() == """
OOO
OOO
OOO
OOO"""[1:]

    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 2
    assert formulaFunc(3) == 4
    assert formulaFunc(4) == 6
    assert formulaFunc(5) == 9
    assert formulaFunc(6) == 12




def test_pat59():  # step increase (2,1),(2,2)
    patternFunc = vp.pattern59

    assert patternFunc(1).rstrip() == """
OOOO
OOOO"""[1:]
    assert patternFunc(2).rstrip() == """
OOOOOO
OOOOOO
OOOOOO"""[1:]
    assert patternFunc(3).rstrip() == """
OOOOOOOO
OOOOOOOO
OOOOOOOO
OOOOOOOO
OOOOOOOO"""[1:]
    assert patternFunc(4).rstrip() == """
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO"""[1:]
    assert patternFunc(5).rstrip() == """
OOOOOOOOOOOO
OOOOOOOOOOOO
OOOOOOOOOOOO
OOOOOOOOOOOO
OOOOOOOOOOOO
OOOOOOOOOOOO
OOOOOOOOOOOO
OOOOOOOOOOOO"""[1:]
    assert patternFunc(6).rstrip() == """
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO"""[1:]


def test_form59():  # step increase (2,1),(2,2)
    formulaFunc = vp.formula59
    assert formulaFunc(1) == 8
    assert formulaFunc(2) == 18
    assert formulaFunc(3) == 40
    assert formulaFunc(4) == 60
    assert formulaFunc(5) == 96
    assert formulaFunc(6) == 126



def test_pat60():  # step increase (3,3),(0,0),(0,0),(0,0)
    patternFunc = vp.pattern60

    assert patternFunc(1).rstrip() == """
O"""[1:]
    assert patternFunc(2).rstrip() == """
OOOO
OOOO
OOOO
OOOO"""[1:]
    assert patternFunc(3).rstrip() == """
OOOO
OOOO
OOOO
OOOO"""[1:]
    assert patternFunc(4).rstrip() == """
OOOO
OOOO
OOOO
OOOO"""[1:]
    assert patternFunc(5).rstrip() == """
OOOO
OOOO
OOOO
OOOO"""[1:]
    assert patternFunc(6).rstrip() == """
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO"""[1:]


def test_form60():  # step increase (3,3),(0,0),(0,0),(0,0)
    formulaFunc = vp.formula60
    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 16
    assert formulaFunc(3) == 16
    assert formulaFunc(4) == 16
    assert formulaFunc(5) == 16
    assert formulaFunc(6) == 49




def test_pat61():  # step increase (2,2),(-1,-1)
    patternFunc = vp.pattern61

    assert patternFunc(1).rstrip() == """
O"""[1:]
    assert patternFunc(2).rstrip() == """
OOO
OOO
OOO"""[1:]
    assert patternFunc(3).rstrip() == """
OO
OO"""[1:]
    assert patternFunc(4).rstrip() == """
OOOO
OOOO
OOOO
OOOO"""[1:]
    assert patternFunc(5).rstrip() == """
OOO
OOO
OOO"""[1:]
    assert patternFunc(6).rstrip() == """
OOOOO
OOOOO
OOOOO
OOOOO
OOOOO"""[1:]


def test_form61():  # step increase (2,2),(-1,-1)
    formulaFunc = vp.formula61
    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 3**2
    assert formulaFunc(3) == 2**2
    assert formulaFunc(4) == 4**2
    assert formulaFunc(5) == 3**2
    assert formulaFunc(6) == 5**2




def test_pat62():  # step increase (2,2),(0,-1)
    patternFunc = vp.pattern62

    assert patternFunc(1).rstrip() == """
O"""[1:]
    assert patternFunc(2).rstrip() == """
OOO
OOO
OOO"""[1:]
    assert patternFunc(3).rstrip() == """
OOO
OOO"""[1:]
    assert patternFunc(4).rstrip() == """
OOOOO
OOOOO
OOOOO
OOOOO"""[1:]
    assert patternFunc(5).rstrip() == """
OOOOO
OOOOO
OOOOO"""[1:]
    assert patternFunc(6).rstrip() == """
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO"""[1:]


def test_form62():  # step increase (2,2),(0,-1)
    formulaFunc = vp.formula62
    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 9
    assert formulaFunc(3) == 6
    assert formulaFunc(4) == 20
    assert formulaFunc(5) == 15
    assert formulaFunc(6) == 35





def test_pat63():  # step increase (2,1),(0,0),(-1,-1),(0,0)
    patternFunc = vp.pattern63

    assert patternFunc(1).rstrip() == """
O"""[1:]
    assert patternFunc(2).rstrip() == """
OOO
OOO"""[1:]
    assert patternFunc(3).rstrip() == """
OOO
OOO"""[1:]
    assert patternFunc(4).rstrip() == """
OO"""[1:]
    assert patternFunc(5).rstrip() == """
OO"""[1:]
    assert patternFunc(6).rstrip() == """
OOOO
OOOO"""[1:]
    assert patternFunc(7).rstrip() == """
OOOO
OOOO"""[1:]
    assert patternFunc(8).rstrip() == """
OOO"""[1:]


def test_form63():  # step increase (2,1),(0,0),(-1,-1),(0,0)
    formulaFunc = vp.formula63
    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 6
    assert formulaFunc(3) == 6
    assert formulaFunc(4) == 2
    assert formulaFunc(5) == 2
    assert formulaFunc(6) == 8
    assert formulaFunc(7) == 8
    assert formulaFunc(8) == 3





def test_pat64():  # step increase (-1,1),(3,4), starting 5,1
    patternFunc = vp.pattern64

    assert patternFunc(1).rstrip() == """
OOOOO"""[1:]
    assert patternFunc(2).rstrip() == """
OOOO
OOOO"""[1:]
    assert patternFunc(3).rstrip() == """
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO"""[1:]
    assert patternFunc(4).rstrip() == """
OOOOOO
OOOOOO
OOOOOO
OOOOOO
OOOOOO
OOOOOO
OOOOOO"""[1:]
    assert patternFunc(5).rstrip() == """
OOOOOOOOO
OOOOOOOOO
OOOOOOOOO
OOOOOOOOO
OOOOOOOOO
OOOOOOOOO
OOOOOOOOO
OOOOOOOOO
OOOOOOOOO
OOOOOOOOO
OOOOOOOOO"""[1:]


def test_form64():  # step increase (-1,1),(3,4), starting 5,1
    formulaFunc = vp.formula64
    assert formulaFunc(1) == 5
    assert formulaFunc(2) == 8
    assert formulaFunc(3) == 42
    assert formulaFunc(4) == 42
    assert formulaFunc(5) == 99






def test_pat65():  # step increase (0, 0),(3, 2),(-1, -1),starting at 1,1
    patternFunc = vp.pattern65

    assert patternFunc(1).rstrip() == """
O"""[1:]
    assert patternFunc(2).rstrip() == """
O"""[1:]
    assert patternFunc(3).rstrip() == """
OOOO
OOOO
OOOO"""[1:]
    assert patternFunc(4).rstrip() == """
OOO
OOO"""[1:]
    assert patternFunc(5).rstrip() == """
OOO
OOO"""[1:]



def test_form65():  # step increase (0, 0),(3, 2),(-1, -1),starting at 1,1
    formulaFunc = vp.formula65
    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 1
    assert formulaFunc(3) == 12
    assert formulaFunc(4) == 6
    assert formulaFunc(5) == 6




def test_pat66():  # step increase (4, 0),(2, -2),(1, 2),starting at 1,3
    patternFunc = vp.pattern66

    assert patternFunc(1).rstrip() == """
O
O
O"""[1:]
    assert patternFunc(2).rstrip() == """
OOOOO
OOOOO
OOOOO"""[1:]
    assert patternFunc(3).rstrip() == """
OOOOOOO"""[1:]
    assert patternFunc(4).rstrip() == """
OOOOOOOO
OOOOOOOO
OOOOOOOO"""[1:]
    assert patternFunc(5).rstrip() == """
OOOOOOOOOOOO
OOOOOOOOOOOO
OOOOOOOOOOOO"""[1:]



def test_form66():  # step increase (4, 0),(2, -2),(1, 2),starting at 1,3
    formulaFunc = vp.formula66
    assert formulaFunc(1) == 3
    assert formulaFunc(2) == 15
    assert formulaFunc(3) == 7
    assert formulaFunc(4) == 24
    assert formulaFunc(5) == 36




def test_pat67():  # step increase (3, 0),(2, 1),starting at 4,3
    patternFunc = vp.pattern67

    assert patternFunc(1).rstrip() == """
OOOO
OOOO
OOOO"""[1:]
    assert patternFunc(2).rstrip() == """
OOOOOOO
OOOOOOO
OOOOOOO"""[1:]
    assert patternFunc(3).rstrip() == """
OOOOOOOOO
OOOOOOOOO
OOOOOOOOO
OOOOOOOOO"""[1:]
    assert patternFunc(4).rstrip() == """
OOOOOOOOOOOO
OOOOOOOOOOOO
OOOOOOOOOOOO
OOOOOOOOOOOO"""[1:]
    assert patternFunc(5).rstrip() == """
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO
OOOOOOOOOOOOOO"""[1:]



def test_form67():  # step increase
    formulaFunc = vp.formula67
    assert formulaFunc(1) == 12
    assert formulaFunc(2) == 21
    assert formulaFunc(3) == 36
    assert formulaFunc(4) == 48
    assert formulaFunc(5) == 70




def test_pat68():  # step increase (4, -1),(2, 2),(4, -2),(0, 2),starting at 2,3
    patternFunc = vp.pattern68

    assert patternFunc(1).rstrip() == """
OO
OO
OO"""[1:]
    assert patternFunc(2).rstrip() == """
OOOOOO
OOOOOO"""[1:]
    assert patternFunc(3).rstrip() == """
OOOOOOOO
OOOOOOOO
OOOOOOOO
OOOOOOOO"""[1:]
    assert patternFunc(4).rstrip() == """
OOOOOOOOOOOO
OOOOOOOOOOOO"""[1:]
    assert patternFunc(5).rstrip() == """
OOOOOOOOOOOO
OOOOOOOOOOOO
OOOOOOOOOOOO
OOOOOOOOOOOO"""[1:]
    assert patternFunc(6).rstrip() == """
OOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOO"""[1:]



def test_form68():  # step increase (4, -1),(2, 2),(4, -2),(0, 2),starting at 2,3
    formulaFunc = vp.formula68
    assert formulaFunc(1) == 6
    assert formulaFunc(2) == 12
    assert formulaFunc(3) == 32
    assert formulaFunc(4) == 24
    assert formulaFunc(5) == 48
    assert formulaFunc(6) == 48




def test_pat69():  # step increase (2, 1),(0, 1),starting at 4,3
    patternFunc = vp.pattern69

    assert patternFunc(1).rstrip() == """
OOOO
OOOO
OOOO"""[1:]
    assert patternFunc(2).rstrip() == """
OOOOOO
OOOOOO
OOOOOO
OOOOOO"""[1:]
    assert patternFunc(3).rstrip() == """
OOOOOO
OOOOOO
OOOOOO
OOOOOO
OOOOOO"""[1:]
    assert patternFunc(4).rstrip() == """
OOOOOOOO
OOOOOOOO
OOOOOOOO
OOOOOOOO
OOOOOOOO
OOOOOOOO"""[1:]
    assert patternFunc(5).rstrip() == """
OOOOOOOO
OOOOOOOO
OOOOOOOO
OOOOOOOO
OOOOOOOO
OOOOOOOO
OOOOOOOO"""[1:]



def test_form69():  # step increase (2, 1),(0, 1),starting at 4,3
    formulaFunc = vp.formula69
    assert formulaFunc(1) == 12
    assert formulaFunc(2) == 24
    assert formulaFunc(3) == 30
    assert formulaFunc(4) == 48
    assert formulaFunc(5) == 56




def test_pat70():  # step increase (0, 2),(2, 1),starting at 3,3
    patternFunc = vp.pattern70

    assert patternFunc(1).rstrip() == """
OOO
OOO
OOO"""[1:]
    assert patternFunc(2).rstrip() == """
OOO
OOO
OOO
OOO
OOO"""[1:]
    assert patternFunc(3).rstrip() == """
OOOOO
OOOOO
OOOOO
OOOOO
OOOOO
OOOOO"""[1:]
    assert patternFunc(4).rstrip() == """
OOOOO
OOOOO
OOOOO
OOOOO
OOOOO
OOOOO
OOOOO
OOOOO"""[1:]
    assert patternFunc(5).rstrip() == """
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO"""[1:]



def test_form70():  # step increase (0, 2),(2, 1),starting at 3,3
    formulaFunc = vp.formula70
    assert formulaFunc(1) == 9
    assert formulaFunc(2) == 15
    assert formulaFunc(3) == 30
    assert formulaFunc(4) == 40
    assert formulaFunc(5) == 63




def test_pat71():  # step increase (1, 0),(3, 3),(4, 0),starting at 2,1
    patternFunc = vp.pattern71

    assert patternFunc(1).rstrip() == """
OO"""[1:]
    assert patternFunc(2).rstrip() == """
OOO"""[1:]
    assert patternFunc(3).rstrip() == """
OOOOOO
OOOOOO
OOOOOO
OOOOOO"""[1:]
    assert patternFunc(4).rstrip() == """
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO"""[1:]
    assert patternFunc(5).rstrip() == """
OOOOOOOOOOO
OOOOOOOOOOO
OOOOOOOOOOO
OOOOOOOOOOO"""[1:]



def test_form71():  # step increase (1, 0),(3, 3),(4, 0),starting at 2,1
    formulaFunc = vp.formula71
    assert formulaFunc(1) == 2
    assert formulaFunc(2) == 3
    assert formulaFunc(3) == 24
    assert formulaFunc(4) == 40
    assert formulaFunc(5) == 44




def test_pat72():  # step increase (-1, 0),(-1, 1),(2, -1),starting at 3,2
    patternFunc = vp.pattern72

    assert patternFunc(1).rstrip() == """
OOO
OOO"""[1:]
    assert patternFunc(2).rstrip() == """
OO
OO"""[1:]
    assert patternFunc(3).rstrip() == """
O
O
O"""[1:]
    assert patternFunc(4).rstrip() == """
OOO
OOO"""[1:]
    assert patternFunc(5).rstrip() == """
OO
OO"""[1:]



def test_form72():  # step increase (-1, 0),(-1, 1),(2, -1),starting at 3,2
    formulaFunc = vp.formula72
    assert formulaFunc(1) == 6
    assert formulaFunc(2) == 4
    assert formulaFunc(3) == 3
    assert formulaFunc(4) == 6
    assert formulaFunc(5) == 4





def test_73(): # stair pattern
    patternFunc = vp.pattern73
    formulaFunc = vp.formula73

    assert patternFunc(1).rstrip() == 'O'
    assert patternFunc(2).rstrip() == 'O\nOO'
    assert patternFunc(3).rstrip() == 'O\nOO\nOOO'
    assert patternFunc(8).rstrip() == 'O\nOO\nOOO\nOOOO\nOOOOO\nOOOOOO\nOOOOOOO\nOOOOOOOO'

    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 3
    assert formulaFunc(3) == 6
    assert formulaFunc(10) == 55

    for i in range(1, 100):
        assert patternFunc(i).rstrip() == vp.pattern73b(i).rstrip()
        assert formulaFunc(i) == vp.formula73b(i)


def test_74(): # reverse stair pattern
    patternFunc = vp.pattern74
    formulaFunc = vp.formula74

    assert patternFunc(1).rstrip() == 'O'
    assert patternFunc(2).rstrip() == 'OO\nO'
    assert patternFunc(3).rstrip() == 'OOO\nOO\nO'
    assert patternFunc(5).rstrip() == 'OOOOO\nOOOO\nOOO\nOO\nO'

    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 3
    assert formulaFunc(3) == 6
    assert formulaFunc(10) == 55







def test_pat75():  # stair starts with 3 rows
    patternFunc = vp.pattern75

    assert patternFunc(1).rstrip() == """
O
OO
OOO"""[1:]
    assert patternFunc(2).rstrip() == """
O
OO
OOO
OOOO"""[1:]
    assert patternFunc(3).rstrip() == """
O
OO
OOO
OOOO
OOOOO"""[1:]
    assert patternFunc(4).rstrip() == """
O
OO
OOO
OOOO
OOOOO
OOOOOO"""[1:]



def test_form75():  # stair starts with 3 rows
    formulaFunc = vp.formula75
    assert formulaFunc(1) == 6
    assert formulaFunc(2) == 10
    assert formulaFunc(3) == 15
    assert formulaFunc(4) == 21


def test_76():  # stair that increases width by 2
    patternFunc = vp.pattern76
    formulaFunc = vp.formula76

    assert patternFunc(1).rstrip() == 'O'
    assert patternFunc(2).rstrip() == 'O\nOOO'
    assert patternFunc(3).rstrip() == 'O\nOOO\nOOOOO'
    assert patternFunc(5).rstrip() == 'O\nOOO\nOOOOO\nOOOOOOO\nOOOOOOOOO'

    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 4
    assert formulaFunc(3) == 9
    assert formulaFunc(10) == 100

    for i in range(1, 100):
        assert formulaFunc(i) == vp.formula76b(i)

'''



def test_pat77():  # double stairs
    patternFunc = vp.pattern77

    assert patternFunc(1).rstrip() == """
O
O"""[1:]
    assert patternFunc(2).rstrip() == """
O
OO
OO
O"""[1:]
    assert patternFunc(3).rstrip() == """
O
OO
OOO
OOO
OO
O"""[1:]
    assert patternFunc(4).rstrip() == """
O
OO
OOO
OOOO
OOOO
OOO
OO
O"""[1:]



def test_form77():  # double stairs
    formulaFunc = vp.formula77
    assert formulaFunc(1) == 2
    assert formulaFunc(2) == 6
    assert formulaFunc(3) == 12
    assert formulaFunc(4) == 20






def test_pat78():  # pat 97 previous stairs increase as well
    patternFunc = vp.pattern78

    assert patternFunc(1).rstrip() == """
O"""[1:]
    assert patternFunc(2).rstrip() == """
OO
OOO"""[1:]
    assert patternFunc(3).rstrip() == """
OOO
OOOO
OOOOO"""[1:]
    assert patternFunc(4).rstrip() == """
OOOO
OOOOO
OOOOOO
OOOOOOO"""[1:]



def test_form78():  # pat 97 previous stairs increase as well
    formulaFunc = vp.formula78
    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 5
    assert formulaFunc(3) == 12
    assert formulaFunc(4) == 22




def test_79():  # stair pattern, increase width and height by 2
    patternFunc = vp.pattern79
    formulaFunc = vp.formula79

    assert patternFunc(1).rstrip() == 'O'
    assert patternFunc(2).rstrip() == 'O\nOOO\nOOOOO'
    assert patternFunc(3).rstrip() == 'O\nOOO\nOOOOO\nOOOOOOO\nOOOOOOOOO'
    assert patternFunc(5).rstrip() == 'O\nOOO\nOOOOO\nOOOOOOO\nOOOOOOOOO\n' + 'O' * 11 + '\n' + 'O' * 13 + '\n' + 'O' * 15 + '\n' + 'O' * 17

    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 9
    assert formulaFunc(3) == 25
    assert formulaFunc(10) == 361



def test_pat80():  # double stairs with one middle, forming an arrow:
    patternFunc = vp.pattern80

    assert patternFunc(1).rstrip() == """
O"""[1:]
    assert patternFunc(2).rstrip() == """
O
OO
O"""[1:]
    assert patternFunc(3).rstrip() == """
O
OO
OOO
OO
O"""[1:]
    assert patternFunc(4).rstrip() == """
O
OO
OOO
OOOO
OOO
OO
O"""[1:]



def test_form80():  # double stairs with one middle, forming an arrow:
    formulaFunc = vp.formula80
    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 4
    assert formulaFunc(3) == 9
    assert formulaFunc(4) == 16








def test_pat81():  # stacked stairs
    patternFunc = vp.pattern81

    assert patternFunc(1).rstrip() == """
O
O"""[1:]
    assert patternFunc(2).rstrip() == """
O
OO
O
OO"""[1:]
    assert patternFunc(3).rstrip() == """
O
OO
OOO
O
OO
OOO"""[1:]
    assert patternFunc(4).rstrip() == """
O
OO
OOO
OOOO
O
OO
OOO
OOOO"""[1:]


def test_form81():  # stacked stairs
    formulaFunc = vp.formula81
    assert formulaFunc(1) == 2
    assert formulaFunc(2) == 6
    assert formulaFunc(3) == 12
    assert formulaFunc(4) == 20






def test_pat82():  # exponential stairs
    patternFunc = vp.pattern82

    assert patternFunc(1).rstrip() == """
O"""[1:]
    assert patternFunc(2).rstrip() == """
O
OOOO"""[1:]
    assert patternFunc(3).rstrip() == """
O
OOOO
OOOOOOOOO"""[1:]
    assert patternFunc(4).rstrip() == """
O
OOOO
OOOOOOOOO
OOOOOOOOOOOOOOOO"""[1:]


def test_form82():  # exponential stairs
    formulaFunc = vp.formula82
    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 5
    assert formulaFunc(3) == 14
    assert formulaFunc(4) == 30







def test_pat83():  # slow growing stairs
    patternFunc = vp.pattern83

    assert patternFunc(1).rstrip() == """
O"""[1:]
    assert patternFunc(2).rstrip() == """
O
O"""[1:]
    assert patternFunc(3).rstrip() == """
O
O
OO"""[1:]
    assert patternFunc(4).rstrip() == """
O
O
OO
OO"""[1:]


def test_form83():  # slow growing stairs
    formulaFunc = vp.formula83
    assert formulaFunc(1) == 1
    assert formulaFunc(2) == 2
    assert formulaFunc(3) == 4
    assert formulaFunc(4) == 6








def test_pat84():  # double stairs
    patternFunc = vp.pattern84

    assert patternFunc(1).rstrip() == """
O
O"""[1:]
    assert patternFunc(2).rstrip() == """
O
O
OO
OO"""[1:]
    assert patternFunc(3).rstrip() == """
O
O
OO
OO
OOO
OOO"""[1:]
    assert patternFunc(4).rstrip() == """
O
O
OO
OO
OOO
OOO
OOOO
OOOO"""[1:]


def test_form84():  # double stairs
    formulaFunc = vp.formula84
    assert formulaFunc(1) == 2
    assert formulaFunc(2) == 6
    assert formulaFunc(3) == 12
    assert formulaFunc(4) == 20









def test_pat85():  # grow by 2, start at 2
    patternFunc = vp.pattern85

    assert patternFunc(1).rstrip() == """
OO"""[1:]
    assert patternFunc(2).rstrip() == """
OO
OOOO"""[1:]
    assert patternFunc(3).rstrip() == """
OO
OOOO
OOOOOO"""[1:]
    assert patternFunc(4).rstrip() == """
OO
OOOO
OOOOOO
OOOOOOOO"""[1:]


def test_form85():  # grow by 2, start at 2
    formulaFunc = vp.formula85
    assert formulaFunc(1) == 2
    assert formulaFunc(2) == 6
    assert formulaFunc(3) == 12
    assert formulaFunc(4) == 20







def test_pat86():  # grow by 3, start at 3
    patternFunc = vp.pattern86

    assert patternFunc(1).rstrip() == """
OOO"""[1:]
    assert patternFunc(2).rstrip() == """
OOO
OOOOOO"""[1:]
    assert patternFunc(3).rstrip() == """
OOO
OOOOOO
OOOOOOOOO"""[1:]
    assert patternFunc(4).rstrip() == """
OOO
OOOOOO
OOOOOOOOO
OOOOOOOOOOOO"""[1:]


def test_form86():  # grow by 3, start at 3
    formulaFunc = vp.formula86
    assert formulaFunc(1) == 3
    assert formulaFunc(2) == 9
    assert formulaFunc(3) == 18
    assert formulaFunc(4) == 30







def test_pat87():  # grow by 2 and double stairs
    patternFunc = vp.pattern87

    assert patternFunc(1).rstrip() == """
OO
OO"""[1:]
    assert patternFunc(2).rstrip() == """
OO
OO
OOOO
OOOO"""[1:]
    assert patternFunc(3).rstrip() == """
OO
OO
OOOO
OOOO
OOOOOO
OOOOOO"""[1:]
    assert patternFunc(4).rstrip() == """
OO
OO
OOOO
OOOO
OOOOOO
OOOOOO
OOOOOOOO
OOOOOOOO"""[1:]


def test_form87():  # grow by 2 and double stairs
    formulaFunc = vp.formula87
    assert formulaFunc(1) == 4
    assert formulaFunc(2) == 12
    assert formulaFunc(3) == 24
    assert formulaFunc(4) == 40















if __name__ == '__main__':
    pytest.main()
