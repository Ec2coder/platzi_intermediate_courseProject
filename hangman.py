import random
from os import system

def main():
    system('clear')
    DB = ["rojo","azul","celeste","purpura"]
    word_found = []
    random_word = random.choice(DB)
    word_len = len(random_word)
    script = ["_" for i in random_word]
    point = 6

    hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


    
    


    while(1 > 0):
        print(hangman[point])
        print(script)
        letter = input("ingrese una letra: ")

        assert len(letter) == 1, "debes ingresar un letra para poder jugar"
        
        if letter in random_word and letter not in word_found:
            word_found.append(letter)
            for i in range(word_len):
                for j in range(word_len):
                    if letter == random_word[j]:
                        script.pop(j)
                        script.insert(j, letter)
                        system('clear')
                        
                    
                    else:
                        continue
        else:
            if letter in word_found:
                system('clear')
                print("ya encontraste esta letra, ingresa una diferente")

        if len(word_found) == len(random_word):
            print("Ganaste")
            break


        if letter not in random_word:
            point -=1
            system('clear')
            if point == 0:
                system('clear')
                print("Game Over")
                break
            
        
        



if __name__ == '__main__':
    main()