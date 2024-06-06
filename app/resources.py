from flask_restful import Resource,Api

api=Api(prefix="/api")


class Test(Resource):

    def get(self):
        a = 20
        b = 5461
        return a+b, 200


#get inventory
#post inventory
#update inventory
#delete inventory

#get menu
#post menu
#update menu
#delete menu

#get shopping list
#update shopping list

#get task
#post task
#update task
#delete task

#get weekend task
#update weekend task


api.add_resource(Test, '/test')