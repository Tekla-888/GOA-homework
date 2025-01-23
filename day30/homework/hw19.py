def is_lower(string):
      for char in string:
        if not char.islower():
            return False
        else:
            return True
print(is_lower("hello"))  
print(is_lower("Hello")) 

