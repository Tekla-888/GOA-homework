def reverse_and_insert(string, sentence):
    reversed_string = string[::-1]
    return sentence.replace("{}", reversed_string)
original_string = "hello"
sentence = "Reversed string: {}"
result = reverse_and_insert(original_string, sentence)
print(result)