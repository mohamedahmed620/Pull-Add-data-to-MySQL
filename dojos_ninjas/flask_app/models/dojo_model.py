# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import MySQLConnection
from flask_app.models.ninja_model import ninja_model
from flask import flash

# model the class after the friend table from our database
class dojo_model:
    
    def __init__(self, data):
        self.id =data["id"]
        self.name= data["name"]
        self.created_at= data["created_at"]
        # i will create the beneath line to house my ninjas
        self.ninjas = []
    
    @staticmethod
    def validate_data(dojo_model):
        is_valid = True
        if len(dojo_model["name"]) <2:
            flash("please enter a  valid dojo name")
            is_valid = False
        return is_valid
    
    @classmethod
    def get_all(cls):

        query = "select * from dojos;"
        results = MySQLConnection("dojo_and_ninja").query_db(query)
        dojos= []
        for dojo in results:
            dojos.append(cls(dojo))
        # print(results)
        return dojos

    @classmethod
    def create_dojo(cls,data):
        query = "insert into dojos (name) values (%(name)s);"
        results = MySQLConnection("dojo_and_ninja").query_db(query, data)
        print(results)
        return results

    @classmethod
    def one_dojo_function(cls,id):

        query = "select * from dojos left join ninjas on dojos.id = ninjas.dojo_id where dojo_id = %(id)s;"
        results = MySQLConnection("dojo_and_ninja").query_db( query,{"id":id} )
        # result is list of objects
        # it doesnt mater which object i choose
        # i want to create instantce of this object
        if len(results) == 0:
            return results
        dojos =  cls(results[0])        

        for nin in results:
            # print(nin)
            n= {
                "id":nin["ninjas.id"],
                "first_name": nin["first_name"],
                "last_name": nin["last_name"],
                "age": nin["age"],
                "dojo_id": nin["dojo_id"]
                }
            dojos.ninjas.append(ninja_model(n))
            return dojos
    

