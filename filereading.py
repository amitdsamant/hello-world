#This script will count the frequency of words in a text file
#input - full filepath
#output - top ten words with highest frequency

import sys
import os


def main():
    filepath = sys.argv[1]
    print(filepath)

    if not os.path.isfile(filepath):
        print("File path {} does not exist.Exiting...".format(filepath))
        sys.exit()

    bag_of_words = {} #the dictionary that will hold the word count against a word

    with open(filepath) as fp:
        cnt = 0
        for line in fp:
            print("line {} contents: {}".format(cnt,line))
            record_word_count(line.strip().split(' '),bag_of_words)
            cnt += 1

    sorted_words = order_bag_of_words(bag_of_words, desc = True)
    print("Most Frequent 10 words {}".format(sorted_words[:10]))

def order_bag_of_words(bag_of_words, desc = False):
    word_tuple = [(word, count) for word, count in bag_of_words.items()]
    return sorted(word_tuple,key=lambda x: x[1], reverse=desc)

#function to count the number of words in a word list
def record_word_count(word_list, bag_of_words):
    for word in word_list:
        if word != '':
            if word.lower() in bag_of_words:
                bag_of_words[word.lower()] += 1
            else:
                bag_of_words[word.lower()] = 1



if __name__=='__main__':
    main()
