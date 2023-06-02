import openai 
import os
import json
import tiktoken
from api.utilities.constances import NO_QUESTIONS_PER_CHUNK
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv('.env'))


# this function takes a list of chunks and a language as input and return a list of quizzes.
def createQuiz(chunks,lang,encodingModel="p50k_base"):
    """
    This function takes a list of chunks and a language as input and return a list of quizzes.
    """
    openai.api_key = os.environ["OPENAI_KEY"]
    prompts = {"fr":f'''\nDonner un quiz sur le text ci-dessus avec ''' + str(NO_QUESTIONS_PER_CHUNK) + ''' question possible.Retourner le quiz sous le form json suivant : {"1": { "Q": "question 1 ?","choix": ["choix 1","choix 2","choix 3","choix 4"],"A": "le bon reponse"},}\n''',
                "en":'''\nGive a quiz on the text above with ''' + str(NO_QUESTIONS_PER_CHUNK) + ''' possible questions.Return the quiz in the following form json : {"1": { "Q": "question 1?","choice": ["choice 1","choice 2","choice 3","choice 4"], "A": "the correct answer"},}\n'''
                }
    quizList = []
    ttEncoding = tiktoken.get_encoding(encodingModel)
    for index,chunk in enumerate(chunks):
        res = openai.Completion.create(
            model = "text-davinci-003",
            prompt = "\n<<text>>\n" + ttEncoding.decode(chunk) + prompts[lang]  + "\n<<QUIZ>>\n",
            temperature = 0,
            max_tokens = 2000
        )

        print(res["choices"][0]["text"])
        quiz = {}
        try:
            quiz = json.loads(res["choices"][0]["text"])
        except:
            print("error in json.loads()")
        for q in quiz:
            quizList.append(quiz[q])
    
    return quizList

