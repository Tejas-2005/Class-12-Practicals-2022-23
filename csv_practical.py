import csv as c
def input_entry():
    file = open(".\King.csv","w+")
    user_id = input("Please input your name : ")
    pswd = (input("Please create a password : "))
    a = c.writer(file)
    data = [user_id,pswd]
    w = a.writerows([data])
    file.close()

def search():
    file = open(".\King.csv","r+")
    name = input("Enter name")
    d = c.DictReader(file,fieldnames=["User","Password"])
    for i in d:
        if i['User'] == name:
            print(i)
    file.close()

input_entry()
search()
