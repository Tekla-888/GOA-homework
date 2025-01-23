def count_word_occurrences(text, word):

    return text.lower().count(word.lower())

my_text = "The quick brown fox jumps over the lazy dog. The end."
search_word = "the"
result = count_word_occurrences(my_text, search_word)

print(f"word{search_word} occurs {result} times")