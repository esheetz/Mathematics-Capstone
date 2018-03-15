#from nltk.corpus import reuters
from nltk import bigrams, trigrams
from collections import defaultdict
import random

file = open("D:/Mathematics-Capstone/math-training-data.txt",'r')
text = file.read()

sentence = '''At eight o'clock on Thursday morning Arthur didn't feel very good.'''

#print(list(bigrams(sentence)))
#print(list(bigrams(sentence, pad_left = True, pad_right = True)))
#print(list(trigrams(sentence)))
#print(list(trigrams(sentence, pad_left = True, pad_right = True)))

def gen_model(file_name):
    # open file
    file = open(file_name, 'r')
    
    # get first sentence
    sentence = file.readline()
    
    # initialize trigram list
    tgs = []
    count = 0
    
    # iterate through each sentence in file, listing trigrams
    while sentence != '':
        #remove newline at end of sentence
        sentence = sentence[:len(sentence)-1]
        tokens = sentence.split(' ')
        tgs.extend(list(trigrams(tokens, pad_left = True, pad_right = True)))
        sentence = file.readline()
        count += 1
        print(count)
        
    # close file
    file.close()
    
    # initialize model    
    model = defaultdict(lambda: defaultdict(lambda: 0))
    
    # put trigram counts in model
    for tg in tgs:
        model[(tg[0], tg[1])][tg[2]] += 1
    
    # make trigram counts probabilities
    for w1_w2 in model:
        total_count = sum(model[w1_w2].values())
        for w3 in model[w1_w2]:
            model[w1_w2][w3] /= total_count
    
    # return the model
    return model

def gen_text(model):
    text = [None, None]
    sentence_finished = False
    
    while not sentence_finished:
        r = random.random()
        accumulator = 0.0
        
        for word in model[tuple(text[-2:])].keys():
            accumulator += model[tuple(text[-2:])][word]
            
            if accumulator >= r:
                text.append(word)
                break
            
        if text[-2:] == [None, None]:
            sentence_finished = True
    
    str = ' '.join([t for t in text if t])
    
    return str
