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
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("could not connect to MongoDB: %s") % e

# Create connection to DB using environment variable stored above
conn = mongo_connect(MONGODB_URI)

# Set the collection name by pass the db name and collection name to the 
# connection
coll = conn[DBS_NAME][COLLECTION_NAME]

# Update one record with nationality = american, to hair color = maroon
coll.update_one({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})

# Find all documents with nationality = american in the db
documents = coll.find({'nationality': 'american'})

# Print each document
for doc in documents:
    print(doc)