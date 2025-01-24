def insert_word(sentence, word, index):

  words = sentence.split()
  if index < 0 or index > len(words):
    return "Index out of range"
new_sentence = " ".join(words)
sentence = "This is a simple sentence"
word = "very"
index = 2
result = insert_word(sentence, word, index)
print(result)