def register():
    db = open("database.txt", "r")
    username = input("create username: ")
    password = input("create password: ")
    password1 = input("confirm password: ")
    d = []
    f = []
    for i in db:
        a, b = i.split(",")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))

    if password != password1:
        print("passwords dont match, restart")
        register()
    else:
        if len(password) not in range(5, 16):
            print("password should be in range(5,16), restart")
            register()
        elif username in d:
            print("username exists")
            register()
        else:
            db = open("database.txt", "a")
            db.write(username + "," + password +"\n")
            print("success")




def access():
    db = open("database.txt", "r")
    username = input("username: ")
    password = input("password: ")

    if not len(username or password) < 1:
        d = []
        f = []
        for i in db:
            a, b = i.split(",")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))

        try:
            if data[username]:
                try:
                    if password == data[username]:
                        print("login succes")
                        print("Hi,", username)
                    else:
                        print("password or username incorrect")
                except:
                    print("incorrect password or username")
            else:
                print("username or password doesn't exist")
        except:
            print("login or password doesn't exist")
    else:
        print("please enter a value")

def home(option = None):
    option = input("Login | Signup: ")
    if option == "Login":
        access()
    elif option == "Signup":
        register()
    else:
        print("Please enter an option")
home()




