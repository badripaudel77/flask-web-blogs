"""
There are several python modules that allow us to connect to and manipulate the database using PostgreSQL, one of them 
is  Psycopg2
To install Psycopg2, we can run the command 
```sudo pip3 install psycopg2``` 
once installed, we can import it and get various available methods.
"""

# This file will create connection to the PostgreSQL database server on my local machine and return it so that it can be used in other files

import psycopg2

def db_connect():
    connection = None
    try:
        #local credentials 
        connection = psycopg2.connect(
                            database ="flask_blogs", 
                            user = "postgres", 
                            password = "_BadriPostgres1@", 
                            host = "localhost", 
                            port = "5432")
        
        # heroku credentials for db TODO : to be chagned later, try to create own credentials, this will not work as heroku changes frequently.
        # connection = psycopg2.connect(
        #                     database ="herokudb", 
        #                     user = "herokuuser", 
        #                     password = "herokupassword", 
        #                     host = "herokouhost", 
        #                     port = "5432")                    
        # print("connected to the DB : ", connection)                    

    except(Exception) as error:
        print("Something went wrong while connecting to PG DB server : ", error)

    finally:
        return connection   

# print(db_connect().cursor()) 


def get_connection():
    connection = db_connect()
    # once connected to the database, we can perform create , ... and more operations
    # user is the reserved word so can't create user table but if insist on doing so ? https://stackoverflow.com/a/22256451/9898251
    if(not connection) :
       print("No connection to the database found")
       exit()
    cursor = connection.cursor()  
    return connection, cursor 
