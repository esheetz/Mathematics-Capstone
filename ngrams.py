#from nltk.corpus import reuters
from nltk import bigrams, trigrams
from collections import defaultdict
import random

f_name = "D:/Mathematics-Capstone/math-training-data.txt"
#file = open("D:/Mathematics-Capstone/math-training-data.txt",'r')
#text = file.read()

#sentence = '''At eight o'clock on Thursday morning Arthur didn't feel very good.'''

#print(list(bigrams(sentence)))
#print(list(bigrams(sentence, pad_left = True, pad_right = True)))
#print(list(trigrams(sentence)))
#print(list(trigrams(sentence, pad_left = True, pad_right = True)))

# generates an n-gram model
# input: file_name, the full path name of the file containing the training dataset
# input: n, integer specifies n-gram model (either 2, 3, or 4)
# input: prob_est, string specifies probability estimator (either MLE or ELE)
# output: n-gram model
def gen_model(file_name, n, prob_est):
    # open file
    file = open(file_name, 'r')
    
    # get first sentence
    sentence = file.readline()
    
    # BIGRAMS
    if n == 2:
        # initialize bigram list
        bgs = []
        count = 0
        
        # iterate through each sentence in file, listing bigrams
        while sentence != '':
            #remove newline at end of sentence
            sentence = sentence[:len(sentence)-1]
            tokens = sentence.split(' ')
            bgs.extend(list(bigrams(tokens, pad_left = True, pad_right = True)))
            sentence = file.readline()
            count += 1
            #print(count)
            
        # close file
        file.close()
        
        # number of trigrams in dataset
        N = len(bgs)
        
        # initialize model    
        model = defaultdict(lambda: defaultdict(lambda: 0))
        
        # put bigram counts in model
        for bg in bgs:
            model[bg[0]][bg[1]] += 1
        
        # MLE
        if prob_est == "MLE":
            # P_mle(w1...wn) = freq/total_count
            # make bigram counts probabilities
            for w1 in model:
                total_count = sum(model[w1].values())
                for w2 in model[w1]:
                    model[w1][w2] /= total_count
                
        elif prob_est == "ELE":
            # P_ele(w1...wn) = (freq + lamb)/(total_count + (B*lamb))
            B = len(model) # number of equivalence classes (determined by n-1 words)
            lamb = 0.5 # determines amount of extra probability space left over
            
            # make bigram counts probabilities
            for w1 in model:
                for w2 in model[w1]:
                    model[w1][w2] += lamb
                    model[w1][w2] /= (N + (B*lamb))
        
        else:
            print("invalid prob_est")
            return
    
    # TRIGRAMS
    elif n == 3:
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
            #print(count)
            
        # close file
        file.close()
        
        # number of trigrams in dataset
        N = len(tgs)
        
        # initialize model    
        model = defaultdict(lambda: defaultdict(lambda: 0))
        
        # put trigram counts in model
        for tg in tgs:
            model[(tg[0], tg[1])][tg[2]] += 1
        
        # MLE
        if prob_est == "MLE":
            # P_mle(w1...wn) = freq/total_count
            # make trigram counts probabilities
            for w1_w2 in model:
                total_count = sum(model[w1_w2].values())
                for w3 in model[w1_w2]:
                    model[w1_w2][w3] /= total_count
                
        elif prob_est == "ELE":
            # P_ele(w1...wn) = (freq + lamb)/(total_count + (B*lamb))
            B = len(model) # number of equivalence classes (determined by n-1 words)
            lamb = 0.5 # determines amount of extra probability space left over
            
            # make trigram counts probabilities
            for w1_w2 in model:
                total_count = sum(model[w1_w2].values())
                for w3 in model[w1_w2]:
                    model[w1_w2][w3] += lamb
                    model[w1_w2][w3] /= (N + (B*lamb))
                    
        else:
            print("invalid prob_est")
            return
                
    elif n == 4:
        print("not written")
        
    # if n is not 2, 3, 4
    else:
        print("invalid n")
        return
    
    # return the model
    return model

# generates a text sample
# input: n-gram model
# input: n, integer representing n-gram model
# output: sentence of generated text
def gen_text(model, n):
    # initialize text
    text = [None] * (n-1)
    
    # initialize flag indicating whether or not sentence is finished
    sentence_finished = False
    
    # generate text
    while not sentence_finished:
#        if n == 2:
#            word = random.sample(list(model[text[len(text)-1]]), 1)
#        if n == 3:
#            word = random.sample(list(model[tuple(text[-(n-1):])]), 1)
#        text.append(word)
        # random probability threshold and initialize probability accumulator
        r = random.random()
        accumulator = 0.0
        
        # loop through possible next word given previous n-1 words
        for word in model[tuple(text[-(n-1):])].keys():
            # accumulate probability
            accumulator += model[tuple(text[-(n-1):])][word] * 10000
            
            # if probability is over threshold
            if accumulator >= r:
                # add word to text, stop looping through possible next words
                text.append(word)
                break
        
        # if the last n-1 generated words are None
        if text[-(n-1):] == [None] * (n-1):
            # end the sentence
            sentence_finished = True
    
    # create text string
    str = ' '.join([t for t in text if t])
    
    # return string
    return str
