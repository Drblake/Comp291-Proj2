# Berkeley DB Example

__author__ = "Bing Xu"
__email__ = "bx3@ualberta.ca"

import bsddb3 as bsddb
import random
# Make sure you run "mkdir /tmp/my_db" first!
DA_FILE = "/tmp/my_db/sample_db"
DB_SIZE = 1000
SEED = 10000000

def get_random():
    return random.randint(0, 63)
def get_random_char():
    return chr(97 + random.randint(0, 25))


def main():
    try:
        db = bsddb.btopen(DA_FILE, "w")
    except:
        print("DB doesn't exist, creating a new one")
        db = bsddb.btopen(DA_FILE, "c")
    random.seed(SEED)

    for index in range(DB_SIZE):
        krng = 64 + get_random()
        key = ""
        for i in range(krng):
            key += str(get_random_char())
        vrng = 64 + get_random()
        value = ""
        for i in range(vrng):
            value += str(get_random_char())
        print (key)
        print (value)
        print ("")
        key = key.encode(encoding='UTF-8')
        value = value.encode(encoding='UTF-8')
        db[key] = value
    try:
        db.close()
    except Exception as e:
        print (e)

if __name__ == "__main__":
    main()
