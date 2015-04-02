import sys
import random
import getpass
import sql as sqlFile
import bsddb3 as bsddb
import os

# This will display the menu and handle input to the menu
# after creating/population tables.
def main():
#        print("Please login before proceeding.")
#        sql = None
#        while(True):
#                try:
#                        user = input("User [%s]:" % getpass.getuser())
#                        if not user:
#                                user = getpass.getuser()
#                        passw = getpass.getpass("Pass:")
#
#                        # create a new instance of a connection object
#                        sql = sqlFile.SqlConnection(user, passw)
#
#                        break
#                except:
#                        print("Oops, try again!")
#                        continue
#
        # Waring if no arguments are used
        if(len(sys.argv) != 2):
                print("Warning: Arguments not properly specified!")
                print("First argument creates specifies database type (btree/hash/indexfile.")
                print("Quitting")
                sys.exit(10)
    
        DATABASE = "tmp/sbaergen_db"
        if not os.path.exists("tmp/"):
            os.makedirs("tmp/") 
        if(str(sys.argv[1]).lower() == "btree"):
            db = bsddb.btopen(DATABASE, 'c')
        
        elif(str(sys.argv[1]).lower() == "hash"):
            db = bsddb.hashopen(DATABASE, 'c')

        elif(str(sys.argv[1]).lower() == "indexfile"):
            #TODO
            pass
        else:
            print("Invalid Argument. Please try again!")
            print(str(sys.argv[1]).lower())
            sys.exit(10)
        
    # Drop & Create Tables
#        if(len(sys.argv) >= 2):
#                print("Dropping / Creating Tables")
#                print("Using the argument " + str(sys.argv[1]))
#                sql.executeFromFile(str(sys.argv[1]))

        # Populate tables
#        if(len(sys.argv) >= 3):
#                print("Populate Tables")
#                print("Using the argument " + str(sys.argv[2]))
#                sql.executeFromFile(str(sys.argv[2]))

        print("")  # put some space between info above and start of menu
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

                choice = sqlFile.getNumber("Choice (1-6): ",1,1, 6, 1)

                if choice == 1:
                        print("Creating/Populating Database")
                        create(5,10000000, db)
                elif choice == 2:
                        print("Retrieving Records with Key:")
                        key()
                elif choice == 3:
                        print("Retrieving Records with Data:")
                        data()
                elif choice == 4:
                        print("Retrieving Records with Key Range:")
                        keyRange()
                elif choice == 5:
                        print("Destroying Database")
                        destroy()
                elif choice == 6:
                        destroy()
                        print("Good Bye.")
                        break
                else:
                        print ("Invalid Input!")


def create(length, seed, db):
	random.seed(seed)

	for value in range(length):
		key_range = integer_generator()
		new_key = ""
		new_value = ""
		for increment in range(key_range):
			new_key += str(char_generator())
		for increment in range(key_range):
			new_value += str(char_generator())
		print("KEY: ", new_key, "\n")
		print("VALUE: ", new_value, "\n")
		print("\n")

		new_key = new_key.encode(encoding ='UTF-8')
		new_value = new_value.encode(encoding = 'UTF-8')
		
		db[new_key] = new_value
	try:
		db.close()
		print("B-Tree Populated Successfully")
	except Exception as Error:
		print(Error)

def key():

def data():
    return
# Get Range of data
def keyRange():
    return

# Destroy database, Clear Answer
def destroy():
    return

def getTime():
    return
    
def integer_generator():
        return random.randint(64,127)
def char_generator():
	return chr(random.randint(97,122))

def finish():
    return

main()  # run the main function
