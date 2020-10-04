punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(str):
    resultado = [char for char in str if char not in punctuation_chars]
    resultado = "".join(resultado)
    return resultado
def get_pos(str):
    frase = strip_punctuation(str)
    frase = frase.split()
    resultado = [word for word in frase if word.lower() in positive_words]
    total = len(resultado)
    return total

def get_neg(str):
    frase = strip_punctuation(str)
    frase = frase.split()
    resultado = [word for word in frase if word.lower() in negative_words]
    total = len(resultado)
    return total

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
data = []
with open("project_twitter_data.csv") as project:
    for row in project:
        linha = row.split(",")
        linha[2] = linha[2].strip("\n")
        data.append(linha)
data.pop(0)
def infoData(matrix):
    tratado = []
    for row in matrix:
        tweet = strip_punctuation(row[0])
        retweets = row[1]
        replies = row[2]
        positive = get_pos(tweet)
        negative = get_neg(tweet)
        netScore = positive - negative
        tratado.append([retweets,replies,positive,negative, netScore])
    return tratado
     
        
        
#não foi usado a biblioteca csv pois o modelo de exercicio não suportava 
        
outfile = open("resulting_data.csv", "w")
outfile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
outfile.write('\n')

dados = infoData(data)
for row in dados:
    row_string = '{},{},{},{},{}'.format(row[0],row[1],row[2],row[3],row[4])
    outfile.write(row_string)
    outfile.write('\n')
outfile.close()    
    