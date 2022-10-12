# by Aldisti

def clockwiseRotation(mat):
    mat[0][0], mat[2][0], mat[2][2], mat[0][2] = mat[2][0], mat[2][2], mat[0][2], mat[0][0]
    mat[1][0], mat[2][1], mat[1][2], mat[0][1] = mat[2][1], mat[1][2], mat[0][1], mat[1][0]

def antiClockwiseRotation(mat):
    mat[0][0], mat[0][2], mat[2][2], mat[2][0] = mat[0][2], mat[2][2], mat[2][0], mat[0][0]
    mat[0][1], mat[1][2], mat[2][1], mat[1][0] = mat[1][2], mat[2][1], mat[1][0], mat[0][1]

def R():
    global MOVES
    MOVES.append("R")

    GREEN[0][2], WHITE[0][2], BLUE[2][0], YELLOW[0][2] = WHITE[0][2], BLUE[2][0], YELLOW[0][2], GREEN[0][2]
    GREEN[1][2], WHITE[1][2], BLUE[1][0], YELLOW[1][2] = WHITE[1][2], BLUE[1][0], YELLOW[1][2], GREEN[1][2]
    GREEN[2][2], WHITE[2][2], BLUE[0][0], YELLOW[2][2] = WHITE[2][2], BLUE[0][0], YELLOW[2][2], GREEN[2][2]
    clockwiseRotation(ORANGE)

def R1():
    global MOVES
    MOVES.append("R'")

    GREEN[0][2], YELLOW[0][2], BLUE[2][0], WHITE[0][2] = YELLOW[0][2], BLUE[2][0], WHITE[0][2], GREEN[0][2]
    GREEN[1][2], YELLOW[1][2], BLUE[1][0], WHITE[1][2] = YELLOW[1][2], BLUE[1][0], WHITE[1][2], GREEN[1][2]
    GREEN[2][2], YELLOW[2][2], BLUE[0][0], WHITE[2][2] = YELLOW[2][2], BLUE[0][0], WHITE[2][2], GREEN[2][2]
    antiClockwiseRotation(ORANGE)

def L():
    global MOVES
    MOVES.append("L")

    GREEN[0][0], YELLOW[0][0], BLUE[2][2], WHITE[0][0] = YELLOW[0][0], BLUE[2][2], WHITE[0][0], GREEN[0][0]
    GREEN[1][0], YELLOW[1][0], BLUE[1][2], WHITE[1][0] = YELLOW[1][0], BLUE[1][2], WHITE[1][0], GREEN[1][0]
    GREEN[2][0], YELLOW[2][0], BLUE[0][2], WHITE[2][0] = YELLOW[2][0], BLUE[0][2], WHITE[2][0], GREEN[2][0]
    # ruoto il centro rosso in senso orario
    clockwiseRotation(RED)

def L1():
    global MOVES
    MOVES.append("L'")
    
    GREEN[0][0], WHITE[0][0], BLUE[2][2], YELLOW[0][0] = WHITE[0][0], BLUE[2][2], YELLOW[0][0], GREEN[0][0]
    GREEN[1][0], WHITE[1][0], BLUE[1][2], YELLOW[1][0] = WHITE[1][0], BLUE[1][2], YELLOW[1][0], GREEN[1][0]
    GREEN[2][0], WHITE[2][0], BLUE[0][2], YELLOW[2][0] = WHITE[2][0], BLUE[0][2], YELLOW[2][0], GREEN[2][0]
    antiClockwiseRotation(RED)

def U():
    global MOVES
    MOVES.append("U")

    GREEN[0], ORANGE[0], BLUE[0], RED[0] = ORANGE[0], BLUE[0], RED[0], GREEN[0]
    # ruoto il centro bianco in senso orario
    clockwiseRotation(YELLOW)

def U1():
    global MOVES
    MOVES.append("U'")
    
    GREEN[0], RED[0], BLUE[0], ORANGE[0] = RED[0], BLUE[0], ORANGE[0], GREEN[0]
    antiClockwiseRotation(YELLOW)

def D():
    global MOVES
    MOVES.append("D")

    GREEN[2], RED[2], BLUE[2], ORANGE[2] = RED[2], BLUE[2], ORANGE[2], GREEN[2]
    # ruoto il centro giallo in senso orario
    clockwiseRotation(WHITE)

