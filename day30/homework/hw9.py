def find_substring(text,substring):
  index = text.find(substring)
  if index != -1:
    return index
  else:
    return"No substring"
text="I am learning programing lenguage python."
substring="python"


result = find_substring(text,substring)
print(result)