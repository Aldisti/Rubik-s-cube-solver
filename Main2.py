# by Aldisti
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver

MOVES = 0

def clockwiseRotation(mat):
    mat[0][0], mat[2][0], mat[2][2], mat[0][2] = mat[2][0], mat[2][2], mat[0][2], mat[0][0]
    mat[1][0], mat[2][1], mat[1][2], mat[0][1] = mat[2][1], mat[1][2], mat[0][1], mat[1][0]

def antiClockwiseRotation(mat):
    mat[0][0], mat[0][2], mat[2][2], mat[2][0] = mat[0][2], mat[2][2], mat[2][0], mat[0][0]
    mat[0][1], mat[1][2], mat[2][1], mat[1][0] = mat[1][2], mat[2][1], mat[1][0], mat[0][1]

def R():
    global MOVES
    MOVES += 1

    GREEN[0][2], WHITE[0][2], BLUE[2][0], YELLOW[0][2] = WHITE[0][2], BLUE[2][0], YELLOW[0][2], GREEN[0][2]
    GREEN[1][2], WHITE[1][2], BLUE[1][0], YELLOW[1][2] = WHITE[1][2], BLUE[1][0], YELLOW[1][2], GREEN[1][2]
    GREEN[2][2], WHITE[2][2], BLUE[0][0], YELLOW[2][2] = WHITE[2][2], BLUE[0][0], YELLOW[2][2], GREEN[2][2]
    clockwiseRotation(ORANGE)

def R1():
    global MOVES
    MOVES += 1

    GREEN[0][2], YELLOW[0][2], BLUE[2][0], WHITE[0][2] = YELLOW[0][2], BLUE[2][0], WHITE[0][2], GREEN[0][2]
    GREEN[1][2], YELLOW[1][2], BLUE[1][0], WHITE[1][2] = YELLOW[1][2], BLUE[1][0], WHITE[1][2], GREEN[1][2]
    GREEN[2][2], YELLOW[2][2], BLUE[0][0], WHITE[2][2] = YELLOW[2][2], BLUE[0][0], WHITE[2][2], GREEN[2][2]
    antiClockwiseRotation(ORANGE)

def L():
    global MOVES
    MOVES += 1

    GREEN[0][0], YELLOW[0][0], BLUE[2][2], WHITE[0][0] = YELLOW[0][0], BLUE[2][2], WHITE[0][0], GREEN[0][0]
    GREEN[1][0], YELLOW[1][0], BLUE[1][2], WHITE[1][0] = YELLOW[1][0], BLUE[1][2], WHITE[1][0], GREEN[1][0]
    GREEN[2][0], YELLOW[2][0], BLUE[0][2], WHITE[2][0] = YELLOW[2][0], BLUE[0][2], WHITE[2][0], GREEN[2][0]
    # ruoto il centro rosso in senso orario
    clockwiseRotation(RED)

def L1():
    global MOVES
    MOVES += 1
    
    GREEN[0][0], WHITE[0][0], BLUE[2][2], YELLOW[0][0] = WHITE[0][0], BLUE[2][2], YELLOW[0][0], GREEN[0][0]
    GREEN[1][0], WHITE[1][0], BLUE[1][2], YELLOW[1][0] = WHITE[1][0], BLUE[1][2], YELLOW[1][0], GREEN[1][0]
    GREEN[2][0], WHITE[2][0], BLUE[0][2], YELLOW[2][0] = WHITE[2][0], BLUE[0][2], YELLOW[2][0], GREEN[2][0]
    antiClockwiseRotation(RED)

def U():
    global MOVES
    MOVES += 1

    GREEN[0], ORANGE[0], BLUE[0], RED[0] = ORANGE[0], BLUE[0], RED[0], GREEN[0]
    # ruoto il centro bianco in senso orario
    clockwiseRotation(YELLOW)

def U1():
    global MOVES
    MOVES += 1
    
    GREEN[0], RED[0], BLUE[0], ORANGE[0] = RED[0], BLUE[0], ORANGE[0], GREEN[0]
    antiClockwiseRotation(YELLOW)

def D():
    global MOVES
    MOVES += 1

    GREEN[2], RED[2], BLUE[2], ORANGE[2] = RED[2], BLUE[2], ORANGE[2], GREEN[2]
    # ruoto il centro giallo in senso orario
    clockwiseRotation(WHITE)

def D1():
    global MOVES
    MOVES += 1
    
    GREEN[2], ORANGE[2], BLUE[2], RED[2] = ORANGE[2], BLUE[2], RED[2], GREEN[2]
    antiClockwiseRotation(WHITE)

def F():
    global MOVES
    MOVES += 1

    YELLOW[2][0], RED[2][2], WHITE[0][2], ORANGE[0][0] = RED[2][2], WHITE[0][2], ORANGE[0][0], YELLOW[2][0]
    YELLOW[2][1], RED[1][2], WHITE[0][1], ORANGE[1][0] = RED[1][2], WHITE[0][1], ORANGE[1][0], YELLOW[2][1]
    YELLOW[2][2], RED[0][2], WHITE[0][0], ORANGE[2][0] = RED[0][2], WHITE[0][0], ORANGE[2][0], YELLOW[2][2]
    # ruoto il centro verde in senso orario
    clockwiseRotation(GREEN)

