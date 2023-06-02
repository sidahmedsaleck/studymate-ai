import pdfplumber
import re

def extract_alphanumeric(text):
  """
    Apply regx to eleminate unwanted charcters.
    return :
    newText: String (the alphanumeric text)
  """
  newText = re.sub('[^a-zA-Z0-9\nÀ-ÖØ-öø-ÿ\.\,\'\?\:\;\-\s]+', ' ', text)
  newText = re.sub(' +',' ',newText)
  newText = re.sub('\n+','\n',newText)
    
 
  return newText

def extractFromPdf(filePath):
  """
  Read the .pdf file and return the plain text in that file.
  filePath: the path of the pdf file
  return:
  text = String (the plain text in the pdf)
  """
  filePages = pdfplumber.open(filePath).pages
  text = ""
  for page in filePages:
    text = page.extract_text() + text
 

  return extract_alphanumeric(text)