def D1():
    global MOVES
    MOVES.append("D'")
    
    GREEN[2], ORANGE[2], BLUE[2], RED[2] = ORANGE[2], BLUE[2], RED[2], GREEN[2]
    antiClockwiseRotation(WHITE)

def F():
    global MOVES
    MOVES.append("F")

    YELLOW[2][0], RED[2][2], WHITE[0][2], ORANGE[0][0] = RED[2][2], WHITE[0][2], ORANGE[0][0], YELLOW[2][0]
    YELLOW[2][1], RED[1][2], WHITE[0][1], ORANGE[1][0] = RED[1][2], WHITE[0][1], ORANGE[1][0], YELLOW[2][1]
    YELLOW[2][2], RED[0][2], WHITE[0][0], ORANGE[2][0] = RED[0][2], WHITE[0][0], ORANGE[2][0], YELLOW[2][2]
    # ruoto il centro verde in senso orario
    clockwiseRotation(GREEN)

def F1():
    global MOVES
    MOVES.append("F'")
    
    YELLOW[2][0], ORANGE[0][0], WHITE[0][2], RED[2][2] = ORANGE[0][0], WHITE[0][2], RED[2][2], YELLOW[2][0]
    YELLOW[2][1], ORANGE[1][0], WHITE[0][1], RED[1][2] = ORANGE[1][0], WHITE[0][1], RED[1][2], YELLOW[2][1]
    YELLOW[2][2], ORANGE[2][0], WHITE[0][0], RED[0][2] = ORANGE[2][0], WHITE[0][0], RED[0][2], YELLOW[2][2]
    antiClockwiseRotation(GREEN)

def B():
    global MOVES
    MOVES.append("B")

    YELLOW[0][0], ORANGE[0][2], WHITE[2][2], RED[2][0] = ORANGE[0][2], WHITE[2][2], RED[2][0], YELLOW[0][0]
    YELLOW[0][1], ORANGE[1][2], WHITE[2][1], RED[1][0] = ORANGE[1][2], WHITE[2][1], RED[1][0], YELLOW[0][1]
    YELLOW[0][2], ORANGE[2][2], WHITE[2][0], RED[0][0] = ORANGE[2][2], WHITE[2][0], RED[0][0], YELLOW[0][2]
    # ruoto il centro verde in senso orario
    clockwiseRotation(BLUE)

def B1():
    global MOVES
    MOVES.append("B'")
    
    YELLOW[0][0], RED[2][0], WHITE[2][2], ORANGE[0][2] = RED[2][0], WHITE[2][2], ORANGE[0][2], YELLOW[0][0]
    YELLOW[0][1], RED[1][0], WHITE[2][1], ORANGE[1][2] = RED[1][0], WHITE[2][1], ORANGE[1][2], YELLOW[0][1]
    YELLOW[0][2], RED[0][0], WHITE[2][0], ORANGE[2][2] = RED[0][0], WHITE[2][0], ORANGE[2][2], YELLOW[0][2]
    antiClockwiseRotation(BLUE)

def M():
    global MOVES
    MOVES.append("M")

    GREEN[0][1], YELLOW[0][1], BLUE[2][1], WHITE[0][1] = YELLOW[0][1], BLUE[2][1], WHITE[0][1], GREEN[0][1]
    GREEN[1][1], YELLOW[1][1], BLUE[1][1], WHITE[1][1] = YELLOW[1][1], BLUE[1][1], WHITE[1][1], GREEN[1][1]
    GREEN[2][1], YELLOW[2][1], BLUE[0][1], WHITE[2][1] = YELLOW[2][1], BLUE[0][1], WHITE[2][1], GREEN[2][1]

def M1():
    global MOVES
    MOVES.append("M'")

    GREEN[0][1], WHITE[0][1], BLUE[2][1], YELLOW[0][1] = WHITE[0][1], BLUE[2][1], YELLOW[0][1], GREEN[0][1]
    GREEN[1][1], WHITE[1][1], BLUE[1][1], YELLOW[1][1] = WHITE[1][1], BLUE[1][1], YELLOW[1][1], GREEN[1][1]
    GREEN[2][1], WHITE[2][1], BLUE[0][1], YELLOW[2][1] = WHITE[2][1], BLUE[0][1], YELLOW[2][1], GREEN[2][1]

