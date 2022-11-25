import pickle as p 
def search():
    file = open(".\King.txt","rb")
    data = {}
    search = int(input("Enter which roll no. to search : "))
    try:
        while True:
            data = p.load(file)
            # print(data)
            if data['Roll no']==search:
                print(data)
            else:
                print("Sorry! This roll no. is not in the file....")
    except:
        file.close()

def update_marks():
    file = open(".\King.txt","r+b")
    a = {}
    roll = int(input("Enter roll no whose marks to be updated : "))
    marks = int(input("Enter marks updation you want : "))
    try:
        while True:
            a = p.load(file)
            if a['Roll no'] == roll:
                print(a)
                a['marks'] = marks
                print(a)
    except:
        file.close()


