def split_sentence_into_words(sentence):
  words = sentence.split()
  return words
sentence = "This is an example sentence to be split into words"
words_list = split_sentence_into_words(sentence)
print(words_list)