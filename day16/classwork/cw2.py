my_num = 7
user_num = int(input("Enter number: "))
counter = 0

while user_num != my_num:
    user_num = int(input("Enter number: "))
    counter += 1

print("you guessed")
print("Your guess count:", str(counter))
