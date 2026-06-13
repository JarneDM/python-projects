import random

def get_word_from_file(file):
    word = random.choice(list(open(file)))
    return word.strip()

def game():
    guesses = 0
    word = get_word_from_file('words.txt').lower()
    print("Welcome to the Morvex word game! Guess the word in 5 guesses and win!")
    letters = []
    for i in range(len(word)):
        letters.append("_")
      
    print(" ".join(letters))

    name = input("> your name: ")



    while guesses <= 5:
        guess = input(f"\n{name}/name ~ ")
        guess = guess.lower()

        if guess != word:
          guesses += 1
          print(f"\nWrong try again! \nGuesses over: {guesses}/5 \n" )
          
          for g in guess:
             if g in word:
                for i in range(len(word)):
                    if word[i] == g:
                        letters[i] = g
          print(" ".join(letters))
        else: 
            print("You won!")
            break
        
        if guesses >= 5:
          print(f"The word was {word}")
          break
            

game()