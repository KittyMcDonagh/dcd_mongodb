# Install the Python Mongo Library
import pymongo

import os

# Use os library to set MONGO_URI by reading in the environment variable 
# MONGO_URI we set in .bashrc
MONGODB_URI = os.getenv("MONGO_URI")

# MonogDB name
DBS_NAME = "KittysTestDB"

# MongoDB Collection name
COLLECTION_NAME = "KittysFirstMDB"

# Create Mongo Connect function
def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("could not connect to MongoDB: %s") % e
        
def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")
    
    option = input("Enter option: ")
    return option
    
def get_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    
    try:
        doc = coll.find_one({'first': first.lower(), 'last':last.lower()})
    except:
        print("Error accessing the database")
    
    if not doc:
        print("")
        print("Error! No results found.")
        
    return doc
        
def add_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter date of birth > ")
    gender = input("Enter gender > ")
    hair_colour = input("Enter hair colour > ")
    occupation = input("Enter occupation > ")
    nationality = input("Enter nationality > ")
    
    new_doc = {'first': first.lower(), 'last': last.lower(), 'dob': dob, 'gender': gender, 'hair_colour': hair_colour, 'occupation': occupation, 'nationality': nationality}
    
    try:
        coll.insert(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")
        
def find_record():
    doc = get_record()
    print("")
    if doc:
        for k, v in doc.items():
            # "_id" is a unique id created by MongoDB. We dont want to print this
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())
                
def edit_record():
    doc = get_record()
    print("")
    if doc:
        print("")
        update_doc = {}
        
        for k, v in doc.items():
            # "_id" is a unique id created by MongoDB. We dont want to print this
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ")
                
                if update_doc[k] == "":
                    update_doc[k] = v
                    
        try:
            coll.update_one(doc, {'$set': update_doc})
            print("")
            print("document updated")
        except:
            print("Error accessing the database")

def delete_record():
    doc = get_record()
    
    if doc:
        print("")
       
        for k, v in doc.items():
            # "_id" is a unique id created by MongoDB. We dont want to print this
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())
                
        print("")
        confirmation = input("Is this the document you want to delete?\nY or N > ")
        print("")
            
        if confirmation.lower() == 'y':
            try:
                coll.remove(doc)
                print("")
                print("document deleted")
            except:
                print("Error accessing the database")
        else:
            print("Document not deleted")
    
def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            print("You have selected option 5")
            conn.close()
            break
        else:
            print("Invalid option")
        
        print("")


# Create connection to DB using environment variable stored above
conn = mongo_connect(MONGODB_URI)

# Set the collection name by pass the db name and collection name to the 
# connection
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()

        
            
            
            
            
    
    
    