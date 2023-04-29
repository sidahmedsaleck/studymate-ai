
from flask import Flask ,request
from flask_restful import Api , Resource
from api.controllers.generateSummary import GenerateSummary
from api.controllers.generarteFlashcards import GenerateFlashcards
from api.controllers.generateQuiz import GenerateQuiz
from api.controllers.home import Home
from api.controllers.all import All
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    api = Api(app)
    CORS(app)

    api.add_resource(Home, '/')
    api.add_resource(GenerateSummary, '/generatesummary')
    api.add_resource(GenerateFlashcards, '/generateflashcards')
    api.add_resource(GenerateQuiz, '/generatequiz')
    api.add_resource(All, '/<id>')

    return app

