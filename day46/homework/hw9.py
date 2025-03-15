sentence = "This sentence contains several words that match the task conditions."
vowels = "aeiouAEIOU"
result = [word for word in sentence.split() if len(word) > 5 and any(vowel in word for vowel in vowels)]
print(result)