from flask import request
from flask_restful import Resource
from api.services.summary.extractFromPdf import extractFromPdf
from api.services.summary.readTextCreateChunks import createChunks 
from api.services.summary.createSummaries import createSummariesWithOpenai
from api.utilities.utils import chunkLimit, tokenLimit
from api.utilities.constances import CHUNK_SIZE , OVERLAP , ENCODING_MODEL
from api.middlewares.verifyAuth import verifyAuth
import os

# what the class SummarixeLongText do:
# 1- extract the text from the pdf file
# 2- create chunks from the text
# 3- summarize each chunk
# 4- return the summarized text to the user


class GenerateSummary(Resource):
    """
    1- extract the text from the pdf file
    2- create chunks from the text
    3- summarize each chunk
    4- return the summarized text to the user
    """
    def post(self):

        try:
            #parsing arguments
            args = request.form
            auth = args['auth']
            fileName = args['fileName']
            tire = args['tire']
            lang = args['lang']
            f = request.files[fileName]
            
            # verifying the authId
            if not verifyAuth(auth):
                return {'success':False,'message':'auth token is not valid'},401
            
            # getting the number of chunks to use
            CHUNK_LIMIT = chunkLimit(tokenLimit(tire))

        
            # saving the file to '/data'
            f.save(f'data/{fileName}')

            # extracting plain text from the file
            longText = extractFromPdf(f"data/{fileName}")

            # creating the chunks
            chunks,lenTokenInFile = createChunks(longText,CHUNK_SIZE,OVERLAP,ENCODING_MODEL)

            # creating the summaries
            summaries = createSummariesWithOpenai(chunks=chunks[:CHUNK_LIMIT],lang=lang,encodingModel=ENCODING_MODEL)
            
            # deleting the file
            os.remove(f"data/{fileName}")

            # returning the summaries to the user
            if summaries:
                
                return {'success': True,
                        'fileName': fileName,
                        'lenTokensInFile':f'{lenTokenInFile}',
                        'summarizedText': summaries
                        },200
        except:
            print("errr")
        
            # returning an error message to the user
            return {'success': False,
                    'summarizedText':"",
                    'lenTokensInFile':f'{lenTokenInFile}',
                    },400
