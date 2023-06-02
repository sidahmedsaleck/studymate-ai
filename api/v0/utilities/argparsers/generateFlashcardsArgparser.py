from flask_restful import reqparse

# This is a utility function that generates a request parser for the generate flashcards endpoint
genereateFlashcardsParser = reqparse.RequestParser()
genereateFlashcardsParser.add_argument('longText',help='the longtext is required',required=True)
genereateFlashcardsParser.add_argument('lang', help='Lang is required',required=True)
genereateFlashcardsParser.add_argument('tire', help='tire is required',required=True)
genereateFlashcardsParser.add_argument('authId', help='authToken is required',required=True)
