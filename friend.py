# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    DB = 'first_flask'
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(cls.DB).query_db(query)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append( cls(friend) )
        return friends
    
    @classmethod
    def get_friend(cls, friend_id):
        query = """
                    SELECT * 
                    FROM friends 
                    WHERE id=%(id)s;
                """
        data = {'id':friend_id}
        result = connectToMySQL(cls.DB).query_db(query, data)
        print(result[0])
        return cls(result[0])
    
    @classmethod
    def insert_friend(cls, data):
        query = 'INSERT INTO friends( first_name, last_name, occupation ) VALUES( %(first_name)s, %(last_name)s, %(occupation)s );'
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete_friend(cls, friend_id):
        query = 'DELETE FROM friends WHERE id= %(id)s ;'
        data = {'id': friend_id}
        return connectToMySQL(cls.DB).query_db(query, data)