def F1():
    global MOVES
    MOVES += 1
    
    YELLOW[2][0], ORANGE[0][0], WHITE[0][2], RED[2][2] = ORANGE[0][0], WHITE[0][2], RED[2][2], YELLOW[2][0]
    YELLOW[2][1], ORANGE[1][0], WHITE[0][1], RED[1][2] = ORANGE[1][0], WHITE[0][1], RED[1][2], YELLOW[2][1]
    YELLOW[2][2], ORANGE[2][0], WHITE[0][0], RED[0][2] = ORANGE[2][0], WHITE[0][0], RED[0][2], YELLOW[2][2]
    antiClockwiseRotation(GREEN)

def B():
    global MOVES
    MOVES += 1

    YELLOW[0][0], ORANGE[0][2], WHITE[2][2], RED[2][0] = ORANGE[0][2], WHITE[2][2], RED[2][0], YELLOW[0][0]
    YELLOW[0][1], ORANGE[1][2], WHITE[2][1], RED[1][0] = ORANGE[1][2], WHITE[2][1], RED[1][0], YELLOW[0][1]
    YELLOW[0][2], ORANGE[2][2], WHITE[2][0], RED[0][0] = ORANGE[2][2], WHITE[2][0], RED[0][0], YELLOW[0][2]
    # ruoto il centro verde in senso orario
    clockwiseRotation(BLUE)

def B1():
    global MOVES
    MOVES += 1
    
    YELLOW[0][0], RED[2][0], WHITE[2][2], ORANGE[0][2] = RED[2][0], WHITE[2][2], ORANGE[0][2], YELLOW[0][0]
    YELLOW[0][1], RED[1][0], WHITE[2][1], ORANGE[1][2] = RED[1][0], WHITE[2][1], ORANGE[1][2], YELLOW[0][1]
    YELLOW[0][2], RED[0][0], WHITE[2][0], ORANGE[2][2] = RED[0][0], WHITE[2][0], ORANGE[2][2], YELLOW[0][2]
    antiClockwiseRotation(BLUE)

def M():
    global MOVES
    MOVES += 1

    GREEN[0][1], YELLOW[0][1], BLUE[2][1], WHITE[0][1] = YELLOW[0][1], BLUE[2][1], WHITE[0][1], GREEN[0][1]
    GREEN[1][1], YELLOW[1][1], BLUE[1][1], WHITE[1][1] = YELLOW[1][1], BLUE[1][1], WHITE[1][1], GREEN[1][1]
    GREEN[2][1], YELLOW[2][1], BLUE[0][1], WHITE[2][1] = YELLOW[2][1], BLUE[0][1], WHITE[2][1], GREEN[2][1]

def M1():
    global MOVES
    MOVES += 1

    GREEN[0][1], WHITE[0][1], BLUE[2][1], YELLOW[0][1] = WHITE[0][1], BLUE[2][1], YELLOW[0][1], GREEN[0][1]
    GREEN[1][1], WHITE[1][1], BLUE[1][1], YELLOW[1][1] = WHITE[1][1], BLUE[1][1], YELLOW[1][1], GREEN[1][1]
    GREEN[2][1], WHITE[2][1], BLUE[0][1], YELLOW[2][1] = WHITE[2][1], BLUE[0][1], YELLOW[2][1], GREEN[2][1]

def E():
    global MOVES
    MOVES += 1

    GREEN[1], RED[1], BLUE[1], ORANGE[1] = RED[1], BLUE[1], ORANGE[1], GREEN[1]

def S():
    global MOVES
    MOVES += 1

    YELLOW[1][0], RED[2][1], WHITE[1][2], ORANGE[0][1] = RED[2][1], WHITE[1][2], ORANGE[0][1], YELLOW[1][0]
    YELLOW[1][1], RED[1][1], WHITE[1][1], ORANGE[1][1] = RED[1][1], WHITE[1][1], ORANGE[1][1], YELLOW[1][1]
    YELLOW[1][2], RED[0][1], WHITE[1][0], ORANGE[2][1] = RED[0][1], WHITE[1][0], ORANGE[2][1], YELLOW[1][2]

def S1():
    global MOVES
    MOVES += 1

    YELLOW[1][0], ORANGE[0][1], WHITE[1][2], RED[2][1] = ORANGE[0][1], WHITE[1][2], RED[2][1], YELLOW[1][0]
    YELLOW[1][1], ORANGE[1][1], WHITE[1][1], RED[1][1] = ORANGE[1][1], WHITE[1][1], RED[1][1], YELLOW[1][1]
    YELLOW[1][2], ORANGE[0][1], WHITE[1][0], RED[2][1] = ORANGE[0][1], WHITE[1][0], RED[2][1], YELLOW[1][2]

