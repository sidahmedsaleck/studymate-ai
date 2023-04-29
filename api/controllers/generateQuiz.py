from flask import request
from flask_restful import Resource
import os
from api.utilities.argparsers.generateQuizArgparser import genereateQuizParser
from api.services.quiz.createQuiz import createQuiz
from api.services.quiz.createChunks import createChunks
from api.utilities.utils import chunkLimit , tokenLimit
from api.utilities.constances import CHUNK_SIZE,OVERLAP,ENCODING_MODEL

# 1. get the long text from the user
# 2. get the language from the user
# 3. get the tire from the user
# 4. get the auth token from the user
# 5. check if the auth token is valid
# 6. create chunks from the long text
# 7. create quiz from the chunks
# 8. return the quiz to the user

class GenerateQuiz(Resource):
    """
    1. get the long text from the user
    2. get the language from the user
    3. get the tire from the user
    4. get the auth token from the user
    5. check if the auth token is valid
    6. create chunks from the long text
    7. create quiz from the chunks
    8. return the quiz to the user
    """
    def post(self):

        #parsing arguments
        args = genereateQuizParser.parse_args()
        longtext = args['longText']
        lang = args['lang']
        tire = args['tire']
        auth = args["authId"]

        # verifying the authId
        if auth != os.environ["STUDYMATE_AUTH"]:
            return {'success':False,'message':'auth token is not valid'},401
        
        
         # getting the number of chunks to use
        CHUNK_LIMIT = chunkLimit(tokenLimit(tire))

        # creating the chunks
        chunks,lenTokensInFile = createChunks(longText=longtext,chunkSize=CHUNK_SIZE,overlap=OVERLAP,encodingModel=ENCODING_MODEL)

        # creating the quiz
        quiz = createQuiz(chunks=chunks[:CHUNK_LIMIT],lang=lang,encodingModel=ENCODING_MODEL)

        # returning the quiz to the user
        if quiz:
            return {'success':True,
                    'Quiz':quiz,
                    'numberOfTokensInFile':lenTokensInFile
                    },200
        
        # returning an error message to the user

        return {'success':False,
                'Quiz':"",
                'numberOfTokensInFile':lenTokensInFile
                },400