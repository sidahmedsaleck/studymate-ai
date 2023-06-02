from flask_restful import reqparse

# This is a utility function that generates a request parser for the generate flashcards endpoint
genereateQuizParser = reqparse.RequestParser()
genereateQuizParser.add_argument('longText',help='the longtext is required',required=True)
genereateQuizParser.add_argument('lang', help='Lang is required',required=True)
genereateQuizParser.add_argument('tire', help='tire is required',required=True)
genereateQuizParser.add_argument('authId', help='authToken is required',required=True)
