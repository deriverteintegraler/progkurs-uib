from random import randint

BOARDSIZE = 16
board = { i:i for i in range(BOARDSIZE) }
board[3] = 8
board[9] = 13
board[10] = 2
board[15] = 6

def roll_dice():
    return randint(1,6)

def simulate(rounds):
    N_players = 10**5
    player_endpos = { i:0 for i in range(BOARDSIZE) }
    managed_rounds = {} #partB
    for _ in range(N_players):
        pos = 0
        n_rounds = 0
        for _ in range(rounds):
            newpos = pos + roll_dice()
            if newpos >= BOARDSIZE:
                newpos = newpos % BOARDSIZE
                n_rounds += 1 #partB
            # apply snakes and ladders
            pos = board[newpos] 

        player_endpos[pos] += 1
        managed_rounds.setdefault(n_rounds,0) #partB
        managed_rounds[n_rounds] += 1 #partB

    for pos in player_endpos.values():
        percent = 100 * pos / N_players
        print(f"{percent:2.0f}", end="  ")
    print()

    # below for part B
    for k,v in sorted(managed_rounds.items()):
        pct = 100 * v / N_players
        print(f'{v:5} players managed {k:2} rounds ({pct:2.0f} %)')

simulate(20)
