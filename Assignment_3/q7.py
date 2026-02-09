#Check correct UserID and Password
uid = input("Enter User ID: ")
password = input("Enter Password: ")

if uid == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid User ID or Password")
