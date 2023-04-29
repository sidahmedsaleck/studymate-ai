# studyMateAi Flask RESTful API

This is the Flask RESTful API for the AI part of the StudyMate app backend. The API provides three routes for summarizing a given pdf file, generating flashcards, and generating a quiz based on a given plain text.

### SummarizeLongText:
This route summarizes a given pdf file using the OpenAI GPT3 API. The steps of summarization are as follows:
##### HTTP Method: POST
##### Endpoint: /summarizeLongText/
##### Request Body:
{
    "auth": "internal authentication id that I use to access the API from the main backend.",
    "tire": "the subscription tire for the end user.",
    "lang": "the language of the pdf file.",
    "fileName": "the file name",
    "file": "the file object"
}

### GenerateFlashcards
This route generates a number of flashcards based on given plain text. It returns a JSON object which contains a list of flashcards.
##### HTTP Method: POST
##### Endpoint: /generateflashcards/
##### Request Body:
{
    "auth": "internal authentication token that I use to access the API from the main backend.",
    "tire": "the subscription tire for the end user.",
    "lang": "the language of the text.",
    "longtext": "the plain text to generate flashcards from."
}

### GenerateQuiz
This route generates a quiz based on a given plain text. It returns a JSON object which contains a list of quizzes.
##### HTTP Method: POST
##### Endpoint: /generatequiz/
##### Request Body:
{
    "auth": "internal authentication token that I use to access the API from the main backend.",
    "tire": "the subscription tire for the end user.",
    "lang": "the language of the text.",
    "longtext": "the plain text to generate quizzes from"
}

