import os
import sys
import pymongo

#Insert sample data
INSERT_DATA = [
{
  "name":"AWS",
  "sku":"222225",
  "description":"All in one",
  "price":300
},
{
  "name":"Azure",
  "sku":"222226",
  "description":"complete coverage of features of Azure",
  "price":300
}
]

#Setting Amazon DocumentDB ceredentials
username = "masteruser"
password = "masteruser@123"
clusterendpoint = "your_endpoint:27017"
tlsCAFile = "global-bundle.pem"

def main(args):
    #Establish DocumentDB connection
    client = pymongo.MongoClient(clusterendpoint, username=username, password=password, tls='true', tlsCAFile=tlsCAFile,retryWrites='false')
    db = client.docdbdemo
    products = db['products']

    #Insert data
    products.insert_many(INSERT_DATA)
    print("Successfully inserted data")

    #Find a document
    query = {'sku': '222225'}
    print("Printing query results")
    print(products.find_one(query))

    #Update a document
    print("Updating document")
    products.update_one(query, {'$set': {'price': 350}})
    print(products.find_one(query))

    #Clean up
    db.drop_collection('products')
    client.close()

if __name__ == '__main__':
    main(sys.argv[1:])
