from flask_restful import Resource,Api

api=Api(prefix="/api")
class Test(Resource):

    def get(self):
        a = 40
        b = 5461
        return a+b, 200
        # return "Hi Souvik!!", 200

class  T2(Resource):
    def get(self):
        file=open("data\Ingredients1.csv","r")
        file.readline()
        ing1=file.readlines()[:5]
        file.close()
        ing=[]
        for ing2 in ing1:
           ing3=ing2.split(" ")
           ing.append(ing3[0])
            
        return ing,200


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
api.add_resource(T2, '/test2')