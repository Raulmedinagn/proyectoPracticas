from flask_restful import Resource



class Helloword(Resource):
    def get(self):
        return {'hola': 'mundo'}