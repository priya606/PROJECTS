secretword="saipriya"
guess_letter=""
tries=6
while tries>0:
    user=input("enter your guess word: ")

    if user in secretword:
        print(f"you guessed the letter remaining {tries} in word ")
    else:
        tries=tries-1
        print(f"you guessed the wrong letter {user} and count is {tries}")
    
    guess_letter=guess_letter+user
    wrongLetterCount=0

    for letter in secretword:
        if letter in guess_letter:
            print(f"gussed letter is: {letter}")
        else:
            print("_",end="")
            wrongLetterCount+=1
    if wrongLetterCount==0:
        print(f"Congrats secret word was:{secretword}")
        break
else:
    print("sorry try again..")