def r():
    global MOVES
    MOVES -= 1

    R(); M1()

def r1():
    global MOVES
    MOVES -= 1

    R1(); M()

def f():
    global MOVES
    MOVES -= 1

    F(); S()

def f1():
    global MOVES
    MOVES -= 1
    
    F1(); S1()

def d():
    global MOVES
    MOVES += 1
    
    GREEN[1], RED[1], BLUE[1], ORANGE[1] = RED[1], BLUE[1], ORANGE[1], GREEN[1]
    GREEN[2], RED[2], BLUE[2], ORANGE[2] = RED[2], BLUE[2], ORANGE[2], GREEN[2]
    clockwiseRotation(WHITE)

def d1():
    global MOVES
    MOVES += 1

    GREEN[1], ORANGE[1], BLUE[1], RED[1] = ORANGE[1], BLUE[1], RED[1], GREEN[1]
    GREEN[2], ORANGE[2], BLUE[2], RED[2] = ORANGE[2], BLUE[2], RED[2], GREEN[2]
    antiClockwiseRotation(WHITE)

def sexyMove(): R(); U(); R1(); U1()

def sexyRevMove(): U(); R(); U1(); R1()

def fromFrontToCross(): F(); D(); R1(); D1()

def moveOut(): R(); U(); R1()

def leftEdge(): U1(); L1(); U(); L(); F1(); L(); F(); L1()

def edgeBack(): R(); U1(); R1(); F(); R1(); F1(); R()

def TEST():
    global MOVES
    MOVES -= 22

    R(); U(); L(); L(); D(); F(); R(); B(); U(); L(); D(); R(); R(); U(); D(); F(); D(); R(); B(); B(); L(); F()

