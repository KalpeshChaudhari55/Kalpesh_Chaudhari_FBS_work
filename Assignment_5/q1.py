correct_id = "asre"
correct_pass = "1234"

for i in range(3):
    user_id = input("enter your id: ")
    user_pass = input("enter your password: ")
    if user_id == correct_id and user_pass == correct_pass:
        print("you enter correct pass")
        break
    else:
        print("re-enter the credentials.")
else:
    print("program terminated")