# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database

DATABASE = 'users_schema'

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of users
        all_users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            all_users.append( cls(user) )
        return all_users

    @classmethod
    def get_one(cls, **data):
        print("################", data)
        query = "SELECT * FROM users WHERE users.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        user = cls(results[0])
        return user

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        user_id = connectToMySQL(DATABASE).query_db(query,data)
        return user_id

    @classmethod
    def update_one(cls, data):
        query = "UPDATE users SET id = %(id)s, first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def delete_one(cls, **data):
        query = "DELETE FROM users WHERE (id = %(id)s);"
        return connectToMySQL(DATABASE).query_db(query,data)