def solve():

    def PLL():
        # controllo che tutti gli angoli siano corretti
        while (not (GREEN[0][0] == GREEN[0][2] and ORANGE[0][0] == ORANGE[0][2] and BLUE[0][0] == BLUE[0][2] and RED[0][0] == RED[0][2])):
            if (RED[0][0] == RED[0][2] and RED[0][1] != RED[0][0] and (GREEN[0][0] != GREEN[0][2] or BLUE[0][0] != BLUE[0][2])):
                sexyMove(); R1(); F(); R(); R(); U1(); R1(); U1(); R(); U(); R1(); F1()
            elif (RED[0][0] == RED[0][1] == RED[0][2] and GREEN[0][0] == BLUE[0][1] and BLUE[0][2] == GREEN[0][1]):
                R1(); U1(); F1(); sexyMove(); R1(); F(); R(); R(); U1(); R1(); U1(); R(); U(); R1(); U(); R()
            elif (RED[0][0] == RED[0][1] == RED[0][2] and GREEN[0][1] == GREEN[0][2] == BLUE[0][0] and GREEN[0][0] == ORANGE[0][1] == ORANGE[0][2]):
                R(); U(); R1(); F1(); sexyMove(); R1(); F(); R(); R(); U1(); R1(); U1()
            elif (GREEN[0][0] == GREEN[1][0] and ORANGE[0][2] == ORANGE[1][2]):
                F(); R(); U1(); R1(); U1(); R(); U(); R1(); F1(); sexyMove(); R1(); F(); R(); F1()
            else: U()
        # è ora degli spigoli
        while (not (GREEN[0][0] == GREEN[0][1] == GREEN[0][2] and ORANGE[0][0] == ORANGE[0][1] == ORANGE[0][2]
                and BLUE[0][0] == BLUE[0][1] == BLUE[0][2] and RED[0][0] == RED[0][1] == RED[0][2])):
            if (BLUE[0][0] == BLUE[0][1] == BLUE[0][2] and GREEN[0][1] == ORANGE[0][0]):
                R(); U1(); R(); U(); R(); U(); R(); U1(); R1(); U1(); R1(); R1()
            elif (BLUE[0][0] == BLUE[0][1] == BLUE[0][2] and GREEN[0][1] == RED[0][0]):
                L1(); U(); L1(); U1(); L1(); U1(); L1(); U(); L(); U(); L(); L()
            elif (GREEN[0][1] == BLUE[0][0] and BLUE[0][1] == GREEN[0][0] and RED[0][1] == ORANGE[0][0]):
                M(); M(); U(); M(); M(); U(); U(); M(); M(); U(); M(); M()
            elif (GREEN[0][1] == ORANGE[0][0] and ORANGE[0][1] == GREEN[0][0] and RED[0][1] == BLUE[0][0]):
                M(); M(); U(); M(); M(); U(); M(); U(); U(); M(); M(); U(); U(); M()
            else: U()
        while (GREEN[0][1] != GREEN[1][1]): U()
        print("Cube solved correctly")

    def OLL(): # come lo farei io, ma "più peggio"
        # controllo che ci sia la croce gialla
        while (not (YELLOW[0][1] == YELLOW[1][0] == YELLOW[2][1] == YELLOW[1][2])):
            if (YELLOW[0][1] != YELLOW[1][1] and YELLOW[1][0] != YELLOW[1][1] and YELLOW[2][1] != YELLOW[1][1] and YELLOW[1][2] != YELLOW[1][1]):
                if (GREEN[0][1] == BLUE[0][1] == YELLOW[1][1] and ORANGE[0] == RED[0]):
                    R(); U1(); U1(); R1(); R1(); F(); R(); F1(); U(); U(); R1(); F(); R(); F1()
                elif (GREEN[0][1] == GREEN[0][2] == ORANGE[0][1] == BLUE[0][0] == BLUE[0][1] == RED[0][0] == RED[0][1] == RED[0][2]):
                    F(); sexyMove(); F1(); f(); sexyMove(); f1()
                elif (GREEN[0][1] == ORANGE[0][1] == BLUE[0][1] == RED[0][1] == YELLOW[0][0] == YELLOW[2][0] == YELLOW[2][2] == YELLOW[0][2]):
                    r(); U(); R1(); U1(); M1(); M1(); U(); R(); U1(); R1(); U1(); M1()
                else: F(); sexyMove(); sexyMove(); F1()
            elif (YELLOW[1][0] == YELLOW[1][1] == YELLOW[1][2]):
                F(); sexyMove(); F1()
            elif (YELLOW[1][0] == YELLOW[1][1] == YELLOW[0][1]):
                F(); sexyMove(); sexyMove(); F1()
            U()
        # completo l'OLL (la faccia gialla)
        while (not (YELLOW[0][0] == YELLOW[2][0] == YELLOW[2][2] == YELLOW[0][2])):
            if (GREEN[0][0] == GREEN[0][2] == BLUE[0][0] == BLUE[0][2] == YELLOW[1][1]):
                R(); U(); U(); R1(); U1(); sexyMove(); R(); U1(); R1()
            elif (GREEN[0][2] == BLUE[0][0] == RED[0][0] == RED[0][2]):
                R(); U(); U(); R(); R(); U1(); R(); R(); U1(); R1(); R1(); U1(); U1(); R()
            elif (BLUE[0][0] == BLUE[0][2] == YELLOW[1][1]):
                R(); R(); D1(); R(); U(); U(); R1(); D(); R(); U(); U(); R()
            elif (GREEN[0][0] == BLUE[0][2] == YELLOW[1][1]):
                r(); U(); R1(); U1(); r1(); F(); R(); F1()
            elif (GREEN[0][2] == RED[0][0] == YELLOW[1][1]):
                F1(); r(); U(); R1(); U1(); r1(); F(); R()
            elif (GREEN[0][2] == ORANGE[0][2] == BLUE[0][2] == YELLOW[1][1]):
                R(); U(); R1(); U(); R(); U1(); U1(); R1()
            elif (GREEN[0][0] == RED[0][0] == BLUE[0][0] == YELLOW[1][1]):
                L1(); U1(); L(); U1(); L1(); U(); U()
            else: U()
        PLL()

    def F2L(): # questo è l'F2L più brutto della storia :)
        # angoli
        while (not (WHITE[0] == WHITE[1] == WHITE[2] and GREEN[1] == GREEN[2] and ORANGE[1] == ORANGE[2] and BLUE[1] == BLUE[2] and RED[1] == RED[2])):
            if (YELLOW[2][2] == WHITE[1][1]):
                while (not (GREEN[0][2] == ORANGE[1][1] and ORANGE[0][0] == GREEN[1][1])): d()
            elif (GREEN[0][2] == WHITE[1][1]):
                while (not (ORANGE[0][0] == ORANGE[1][1] and YELLOW[2][2] == GREEN[1][1])): d()
            elif (ORANGE[0][0] == WHITE[1][1]):
                while (not (GREEN[0][2] == GREEN[1][1] and YELLOW[2][2] == ORANGE[1][1])): d()
            else:
                while (GREEN[1][1] == GREEN[1][2] == GREEN[2][1] == GREEN[2][2]
                       and ORANGE[1][0] == ORANGE[1][1] == ORANGE[2][0] == ORANGE[2][1]): d1()
            # F2L advanced
            if (WHITE[0][2] == WHITE[1][1] and GREEN[2][2] == GREEN[1][1] and ORANGE[2][0] == ORANGE[1][1]): # angolo corretto
                if (GREEN[1][2] == ORANGE[1][1] and ORANGE[1][0] == GREEN[1][1]):
                    R(); U1(); R1(); U(); F1(); U(); U(); F(); U1(); F(); R1(); F1(); R()
                elif ((YELLOW[0][1] == ORANGE[1][1] and BLUE[0][1] == GREEN[1][1]) or (YELLOW[1][0] == ORANGE[1][1] and RED[0][1] == GREEN[1][1])
                    or (YELLOW[2][1] == ORANGE[1][1] and GREEN[0][1] == GREEN[1][1]) or (YELLOW[1][2] == ORANGE[1][1] and ORANGE[0][1] == GREEN[1][1])):
                    while (RED[0][1] != GREEN[1][1] and YELLOW[1][0] != ORANGE[1][1]): U()
                    R(); U1(); R1(); F(); R1(); F1(); R()
                elif ((YELLOW[0][1] == GREEN[1][1] and BLUE[0][1] == ORANGE[1][1]) or (YELLOW[1][0] == GREEN[1][1] and RED[0][1] == ORANGE[1][1])
                    or (YELLOW[2][1] == GREEN[1][1] and GREEN[0][1] == ORANGE[1][1]) or (YELLOW[1][2] == GREEN[1][1] and ORANGE[0][1] == ORANGE[1][1])):
                    while (BLUE[0][1] != ORANGE[1][1] and YELLOW[0][1] != GREEN[1][1]): U()
                    F1(); U(); F(); R1(); F(); R(); F1()
                elif (GREEN[1][2] != YELLOW[1][1] and ORANGE[1][0] != YELLOW[1][1]):
                    while (YELLOW[1][0] != YELLOW[1][1] and RED[0][1] != YELLOW[1][1]): U()
                    R(); U1(); R1(); F(); R1(); F1(); R()
                else:
                    d1()
                    print("ciao")
            elif (GREEN[2][2] == WHITE[1][1] and ORANGE[2][0] == GREEN[1][1] and WHITE[0][2] == ORANGE[1][1]): # colori angolo giusti, ma bianco verso sinistra
                if (GREEN[1][2] == GREEN[1][1] and ORANGE[1][0] == ORANGE[1][1]): # F2L-4
                    sexyMove(); R(); U(); U(); R1(); U1(); R(); U(); R1()
                elif (GREEN[1][2] == ORANGE[1][1] and ORANGE[1][0] == GREEN[1][1]): # F2L-5
                    R(); F(); U(); R(); U1(); R1(); F1(); U1(); R1()
                elif (GREEN[0][1] == GREEN[1][1] and YELLOW[2][1] == ORANGE[1][1]): # F2L-6
                    F1(); U1(); F(); U(); F1(); U1(); F()
                elif (YELLOW[1][2] == GREEN[1][1] and ORANGE[0][1] == ORANGE[1][1]): # F2L-7
                    R(); U1(); R1(); U(); R(); U1(); R1()
                else:
                    sexyRevMove(); sexyRevMove()
                    if (GREEN[1][2] != YELLOW[1][1] and ORANGE[1][0] != YELLOW[1][1]):
                        while (not (YELLOW[2][1] == YELLOW[1][1]) and not (GREEN[0][1] == YELLOW[1][1])): U()
                        U(); R(); U1(); R1(); F(); R1(); F1(); R()
                        continue
            elif (ORANGE[2][0] == WHITE[1][1] and GREEN[2][2] == ORANGE[1][1] and WHITE[0][2] == GREEN[1][1]): # colori angolo giusti, ma bianco verso destra
                if (GREEN[1][2] == GREEN[1][1] and ORANGE[1][0] == ORANGE[1][1]): # F2L-8
                    R(); U1(); R1(); U(); R(); U1(); U1(); R1(); U(); R(); U1(); R1()
                elif (GREEN[1][2] == ORANGE[1][1] and ORANGE[1][0] == GREEN[1][1]): # F2L-9
                    R(); U(); F(); sexyMove(); F1(); R1()
                elif (GREEN[0][1] == GREEN[1][1] and YELLOW[2][1] == ORANGE[1][1]): # F2L-10
                    F1(); U(); F(); U1(); F1(); U(); F()
                elif (ORANGE[0][1] == ORANGE[1][1] and YELLOW[1][2] == GREEN[1][1]): # F2L-11
                    sexyMove(); R(); U(); R1()
                else:
                    sexyMove(); sexyMove()
                    if (GREEN[1][2] != YELLOW[1][1] and ORANGE[1][0] != YELLOW[1][1]):
                        while (not (YELLOW[2][1] == YELLOW[1][1]) and not (GREEN[0][1] == YELLOW[1][1])): U()
                        U(); R(); U1(); R1(); F(); R1(); F1(); R()
                        continue
            elif (GREEN[0][2] == WHITE[1][1] and YELLOW[2][2] == GREEN[1][1]): # angolo giusto, ma in alto e con bianco verso sinistra
                if (GREEN[1][2] == GREEN[1][1] and ORANGE[1][0] == ORANGE[1][1]): # F2L-12
                    U1(); R(); U1(); R1(); U(); U(); R(); U1(); R1()
                elif (GREEN[1][2] == ORANGE[1][1] and ORANGE[1][0] == GREEN[1][1]): # F2L-13
                    U1(); R(); U(); R1(); U(); F1(); U1(); F()
                elif (YELLOW[1][0] == ORANGE[1][1] and RED[0][1] == GREEN[1][1]): # F2L-14
                    F1(); U1(); F()
                elif (YELLOW[1][2] == GREEN[1][1] and ORANGE[0][1] == ORANGE[1][1]): # F2L-15
                    R1(); F(); R(); F1()
                elif (YELLOW[0][1] == GREEN[1][1] and BLUE[0][1] == ORANGE[1][1]): # F2L-16
                    U1(); R(); U(); R1(); U(); R1(); F(); R(); F1()
                elif (YELLOW[2][1] == GREEN[1][1] and GREEN[0][1] == ORANGE[1][1]): # F2L-17
                    U(); F1(); U(); F(); U1(); U1(); R(); U(); U(); R1(); U(); R1(); F(); R(); F1()
                elif (YELLOW[1][0] == ORANGE[1][1] and RED[0][1] == GREEN[1][1]): # F2L-18
                    F1(); U1(); F()
                elif (YELLOW[2][1] == ORANGE[1][1] and GREEN[0][1] == GREEN[1][1]): # F2L-29
                    U(); F1(); U(); F(); U1(); F1(); U1(); F()
                elif (YELLOW[0][1] == ORANGE[1][1] and BLUE[0][1] == GREEN[1][1]): # F2L-20
                    U1(); R(); U1(); R1(); U(); F1(); U1(); F()
                elif (YELLOW[1][2] == ORANGE[1][1] and ORANGE[0][1] == GREEN[1][1]): # F2L-21
                    U1(); R(); U(); U(); R1(); U(); F1(); U1(); F()
                else:
                    sexyRevMove()
                    if (GREEN[1][2] != YELLOW[1][1] and ORANGE[1][0] != YELLOW[1][1]):
                        while (not (YELLOW[2][1] == YELLOW[1][1]) and not (GREEN[0][1] == YELLOW[1][1])): U()
                        U(); R(); U1(); R1(); F(); R1(); F1(); R()
                        continue
            elif (ORANGE[0][0] == WHITE[1][1] and YELLOW[2][2] == ORANGE[1][1]): # angolo giusto, ma in alto e con bianco verso destra
                if (GREEN[1][2] == GREEN[1][1] and ORANGE[1][0] == ORANGE[1][1]): # F2L-22
                    U1(); R(); U1(); U1(); R1(); U(); R(); U(); R1()
                elif (GREEN[1][2] == ORANGE[1][1] and ORANGE[1][0] == GREEN[1][1]): # F2L-23
                    U(); F1(); U1(); F(); U1(); R(); U(); R1()
                elif (YELLOW[2][1] == ORANGE[1][1] and GREEN[0][1] == GREEN[1][1]): # F2L-24
                    F(); R1(); F1(); R()
                elif (YELLOW[1][0] == ORANGE[1][1] and RED[0][1] == GREEN[1][1]): # F2L-25
                    U(); F1(); U1(); F(); U1(); F(); R1(); F1(); R()
                elif (YELLOW[0][1] == ORANGE[1][1] and BLUE[0][1] == GREEN[1][1]): # F2L-26
                    U(); F1(); U1(); U1(); F(); U1(); F(); R1(); F1(); R()
                elif (YELLOW[1][2] == ORANGE[1][1] and ORANGE[0][1] == GREEN[1][1]): # F2L-27
                    U1(); R(); U1(); U1(); R1(); U(); U(); F1(); U1(); F(); U1(); F(); R1(); F1(); R()
                elif (YELLOW[0][1] == GREEN[1][1] and BLUE[0][1] == ORANGE[1][1]): # F2L-28
                    R(); U(); R1()
                elif (YELLOW[1][0] == GREEN[1][1] and RED[0][1] == ORANGE[1][1]): # F2L-29
                    U(); F1(); U(); F(); U1(); R(); U(); R1()
                elif (YELLOW[1][2] == GREEN[1][1] and ORANGE[0][1] == ORANGE[1][1]): # F2L-30
                    U1(); R(); U1(); R1(); U(); R(); U(); R1()
                elif (YELLOW[2][1] == GREEN[1][1] and GREEN[0][1] == ORANGE[1][1]): # F2L-31
                    U(); F1(); U(); U(); F(); U1(); R(); U(); R1()
                else:
                    sexyMove()
                    if (GREEN[1][2] != YELLOW[1][1] and ORANGE[1][0] != YELLOW[1][1]):
                        while (not (YELLOW[2][1] == YELLOW[1][1]) and not (GREEN[0][1] == YELLOW[1][1])): U()
                        U(); R(); U1(); R1(); F(); R1(); F1(); R()
                        continue
            elif (YELLOW[2][2] == WHITE[1][1] and ORANGE[0][0] == GREEN[1][1] and GREEN[0][2] == ORANGE[1][1]): # angolo giusto, ma in alto e con bianco verso l'alto
                if (GREEN[1][2] == GREEN[1][1] and ORANGE[1][0] == ORANGE[1][1]): # F2L-32
                    sexyMove(); sexyMove(); sexyMove()
                elif (GREEN[1][2] == ORANGE[1][1] and ORANGE[1][0] == GREEN[1][1]): # F2L-33
                    R(); U1(); R1(); U(); F1(); U(); F()
                elif (YELLOW[0][1] == GREEN[1][1] and BLUE[0][1] == ORANGE[1][1]): # F2L-34
                    U(); R(); U(); U(); R1(); U(); R(); U1(); R1()
                elif (YELLOW[1][0] == GREEN[1][1] and RED[0][1] == ORANGE[1][1]): # F2L-35
                    U(); U(); R(); U(); R1(); R1(); F(); R(); F1()
                elif (YELLOW[2][1] == GREEN[1][1] and GREEN[0][1] == ORANGE[1][1]): # F2L-36
                    U(); F1(); U(); U(); F(); R(); U(); U(); R1(); U(); R(); U1(); R1()
                elif (YELLOW[1][2] == GREEN[1][1] and ORANGE[0][1] == ORANGE[1][1]): # F2L-37
                    U1(); R(); U(); U(); R1(); U1(); R(); U(); R1(); U(); R(); U1(); R1()
                elif (YELLOW[0][1] == ORANGE[1][1] and BLUE[0][1] == GREEN[1][1]): #F2L-38
                    U(); U(); F1(); U1(); F(); F(); R1(); F1(); R()
                elif (YELLOW[1][0] == ORANGE[1][1] and RED[0][1] == GREEN[1][1]): # F2L-39
                    U1(); F1(); U(); U(); F(); F(); R1(); F1(); R()
                elif (YELLOW[1][2] == ORANGE[1][1] and ORANGE[0][1] == GREEN[1][1]): # F2L-40
                    U1(); R(); U1(); R1(); U1(); F1(); U1(); F(); F(); R1(); F1(); R()
                elif (YELLOW[2][1] == ORANGE[1][1] and GREEN[0][1] == GREEN[1][1]): # F2L-41
                    U(); F1(); U(); U(); F(); U(); F1(); U1(); F(); F(); R1(); F1(); R()
                else:
                    sexyMove(); sexyMove(); sexyMove()
                    if (GREEN[1][2] != YELLOW[1][1] and ORANGE[1][0] != YELLOW[1][1]):
                        while (not (YELLOW[2][1] == YELLOW[1][1]) and not (GREEN[0][1] == YELLOW[1][1])): U()
                        U(); R(); U1(); R1(); F(); R1(); F1(); R()
                        continue
            elif ((WHITE[0][2] == WHITE[1][1] and GREEN[2][2] != GREEN[1][1]) or (GREEN[2][2] == WHITE[1][1] and ORANGE[2][0] != GREEN[1][1])
                  or (ORANGE[2][0] == WHITE[1][1] and WHITE[0][2] != ORANGE[1][1])): # angolo è inserito, ma colori sbagliati
                R(); U(); R1()
            else:
                c = 0
                for c in range(5):
                    U()
                    if (GREEN[0][2] == WHITE[1][1] or ORANGE[0][0] == WHITE[1][1] or YELLOW[2][2] == WHITE[1][1]):
                        break
                if (c == 4): d1()

        OLL()

    def cross():
        while (WHITE[0][1] != WHITE[1][1] or WHITE[1][0] != WHITE[1][1] or WHITE[1][2] != WHITE[1][1] or WHITE[2][1] != WHITE[1][1]):
            if (GREEN[1][2] == WHITE[1][1] or YELLOW[1][2] == WHITE[1][1] or BLUE[1][0] == WHITE[1][1]):
                while (WHITE[1][2] == WHITE[1][1]): D()
                while (WHITE[1][2] != WHITE[1][1]): R()
            elif (GREEN[1][0] == WHITE[1][1] or YELLOW[1][0] == WHITE[1][1] or BLUE[1][2] == WHITE[1][1]):
                while (WHITE[1][0] == WHITE[1][1]): D()
                while (WHITE[1][0] != WHITE[1][1]): L()
            elif (RED[1][0] == WHITE[1][1] or YELLOW[0][1] == WHITE[1][1] or ORANGE[1][2] == WHITE[1][1]):
                while (WHITE[2][1] == WHITE[1][1]): D()
                while (WHITE[2][1] != WHITE[1][1]): B()
            elif (RED[1][2] == WHITE[1][1] or YELLOW[2][1] == WHITE[1][1] or ORANGE[1][0] == WHITE[1][1]):
                while (WHITE[0][1] == WHITE[1][1]): D()
                while (WHITE[0][1] != WHITE[1][1]): F()
            elif (GREEN[0][1] == WHITE[1][1] or RED[0][1] == WHITE[1][1] or BLUE[0][1] == WHITE[1][1] or ORANGE[0][1] == WHITE[1][1]):
                while (GREEN[0][1] != WHITE[1][1]): U()
                while (WHITE[0][1] == WHITE[1][1]): D()
                fromFrontToCross()
            elif (GREEN[2][1] == WHITE[1][1] or RED[2][1] == WHITE[1][1] or BLUE[2][1] == WHITE[1][1] or ORANGE[2][1] == WHITE[1][1]):
                while (GREEN[2][1] != WHITE[1][1]): D()
                while (GREEN[0][1] != WHITE[1][1]): F()
                fromFrontToCross()
            elif (GREEN[1][0] == WHITE[1][1] or GREEN[1][2] == WHITE[1][1] or RED[1][0] == WHITE[1][1] or RED[1][2] == WHITE[1][1]
                or BLUE[1][0] == WHITE[1][1] or BLUE[1][2] == WHITE[1][1] or ORANGE[1][0] == WHITE[1][1] or ORANGE[1][2] == WHITE[1][1]):
                while (GREEN[1][0] != WHITE[1][1] and GREEN[1][2] != WHITE[1][1]): E()
                while (WHITE[0][1] == WHITE[1][1]): D()
                while (GREEN[0][1] != WHITE[1][1]): F()
                fromFrontToCross()
                while (GREEN[1][1] != green): E()
                while (GREEN[2][1] != green): D()
            else: pass
        # controllo che la croce sia giusta
        cs = [green, orange, blue, red]
        while (GREEN[2][1] != GREEN[1][1] or RED[2][1] != RED[1][1] or BLUE[2][1] != BLUE[1][1] or ORANGE[2][1] != ORANGE[1][1]):
            if (cs.index(GREEN[2][1]) - cs.index(BLUE[2][1]) == -2
                and cs.index(RED[2][1]) - cs.index(ORANGE[2][1]) == -2): # entrambi opposti
                D(); D()
            elif (cs.index(GREEN[2][1]) - cs.index(BLUE[2][1]) == -2
                or cs.index(RED[2][1]) - cs.index(ORANGE[2][1]) == -2): # uno opposto
                F(); F(); U(); U(); B(); B(); U(); U(); F(); F()
                while (GREEN[2][1] != GREEN[1][1]): D()
            elif ((cs.index(GREEN[2][1]) - cs.index(ORANGE[2][1]) == 1 or cs.index(GREEN[2][1]) - cs.index(ORANGE[2][1]) == -3)
                  and (cs.index(BLUE[2][1]) - cs.index(RED[2][1]) == -1 or cs.index(BLUE[2][1]) - cs.index(RED[2][1]) == 3)): # close swap
                F(); F(); U1(); R(); R(); U(); F(); F()
                while (GREEN[2][1] != GREEN[1][1]): D()
            else: D()
        F2L()
    cross()

