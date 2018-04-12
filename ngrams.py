# FUNCTIONS FOR BUILDING AND USING NGRAM MODELS
# MATHEMATICS CAPSTONE



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
# input: n, integer specifies n-gram model (either 2, 3, 4, 5)
# output: n-gram model
def gen_model(file_name, n):
    # open file
    file = open(file_name, 'r')
    
    # get first sentence
    sentence = file.readline()
    
    # BIGRAMS
    if n == 2:
        # initialize bigram list
        bgs = []
        
        # iterate through each sentence in file, listing bigrams
        while sentence != '':
            #remove newline at end of sentence
            sentence = sentence[:len(sentence)-1]
            tokens = sentence.split(' ')
            bgs.extend(list(bigrams(tokens, pad_left = True, pad_right = True)))
            sentence = file.readline()
            
        # close file
        file.close()
        
        # initialize model    
        model = defaultdict(lambda: defaultdict(lambda: 0))
        
        # put bigram counts in model
        for bg in bgs:
            model[bg[0]][bg[1]] += 1
        
        # make bigram counts probabilities using MLE
        # P_mle(w1...wn) = freq/total_count
        for w1 in model:
            total_count = sum(model[w1].values())
            for w2 in model[w1]:
                model[w1][w2] /= total_count
    
    # TRIGRAMS
    elif n == 3:
        # initialize trigram list
        tgs = []
        
        # iterate through each sentence in file, listing trigrams
        while sentence != '':
            #remove newline at end of sentence
            sentence = sentence[:len(sentence)-1]
            tokens = sentence.split(' ')
            tgs.extend(list(trigrams(tokens, pad_left = True, pad_right = True)))
            sentence = file.readline()
            
        # close file
        file.close()
        
        # initialize model    
        model = defaultdict(lambda: defaultdict(lambda: 0))
        
        # put trigram counts in model
        for tg in tgs:
            model[(tg[0], tg[1])][tg[2]] += 1
        
        # make trigram counts probabilities using MLE
        # P_mle(w1...wn) = freq/total_count
        for w1_w2 in model:
            total_count = sum(model[w1_w2].values())
            for w3 in model[w1_w2]:
                model[w1_w2][w3] /= total_count
                
    # 4-GRAMS
    elif n == 4:
        # initialize 4-gram list
        fgs = []
        
        # iterate through each sentence in file, listing 4-grams
        while sentence != '':
            # remove newline at end of sentence
            sentence = sentence[:len(sentence)-1]
            tokens = sentence.split(' ')
            sent_fgs = get_sent_fgs(tokens, n)
            fgs.extend(sent_fgs)
            sentence = file.readline()
            
        # close file
        file.close()
        
        # initialize model
        model = defaultdict(lambda: defaultdict(lambda: 0))
        
        # put 4-gram counts in model
        for fg in fgs:
            model[(fg[0], fg[1], fg[2])][fg[3]] += 1
            
        # make 4-gram counts probabilities using MLE
        # P_mle(w1...wn) = freq/total_count
        for w1_w2_w3 in model:
            total_count = sum(model[w1_w2_w3].values())
            for w4 in model[w1_w2_w3]:
                model[w1_w2_w3][w4] /= total_count
                
    elif n == 5:
        # initialize 5-gram list
        fgs = []
        
        # iterate through each sentence in file, listing 5-grams
        while sentence != '':
            # remove newline at end of sentence
            sentence = sentence[:len(sentence)-1]
            tokens = sentence.split(' ')
            sent_fgs = get_sent_fgs(tokens, n)
            fgs.extend(sent_fgs)
            sentence = file.readline()
            
        # close file
        file.close()
        
        # initialize model
        model = defaultdict(lambda: defaultdict(lambda: 0))
        
        # put 5-gram counts in model
        for fg in fgs:
            model[(fg[0], fg[1], fg[2], fg[3])][fg[4]] += 1
        
        # make 5-gram counts probabilities using MLE
        # P_mle(w1...wn) = freq/total_count
        for w1_w2_w3_w4 in model:
            total_count = sum(model[w1_w2_w3_w4].values())
            for w5 in model[w1_w2_w3_w4]:
                model[w1_w2_w3_w4][w5] /= total_count
        
    # if n is not 2, 3, 4, 5
    else:
        print("invalid n:", n)
        return
    
    # return the model
    return model

# parses a sentence into a list of tuples representing the n-grams
# input: tokens, the tokenized sentence
# input: n, integer specifies the n-grams
# output: the n-grams of a particular sentence (list of tuples)
def get_sent_fgs(tokens, n):
    sent_fgs = []
    l = len(tokens)
    for i in range(l + (n-1)):
        if i < (n-1) and i < l:
            fg = [None] * ((n-1)-i)
            fg.extend(tokens[0:i+1])
            fg = tuple(fg)
            sent_fgs.append(fg)
        elif i > (l-1):
            if l > n:
                fg = tokens[-(n-(i-(l-1))):]
                fg.extend([None] * (i-(l-1)))
            else: # l <= n
                fg = [None] * ((n-(i-(l-1)))-l)
                fg.extend(tokens[-(n-(i-(l-1))):])
                fg.extend([None]* (i-(l-1)))
            fg = tuple(fg)
            sent_fgs.append(fg)
        else:
            fg = tokens[i-(n-1):i+1]
            fg = tuple(fg)
            sent_fgs.append(fg)
    return sent_fgs

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
        if n == 2:
            word = random.sample(list(model[text[len(text)-1]]), 1)
        elif n == 3 or n == 4 or n == 5:
            word = random.sample(list(model[tuple(text[-(n-1):])]), 1)
        else:
            print("invalid n:", n)
            return
        text.extend(word)
        
        # if the last n-1 generated words are None
        if text[-(n-1):] == [None] * (n-1):
            # end the sentence
            sentence_finished = True
    
    # create text string
    sent = ' '.join([t for t in text if t])
    
    # return string
    return sent

# generates several text samples using an n-gram model and writes to file
# input: model, the n-gram model to use to generate text
# input: n, integer representing the n-gram model
# input: numSamps, the number of text samples to generate
# input: write_file, the full path of the file to write to
# output: string indicating that text has been written to file
def gen_n_text_samples(model, n, num_samps, write_file):
    file = open(write_file, 'a')
    for i in range(num_samps):
        sent = gen_text(model, n)
        file.write(sent + '\n')
    file.close()
    return str(num_samps) + " text samples written to " + write_file
    