import random

def game():
    print("Welcome to the Guessing Game!")
    score = random.randint(1,100)

    with open("hiscore.txt","r") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Current High Score: {hiscore}")
    if score > hiscore:
        print("Congratulations! You have the new high score!")
        with open("hiscore.txt","w") as f:
            f.write(str(score))

game()
        
    
    
