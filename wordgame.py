### Wordgame: 25 pt


from random import choice

words = [
    "oppvaskmaskin", 
    "husleie", 
    "programmering",
    "elefant",
    "spiseskje"
]

def hide(word, open_letters):
    result = []
    for let in word:
        r = let if let in open_letters else '*'
        result.append(r)
    return ''.join(result)

MAX_ROUNDS = 6
win = 0
while True:
    word = choice(words)   
    open_letters = []
    success = False
    for current in range(1, MAX_ROUNDS+1):
        hidden = hide(word, open_letters)
        print(f'Ordet er {hidden}')
        ans = input(f'Bokstav eller løsning ({current}/{MAX_ROUNDS}): ')
        if len(ans) == 1:
            if ans in word:
                open_letters.append(ans)
            else:
                print('Feil bokstav')
        else:
            if ans == word:
                print('Riktig!')
                success = True
                break
            else:
                print('Nei. Prøv en gang til.')

    if success:
        win += 1

    again = input('Et nytt ord? [j/n] ')
    
    if again == 'n':
        break

print(f'Du gjettet {win} riktige ord.')
