def is_lowercase(string):
 for char in string:
    if not char.islower():
      return False
    return True

user_input = input("Enter string:")

if is_lowercase(user_input):
  
  print("string is in lowercase.")
else:
  
 print("strig has upper case to:")