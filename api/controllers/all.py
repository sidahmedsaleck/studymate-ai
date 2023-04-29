 

from flask_restful import Resource


class All(Resource):
    def get(self,id):
        return {'message':'this route does not existes'},404
    
    def post(self,id):
        return {'message':'this route does not existes'},404