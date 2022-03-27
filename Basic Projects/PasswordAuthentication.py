
# Password Authentication is the process of checking the identity of a user.
"""
A password authentication system is a system that is used for the identification
of a user. Think of it like a login screen that you see while logging in to your
Facebook account. It asks for your email or a username and then it asks for your
password.
If you have entered the correct password then it verifies you as the real user.
"""

database = {"aman.kharwal": "123456", "kharwal.aman": "654321", "sonam": "sona124"}
username = input("Enter Your Username : ")
password = input("Enter Your Password : ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = input("Enter Your Password Again : ")
        break

        print("Verified")