OPTIONS = Options()
OPTIONS.add_argument('--kiosk-printing')
OPTIONS.add_argument('--incognito')
OPTIONS.add_argument('--disable-extensions')
OPTIONS.add_argument('--profile-directory=Default')
OPTIONS.add_argument("--disable-plugins-discovery")

def scramble():
    global MOVES
    driver = webdriver.Chrome(executable_path = r"C:\Users\aless\OneDrive\Python\ProjectZ\chromedriver.exe", options = OPTIONS)
    wait = WebDriverWait(driver, 5)

    driver.get("https://ruwix.com/puzzle-scramble-generator/")
    driver.minimize_window()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]')))
    driver.find_element(By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]').click()
    wait.until(EC.element_to_be_clickable((By.ID, "scramblebutton")))
    driver.find_element(By.ID, "scramblebutton")
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tobbscrmble"]/div[1]/div[3]')))
    st = driver.find_element(By.XPATH, '//*[@id="tobbscrmble"]/div[1]/div[3]').text
    driver.close()
    moves = ""
    for i in range(len(st)):
        if (st[i] == "2"): moves += f" {st[i - 1]}"
        elif (st[i] == "'"): moves += "1"
        else: moves += st[i]
    moves = moves.split()
    #moves = 
    print(moves)
    for i in moves:
        globals()[i]()
        MOVES -= 1

