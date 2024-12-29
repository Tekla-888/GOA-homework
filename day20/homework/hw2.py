num1 = int(input("Enter your number: "))
is_valid = True

if num1 < 0:
    is_valid = False
# 2-დან num1-მდე

for i in range(2, num1):

    # ნაშთიანი გაყოფის შედეგი თუ არის 0-ის ტოლი
    if num1 % i == 0:
        is_valid = False

if is_valid == True: print("Your number is prime")

else: print("Your number is not prime")