
def manual_find(main_string, str_to_find):
  

  index = 0
  while index < len(main_string):
    if main_string[index:].startswith(str_to_find):
      return index
    index += 1
  return -1


main_string = "Hello world!"
str_to_find = "world"
result = manual_find(main_string, str_to_find)
print(result)  