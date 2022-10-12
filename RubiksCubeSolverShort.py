# by Aldisti

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

def sexyMove(): R(); U(); R1(); U1()

def sexyRevMove(): U(); R(); U1(); R1()

def fromFrontToCross(): F(); D(); R1(); D1()

def moveOut(): R(); U(); R1()

def rightEdge(): U(); R(); U1(); R1(); F(); R1(); F1(); R()

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
            if (RED[0][0] == RED[0][2] != RED[0][1] and GREEN[0][0] != GREEN[0][2] and ORANGE[0][0] != ORANGE[0][2]):
                sexyMove(); R1(); F(); R(); R(); U1(); R1(); U1(); R(); U(); R1(); F1()
            elif (RED[0][0] == RED[0][1] == RED[0][2] and GREEN[0][1] == BLUE[1][1] and BLUE[0][1] == GREEN[1][1]):
                R1(); U1(); F1(); sexyMove(); R1(); F(); R(); R(); U1(); R1(); U1(); R(); U(); R1(); U(); R()
            elif (GREEN[0][0] == GREEN[1][1] != GREEN[0][2] and ORANGE[0][2] == ORANGE[1][1] != ORANGE[0][0] and BLUE[0][0] == BLUE[1][1] != BLUE[0][2] and RED[0][2] == RED[1][1] != RED[0][0]):
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
        print("Cube solved correctly\n")

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
        while (not (WHITE[0] == WHITE[1] == WHITE[2] and GREEN[2][0] == GREEN[2][1] == GREEN[2][2])):
            while (GREEN[2][2] == GREEN[2][1] and ORANGE[2][0] == ORANGE[2][1] and WHITE[0][2] == WHITE[1][1]): D()
            if (ORANGE[0][0] == WHITE[1][1]):
                while (not (GREEN[0][2] == GREEN[2][1] and YELLOW[2][2] == ORANGE[2][1])): D()
                sexyMove();
            elif (YELLOW[2][2] == WHITE[1][1]):
                while (not (GREEN[0][2] == ORANGE[2][1] and ORANGE[0][0] == GREEN[2][1])): D()
                sexyMove(); sexyMove(); sexyMove();
            elif (GREEN[0][2] == WHITE[1][1]):
                while (not (ORANGE[0][0] == ORANGE[2][1] and YELLOW[2][2] == GREEN[2][1])): D()
                sexyRevMove()
            elif ((WHITE[0][2] == WHITE[1][1] or GREEN[2][2] == WHITE[1][1] or ORANGE[2][0] == WHITE[1][1])
                 and (GREEN[2][2] != GREEN[2][1] or ORANGE[2][0] != ORANGE[2][1])): moveOut()
            else: U()
        while (GREEN[2][1] != GREEN[1][1]): D()
        # spigoli
        while (not (GREEN[1][0] == GREEN[1][1] == GREEN[1][2] and ORANGE[1][0] == ORANGE[1][1] == ORANGE[1][2] 
                and BLUE[1][0] == BLUE[1][1] == BLUE[1][2] and RED[1][0] == RED[1][1] == RED[1][2])):
            for __ in range(4):
                if (GREEN[0][1] == GREEN[1][1] and YELLOW[2][1] != YELLOW[1][1]):
                    if (YELLOW[2][1] == ORANGE[1][1]): rightEdge()
                    elif (YELLOW[2][1] == RED[1][1]): leftEdge()
                    break
                if ((GREEN[1][2] != GREEN[1][1] or ORANGE[1][0] != ORANGE[1][1]) and GREEN[1][2] != YELLOW[1][1] and ORANGE[1][0] != YELLOW[1][1]):
                    edgeBack()
                U()
            E()
        OLL()

    def checkCross():
        colors = [green, red, blue, orange]
        while (GREEN[2][1] != GREEN[1][1] or RED[2][1] != RED[1][1] or BLUE[2][1] != BLUE[1][1] or ORANGE[2][1] != ORANGE[1][1]):
            if (GREEN[2][1] == BLUE[1][1] and BLUE[2][1] == GREEN[1][1] and RED[2][1] == ORANGE[1][1]):
                D(); D()
            elif (GREEN[2][1] == BLUE[1][1] and BLUE[2][1] == GREEN[1][1] and RED[2][1] == RED[1][1]):
                F(); F(); U(); U(); B(); B(); U(); U(); F1(); F1()
            elif (GREEN[2][1] == RED[1][1] and RED[2][1] == GREEN[1][1]):
                F(); F(); U(); L(); L(); U1(); F1(); F1()
            else:
                D()
        F2L()

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
        checkCross()
    cross()

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



TEST()
solve()
for face in CUBE:
    print(face)
print(MOVES)
