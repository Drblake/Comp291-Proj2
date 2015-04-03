import sys
import random
import bsddb3 as bsddb
import os

# This will display the menu and handle input to the menu
# after creating/population tables.
def main():
    if(len(sys.argv) != 2):
        sys.exit("Warning: Arguments not properly specified!\n" + \
        "First argument creates specifies database type (btree/hash/indexfile).\n" + \
        "Quitting.")

    db = open_db()
    try:
        answer = open("answers", 'w')
    except Exception as Error:
        print(Error)

    while(True):
        print (
"""----------------------------------------
Please Select from the following:
        1:Create and Populate Database
        2:Retrieve records with Key
        3:Retrive records with Data
        4:Retrieve records with Key Range
        5:Destroy Database
        6:Quit""")
        
        choice = getNumber("Choice (1-6): ",1,1, 6, 1)

        if choice == 1:
            print("Creating/Populating Database")
            create(10000,10000000, db)
        elif choice == 2:
            print("Retrieving Records with Key:")
            key(db, answer)
        elif choice == 3:
            print("Retrieving Records with Data:")
            data(db, answer)
        elif choice == 4:
            print("Retrieving Records with Key Range:")
            keyRange(db, answer)
        elif choice == 5:
            print("Destroying Database")
            db = destroy(db)
        elif choice == 6:
            print("Good Bye.")
            break
        else:
            print ("Invalid Input!")
    db.close()
    os.remove("tmp/sbaergen_db")
    answer.close()
    
def create(length, seed, db):
    random.seed(seed)

    for value in range(length):
        key_range = integer_generator()
        value_range = integer_generator()
        new_key = ""
        new_value = ""
        for increment in range(key_range):
            new_key += str(char_generator())
        for increment in range(value_range):
            new_value += str(char_generator())
        try:
            Data = db[new_key]
        except:
            new_key = new_key.encode(encoding ='UTF-8')
            new_value = new_value.encode(encoding = 'UTF-8')
            db[new_key] = new_value
       
    print("Database Populated Successfully")


def key(db, answer):
    search_key = input("Enter the key value you wish to search for: ")               
    search_key = search_key.encode(encoding ='UTF-8')
    try:
        data = db[search_key]
        answer.write(search_key.decode(encoding ='UTF-8') + '\n')
        answer.write(data.decode(encoding = 'UTF-8') + '\n')
        answer.write('\n')
        return
    except Exception as error:
        print(error)
        print("Key does not exist")
    return

def data(db, answer):
    search_data = input("Enter the data you wish to search for: ")
    search_data = search_data.encode(encoding = 'UTF-8')
    try:
        for key in db:
            if db[key] == search_data:
                answer.write(key.decode(encoding ='UTF-8') + '\n')
                answer.write(search_data.decode(encoding = 'UTF-8') + '\n')
                answer.write('\n')
    except Exception as error:
        print(error)
        print("Data does not exist")

    return

# Get Range of data
def keyRange(db, answer):
    search_key_min = input("Enter the minimum key value you wish to search for: ")       
    search_key_max = input("Enter the maximum key value you wish to search for: ")        
    search_key_min = search_key_min.encode(encoding ='UTF-8')
    search_key_max = search_key_max.encode(encoding ='UTF-8')
    count = 0
    try:
        for key in db:
            if key > search_key_min and key < search_key_max:
                count+=1
                solution_key = key
                solution_data = db[solution_key]
                answer.write(solution_key.decode(encoding ='UTF-8') + '\n')
                answer.write(solution_data.decode(encoding = 'UTF-8') + '\n')
                answer.write('\n')
                print(count)
        print("Result Recorded")
        return 
    except Exception as error:
        print(error)
        print("Key does not exist")
    
    return

# Destroy database, Clear Answer
def destroy(db):
    db.close()
    db = open_db()
    return db

def getTime():
    return
    
def integer_generator():
    return random.randint(64,127)
def char_generator():
    return chr(random.randint(97,122))

def open_db():
    DATABASE = "tmp/sbaergen_db"
    if not os.path.exists("tmp/"):
        os.makedirs("tmp/") 
    if(str(sys.argv[1]).lower() == "btree"):     
        try:
            db = bsddb.btopen(DATABASE, 'w')
        except:
            db = bsddb.btopen(DATABASE, 'c')
    elif(str(sys.argv[1]).lower() == "hash"):
        try:
            db = bsddb.hashopen(DATABASE, 'w')
        except:
            db = bsddb.hashopen(DATABASE, 'c')
    elif(str(sys.argv[1]).lower() == "indexfile"):
        #TODO
        pass
    else:
        sys.exit("Invalid Argument. Please try again!\n" + str(sys.argv[1]).lower())

    print("")  # put some space between info above and start of menu
    return db
 
# from sql.py in proj1
def getNumber(message, maxLen = None, minLen = 0, maxValue = None, minValue = None):
    number = None
    while(True):
        try:
            number = eval(input(message))
        except:
            print("Invalid input, try again.")
            continue
        length = len(str(number))
        if maxLen is not None:
            if length > maxLen:
                print("Number length too long, try again.")
                continue
        if minLen is not None:
            if length < minLen:
                print("Number length too short, try again.")
                continue
        if maxValue is not None:
            if number > maxValue:
                print("Value too large, try again.")
                continue
        if minValue is not None:
            if number < minValue:
                print("Value too small, try again.")
                continue
        return number

# only want the main function called if this is the main file
if __name__ == "__main__":
    main()
