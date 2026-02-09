#UserID, Password & Captcha
uid = input("Enter User ID: ")
password = input("Enter Password: ")

if uid == "admin" and password == "1234":
    captcha = 5678
    print("Captcha:", captcha)
    user_captcha = int(input("Enter Captcha: "))

    if user_captcha == captcha:
        print("Login Successful")
    else:
        print("Captcha Failed")
else:
    print("Invalid User ID or Password")
