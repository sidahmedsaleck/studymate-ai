import openai 
import tiktoken 
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv('.env'))

# what does createSummariesWithOpenai do:
# 1. Summaries each chunk using GPT3-text-davinci-003 model.
# 2. chunks: array of enceded chunkes.
# 3. lang: "fr" or "en" the language of the text provided.
# 4. encodingModel : the totktoken tokenizer encoding model , default = "p50k_base".
# return:
#   summary : String[] (array of the sumary of each chunk.)

def createSummariesWithOpenai(chunks,lang,encodingModel="p50k_base"):
  """
  * Summaries each chunk using GPT3-text-davinci-003 model.
  * chunks: array of enceded chunkes.
  * lang: "fr" or "en" the language of the text provided.
  * encodingModel : the totktoken tokenizer encoding model , default = "p50k_base".
  return:
    summary
  """

  openai.api_key = os.environ["OPENAI_KEY"]
  prompts = {"en":"Pretend you're an expert writer. write a detailed summary of this text bellow, in form of bullet points. Don't inject any begining text: \n<<text>>\n",
            'fr':"Imaginez que vous êtes un écrivain expert. rédiger un résumé Bien détaillé de ce texte ci-dessous, sous forme de puces.ne maiter pas du text de start : \n<<text>\n"}
  summary = []
  ttEncoding = tiktoken.get_encoding(encodingModel)
  for index,chunk in enumerate(chunks):
    res = openai.Completion.create(
        model = "text-davinci-003",
        prompt = prompts[lang] + ttEncoding.decode(chunk) + "<<Summary>>\n",
        temperature = 0,
        max_tokens = 2000
    )
    summary.append(res["choices"][0]["text"])
    print('\n\n',res["choices"][0]["text"],'\n\n')
  
  finalSummary = "\n".join(summary)
  
  return finalSummary