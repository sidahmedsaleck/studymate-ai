from flask import request
from flask_restful import Resource
import json
from api.utilities.argparsers.generateFlashcardsArgparser import genereateFlashcardsParser
from api.services.flashcards.createFlashcards import createFlashcards
from api.services.flashcards.createChunks import createChunks
from api.utilities.utils import tokenLimit , chunkLimit
from api.middlewares.verifyAuth import verifyAuth 
from api.utilities.constances import CHUNK_SIZE,OVERLAP,ENCODING_MODEL



# 1- it takes the long text from the user and the language and the tire and the auth token
# 2- it checks if the auth token is valid
# 3- it creates the chunks of the text
# 4- it creates the flashcards
# 5- it returns the flashcards to the user

class GenerateFlashcards(Resource):
    """
    1- it takes the long text from the user and the language and the tire and the auth token
    2- it checks if the auth token is valid
    3- it creates the chunks of the text
    4- it creates the flashcards
    5- it returns the flashcards to the user
    """
    def post(self):

        #parsing arguments
        args = genereateFlashcardsParser.parse_args()
        longtext = args['longText']
        lang = args['lang']
        tire = args['tire']
        auth = args["auth"]

        # verifying the authId
        if not verifyAuth(auth):
            return {
                'success':False,
                'message':'auth token is not valid'},401
        
        

         # getting the number of chunks to use
        CHUNK_LIMIT = chunkLimit(tokenLimit(tire))

        # creating the chunks
        chunks,lenTokensInFile = createChunks(longText=longtext,chunkSize=CHUNK_SIZE,overlap=OVERLAP,encodingModel=ENCODING_MODEL)

        # creating the flashcards
        flashcards = createFlashcards(chunks=chunks[:CHUNK_LIMIT],lang=lang,encodingModel=ENCODING_MODEL)
        
        # returning the flashcards to the user
        if flashcards:
            return {
                'success':True,
                'flashcards':flashcards,
                'numberOfTokensInFile':lenTokensInFile,
                },200
        
        # returning an error message to the user
        return {
                'success':False,
                'flashcards':"",
                'numberOfTokensInFile':lenTokensInFile,
                },400