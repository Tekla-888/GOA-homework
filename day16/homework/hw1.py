correct_username = "user66"
correct_password = "1234"

user_input1 = input("Enter username: ")
user_password = input("Enter password: ")

while (user_input1 != correct_username) or (user_password != correct_password):
    print("Incorrect info")
    user_input1 = input("Enter username: ")
    user_password = input("Enter password: ")
print("Correct username and correct password. logged in")