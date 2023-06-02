
from flask import Flask ,request
from flask_restful import Api , Resource 
from controllers.generateSummary import GenerateSummary
from controllers.generarteFlashcards import GenerateFlashcards
from controllers.generateQuiz import GenerateQuiz
from controllers.home import Home
from controllers.all import All
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

