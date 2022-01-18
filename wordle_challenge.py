# Using the rules of Wordle, given a guessWord and a solutionWord, return a set of emojis returned from the guessWord.

emojis = {
    "green": "💚",
    "black": "⬛",
    "yellow": "💛",
}

list = [] 

def wordleGuess(guessWord, solutionWord):
    "Using the rules of Wordle, given a guessWord and a solutionWord, return a set of emojis returned from the guessWord."
    if guessWord == solutionWord:
        length = len(guessWord)
        print(length)
        for i in range(length):
            list.append(emojis['green']) 
    if len(guessWord) != len(solutionWord):
        print('params must be the same length')
        
    if guessWord != solutionWord:

        for i in range(len(guessWord)):
            if guessWord[i] not in solutionWord:
                list.append(emojis['black'])
            elif guessWord[i] in solutionWord and solutionWord.index(guessWord[i]) == i:
                list.append(emojis['green'])
            elif guessWord[i] in solutionWord:
                list.append(emojis['yellow'])
    print(list)
  

wordleGuess('hello', 'wrwrw2')
