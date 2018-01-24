# FUNCTIONS FOR TEXT PREPROCESSING
# MATHEMATICS CAPSTONE

# gets the text out of a .txt file into a string
# input: file_name, the full path name of the file to be read
# output: the string containing all of the text in the file
def get_text(file_name):
    file = open(file_name, 'r')
    str = file.read()
    return str

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

test_str = "a\n b\n c\n d\n e\n f"
test_str_prep = remove_extra_space(test_str)
print(test_str_prep + "\n")



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
            
    # remove extra spaces after newlines
    str_prep = remove_extra_space(str_prep)
    
    # catch common errors
    str_prep = str_prep.replace(" mr\n", " mr ")
    str_prep = str_prep.replace(" ms\n", " ms ")
    str_prep = str_prep.replace(" mrs\n", " mrs. ")
    str_prep = str_prep.replace(" dr\n", " dr ")
            
    # return output
    return str_prep

# FOR TESTS, UNCOMMENT FOLLOWING LINES:

test_str1 = "Hello world. I am trying to test something.\nI\'m very proud. Here we go >>><<<!!#$!"
test_str2 = "~`@#$%^&*()_-+={}[]|\<>/"

test_str1_prep = text_prep(test_str1)
test_str2_prep = text_prep(test_str2)

print(test_str1_prep + "\n")
print(test_str2_prep + "\n")



# test preprocessing
# first paragraph of The Gold Bug, by Edgar Allen Poe
test = '''MANY years ago, I contracted an intimacy with a Mr. William Legrand.
He was of an ancient Huguenot family, and had once been wealthy; but
a series of misfortunes had reduced him to want. To avoid the
mortification consequent upon his disasters, he left New Orleans, the
city of his forefathers, and took up his residence at Sullivan’s Island,
near Charleston, South Carolina. This Island is a very singular one.
It consists of little else than the sea sand, and is about three
miles long. Its breadth at no point exceeds a quarter of a mile. It is
separated from the main land by a scarcely perceptible creek, oozing its
way through a wilderness of reeds and slime, a favorite resort of the
marsh hen. The vegetation, as might be supposed, is scant, or at least
dwarfish. No trees of any magnitude are to be seen. Near the western
extremity, where Fort Moultrie stands, and where are some miserable
frame buildings, tenanted, during summer, by the fugitives from
Charleston dust and fever, may be found, indeed, the bristly palmetto;
but the whole island, with the exception of this western point, and
a line of hard, white beach on the seacoast, is covered with a dense
undergrowth of the sweet myrtle, so much prized by the horticulturists
of England. The shrub here often attains the height of fifteen or twenty
feet, and forms an almost impenetrable coppice, burthening the air with
its fragrance.'''
test_prep = text_prep(test)
print(test_prep)
# to see output more clearly, type test_prep in console
