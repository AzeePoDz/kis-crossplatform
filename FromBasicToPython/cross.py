import random


def tab(x):
    for i in range(x):
        print(' ', end='')

tab(28)
print("TWO TO TEN")
tab(15)
print("CREATIVE COMPUTING  MORRISTOWN NEW JERSEY\n\n\n")
print("WELCOME TO THE GAME OF TWO TO TEN.  THAT NAME COMES FROM THE")
print("SPECIAL 'DECK OF CARDS' USED. THERE ARE NO FACE CARDS - ONLY")
print("THE CARDS 2-10.  THIS GAME IS EASY AND FUN TO PLAY IF YOU")
print("UNDERSTAND WHAT YOU ARE DOING SO READ THE INSTRUCTIONS")
print("CAREFULLY.")
print("AT THE START OF THE GAME, YOU BET ON WINNING. TYPE IN ANY")
print("NUMBER BETWEEN 0 AND 200.  I THEN PICK A RANDOM NUMBER")
print("YOU ARE TO REACH BY THE SUM TOTAL OF MORE CARDS CHOSEN.")
print("BECAUSE OF THE RARE CHANCE OF YOU GETTING TO THAT NUMBER")
print("EXACTLY, YOU ARE GIVEN AN ALLOWANCE CARD.  THE OBJECT OF")
print("THE GAME OF TO GET THE TOTAL OF CARDS WITHIN THE MYSTERY")
print("NUMBER WITHOUT GOING OVER.")
print("YOU ARE GIVEN A HINT AS TO WHAT THE NUMBER IS.  THIS IS NOT")
print("THE EXACT NUMBER ONLY ONE CLOSE. ALL YOU DO IN THIS GAME IS")
print("DECIDE WHEN TO STOP.  AT THIS POINT YOUR TOTAL IS COMPARED")
print("WITH THE NUMBER AND YOUR WINNINGS ARE DETERMINED.")
M = 200
while str(input("WOULD YOU LIKE TO PLAY THE NEXT GAME (Y/N)? ")) == 'Y':
    D = 0
    T = 0
    O = int(random.randint(25, 35))
    N = int(random.randint(O, O))
    R = (int(random.randint(1, 15))) / 100
    S = int(random.randint(1, 2))
    if S != 1:
        E = int(N + (N * R))
    else:
        E = int(N - (N * R))
    A = int(random.randint(2, 9))
    print("\nPLACE YOUR BET ... YOU HAVE $", M, " TO SPEND.? ", end='')
    B = int(input())
    print("")
    while B < 0:
        print("YOU MAY NOT BET AGAINST YOURSELF.")
        print("")
        print("PLACE YOUR BET ... YOU HAVE $", M, " TO SPEND.? ", end='')
        B = int(input())
        print("")
    while M < B:
        print("YOU CAN'T BET MORE THAT YOU'VE GOT!")
        print("")
        print("PLACE YOUR BET ... YOU HAVE $", M, " TO SPEND.? ", end='')
        B = int(input())
        print("")
    if M >= B:
        print("YOUR 'LUCKY LIMIT' CARD IS A ", A)
        print("YOU MUST COME WITHIN ", A, " WITHOUT GOING OVER TO WIN.")
        print("\nHERE WE GO\n\n")
        D = D + 1
        C = int(random.randint(2, 9))
        print("CARD #",D," IS A ",C,".YOU ARE TRYING TO COME NEAR ",E)
        T = T + C
        print("YOUR TOTAL IS ", T, end='')
        while str(input(" DO YOU WANT TO CONTINUE(Y/N)? ")) == 'Y':
            print("\n")
            D = D + 1
            C = int(random.randint(2, 9))
            print("CARD #", D, " IS A ", C, ".YOU ARE TRYING TO COME NEAR ", E)
            T = T + C
            if T <= N:
                print("YOUR TOTAL IS ", T, end='')
            else:
                print("YOUR TOTAL IS OVER THE NUMBER", N, " AN AUTOMATIC LOSS!")
                M = M - B
                print("YOU NOW HAVE $", M, " IN CASH TO BET IN THE NEXT GAME!")
                break
        else:
            if T < N - A or T > N:
                print("YOU BLEW IT!  THE NUMBER WAS ", N, ", OUTSIDE YOUR LIMIT BY ", end='')
                print((N - A) - T)
                print("")
                M = M - B
                print("YOU NOW HAVE $", M, " IN CASH TO BET IN THE NEXT GAME!")
            else:
                print("YOU WIN!  THE NUMBER WAS ", N, " YOUR GUESS TOTAL WAS", T)
                print("WITHIN YOUR LIMIT CARD.")
                M = M + B
                print("\nYOU NOW HAVE $", M, " IN CASH TO BET IN THE NEXT GAME!")
        if M <= 0:
            print("YOU ARE BROKE!! YOU MAY NOT PLAY ANYMORE!!")
            break
else:
    print("HOPE YOU HAD FUN.")
