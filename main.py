from nltk.corpus import words

word_list = words.words()

# filter in words with 5 letters
temp = [word.lower() for word in word_list if len(word) == 5]
word_list = temp

# assign a score for each word
def word_weight(word):
    temp = []
    for letter in word:
        if letter not in temp:
            temp.append(letter)
    return len(temp)

# map the word with it's score
word_dict = {}
for word in word_list:
    word_dict[word] = word_weight(word)
words_list = list(word_dict.items())


# sort based on score
for i in range(len(words_list)-1):
    for j in range(len(words_list)-i-1):
        if words_list[j][1] < words_list[j+1][1]:
            words_list[j], words_list[j+1] = words_list[j+1],words_list[j]

# remove words that has the letter
def remove_letter(guess,idx):
    global words_list
    temp = []
    for i in words_list:
        if guess[idx] not in i[0]:
             temp.append(i)
    words_list = temp

# filter in the only words with the letter
def letter_present(guess,idx):
    global words_list
    temp = []
    for i in words_list:
        if guess[idx] in i[0] and guess[idx] != i[0][idx]:
            temp.append(i)
    words_list = temp

# filter in only the words with the letter at a particular index
def letter_present_in_index(guess, idx):
    global words_list
    temp = []
    for i in words_list:
        if guess[idx] == i[0][idx]:
            temp.append(i)
    words_list = temp

ch = True

# start guessing
while ch:

    guess = words_list[0][0]
    print("Machine's Guess: "+guess)
    inp = input()
    
    for i in range(len(inp)):

        if inp[i] == '.':
            remove_letter(guess,i)

        elif inp[i] == '*':
            letter_present(guess,i)

        elif inp[i] == "+":
            letter_present_in_index(guess,i)
    
    ch = bool(input("Do you want to continue : "))