from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import ninja_model 


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        # Create an empty list to append our instances of friends
        dojo_instance = []
        # Iterate over the db results and create instances of friends with cls.
        if results:  # queriees we make give results
            for row in results:
                this_dojo = cls(row)
                dojo_instance.append(this_dojo)
            return dojo_instance
        return False

    @classmethod
    def get_one_dojo(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
        dojo_one = cls(results[0])  # make dojo instance
        all_ninjas = []# creating list for all ninjas that are targeting dojo instance
        for row in results:  # creating dict of one ninja
            ninja_row = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],  # keys of ninja class
                'age': row['age'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at'],
                'dojo_id': row['dojo_id']
            }
            # this creates one of the ninjas
            this_ninja = ninja_model.Ninja(ninja_row)
            all_ninjas.append(this_ninja)  # pushes the ninja into the empty list
        # creating new key in the dojo dict that has a list of all ninjas
        dojo_one.ninjas = all_ninjas
        return dojo_one

    @classmethod
    def save_one_dojo(cls, data):
        query = "INSERT INTO dojos(name) VALUES (%(name)s);"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_one_dojo(cls, data):
        query = 'DELETE FROM dojos WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def edit_dojo(cls, data):
        query = 'UPDATE dojos SET name = %(name)s WHERE id = %(id)s;'
        return connectToMySQL(DATABASE).query_db(query, data)
