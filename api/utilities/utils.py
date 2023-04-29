from api.utilities.constances import CHUNK_SIZE

def tokenLimit(tire):
    if tire == 'free':
        return 10000
    if tire== 'paid':
        return 10000
    return 0

def chunkLimit(tokenLimit):
    return int (float(tokenLimit)/float(CHUNK_SIZE))


