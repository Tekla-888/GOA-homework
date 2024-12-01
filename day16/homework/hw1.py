correct_password="0912"

while True:
    password=input("Enter  password:")
    if password==correct_password:
        print("password is write")
        break
    else:
        print("password isn't write try again.")