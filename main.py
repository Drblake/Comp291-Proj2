import sys
import getpass
import sql as sqlFile
import bsddb3 as db

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
                print("Waring: Arguments not properly specified!")
                print("First argument creates specifies database type (btree/hash/indexfile.")
                print("Quitting")
                sys.exit(10)
    
        DATABASE = "cstudents.db"
        if(argv[1].lower() is "btree"):
            db = db.btopen(DATABASE, 'c')
        
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
                        create(5,10000000,"FILE POSITION HERE")
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

#        sql.close()  # clean up sql object


def create(length, seed, File):
	#MAY NEED MULTIPLE FOR MULTIPLE TYPES?????
	try:
		db = bsddb.btopen(File, "w")
	except:
		print("No database found, creating new database")
		db = bsddb.btopen(File, "c")

	random.seed(seed)

	for value in range(length):
		key_range = integer_generator()
		new_key = ""
		new_value = ""
		for increment in range(key_range):
			new_key += str(char_generator())
		for increment in range(key_range):
			new_key += str(char_generator())
		print("KEY: ", new_key, "\n")
		print("VALUE: ", new_value, "\n")
		print("\n")
		new_key = new_key.encode(encoding ='UTF-8')
		new_value = new_value.encode(encoding = 'UTF-8')
		
		if database = 1:
			db[new_key] = new_value

		elif database = 2:
			db[new_key] = new_value

		else:
			db[new_key] = new_value
	if database = 1:
		try:
			db.close()
			print("B-Tree Populated Successfully")
		except Exception as Error:
			print(Error)

	elif database = 2:
		try:
			db.close()
			print("Hash Table Populated Successfully")
		except Exception as Error:
			print(Error)

	else:
		try:
			db.close()
			print("Index File Populated Succesfully")
		except Exception as Error:
			print(Error)



def key():

def data():

# Get Range of data
def keyRange():


# Destroy database, Clear Answer
def destroy():


def getTime():
    
def integer_generator():
        return random.randint(64,127)
def char_generator():
	return chr(random.randint(97,122))



main()  # run the main function
