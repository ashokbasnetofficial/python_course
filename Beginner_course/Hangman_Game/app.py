import random;
words = ['banana']
random_word = random.choice(words);
word_length = len(random_word)
total_hangman_steps =6;
flag =0;
blank = '_'*word_length;
filled_blank = list(blank);
while total_hangman_steps>0:
    letter_counter = 0
    letter = str(input('Guess the letter:')); 
    letter = letter.lower();
    if letter in random_word:
        for i in range(word_length):
            if random_word[i]==letter and filled_blank[i]=='_':
                filled_blank[i]=letter 
                letter_counter+=1
                break
        print(' '.join(filled_blank));
    if letter not in random_word or letter_counter==0:
        total_hangman_steps-=1
        print("Wrong guess! You have", total_hangman_steps, "steps left.")  
    if '_' not in filled_blank:
        print("Congratulations! You've guessed the word:", random_word)
        break          
        
# game over when steps is equal to 0 
if total_hangman_steps == 0:
    print("Sorry, you've run out of steps. The word was:", random_word)