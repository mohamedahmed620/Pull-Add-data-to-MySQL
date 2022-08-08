# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash

# model the class after the friend table from our database
class ninja_model:
    
    def __init__(self, data):
        self.id =data["id"]
        self.first_name= data["first_name"]
        self.last_name= data["last_name"]
        self.age= data["age"]
        self.dojo_id= data["dojo_id"]
    
    @staticmethod
    def validate_data(ninja_model):
        is_valid = True
        if len(ninja_model["first_name"]) <2:
            flash ("please enter a valid ninja First Name")
            is_valid = False
        if len(ninja_model["last_name"]) <2:
            flash ("please enter a valid ninja Last Name")
            is_valid = False
        if int(ninja_model["age"]) <16:
            flash ("please enter a valid ninja Age")
            is_valid = False
        return is_valid
    
    @classmethod
    def get_all(cls):

        query = "select * from ninjas where dojo_id = %(id)s;"
        results = MySQLConnection("dojo_and_ninja").query_db(query)
        ninjas= []
        for ninja in results:
            ninjas.append(cls(ninja))
        # print(results)
        return ninjas

    @classmethod
    def create_ninja(cls,data):
        query = "insert into ninjas (first_name, last_name, age, dojo_id) values (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        results = MySQLConnection("dojo_and_ninja").query_db(query, data)
        print(results)
        return results

    # @classmethod
    # def one_ninja_function(cls,data):
    #     # query= "select * from dojo_and_ninja where id = %(id)s"
    #     query = "select * from dojo left join ninja on dojo.id = ninja.dojo_id where dojo.id =%(id)s;"
    #     results = MySQLConnection("dojo_and_ninja").query_db( query,data )
    #     # print(ninja)
    #     ninjas = cls( results[0] )
    #     for ninja in ninjas:
    #             # Now we parse the burger data to make instances of burgers and add them into our list.
    #             ninja_data = {
    #                 "id" : ninja_data["ninja.id"],
    #                 "name" : ninja_data["ninja.first_name"],
    #                 "bun" : ninja_data["ninja.last_name"],
    #                 "meat" : ninja_data["ninja.age"],
    #                 "created_at" : ninja_data["ninja..created_at"],
    #                 "updated_at" : ninja_data["ninja.updated_at"]
    #             }
    #             # ninjas.ninja.append( burger.Burger( ninja_data ) )
    #     print(ninja_data)
    #     return ninjas
    #     # return cls(ninja[0])
    
    @classmethod
    def edit_user_info(cls,data):
        query = "update dojo_and_ninja set first_name = %(first_name)s, last_name=%(last_name)s, age=%(age)s where id = %(id)s;"
        results = MySQLConnection("dojo_and_ninja").query_db(query, data)

        return results
    
    @classmethod
    def delete_user_info(cls,data):
        query = "delete from dojo_and_ninja where id = %(id)s;"
        results = MySQLConnection("dojo_and_ninja").query_db(query, data)
        return results

