def count_character(text, character):
  return text.count(character)

user_text=input("Enter string:")
user_char = input("Enter simbol to count:")

result = count_character(user_text, user_char)


print(user_char,result)


