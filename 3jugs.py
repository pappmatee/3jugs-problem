#!/usr/bin/env python3

state = [0, 0, 5]
maximum = [2, 3, 5]


def isValid():
    sum = 0

    for i in range(len(state)):
        sum += state[i]
        # Kevesebb mint 0, vagy több mint a maximum van-e benne?
        if state[i] < 0 or state[i] > maximum[i]:
            return False
    
    # Összesen annyi folyadék van-e, mint a kezdetben?
    return sum == maximum[2]
    

def isGoalState():
    # Célállapot, ha 4 liter van az utolsó kancsóban
    return state[2] == 4


def isValidOperation(from_where, to_where):
    # a 'honnan' és 'hova' kancsók megfelelő indexeket jelölnek-e
    # üresbe öntünk-e
    # üresből öntünk-e
    return (from_where > -1) and (from_where < 3) and (to_where > -1) and (to_where < 3) and (from_where != to_where) and (state[from_where] != 0) and (state[to_where] != maximum[to_where])


def pour(from_where, to_where):
    # A n. kancsó az az n-1. indexen van..
    from_where -= 1
    to_where -= 1

    # Operátor alkalmazási előfeltétel ellenőrzés
    if not(isValidOperation(from_where, to_where)):
        print("The requested operation is not valid...")
        return

    # Amennyi át lesz öntve:
    # min ('honnan' kancsó tartalma, 'hova' kancsóban levő üres hely)
    value = min(state[from_where], maximum[to_where] - state[to_where])

    # Operátor hatás
    state[from_where] -= value
    state[to_where] += value


def printState():
    print("")
    print("{", end="")
    for i in range(0,3):
        if i > 0:
            print(", ", end="")
        print(state[i], end="")
    print("}")



def main():
    printState()

    while(not(isGoalState())):
        from_where = input("From: ")
        to_where = input("To: ")

        pour(int(from_where), int(to_where))

        printState()


##################################################################################

if __name__ == "__main__":
    main()