#this is a example of a computer memory in python made by: Dan7elB v.1.0

#memory of 8 bytes
bytes = 8
SSD = [ "00000000" for i in range(bytes)]


#functions
def readByte():
    print(SSD[int(input("what byte do you want to read? "))])
    print("Done") 
    menu()

def replaceByte():
    SSD[int(input("what byte do you want to replace? "))] = int(input("write your new byte here "))
    print("Done")  
    menu()  

def readAll():
    print(SSD)
    print("this storage has", bytes, "bytes")
    menu()

def clearSSD():
    global SSD
    print("are you sure you want to clear everything on the storage?")
    print("1. yes")
    print("0. no") 
    decision = input("enter a number ")
    if decision == "1":
        SSD = [ "00000000" for i in range(bytes)]
    elif decision == "0":
        print("ok")
        menu()
    else:
        print("invalid number")
    print("Done") 
    menu()



#menu
print("hi, welcome to my memory example. this storage has currently 8 bytes of memory but you can read the memory or replace a byte with a new one or read a certain byte on the memory or clear everything")
def menu():
    print("what action would you like to perform?")
    print("1. read a byte(anyone you want)")
    print("2. replace a byte with a a new one")
    print("3. read everything on the storage")
    print("4. clear everything")
    action = input("enter a number ")
    if action == "1":
        readByte()
    elif action == "2":
        replaceByte()
    elif action == "3":
        readAll()
    elif action == "4":
        clearSSD()
    else:
        print("wrong number")
menu()
