import random
from hangmanArt import HANGMANPICS
with open("words.txt", "r") as file:
    words = [line.strip() for line in file if line.strip()]
secret = random.choice(words)
placeholder=""
for w in secret:
    placeholder+="_"
placeList=list(placeholder)
print(placeholder)
game_over=False
score=0
wrongGuess=6
lives=7
print(HANGMANPICS[wrongGuess])
while not game_over:
    guess=input("Enter your guess: ")
    if guess in secret: 
        if guess in placeList:
            print("You've already guessed this letter.")
        else: 
            for w in range(len(secret)):
                if secret[w]==guess:
                    placeList[w]=guess
                    score=(100/len(secret))+score
                    print(HANGMANPICS[6])
    else:
        lives-=1
        print("Wrong Guess")
        print(f"{lives}/7 lives left.")
        print(HANGMANPICS[wrongGuess])
        wrongGuess-=1
        if lives==0:
            print("Game Over.")
            print(secret)
            game_over=True
        
    placeholder="".join(placeList)
    print(placeholder)
    print(f"Score : {int(score)}%")
    if secret==placeholder:
        game_over=True