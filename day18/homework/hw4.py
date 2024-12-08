correct_password="Goa best"
incorrect_attemps=0

while True:
    password=input("Enter password:")
    if password == correct_password:
        print("password is correct!")
    break

else:
    if password!=correct_password:
        print("passsword is incorrect try again")
incorrect_attemps+=1
print(" count of incorrect passwords:",str(incorrect_attemps))