def E():
    global MOVES
    MOVES.append("E")

    GREEN[1], RED[1], BLUE[1], ORANGE[1] = RED[1], BLUE[1], ORANGE[1], GREEN[1]

def E1():
    global MOVES
    MOVES.append("E'")

    GREEN[1], ORANGE[1], BLUE[1], RED[1] = ORANGE[1], BLUE[1], RED[1], GREEN[1]

def S():
    global MOVES
    MOVES.append("S")

    YELLOW[1][0], RED[2][1], WHITE[1][2], ORANGE[0][1] = RED[2][1], WHITE[1][2], ORANGE[0][1], YELLOW[1][0]
    YELLOW[1][1], RED[1][1], WHITE[1][1], ORANGE[1][1] = RED[1][1], WHITE[1][1], ORANGE[1][1], YELLOW[1][1]
    YELLOW[1][2], RED[0][1], WHITE[1][0], ORANGE[2][1] = RED[0][1], WHITE[1][0], ORANGE[2][1], YELLOW[1][2]

def S1():
    global MOVES
    MOVES.append("S'")

    YELLOW[1][0], ORANGE[0][1], WHITE[1][2], RED[2][1] = ORANGE[0][1], WHITE[1][2], RED[2][1], YELLOW[1][0]
    YELLOW[1][1], ORANGE[1][1], WHITE[1][1], RED[1][1] = ORANGE[1][1], WHITE[1][1], RED[1][1], YELLOW[1][1]
    YELLOW[1][2], ORANGE[2][1], WHITE[1][0], RED[0][1] = ORANGE[2][1], WHITE[1][0], RED[0][1], YELLOW[1][2]

def r():
    global MOVES
    MOVES.append("r")

    R(); M1()
    
    MOVES.pop(-1)
    MOVES.pop(-1)

def r1():
    global MOVES
    MOVES.append("r'")

    R1(); M()
    
    MOVES.pop(-1)
    MOVES.pop(-1)

def f():
    global MOVES
    MOVES.append("f")

    F(); S()
    
    MOVES.pop(-1)
    MOVES.pop(-1)

def f1():
    global MOVES
    MOVES.append("f'")
    
    F1(); S1()
    
    MOVES.pop(-1)
    MOVES.pop(-1)

def d():
    global MOVES
    MOVES.append("d")
    
    GREEN[1], RED[1], BLUE[1], ORANGE[1] = RED[1], BLUE[1], ORANGE[1], GREEN[1]
    GREEN[2], RED[2], BLUE[2], ORANGE[2] = RED[2], BLUE[2], ORANGE[2], GREEN[2]
    clockwiseRotation(WHITE)

def d1():
    global MOVES
    MOVES.append("d'")

    GREEN[1], ORANGE[1], BLUE[1], RED[1] = ORANGE[1], BLUE[1], RED[1], GREEN[1]
    GREEN[2], ORANGE[2], BLUE[2], RED[2] = ORANGE[2], BLUE[2], RED[2], GREEN[2]
    antiClockwiseRotation(WHITE)

def sexyMove():
    R(); U(); R1(); U1()

def sexyRevMove():
    U(); R(); U1(); R1()

def fromFrontToCross():
    F(); D(); R1(); D1()

