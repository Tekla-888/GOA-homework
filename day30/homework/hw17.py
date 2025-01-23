def find_character_index(text, character):
     index = text.find(character)

     return index
my_string = "Hello, world!"
char = 'o'
result = find_character_index(my_string, char)
print(result) 