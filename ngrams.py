#from nltk.corpus import reuters
from nltk import bigrams, trigrams
from collections import defaultdict
import random

file = open("D:/Mathematics-Capstone/math-training-data.txt",'r')
text = file.read()

#sentence = '''At eight o'clock on Thursday morning Arthur didn't feel very good.'''

#print(list(bigrams(sentence)))
#print(list(bigrams(sentence, pad_left = True, pad_right = True)))
#print(list(trigrams(sentence)))
#print(list(trigrams(sentence, pad_left = True, pad_right = True)))

# generates an n-gram model (trigram) using maximum likelihood estimation (MLE)
# input: file_name, the full path name of the file containing the training dataset
# output: n-gram model
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

# generates a text sample
# input: n-gram model (trigram)
# output: sentence of generated text
def gen_text(model):
    # initialize text
    text = [None, None]
    
    # initialize flag indicating whether or not sentence is finished
    sentence_finished = False
    
    # generate text
    while not sentence_finished:
        # random probability threshold and initialize probability accumulator
        r = random.random()
        accumulator = 0.0
        
        # loop through possible next word given previous two words
        for word in model[tuple(text[-2:])].keys():
            # accumulate probability
            accumulator += model[tuple(text[-2:])][word]
            
            # if probability is over threshold
            if accumulator >= r:
                # add word to text, stop looping through possible next words
                text.append(word)
                break
        
        # if the last two generated words are None, None
        if text[-2:] == [None, None]:
            # end the sentence
            sentence_finished = True
    
    # create text string
    str = ' '.join([t for t in text if t])
    
    # return string
    return str
