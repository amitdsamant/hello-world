from nltk.corpus import stopwords
import re, string

# Calculates the Jaccard distance of a tweet using set notation
def jaccard_distance(setOne, setTwo):
    return 1 - float(len(setOne.intersection(setTwo))) / float(len(setOne.union(setTwo)))


def create_bag_of_words(text):
    stop_words = stopwords.words("english")
    text_lower_case = text.lower()
    line = text_lower_case.split(" ")
    sentence = [] # empty list
    regex = re.compile("[%s]" % re.escape(string.punctuation))
    for word in line:
        word = word.strip()
        if not re.match(r'^https?:\/\/.*[\r\n]*', word) and word != '' and not re.match('\s',word) and word != 'rt' and not re.match('^@.*', word) and word not in stop_words:
            clean_word = regex.sub("", word)
            sentence.append(clean_word)
    print("Printing Sentence: ", str(sentence))
    return sentence



#Calculate the Jaccard distance between each pair of tweet. This will save up time
def initialize_jaccard_table(texts):
    jaccard_table = {} # this is a dictionary #key =id value = dictionary of distances from each other text

    #For each text in the texts list
    for textone in texts:
        jaccard_table[textone] = {} #key =text value = dictionary
        text_bag_words_one = set(create_bag_of_words(texts[textone]["text"]))
        #the above will return a bag of words for the text passed in the parameter

        #Now compare the above bag of words to other texts

        for texttwo in texts:
            if texttwo not in jaccard_table:
                jaccard_table[texttwo] = {}
            text_bag_words_two = set(create_bag_of_words(texts[texttwo]["text"]))
            jaccard_dist = jaccard_distance(text_bag_words_one,text_bag_words_two)
            jaccard_table[textone][texttwo], jaccard_table[textone][texttwo] = jaccard_dist, jaccard_dist
    print("printing jaccard table", str(jaccard_table))
    return jaccard_table




def k_means_set_up(seeds,texts,num_of_centroids):
    jaccard_table = initialize_jaccard_table(texts)
    return jaccard_table

#Run kmeans algorithm on text
def k_means(seeds,texts,num_of_centroids):

    #initialize a look up table to calculate all the jaccard distances pairs. initialize all clusters
    jaccard_table = k_means_set_up(seeds,texts,num_of_centroids)