def solve():
    global MOVES
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
            else:
                if (RED[0][0] == RED[0][2] and ORANGE[0][0] != ORANGE[0][2]):
                    sexyMove(); R1(); F(); R(); R(); U1(); R1(); U1(); R(); U(); R1(); F1()
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
        #print("Cube solved correctly")

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
                else: F(); sexyMove(); sexyMove(); F1(); U(); F(); sexyMove(); F1()
            elif (YELLOW[1][0] == YELLOW[1][1] == YELLOW[1][2]):
                F(); sexyMove(); F1()
            elif (YELLOW[1][0] == YELLOW[1][1] == YELLOW[0][1]):
                F(); sexyMove(); sexyMove(); F1()
            else: U()
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
                L1(); U1(); L(); U1(); L1(); U(); U(); L()
            else: U()
        PLL()

    def F2L(): # questo è l'F2L più brutto della storia :)
        # angoli
        while (not (WHITE[0] == WHITE[1] == WHITE[2] and GREEN[2][0] == GREEN[2][1] == GREEN[2][2]and ORANGE[2][0] == ORANGE[2][1] == ORANGE[2][2] and BLUE[2][0] == BLUE[2][1] == BLUE[2][2])):
            while (GREEN[2][2] == GREEN[2][1] and ORANGE[2][0] == ORANGE[2][1]): D()
            if (GREEN[0][2] == WHITE[1][1]):
                while (ORANGE[0][0] != ORANGE[2][1] and YELLOW[2][2] != GREEN[2][1]): D()
                sexyRevMove()
            elif (ORANGE[0][0] == WHITE[1][1]):
                while (GREEN[0][2] != GREEN[2][1] and YELLOW[2][2] != ORANGE[2][1]): D()
                sexyMove()
            elif (YELLOW[2][2] == WHITE[1][1]):
                while (GREEN[0][2] != ORANGE[2][1] and ORANGE[0][0] != GREEN[2][1]): D()
                sexyMove(); sexyMove(); sexyMove()
            else:
                while (GREEN[0][2] != YELLOW[1][1] and ORANGE[0][0] != YELLOW[1][1] and YELLOW[2][2] != YELLOW[1][1]): U()
                if (WHITE[0][2] == WHITE[1][1] or GREEN[2][2] == WHITE[1][1] or ORANGE[2][0] == WHITE[1][1]):
                    R(); U(); R1()
                U()
        while (GREEN[2][1] != GREEN[1][1]): D()
        # spigoli
        while (not (GREEN[1][0] == GREEN[1][1] == GREEN[1][2] and ORANGE[1][0] == ORANGE[1][1] == ORANGE[1][2] and BLUE[1][0] == BLUE[1][1] == BLUE[1][2] and RED[1][0] == RED[1][1] == RED[1][2])):
            if (GREEN[1][2] == GREEN[1][1] and ORANGE[1][0] == ORANGE[1][1]): E()
            if (GREEN[0][1] != YELLOW[1][1] and YELLOW[2][1] != YELLOW[1][1]):
                while (GREEN[0][1] != GREEN[1][1]): E()
                if (YELLOW[2][1] == ORANGE[1][1]):
                    U(); R(); U1(); R1(); F(); R1(); F1(); R()
                elif (YELLOW[2][1] == RED[1][1]):
                    U1(); L1(); U(); L(); F1(); L(); F(); L1()
            elif (GREEN[1][2] == ORANGE[1][1] and ORANGE[1][0] == GREEN[1][1]):
                R(); U1(); R1(); U(); F1(); U(); U(); F(); U1(); F(); R1(); F1(); R()
            elif ((GREEN[1][2] != GREEN[1][1] or ORANGE[1][0] != ORANGE[1][1]) and (GREEN[1][2] != YELLOW[1][1] and ORANGE[1][0] != YELLOW[1][1])):
                while (RED[0][1] != YELLOW[1][1] and YELLOW[1][0] != YELLOW[1][1]): U()
                R(); U1(); R1(); F(); R1(); F1(); R(); U1()
                while (GREEN[0][1] == YELLOW[1][1] or YELLOW[2][1] == YELLOW[1][1]): U()
            elif (GREEN[1][0] != GREEN[1][1] and GREEN[1][0] != YELLOW[1][1] and RED[1][2] != RED[1][1] and RED[1][2] != YELLOW[1][1]):
                while (ORANGE[0][1] != YELLOW[1][1] and YELLOW[1][2] != YELLOW[1][1]): U()
                L1(); U(); L(); F1(); L(); F(); L1(); U()
            else: U()
        while (GREEN[1][1] != GREEN[2][1]): E()
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
    MOVES = []

    cross()

    for i in range(len(MOVES) - 3): # elimino 4 mosse uguali (es. R R R R)
        if ( MOVES[i] != "&" and MOVES[i] == MOVES[i + 1] == MOVES[i + 2] == MOVES[i + 3]):
            MOVES[i] = "&"
            MOVES[i + 1] = "&"
            MOVES[i + 2] = "&"
            MOVES[i + 3] = "&"
        if ( MOVES[i] != "&" and MOVES[i] == MOVES[i + 1] == MOVES[i + 2]):
            if (len(MOVES[i]) == 1):
                MOVES[i] += "'"
            else:
                MOVES[i] = MOVES[i][0]
            MOVES[i + 1] = "&"
            MOVES[i + 2] = "&"
        if (MOVES[i] != "&" and MOVES[i][0] == MOVES[i + 1][0] and MOVES[i] != MOVES[i + 1]):
            MOVES[i] = "&"
            MOVES[i + 1] = "&"
    for _ in range(len(MOVES)):
        try:
            MOVES.remove("&")
        except ValueError:
            break

