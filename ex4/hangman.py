import random

word_list = ["python", "java", "kotlin", "javascript"]

def num_char(word):
    # change word to -
    return "-" * len(word) 

def check(char, word, word_ans, life):
    """
    check 1. Is word already have char in it and life -1?
          2. Is char in word_ans add char to word
          3. Is char not in word_ans life - 1
    """
    if char in word:
        print("No improvements")
        life -= 1
        return word, life

    elif char in word_ans:
        for i in range(len(word)):
            if char == word_ans[i]:
                word = word[:i] + char + word[i+1:]
                
                

    elif char not in word_ans:
        print("No such letter in the word")
        life -= 1
        return word, life
    
    return word, life
    
    

def play():
    """
    start game
    """
    print("H A N G M A N \n")
    # random word
    word_ans = random.choice(word_list)
    word = num_char(word_ans)
    life = 8
    print(word)
    # play loop untill user get right answer or life == 0
    while True:
        char = input("Input a letter: > ")
        word, life = check(char, word, word_ans, life)    
        print(word + "\n")
        
        if word == word_ans:
            print("You guessed the word!")
            print("You survied")
            break
        elif life == 0:
            print("You are hang!!")
            break

play()  



