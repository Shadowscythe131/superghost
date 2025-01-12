from superghost import Solver
s=Solver()
game=""
while(True):
    game=s.bestMove(game)
    if game=="That's a word, computer wins":
        print("That's a word, computer wins")
        break
    elif game=="Computer calls the bluff and wins":
        print("Computer calls the bluff and wins")
        break
    print("computer goes "+game)
    move=input("move > ")
    if move=="resign":
        print("computer wins")
        break
    elif move=="challenge":
        print("computer responds with: "+s.respond(game))
        break
    else:
        letter=move[0]
        typ=move[1]
        if typ=="+":
            game=letter+game
        else:
            game=game+letter
    print("player goes "+game)
