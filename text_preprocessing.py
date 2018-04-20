# FUNCTIONS FOR TEXT PREPROCESSING
# MATHEMATICS CAPSTONE



###########################
### HIGH LEVEL FUNCTION ###
###########################

# opens file, reads text from file, preps text, writes text to file
# input: read_file, the full path name of the file to be read and prepped
# output: the number of characters written to the file
def prep_text_file(read_file):
    write_file = "D:/Mathematics-Capstone/math-prest-data.txt"
    #"D:/Mathematics-Capstone/math-training-data.txt"
    #"D:/Mathematics-Capstone/math-testing-data.txt"
    str = get_text(read_file)
    prepped_str = text_prep(str)
    numChars = write_str_to_file(prepped_str, write_file)
    return numChars

# possible files
read_file01 = "D:/Capstone-Texts/Capstone-Texts-Prepped/holland-twenty-five-ghost-stories.txt"
read_file02 = "D:/Capstone-Texts/Capstone-Texts-Prepped/kafka-metamorphosis.txt"
read_file03 = "D:/Capstone-Texts/Capstone-Texts-Prepped/kafka-the-trial.txt"
read_file04 = "D:/Capstone-Texts/Capstone-Texts-Prepped/lovecraft-the-shunned-house.txt"
read_file05 = "D:/Capstone-Texts/Capstone-Texts-Prepped/poe-volume1.txt"
read_file06 = "D:/Capstone-Texts/Capstone-Texts-Prepped/poe-volume2.txt"
read_file07 = "D:/Capstone-Texts/Capstone-Texts-Prepped/poe-volume3.txt"
read_file08 = "D:/Capstone-Texts/Capstone-Texts-Prepped/poe-volume4.txt"
read_file09 = "D:/Capstone-Texts/Capstone-Texts-Prepped/poe-volume5.txt"
read_file10 = "D:/Capstone-Texts/Capstone-Texts-Prepped/prest-varney-the-vampire.txt"
read_file11 = "D:/Capstone-Texts/Capstone-Texts-Prepped/stevenson-strange-case-jekyll-hyde.txt"
read_file12 = "D:/Capstone-Texts/Capstone-Texts-Prepped/stoker-dracula.txt"
read_file13 = "D:/Capstone-Texts/Capstone-Texts-Prepped/stoker-dracula's-guest.txt"
read_file14 = "D:/Capstone-Texts/Capstone-Texts-Prepped/stoker-jewel-of-seven-stars.txt"
read_file15 = "D:/Capstone-Texts/Capstone-Texts-Prepped/stoker-lady-of-the-shroud.txt"
read_file16 = "D:/Capstone-Texts/Capstone-Texts-Prepped/stoker-lair-of-white-worm.txt"
read_file17 = "D:/Capstone-Texts/Capstone-Texts-Prepped/stoker-the-man.txt"



################
### FILE I/O ###
################

# gets the text out of a .txt file into a string
# input: file_name, the full path name of the file to be read
# output: the string containing all of the text in the file
def get_text(file_name):
    file = open(file_name, 'r')
    str = file.read()
    return str

# writes string to file by appending the string to the file
# input: str, the string to be written
# input: file_name, the full path name of the file to be appended to
# output: the number of characters written to the file
def write_str_to_file(str, file_name):
    file = open(file_name, 'a')
    numChars = file.write(str)
    file.close()
    return numChars

# counts the number of lines in the file (number of data samples)
# finds the maximum line length (max training sample length)
# computes the average line length (average training sample length)
# input: file_name, the full path name of the file to be read
# output: numLines, maxLen, aveLen
def dataset_info(file_name):
    file = open(file_name, 'r')
    numLines = 0
    maxLen = 0
    sumLen = 0
    line = file.readline()
    while line != '':
        numLines = numLines + 1
        maxLen = max(maxLen, len(line))
        sumLen = sumLen + len(line)
        line = file.readline()
    aveLen = sumLen/numLines
    file.close()
    return [numLines, maxLen, aveLen]



##########################
### TEXT PREPROCESSING ###
##########################

