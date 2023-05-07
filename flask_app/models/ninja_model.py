from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = ['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def get_all_ninja(cls):
        query = "SELECT * FROM ninjas;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        # Create an empty list to append our instances of friends
        ninja_instance = []
        # Iterate over the db results and create instances of friends with cls.
        if results:  # queriees we make give results
            for row in results:
                this_ninja = cls(row)
                ninja_instance.append(this_ninja)
            return ninja_instance
        return False

    @classmethod
    def get_one_ninja(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def save_one_ninja(cls, data):
        query = "INSERT INTO ninjas(first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_one_ninja(cls, data):
        query = 'DELETE FROM ninjas WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def edit_ninja(cls, data):
        query = 'UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)
