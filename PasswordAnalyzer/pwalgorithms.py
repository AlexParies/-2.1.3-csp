# Module pwalgorithms

# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("dictionary.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses

def twoWord(password):
    words = get_dictionary()
    guesses = 0
    for w in words:
        for x in words:
            guesses +=1
            if(w+x == password):
                return True, guesses
    return False, guesses


def twoWordDigit(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w1 in words:
    for w2 in words:
      for num in range(0,100):
        guesses += 1
        print(guesses)
        if (str(num) + w1 + w2 == password):
          return True, guesses
        if (w1 + w2 + str(num) == password):
          return True, guesses
        if (w1 + str(num) + w2 == password):
          return True, guesses
  return False, guesses
