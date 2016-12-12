restart= 1
while restart!="x":

    print("Welcome to the game of Hang-woman!")
    print("A word will be chosen at random and you have to try to guess the word")
    print ("before you run out of attempts""")


    f = open("words.txt")
    import random 
    f = open("words.txt", 'r')
    wordbank = [line.strip() for line in f.readlines()]
    f.close() #inputs random word

    word=random.choice(wordbank)
    original=list(word.upper())
    guess=[]
    guesses=int(0) 
    user='' # user input
    change=int(0) #position of the character in the word
    space=list(word)
    alph=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')


    for char in range(len(original)): 
        if (original[char]=='A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
            guess.append('_') # creates the spaces per letters

    print guess



    while guesses<10:
        user=str.upper(raw_input('Guess : '))

        if len(user)>1: 
            print 'ERROR, please only one letter!'
            continue
        if len(user)<1:
            print 'ERROR, Please guess a letter!'
            continue
        if user not in alph:
            print 'ERROR, only input letters'
            continue


        if user in original:

            while user in space:
                guess.remove(change,'_')
                input(user) in change

                
            for user in range(len(original)):
                if space[char]=='_':
                    change+=1

            if change==len(original): 
                print 'Correct!!', guess
                print 'You Win !'
                guesses=10
                break
            

            print 'Correct!' , guess , 'Guesses left: ', (10-guesses)

        else:
            guesses+=1
            print 'Incorrect!', 'Guesses left: ', (10-guesses)
    else:
         print 'You Lose !'
         print 'Correct answer was', original

    input("press '1 + ENTER' to play again, exit out to be done.")

                
                
