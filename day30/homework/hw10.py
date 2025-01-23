def find_character_index(string,character):
    index=string.find(character)
    return index
text="Hello world"
char="o"
result=find_character_index(text,char)
print(result)