import openai 
import os
import json
import tiktoken
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv('.env'))
from api.utilities.constances import NO_FLASHCARDS_PER_CHUNK


# what does the function createFlashcards do:
# 1. it takes the chunks of text encoded  and the language as input
# 2. it uses the openai api to generate flashcards
# 3. it returns the flashcards

def createFlashcards(chunks,lang,encodingModel="p50k_base"):
    """
    This function takes the chunks of text encoded  and the language as input
    It uses the openai api to generate flashcards
    It returns the flashcards
    """
    openai.api_key = os.environ["OPENAI_KEY"]
    prompts = {"en":'''\nGive ''' + str(NO_FLASHCARDS_PER_CHUNK) + ''' simple and precise flashcards on the above text. Your response must be in this form : {"1":{"Q":"question1","A":"answer to question 1"},"2":{"Q":"question2","A":"answer to question 2"},}''',
                "fr":'''\nDonner ''' + str(NO_FLASHCARDS_PER_CHUNK) + ''' des flashcards simple et precis sur le text ci-dessus.votre reponse doit etre de la forme suivant : {"1":{"Q":"question 1","A":"reponse du question 1"},"2":{"Q":"question2","A":"reponse du question 2"},}'''
                }
    flashcardsList = []
    ttEncoding = tiktoken.get_encoding(encodingModel)
    for index,chunk in enumerate(chunks):
        res = openai.Completion.create(
            model = "text-davinci-003",
            prompt = "<<text>>\n" + ttEncoding.decode(chunk) + prompts[lang]  + "\n<<flashcards>>\n",
            temperature = 0,
            max_tokens = 2000
        )


        flashcards= json.loads(res["choices"][0]["text"])
        for f in flashcards:
            flashcardsList.append(flashcards[f])
        
    
    return flashcardsList

