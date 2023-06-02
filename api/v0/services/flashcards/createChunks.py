import tiktoken


def createChunks(longText,chunkSize,overlap=0,encodingModel="p50k_base"):
  """
    * The function read the the text file and return the encoded tokens in seperatred chunks
    * filePath : the path of the text file to tokenize.
    * chunkSize : the max number of tokens in each chunk.
    * overlap : the overlap between chunks default = 0.
    * encodingModel : the totktoken tokenizer encoding model , default = "p50k_base".
    return :
      chunks=[] (array of enceded chunkes).
      numberOfTokensInFile=int (the totla number of tokens).
  """
   
  ttEncoding = tiktoken.get_encoding(encodingModel)

  fileText = longText

  tokens = ttEncoding.encode(fileText)
  numberOfTokensInFile = len(tokens)

  chunks = []
  for i in range(0,numberOfTokensInFile,chunkSize-overlap):
    chunk = tokens[i:i+chunkSize]
    chunks.append(chunk)
  

  return chunks,numberOfTokensInFile