# removes extra spaces after newlines
# input: str, unprocessed string
# output: processed string
#   removes extra spaces that may be after newlines
#   newlines indicate start of new sentence, which should not be space
def remove_extra_space(str):
    # length of string
    length = len(str)
    
    # if string is empty, no white space needs to be removed
    if length == 0:
        return str
    
    # initialize processed string, will accumulate processed characters
    str_prep = str[0]
    
    # loop through characters in string
    for i in range(1, length):
        # if newline followed by space, remove space
        if (str[i-1] == "\n" and str[i] == " "):
            str_prep = str_prep + ""
        else:
            str_prep = str_prep + str[i]
    
    return str_prep

# FOR TESTS, UNCOMMENT FOLLOWING LINES:

#test_str = "a\n b\n c\n d\n e\n f"
#test_str_prep = remove_extra_space(test_str)
#print(test_str_prep + "\n")



# preprocesses text
# input: str, unprocessed string
# output: processed string
#   removes anything that is not a lowercase letter or space
#   changes capital letters to lowercase letters
#   removes punctuation and numbers
# sentences are separated with newlines
def text_prep(str):
    # length of string
    length = len(str)
    
    # initialize processed string, will accumulate processed characters
    str_prep = ""
    
    # loop through characters in string
    for i in range(0, length):
        # if in character vocabulary, accumulate character in str_prep
        if (str[i].islower() or str[i] == " "):
            str_prep = str_prep + str[i]
            
        # change capital letters to lowercase
        if (str[i].isupper()):
            str_prep = str_prep + str[i].lower()
        
        # if end of sentence, add newline
        if (str[i] == "." or str[i] == "!" or str[i] == "?"):
            str_prep = str_prep + "\n"
        
        # if newline, add a space
        if str[i] == "\n":
            str_prep = str_prep + " "
    
    # catch common errors
    # incorrectly finding ends of sentences
#    str_prep = str_prep.replace(" mr\n", " mr ")
#    str_prep = str_prep.replace(" ms\n", " ms ")
#    str_prep = str_prep.replace(" mrs\n", " mrs ")
#    str_prep = str_prep.replace(" dr\n", " dr ")
#    str_prep = str_prep.replace(" jr\n", " jr ")
#    str_prep = str_prep.replace(" st\n", " st ")
    # replacing multiple spaces with one
    str_prep = str_prep.replace("  ", " ")
        
    # remove extra spaces after newlines
    str_prep = remove_extra_space(str_prep)
            
    # return output
    return str_prep

# FOR TESTS, UNCOMMENT FOLLOWING LINES:

#test_str1 = "Hello world. I am trying to test something.\nI\'m very proud. Here we go >>><<<!!#$!"
#test_str2 = "~`@#$%^&*()_-+={}[]|\<>/"
#test_str3 = "I said, \"I am trying something intereseting.\" Hello. \"If only.\" "
#
#test_str1_prep = text_prep(test_str1)
#test_str2_prep = text_prep(test_str2)
#test_str3_prep = text_prep(test_str3)
#
#print(test_str1_prep + "\n")
#print(test_str2_prep + "\n")
#print(test_str3_prep + "\n")



# test preprocessing
# first paragraph of The Gold Bug, by Edgar Allen Poe
#test = '''MANY years ago, I contracted an intimacy with a Mr. William Legrand.
#He was of an ancient Huguenot family, and had once been wealthy; but
#a series of misfortunes had reduced him to want. To avoid the
#mortification consequent upon his disasters, he left New Orleans, the
#city of his forefathers, and took up his residence at Sullivan’s Island,
#near Charleston, South Carolina. This Island is a very singular one.
#It consists of little else than the sea sand, and is about three
#miles long. Its breadth at no point exceeds a quarter of a mile. It is
#separated from the main land by a scarcely perceptible creek, oozing its
#way through a wilderness of reeds and slime, a favorite resort of the
#marsh hen. The vegetation, as might be supposed, is scant, or at least
#dwarfish. No trees of any magnitude are to be seen. Near the western
#extremity, where Fort Moultrie stands, and where are some miserable
#frame buildings, tenanted, during summer, by the fugitives from
#Charleston dust and fever, may be found, indeed, the bristly palmetto;
#but the whole island, with the exception of this western point, and
#a line of hard, white beach on the seacoast, is covered with a dense
#undergrowth of the sweet myrtle, so much prized by the horticulturists
#of England. The shrub here often attains the height of fifteen or twenty
#feet, and forms an almost impenetrable coppice, burthening the air with
#its fragrance.'''
#test_prep = text_prep(test)
#print(test_prep)
# to see output more clearly, type test_prep in console
