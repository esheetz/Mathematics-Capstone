# FUNCTIONS FOR EVALUATING NGRAM MODELS
# MATHEMATICS CAPSTONE



from nltk import bigrams, trigrams
import random
import math
from text_preprocessing import dataset_info
from ngrams import get_sent_fgs

bg_file_name = "D:/Mathematics-Capstone/text-samples/2gram-text-samples.txt"
tg_file_name = "D:/Mathematics-Capstone/text-samples/3gram-text-samples.txt"
frg_file_name = "D:/Mathematics-Capstone/text-samples/4gram-text-samples.txt"
fvg_file_name = "D:/Mathematics-Capstone/text-samples/5gram-text-samples.txt"

eval_file = "D:/Mathematics-Capstone/math-testing-data.txt"

# gets random text samples from file
# input: file_name, the full path of the file to be read from
# input: num_samps, the number of samples to be pulled from file_name
# output: a list of text samples
def get_rand_samps(file_name, num_samps):
    # randomly select samples
    total_samps, _, _ = dataset_info(file_name)
    rand_samps = random.sample(range(1, total_samps), num_samps)
    rand_samps.sort()

    # initialize sample list and count
    samps_list = []
    count = 1
    
    # open file
    file = open(file_name, 'r')
    
    # read lines from file until we find samples to be selected
    for i in range(len(rand_samps)):
        while count < rand_samps[i]:
            file.readline()
            count += 1
        # get here when count = rand_samps[i]
        samp = file.readline()
        count += 1
        samps_list.append(samp)
    
    # return samps_list
    return samps_list

# computes the perplexity of a model based on a randomly selected test sample
# input: model, the model to be evaluated
# input: n, integer representing n-gram model
# input: sent, the random test sample used to compute perplexity
# output: cross entropy of the model
# output: perplexity of the model
def perplexity(model, n, sent):
    # get n-grams of evaluation sentence
    tokens = sent.split(' ')
    if n == 2:
        grams = list(bigrams(tokens, pad_left = True, pad_right = True))
    elif n == 3:
        grams = list(trigrams(tokens, pad_left = True, pad_right = True))
    elif n == 4 or n == 5:
        grams = get_sent_fgs(tokens, n)
    else:
        print("invalid n:", n)
        return
    
    # compute cross entropy, H
    # H = (-1/N)sum(log2(P[wn|w1...wn-1]))
    # for each n-gram in evaluation sentence, look up probability in model
    H = 0
    N = len(grams)
    if n == 2:
        for gram in grams:
            if model[gram[0]][gram[1]] != 0:
                H += math.log2(model[gram[0]][gram[1]])
    elif n == 3:
        for gram in grams:
            if model[(gram[0], gram[1])][gram[2]] != 0:
                H += math.log2(model[(gram[0], gram[1])][gram[2]])
    elif n == 4:
        for gram in grams:
            if model[(gram[0], gram[1], gram[2])][gram[3]] != 0:
                H += math.log2(model[(gram[0], gram[1], gram[2])][gram[3]])
    elif n == 5:
        for gram in grams:
            if model[(gram[0], gram[1], gram[2], gram[3])][gram[4]] != 0:
                H += math.log2(model[(gram[0], gram[1], gram[2], gram[3])][gram[4]])  
    H /= N
    H = -H
    
    # compute perplexity
    # PPL = 2^H
    ppl = math.pow(2, H)
    return [H, ppl]

# computes the probability of a particular text sample
# input: model, the model to be evaluated
# input: n, integer representing n-gram model
# input: sent, the text sample to be evaluated
# output: the probability the model would assign to the given sample    
def prob_of_sample(model, n, sent):
    # get n-grams of evaluation sentence
    tokens = sent.split(' ')
    if n == 2:
        grams = list(bigrams(tokens, pad_left = True, pad_right = True))
    elif n == 3:
        grams = list(trigrams(tokens, pad_left = True, pad_right = True))
    elif n == 4 or n == 5:
        grams = get_sent_fgs(tokens, n)
    else:
        print("invalid n:", n)
        return
    
    # initialize probability
    prob = 0
    
    # for each n-gram in sentence, look up probability in model
    if n == 2:
        for gram in grams:
            if model[gram[0]][gram[1]] != 0:
                prob *= model[gram[0]][gram[1]]
    elif n == 3:
        for gram in grams:
            if model[(gram[0], gram[1])][gram[2]] != 0:
                prob *= model[(gram[0], gram[1])][gram[2]]
    elif n == 4:
        for gram in grams:
            if model[(gram[0], gram[1], gram[2])][gram[3]] != 0:
                prob *= model[(gram[0], gram[1], gram[2])][gram[3]]
    elif n == 5:
        for gram in grams:
            if model[(gram[0], gram[1], gram[2], gram[3])][gram[4]] != 0:
                prob *= model[(gram[0], gram[1], gram[2], gram[3])][gram[4]]
    
    return prob # probabilities are so small, prob ~= 0