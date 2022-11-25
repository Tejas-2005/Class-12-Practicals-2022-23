def seperation(char):
    file = open(".\practic3e.txt","r")
    a = file.readlines()
    for i in a:
        for x in i.split():
            print(x,end=char)
    file.close()

def counting():
    file = open(".\practic3e.txt","r")
    a = file.readlines()
    vowels = ['a','e','i','o','u','A','E',"I","O","U"]
    v = 0
    c = 0
    for i in a:
        for j in i:
            if j in vowels:
                v = v+1
            else:
                c = c+1
    print("No. of Consonants",c)
    print("No. of Vowels",v)

def removal_of_a():
    file = open(".\practic3e.txt","r")
    a = file.readlines()
    for i in a:
        print(i.replace('a',""))
    file2 = open("./anotherfile.txt","w")
    file2.writelines(i)
    file.close()
    file2.close()