def scramble():
    with open(r"path\to\scrambles.txt", "r") as f:
        lines = f.readlines()
    line = lines[0]
    lines.append(lines.pop(0))
    with open(r"path\to\scrambles.txt", "w") as f:
        f.writelines(lines)
    return (line[:-1])

def reset():
    global MOVES, CUBE, GREEN, ORANGE, BLUE, RED, YELLOW, WHITE, green, orange, blue, red, yellow, white, Reset

    MOVES = []

    green, red, blue, white, yellow, orange, Reset = '\033[48;2;22;160;90m', '\033[48;2;255;0;65m', '\033[48;2;13;71;161m', '\033[47m', '\033[48;2;255;225;40m', '\033[48;2;255;165;0m', '\033[0m'

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

def showCube():
    for x in range(3):
        s = "  " * 3
        for y in range(3):
            s += YELLOW[x][y] + "  " + Reset
        print(s)
    a, b, c = "", "", ""
    for i in [RED, GREEN, ORANGE, BLUE]:
        for x in range(3):
            for y in range(3):
                if (x == 0):
                    a += i[x][y] + "  " + Reset
                elif (x == 1):
                    b += i[x][y] + "  " + Reset
                else:
                    c += i[x][y] + "  " + Reset
    print(a)
    print(b)
    print(c)
    for x in range(3):
        s = "  " * 3
        for y in range(3):
            s += WHITE[x][y] + "  " + Reset
        print(s)

def play():
    global MOVES
    moves = ""

    while True:
        print("""Le mosse disponibili sono le seguenti (e i loro rispettivi primi): R, L, U, D, F, B, M, E, S, r, f, d
Per uscire dal programma inserire: -1
Per visualizzare il cubo inserire: 0
Per visualizzare le mosse fatte: 1
Per resettare il cubo inserire: 2
Per risolvere il cubo inserire: 3
Per tornare indietro inserire: 8""")
        choice = str(input("Inserire un valore: ")).replace("'", "1")
        if (choice == "-1"):
            print("Pulisco la memoria...")
            # free(all)
            print("Chiudo il programma...")
            quit()
        elif (choice == "0"):
            showCube()
        elif (choice == "8"):
            break
        elif (choice == "1"):
            print(moves.strip())
        elif (choice == "2"):
            reset()
            moves = ""
        elif (choice == "3"):
            solve()
            print(f"Algoritmo trovato: {''.join(i + ' ' for i in MOVES).strip()}")
            print(f"Numero mosse: {len(MOVES)}")
            moves = ""
        else:
            try:
                globals()[choice]()
                moves += choice.replace("1", "'") + " "
            except KeyError:
                print(red + "Valore inserito non valido!!!" + Reset)

def home():
    global MOVES

    while True:
        print("""
0: scramble the cube and solve it
1: enter play mode
2: resets the cube and all the global variables
3: shows the cube
4: quit the program
""")
        try:
            choice = int(input("Inserire un valore: "))
        except ValueError:
            choice = -1
        print()
        if (choice == 0):
            reset()
            print("Inizio a mischiare il cubo...")
            s = scramble()
            for i in s.split():
                globals()[i]()
            print(f"Scramble: {s}")
            MOVES = []
            print("Risolvo il cubo...")
            solve()
            print(f"Mosse: {''.join(i + ' ' for i in MOVES).strip()}\nNumero mosse: {len(MOVES)}")
        elif (choice == 1):
            reset()
            print("Entro nella modalità play...")
            play()
        elif (choice == 2):
            reset()
            print("Ho resettato tutte le variabili :)")
        elif (choice == 3):
            showCube()
        elif (choice == 4):
            print("Pulisco la memoria...")
            # free(all)
            print("Memoria pulita. Chiudo il programma")
            quit()
        else:
            print(red + "Inserire un valore valido!!!" + Reset)

reset()
home()