green, red, blue, white, yellow, orange = "green", "red", "blue", "white", "yellow", "orange"

GREEN = [
    [green, green, green],
    [green, green, green],
    [green, green, green]
]
RED = [
    [red, red, red],
    [red, red, red],
    [red, red, red]
]
BLUE = [
    [blue, blue, blue],
    [blue, blue, blue],
    [blue, blue, blue]
]
WHITE = [
    [white, white, white],
    [white, white, white],
    [white, white, white]
]
YELLOW = [
    [yellow, yellow, yellow],
    [yellow, yellow, yellow],
    [yellow, yellow, yellow]
]
ORANGE = [
    [orange, orange, orange],
    [orange, orange, orange],
    [orange, orange, orange]
]

CUBE = [GREEN, ORANGE, BLUE, RED, YELLOW, WHITE]

def test():
    global MOVES

    a = ['R', 'R', 'U', 'U', 'R', 'L1', 'D', 'B', 'B', 'D', 'U1', 'R', 'R', 'B1', 'U', 'U', 'R', 'F', 'R', 'R', 'D', 'D', 'L', 'L', 'B', 'B', 'U', 'F', 'F', 'D', 'D', 'F1', 'L', 'L', 'U1', 'F', 'B']
    for i in a:
        globals()[i]()
        MOVES -= 1

for _ in range(10):
    #scramble()
    test()
    solve()
    for face in CUBE:
        print(face)
    print(MOVES)
